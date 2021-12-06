import cv2
import pytest
import numpy as np

from CLI.utils import Processor, read_image

image_1 = read_image("Files/Image_1.jpg")
image_2 = np.random.randint(low=0, high=255, size=(224, 224, 3)).astype("uint8")
image_3 = np.random.randint(low=0, high=255, size=(360, 640, 3)).astype("uint8")


@pytest.mark.parametrize("image, kernel_size, sigmaX",[(image_1, 5, 0), (image_2, 15, 3), (image_3, 25, 25)])
def test_gaussian_blur_1(image, kernel_size, sigmaX):   
    assert Processor.gauss_blur(image, kernel_size, sigmaX).all() == cv2.GaussianBlur(src=image, ksize=(kernel_size, kernel_size), sigmaX=sigmaX).all()


@pytest.mark.parametrize("image, kernel_size, sigmaX",[(image_1, 24, 0), (image_2, 26, 12), (image_3, 4, 2.5)])
def test_gaussian_blur_2(image, kernel_size, sigmaX):   
    assert Processor.gauss_blur(image, kernel_size, sigmaX).all() == cv2.GaussianBlur(src=image, ksize=(kernel_size+1, kernel_size+1), sigmaX=sigmaX).all()

