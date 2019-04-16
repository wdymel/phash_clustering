import numpy as np
import cv2.cv2 as cv2


def p_hash(path, size=(32, 32), show=False):

    # http://www.hackerfactor.com/blog/index.php?/archives/432-Looks-Like-It.html
    # load image in gray scale
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise RuntimeError

    img = cv2.resize(img, size)         # resize image to smaller size
    imf = np.float32(img) / 255.        # covert values from 0..255 to 0..1
    dst = cv2.dct(imf)                  # run discrete cosine transform
    dst = dst[:8, :8]                   # grab only lower frequencies from the dst

    # compute average value excluding first term since the DC coefficient can be significantly different
    #   from the other values and will throw off the average
    #   see more below
    #   http://www.cmlab.csie.ntu.edu.tw/cml/dsp/training/coding/jpeg/jpeg/encoder.htm
    average = -dst.item(0, 0)
    for i in dst:
        for j in i:
            average += j
    average /= dst.size

    # further reduce the dct, set the hash bits to 0 or 1 depending whether they're above or below the average
    mask0 = dst < average
    mask1 = dst >= average
    dst[mask0] = 0
    dst[mask1] = 1

    # convert hash bits to integer
    h = 0
    for bit in dst.flatten():
        h <<= 1
        h |= int(bit)

    if show:
        print(hex(h))

        cv2.namedWindow('image', cv2.WINDOW_NORMAL)
        cv2.imshow('image', img)
        cv2.resizeWindow('image', 512, 512)
        cv2.namedWindow('dst', cv2.WINDOW_NORMAL)
        cv2.imshow('dst', dst)
        cv2.resizeWindow('dst', 512, 512)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    return hex(h)

