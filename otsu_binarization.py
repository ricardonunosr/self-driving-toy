import numpy as np


def compute_otsu_binarization(gray):
    pixel_number = gray.size
    mean_weigth = 1.0/pixel_number
    his, bins = np.histogram(gray, np.array(range(0, 256)))
    final_thresh = -1
    final_value = -1
    for t in bins[1:-1]:
        Wb = np.sum(his[:t]) * mean_weigth
        Wf = np.sum(his[t:]) * mean_weigth

        mub = np.mean(his[:t])
        muf = np.mean(his[t:])

        value = Wb * Wf * (mub - muf) ** 2

        if value > final_value:
            final_thresh = t
            final_value = value
    final_img = gray.copy()
    final_img[gray > final_thresh] = 255
    final_img[gray < final_thresh] = 0
    return final_img


def grayConversion(image):
    grayValue = 0.07 * image[:, :, 2] + 0.72 * \
        image[:, :, 1] + 0.21 * image[:, :, 0]
    gray_image = grayValue.astype(np.uint8)
    return gray_image
