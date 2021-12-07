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

    def gauss_blur(self, image: np.ndarray, kernel_size, sigmaX) -> np.ndarray:
        kernel_size = int(kernel_size)

        if kernel_size == 1:
            kernel_size = 3
        
        if kernel_size % 2 == 0:
            kernel_size += 1
        
        if sigmaX != "": sigmaX = int(sigmaX)
        else: sigmaX = 0

        return cv2.GaussianBlur(src=image, ksize=(kernel_size, kernel_size), sigmaX=sigmaX)
    
    def average_blur(self, image: np.ndarray, kernel_size: int) -> np.ndarray:
        return cv2.blur(src=image, ksize=(kernel_size, kernel_size))
    
    def median_blur(self, image: np.ndarray, kernel_size) -> np.ndarray:
        kernel_size = int(kernel_size)

        if kernel_size == 1:
            kernel_size = 3
        
        if kernel_size % 2 == 0:
            kernel_size += 1

        return cv2.medianBlur(src=image, ksize=kernel_size)
    
    def adjust_gamma(self, image: np.ndarray, gamma: float) -> np.ndarray:
        image = image / 255
        image = np.clip(((image ** gamma) * 255), 0, 255).astype("uint8")
        return image
    
    def adjust_linear_contrast(self, image: np.ndarray, alpha: float) -> np.ndarray:
        return np.clip((image + alpha), 0, 255).astype("uint8")
    
    def adaptive_equalization(self, image: np.ndarray, clipLimit: float, tileGridSize) -> np.ndarray:
        if tileGridSize != "": tileGridSize = int(tileGridSize)
        else: tileGridSize = 2

        clahe = cv2.createCLAHE(clipLimit=clipLimit, tileGridSize=(tileGridSize, tileGridSize))
        if len(image.shape) == 3:
            for i in range(3):
                image[:, :, i] = clahe.apply(image[:, :, i])
        else:
            image = clahe.apply(image)
        return image
    
    def histogram_equalization(self, image: np.ndarray) -> np.ndarray:
        if len(image.shape) == 3:
            for i in range(3):
                image[:, :, i] = cv2.equalizeHist(image[:, :, i])
        else:
            image = cv2.equalizeHist(image)
        return image
    
    def adjust_hue(self, image: np.ndarray, hue: float):
        image = cv2.cvtColor(src=image, code=cv2.COLOR_BGR2HSV)
        feature = image[:, :, 0]
        feature = np.clip((hue * feature), 0, 179).astype("uint8")
        image[:, :, 0] = feature
        return cv2.cvtColor(src=image, code=cv2.COLOR_HSV2BGR)

    def adjust_saturation(self, image: np.ndarray, saturation: float):
        image = cv2.cvtColor(src=image, code=cv2.COLOR_BGR2HSV)
        feature = image[:, :, 1]
        feature = np.clip((saturation * feature), 0, 255).astype("uint8")
        image[:, :, 1] = feature
        return cv2.cvtColor(src=image, code=cv2.COLOR_HSV2BGR)

    def adjust_vibrance(self, image: np.ndarray, vibrance: float):
        image = cv2.cvtColor(src=image, code=cv2.COLOR_BGR2HSV)
        feature = image[:, :, 2]
        feature = np.clip((vibrance * feature), 0, 255).astype("uint8")
        image[:, :, 2] = feature
        return cv2.cvtColor(src=image, code=cv2.COLOR_HSV2BGR)

Processor = ImageProcessor()