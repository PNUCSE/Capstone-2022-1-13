import imghdr
import os
import torch
import cv2
import datetime
import json
from pathlib import Path

from django.conf import settings
from logo.models import Logo, LogoResult
from logo.services.classifier import SecondClassifier

from yolov5.utils.general import (LOGGER, check_file, check_img_size, check_imshow, check_requirements, colorstr, cv2,
                           increment_path, non_max_suppression, print_args, scale_coords, strip_optimizer, xyxy2xywh)
from yolov5.utils.torch_utils import select_device, time_sync
from yolov5.utils.dataloaders import LoadImages
from yolov5.utils.plots import Annotator, colors, save_one_box
from yolov5.models.common import DetectMultiBackend

class MyDetectLogo:
    def __init__(self, imgSz, conf, logo, thres):
        # self.weights = os.path.join(self.base_dir, 'logo/services/best.pt')
        self.base_dir = getattr(settings, 'BASE_DIR', '/')
        self.imgsz = imgSz
        self.logo = logo

        self.weight = os.path.join(self.base_dir, 'logo/services/best.pt')
        self.device = select_device('')
        self.model = DetectMultiBackend(self.weight, device=self.device)
        self.thres = thres
        LOGGER.info(f"Thres value is {self.thres}")

        # self.model = torch.hub.load('ultralytics/yolov5', 'custom', os.path.join(self.base_dir, 'logo/services/best.pt'))
        # self.device = select_device('')

    def find_logo(self):
        source = self.logo.video.path

        logoResult = LogoResult(logo = self.logo)
        logoResult.thres = self.thres
        logoResult.save()

        logo_img = self.logo.image.path
        logo_img = cv2.imread(logo_img, cv2.IMREAD_COLOR)
        classifier = SecondClassifier(logo=logo_img, device=self.device)

        save_dir = Path(os.path.join(self.base_dir, 'files/results'))
        save_dir.mkdir(parents=True, exist_ok=True)

        stride, names, pt = self.model.stride, self.model.names, self.model.pt
        imgsz = check_img_size(self.imgsz, s=stride)

        datasets = LoadImages(source, img_size=imgsz, stride=stride, auto=pt)
        bs = 1  # batch_size
        vid_path, vid_writer = [None] * bs, [None] * bs

        seen, dt = 0, [0.0, 0.0, 0.0]
        preSeen = 0
        nowTime = datetime.datetime.min
        seen_result = []
        for path, im, im0s, vid_cap, s in datasets:
            im = torch.from_numpy(im).to(self.device)
            im = im.float()
            im /= 255
            if len(im.shape) == 3:
                im = im[None]

            pred = self.model(im, augment=False, visualize=False)

            conf_thres = 0.25
            iou_thres=0.45
            classes=None
            agnostic_nms=False
            # pred = non_max_suppression(pred, conf_thres=0.25, iou_thres=0.45, classes=None, agnostic_nms=False, max_det=1000)
            pred = non_max_suppression(pred, conf_thres, iou_thres, classes, agnostic_nms, max_det=1000)

            pred = classifier.calculate_similarity(pred, im, im0s, thres=self.thres)

            logoSeen = 0
            for i, det in enumerate(pred): # per image
                seen += 1
                logoSeen = len(det)
                p, im0, frame = path, im0s.copy(), getattr(datasets, 'frame', 0)

                p = Path(p)  # to Path
                save_path = str(save_dir / p.name)  # im.jpg

                # Labeling
                annotator = Annotator(im0, line_width=3, example=str(names))
                if len(det):
                    det[:, :4] = scale_coords(im.shape[2:], det[:, :4], im0.shape).round()

                    for *xyxy, conf, cls in reversed(det):
                        if True:
                            c = int(cls)  # integer class
                            label = None if False else (names[c] if False else f'{names[c]} {conf:.2f}')
                            annotator.box_label(xyxy, label, color=colors(c, True))

                if vid_path[i] != save_path:
                    vid_path[i] = save_path
                    if isinstance(vid_writer[i], cv2.VideoWriter):
                        vid_writer[i].release()  # release previous video writer
                    if vid_cap:  # video
                        fps = vid_cap.get(cv2.CAP_PROP_FPS)
                        w = int(vid_cap.get(cv2.CAP_PROP_FRAME_WIDTH))
                        h = int(vid_cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

                    save_path = str(Path(save_path).with_suffix('.mp4'))  # force *.mp4 suffix on results videos
                    vid_writer[i] = cv2.VideoWriter(save_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, (w, h))
                vid_writer[i].write(im0)

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

        stat = classifier.get_stat()

        LOGGER.info(f'\nTotal Similiarty')
        # LOGGER.info(f'\nstat: {stat}')
        sorted_stat = sorted(stat.items())
        LOGGER.info(f'\n{sorted_stat}')

        LOGGER.info(f'\nTotal Result time Stamp')
        LOGGER.info(f'\n{mani_seen_result}')

        s = f"\n{len(list(save_dir.glob('labels/*.txt')))} labels saved to {save_dir / 'labels'}" if False else ''
        LOGGER.info(f"Results saved to {colorstr('bold', save_dir)}{s}")

        logoResult.result.name = os.path.join('results', os.path.basename(source))
        logoResult.stamp = json.dumps(mani_seen_result, indent=4, sort_keys=True, default=str)
        logoResult.save()

        # os.system(f"ffmpeg -i {os.path.join(save_dir, os.path.basename(source))} -vcodec libx264 {os.path.join(save_dir, 'result.mp4')}")
        return logoResult