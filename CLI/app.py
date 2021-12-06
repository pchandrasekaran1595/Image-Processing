import os
import sys

from .utils import READ_PATH, Processor, read_image, save_image, show


def run():
    args_1 = ["--file", "-f"]
    args_2 = ["--gauss-blur", "-gb"]
    args_10 = ["--save", "-s"]

    filename = None
    do_gauss_blur = False
    save = False

    if args_1[0] in sys.argv: filename = sys.argv[sys.argv.index(args_1[0]) + 1]
    if args_1[1] in sys.argv: filename = sys.argv[sys.argv.index(args_1[1]) + 1]

    if args_2[0] in sys.argv: 
        do_gauss_blur = True
        setup = sys.argv[sys.argv.index(args_2[0]) + 1] + ","
        gaussian_blur_kernel_size = setup.split(",")[0]
        gaussian_blur_sigmaX = setup.split(",")[1]
    if args_2[1] in sys.argv: 
        do_gauss_blur = True
        setup = sys.argv[sys.argv.index(args_2[1]) + 1] + ","
        gaussian_blur_kernel_size = setup.split(",")[0]
        gaussian_blur_sigmaX = setup.split(",")[1]
    
    if args_10[0] in sys.argv: save = True
    if args_10[1] in sys.argv: save = True

    assert filename is not None, "Missing value for --file | -f"
    assert filename in os.listdir(READ_PATH), "File Not Found"

    image = read_image(os.path.join(READ_PATH, filename))

    if do_gauss_blur:
        image = Processor.gauss_blur(image=image, kernel_size=gaussian_blur_kernel_size, sigmaX=gaussian_blur_sigmaX)
    
    if not save:
        show(image)
    else:
        save_image(image)
