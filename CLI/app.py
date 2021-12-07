import os
import sys

from .utils import READ_PATH, Processor, read_image, save_image, show


def run():
    args_1  = ["--file", "-f"]
    args_2  = ["--gauss-blur", "-gb"]
    args_3  = ["--avg-blur", "-ab"]
    args_4  = ["--median-blur", "-mb"]
    args_5  = ["--gamma", "-g"]
    args_6  = ["--linear", "-l"]
    args_7  = ["--clahe", "-ae"]
    args_8  = ["--hist-equ", "-he"]
    args_9  = ["--hue"]
    args_10 = ["--saturation", "-sat"]
    args_11 = ["--vibrance", "-v"]
    args_12 = ["--width", "-w"]
    args_13 = ["--height", "-h"]
    args_14 = ["--sharpen", "-sh"]
    args_15 = ["--posterize", "-post"]
    args_16 = ["--dither", "-dit"]
    args_20 = ["--save", "-s"]

    filename = None
    do_gauss_blur = False
    do_average_blur = False
    do_median_blur = False
    do_gamma = False
    do_linear = False
    do_clahe = False
    do_histogram_equalization = False
    do_hue = False
    do_saturation = False
    do_vibrance = False
    width, height = None, None
    do_sharpen = False
    do_posterize = False
    do_dither = False
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
    
    if args_9[0] in sys.argv:
        do_hue = True
        hue = float(sys.argv[sys.argv.index(args_9[0]) + 1])
    
    if args_10[0] in sys.argv:
        do_saturation = True
        saturation = float(sys.argv[sys.argv.index(args_10[0]) + 1])
    if args_10[1] in sys.argv:
        do_saturation = True
        saturation = float(sys.argv[sys.argv.index(args_10[1]) + 1])
    
    if args_11[0] in sys.argv:
        do_vibrance = True
        vibrance = float(sys.argv[sys.argv.index(args_11[0]) + 1])
    if args_11[1] in sys.argv:
        do_vibrance = True
        vibrance = float(sys.argv[sys.argv.index(args_11[1]) + 1])
    
    if args_12[0] in sys.argv:
        width = int(sys.argv[sys.argv.index(args_12[0]) + 1])
    if args_12[1] in sys.argv:
        width = int(sys.argv[sys.argv.index(args_12[1]) + 1])
    
    if args_13[0] in sys.argv:
        height = int(sys.argv[sys.argv.index(args_13[0]) + 1])
    if args_13[1] in sys.argv:
        height = int(sys.argv[sys.argv.index(args_13[1]) + 1])
    
    if args_14[0] in sys.argv:
        do_sharpen = True
        sharpen_kernel_size = sys.argv[sys.argv.index(args_14[0]) + 1]
    if args_14[1] in sys.argv:
        do_sharpen = True
        sharpen_kernel_size = sys.argv[sys.argv.index(args_14[1]) + 1]
    
    if args_15[0] in sys.argv:
        do_dither = True
        num_colors = int(sys.argv[sys.argv.index(args_15[0]) + 1])
    if args_16[1] in sys.argv:
        do_dither = True
        num_colors = int(sys.argv[sys.argv.index(args_16[1]) + 1])
    
    if args_16[0] in sys.argv:
        do_posterize = True
        num_colors = int(sys.argv[sys.argv.index(args_16[0]) + 1])
    if args_15[1] in sys.argv:
        do_posterize = True
        num_colors = int(sys.argv[sys.argv.index(args_15[1]) + 1])

  
    if args_20[0] in sys.argv: save = True
    if args_20[1] in sys.argv: save = True

    assert filename is not None, "Missing value for --file | -f"
    assert filename in os.listdir(READ_PATH), "File Not Found"

    image = read_image(os.path.join(READ_PATH, filename))

    if do_gauss_blur: image = Processor.gauss_blur(image=image, kernel_size=gaussian_blur_kernel_size, sigmaX=gaussian_blur_sigmaX)
    if do_average_blur: image = Processor.average_blur(image=image, kernel_size=average_blur_kernel_size)
    if do_median_blur: image = Processor.median_blur(image=image, kernel_size=median_blur_kernel_size)
    if do_gamma: image = Processor.adjust_gamma(image=image, gamma=gamma)
    if do_linear: image = Processor.adjust_linear_contrast(image=image, alpha=linear)
    if do_clahe: image = Processor.adaptive_equalization(image=image, clipLimit=clipLimit, tileGridSize=tileGridSize)
    if do_histogram_equalization: image = Processor.histogram_equalization(image=image)
    if do_hue: image = Processor.adjust_hue(image=image, hue=hue)
    if do_saturation: image = Processor.adjust_saturation(image=image, saturation=saturation)
    if do_vibrance: image = Processor.adjust_vibrance(image=image, vibrance=vibrance)
    if do_sharpen: image = Processor.sharpen(image=image, kernel_size=sharpen_kernel_size)
    if do_posterize: image = Processor.posterize_image(image=image, num_colors=num_colors)
    if do_dither: image = Processor.dither_image(image=image, num_colors=num_colors)


    if isinstance(width, int) and height is None:
        h, _, _ = image.shape
        image = Processor.resize_image(image, width, h)

    if width is None and isinstance(height, int):
        _, w, _ = image.shape
        image = Processor.resize_image(image, w, height)
    
    if isinstance(width, int) and isinstance(height, int):
        image = Processor.resize_image(image, width, height)

    if not save: show(image)
    else: save_image(image)
