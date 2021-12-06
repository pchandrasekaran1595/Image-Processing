import os
import cv2
import numpy as np
import matplotlib.pyplot as plt


READ_PATH = "Files"
SAVE_PATH = "Processed"


if not os.path.exists(SAVE_PATH):
    os.makedirs(SAVE_PATH)


def read_image(path: str) -> np.ndarray:
    return cv2.imread(path, cv2.IMREAD_COLOR)


def save_image(image) -> None:
    cv2.imwrite(os.path.join(SAVE_PATH, "Processed.jpg"), image)


def show(image: np.ndarray, title=None):
    plt.figure()
    plt.imshow(cv2.cvtColor(src=image, code=cv2.COLOR_BGR2RGB))
    plt.axis("off")
    if title:
        plt.title(title)
    figmanager = plt.get_current_fig_manager()
    figmanager.window.state("zoomed")
    plt.show()


class ImageProcessor(object):
    def __init__(self):
        pass

    def gauss_blur(self, image: np.ndarray, kernel_size: int, sigmaX: float):
        kernel_size = int(kernel_size)

        if kernel_size == 1:
            kernel_size = 3
        
        if kernel_size % 2 == 0:
            kernel_size += 1
        
        if sigmaX != "": sigmaX = int(sigmaX)
        else: sigmaX = 0

        return cv2.GaussianBlur(src=image, ksize=(kernel_size, kernel_size), sigmaX=sigmaX)


Processor = ImageProcessor()