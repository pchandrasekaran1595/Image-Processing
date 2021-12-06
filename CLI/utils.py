import os


READ_PATH = "Files"
SAVE_PATH = "Processed"


if not os.path.exists(SAVE_PATH):
    os.makedirs(SAVE_PATH)


class ImageProcessor(object):
    def __init__(self):
        pass


Processor = ImageProcessor()