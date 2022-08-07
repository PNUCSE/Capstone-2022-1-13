from pathlib import Path


class DetectLogo:
    def __init__(self, weight, img, conf, source):
        self.weight = weight
        self.img = img
        self.conf = conf
        self.source = source

    def find_logo(self):
        source = str(self.source)
        