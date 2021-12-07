import os
import sys

from .utils import READ_PATH, Processor, read_image, save_image, show


def run():
    args_1 = ["--file", "-f"]
    args_2 = ["--gauss-blur", "-gb"]
    args_3 = ["--avg-blur", "-ab"]
    args_4 = ["--median-blur", "-mb"]
    args_5 = ["--gamma", "-g"]
    args_6 = ["--linear", "-l"]
    args_7 = ["--clahe", "-ae"]
    args_8 = ["--hist-equ", "-he"]
    args_10 = ["--save", "-s"]

    filename = None
    do_gauss_blur = False
    do_average_blur = False
    do_median_blur = False
    do_gamma = False
    do_linear = False
    do_clahe = False
    do_histogram_equalization = False
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
    
    if args_3[0] in sys.argv: 
        do_average_blur = True
        average_blur_kernel_size = int(sys.argv[sys.argv.index(args_3[0]) + 1])
    if args_3[1] in sys.argv: 
        do_average_blur = True
        average_blur_kernel_size = int(sys.argv[sys.argv.index(args_3[1]) + 1])
    
    if args_4[0] in sys.argv: 
        do_median_blur = True
        median_blur_kernel_size = sys.argv[sys.argv.index(args_4[0]) + 1]
    if args_4[1] in sys.argv: 
        do_median_blur = True
        median_blur_kernel_size = sys.argv[sys.argv.index(args_4[1]) + 1]
    
    if args_5[0] in sys.argv: 
        do_gamma = True
        gamma = float(sys.argv[sys.argv.index(args_5[0]) + 1])
    if args_5[1] in sys.argv: 
        do_gamma = True
        gamma = float(sys.argv[sys.argv.index(args_5[1]) + 1])
    
    if args_6[0] in sys.argv: 
        do_linear = True
        linear = float(sys.argv[sys.argv.index(args_6[0]) + 1])
    if args_6[1] in sys.argv: 
        do_linear= True
        linear = float(sys.argv[sys.argv.index(args_6[1]) + 1])
    
    if args_7[0] in sys.argv: 
        do_clahe = True
        setup = sys.argv[sys.argv.index(args_7[0]) + 1] + ","
        clipLimit = float(setup.split(",")[0])
        tileGridSize = setup.split(",")[1]
    if args_7[1] in sys.argv: 
        do_clahe = True
        setup = sys.argv[sys.argv.index(args_7[1]) + 1] + ","
        clipLimit = float(setup.split(",")[0])
        tileGridSize = setup.split(",")[1]
    
    if args_8[0] in sys.argv: 
        do_histogram_equalization = True
    if args_8[1] in sys.argv: 
        do_histogram_equalization = True
  
    if args_10[0] in sys.argv: save = True
    if args_10[1] in sys.argv: save = True

    assert filename is not None, "Missing value for --file | -f"
    assert filename in os.listdir(READ_PATH), "File Not Found"

    image = read_image(os.path.join(READ_PATH, filename))

    if do_gauss_blur: image = Processor.gauss_blur(image=image, kernel_size=gaussian_blur_kernel_size, sigmaX=gaussian_blur_sigmaX)
    if do_average_blur: image = Processor.average_blur(image=image, kernel_size=average_blur_kernel_size)
    if do_median_blur: image = Processor.median_blur(image=image, kernel_size=median_blur_kernel_size)
    if do_gamma: image = Processor.adjust_gamma(image=image, gamma=gamma)
    if do_linear: image = Processor.adjust_linear_contrast(image=image, alpha=linear)
    if do_clahe: image = Processor.adaptive_equalization(image=image, clipLimit=clipLimit, tileGridSize=tileGridSize)
    if do_histogram_equalization: Processor.histogram_equalization(image=image)

    if not save: show(image)
    else: save_image(image)
