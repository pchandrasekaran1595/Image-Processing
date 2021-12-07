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


@pytest.mark.parametrize("image, kernel_size",[(image_1, 24), (image_2, 51), (image_3, 5)])
def test_average_blur(image, kernel_size):
    assert Processor.average_blur(image, kernel_size).all() == cv2.blur(src=image, ksize=(kernel_size, kernel_size)).all()


@pytest.mark.parametrize("image, kernel_size",[(image_1, 5), (image_2, 15), (image_3, 25)])
def test_median_blur_1(image, kernel_size):   
    assert Processor.median_blur(image, kernel_size).all() == cv2.medianBlur(src=image, ksize=kernel_size).all()


@pytest.mark.parametrize("image, kernel_size",[(image_1, 24), (image_2, 26), (image_3, 4)])
def test_median_blur_2(image, kernel_size):   
    assert Processor.median_blur(image, kernel_size).all() == cv2.medianBlur(src=image, ksize=kernel_size+1).all()


@pytest.mark.parametrize("image, gamma",[(image_1, 1.8), (image_2, 0.5), (image_3, 2.8)])
def test_gamma(image, gamma): 
    image = image / 255
    image = np.clip(((image ** gamma) * 255), 0, 255).astype("uint8")
    assert Processor.adjust_gamma(image, gamma).all() == image.all()


@pytest.mark.parametrize("image, linear",[(image_1, 100), (image_2, 75.625), (image_3, 300)])
def test_linear_contrast(image, linear): 
    assert Processor.adjust_linear_contrast(image, linear).all() == np.clip((image + linear), 0, 255).astype("uint8").all()


@pytest.mark.parametrize("image, clipLimit, tileGridSize",[(image_1, 24, 1), (image_2, 2.5, 4), (image_3, 4.7625, 8)])
def test_adaptive_equalization(image, clipLimit, tileGridSize):  
    clahe = cv2.createCLAHE(clipLimit=clipLimit, tileGridSize=(tileGridSize, tileGridSize))
    if len(image.shape) == 3:
        for i in range(3):
            image[:, :, i] = clahe.apply(image[:, :, i])
    else:
        image = clahe.apply(image) 
    assert Processor.adaptive_equalization(image, clipLimit, tileGridSize).all() == image.all()


@pytest.mark.parametrize("image",[(image_1), (image_2), (image_3)])
def test_histogram_equalization(image):  
    if len(image.shape) == 3:
        for i in range(3):
            image[:, :, i] = cv2.equalizeHist(image[:, :, i])
    else:
        image = cv2.equalizeHist(image) 
    assert Processor.histogram_equalization(image).all() == image.all()