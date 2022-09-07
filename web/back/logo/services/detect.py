from pathlib import Path

from django.conf import settings
from django.core.files import File

from yolov5.utils.general import (LOGGER, check_file, check_img_size, check_imshow, check_requirements, colorstr, cv2,
                           increment_path, non_max_suppression, print_args, scale_coords, strip_optimizer, xyxy2xywh)
from yolov5.utils.torch_utils import select_device, time_sync
from yolov5.utils.dataloaders import LoadImages
from yolov5.utils.plots import Annotator, colors, save_one_box
from yolov5.models.common import DetectMultiBackend

import torch
import torch.backends.cudnn as cudnn

from logo.models import Logo, LogoResult

import os
import datetime

# from logo.services.classifier import similarity_classifier
from logo.services.classifier import SecondClassifier

class DetectLogo:
    def __init__(self, imgSz, conf, logo):
        self.imgsz = imgSz
        self.conf = conf
        self.logo = logo
        self.base_dir = getattr(settings, 'BASE_DIR', '/')

    def find_logo(self):
        source = self.logo.video.path
        weights = os.path.join(self.base_dir, 'logo/services/best.pt')

        logoResult = LogoResult(logo = self.logo)
        logoResult.save()

        logo_img = self.logo.image.path
        logo_img = cv2.imread(logo_img, cv2.IMREAD_COLOR)
        # logo_img = cv2.cvtColor(logo_img, cv2.COLOR_BGR2RGB)
        classifier = SecondClassifier(logo_img)

        # save_dir = increment_path(Path(os.path.join(self.base_dir, 'logo/result')) / 'exp', exist_ok=False)  # increment run
        # save_dir.mkdir(parents=True, exist_ok=True)  # make dir
        # save_dir = os.path.join(self.base_dir, 'results')
        save_dir = Path(os.path.join(self.base_dir, 'files/results'))
        save_dir.mkdir(parents=True, exist_ok=True)

        device = select_device('')
        # data = self.base_dir + '/yolov5/data/coco128.yaml' # 뒤에 바꿔야됨
        data = os.path.join(self.base_dir, 'yolov5/data/coco128.yaml')
        model = DetectMultiBackend(weights, device=device, dnn=False, data=data, fp16=False)
        stride, names, pt = model.stride, model.names, model.pt
        imgsz = check_img_size(self.imgsz, s=stride)

        datasets = LoadImages(source, img_size=imgsz, stride=stride, auto=pt)
        bs = 1  # batch_size
        vid_path, vid_writer = [None] * bs, [None] * bs

        model.warmup(imgsz=(1 if pt else bs, 3, *imgsz))  # warmup
        seen, windows, dt = 0, [], [0.0, 0.0, 0.0]

        preSeen = 0
        nowTime = datetime.datetime.min
        seen_result = []
        # playTime = datetime.date
        
        for path, im, im0s, vid_cap, s in datasets:
            t1 = time_sync()
            im = torch.from_numpy(im).to(device)
            im = im.half() if model.fp16 else im.float()  # uint8 to fp16/32
            im /= 255  # 0 - 255 to 0.0 - 1.0
            if len(im.shape) == 3:
                im = im[None]  # expand for batch dim
            t2 = time_sync()
            dt[0] += t2 - t1

            # Inference
            pred = model(im, augment=False, visualize=False)
            t3 = time_sync()
            dt[1] += t3 - t2
            
            # NMS
            conf_thres = 0.25
            iou_thres=0.45
            classes=None
            agnostic_nms=False
            # pred = non_max_suppression(pred, conf_thres=0.25, iou_thres=0.45, classes=None, agnostic_nms=False, max_det=1000)
            pred = non_max_suppression(pred, conf_thres, iou_thres, classes, agnostic_nms, max_det=1000)
            dt[2] += time_sync() - t3

            # need 2nd stage
            # something need
            pred, stat = classifier.calculate_similarity(pred, im, im0s, thres=0.99)
            # pred = similarity_classifier(pred, im, im0s, logo_img)

            # Process predictions
            logoSeen = 0
            for i, det in enumerate(pred):  # per image
                seen += 1
                logoSeen = len(det)
                p, im0, frame = path, im0s.copy(), getattr(datasets, 'frame', 0)

                p = Path(p)  # to Path
                save_path = str(save_dir / p.name)  # im.jpg
                txt_path = str(save_dir / 'labels' / p.stem) + ('' if datasets.mode == 'image' else f'_{frame}')  # im.txt
                s += '%gx%g ' % im.shape[2:]  # print string
                gn = torch.tensor(im0.shape)[[1, 0, 1, 0]]  # normalization gain whwh
                # imc = im0.copy() if save_crop else im0  # for save_crop
                annotator = Annotator(im0, line_width=3, example=str(names))
                if len(det):
                    # Rescale boxes from img_size to im0 size
                    det[:, :4] = scale_coords(im.shape[2:], det[:, :4], im0.shape).round()

                    # Print results
                    for c in det[:, -1].unique():
                        n = (det[:, -1] == c).sum()  # detections per class
                        s += f"{n} {names[int(c)]}{'s' * (n > 1)}, "  # add to string

                    # Write results
                    for *xyxy, conf, cls in reversed(det):
                        if True:
                            c = int(cls)  # integer class
                            label = None if False else (names[c] if False else f'{names[c]} {conf:.2f}')
                            annotator.box_label(xyxy, label, color=colors(c, True))
                        # if save_crop:
                        #     save_one_box(xyxy, imc, file=save_dir / 'crops' / names[c] / f'{p.stem}.jpg', BGR=True)

                if True:
                    if datasets.mode == 'image':
                        cv2.imwrite(save_path, im0)
                    else:  # 'video' or 'stream'
                        if vid_path[i] != save_path:  # new video
                            vid_path[i] = save_path
                            if isinstance(vid_writer[i], cv2.VideoWriter):
                                vid_writer[i].release()  # release previous video writer
                            if vid_cap:  # video
                                fps = vid_cap.get(cv2.CAP_PROP_FPS)
                                w = int(vid_cap.get(cv2.CAP_PROP_FRAME_WIDTH))
                                h = int(vid_cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
                            else:  # stream
                                fps, w, h = 30, im0.shape[1], im0.shape[0]
                            save_path = str(Path(save_path).with_suffix('.mp4'))  # force *.mp4 suffix on results videos
                            vid_writer[i] = cv2.VideoWriter(save_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, (w, h))
                        vid_writer[i].write(im0)

            # Print time (inference-only)
            # LOGGER.info(f'{s}Done. ({t3 - t2:.3f}s)')

            nowTime = nowTime + datetime.timedelta(milliseconds=33)
            if logoSeen != 0:
                if preSeen == 0:
                    seenData = {
                        "start": nowTime - datetime.datetime.min
                    }
                    # print("logo start at ", nowTime - datetime.datetime.min)
                else :
                    pass
            else :
                if preSeen == 0:
                    pass
                else :
                    seenData["end"] = nowTime - datetime.datetime.min
                    # print("logo end at ", nowTime - datetime.datetime.min)
                    seen_result.append(seenData)

            preSeen = logoSeen

        # Print results
        t = tuple(x / seen * 1E3 for x in dt)  # speeds per image
        LOGGER.info(f'Speed: %.1fms pre-process, %.1fms inference, %.1fms NMS per image at shape {(1, 3, *imgsz)}' % t)

        mani_seen_result = []
        preElem = None
        seenData = None

        for i, elem in enumerate(seen_result):
            if preElem is None:
                seenData = elem
            else:
                if preElem["end"].seconds <= elem["start"].seconds <= preElem["end"].seconds + 1:
                    seenData["end"] = elem["end"]
                else:
                    mani_seen_result.append(seenData)
                    seenData = elem

            preElem = elem
        mani_seen_result.append(seenData)

        # if save_txt or save_img:
        if False or True:
            LOGGER.info(f'\nTotal Similiarty')
            # LOGGER.info(f'\nstat: {stat}')
            sorted_stat = sorted(stat.items())
            LOGGER.info(f'\n{sorted_stat}')

            LOGGER.info(f'\nTotal Result time Stamp')
            LOGGER.info(f'\n{mani_seen_result}')

            s = f"\n{len(list(save_dir.glob('labels/*.txt')))} labels saved to {save_dir / 'labels'}" if False else ''
            LOGGER.info(f"Results saved to {colorstr('bold', save_dir)}{s}")

            logoResult.result.name = os.path.join(save_dir, os.path.basename(source))
            logoResult.save()
        # if update:
        if False:
            strip_optimizer(weights[0])  # update model (to fix SourceChangeWarning)

        # os.system(f"ffmpeg -i {os.path.join(save_dir, os.path.basename(source))} -vcodec libx264 {os.path.join(save_dir, 'result.mp4')}")
        return mani_seen_result
