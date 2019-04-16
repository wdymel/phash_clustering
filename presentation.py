import numpy as np
import cv2.cv2 as cv2
from win32api import GetSystemMetrics


def display_img(caption, img, wait_for_key=True):
    cv2.namedWindow(caption, cv2.WINDOW_NORMAL)
    cv2.imshow(caption, img)
    h1, w1 = img.shape[:2]
    cv2.resizeWindow(caption, w1, h1)
    if wait_for_key:
        cv2.waitKey(0)


def show_grouped_images(groups, disp_single_groups=True):
    path = "data/"
    screen_widht = GetSystemMetrics(0)
    for gHash, gImages in groups.items():
        # print(f"{gHash}: {gImages}")
        name = gHash + ': '
        img1 = None
        for image in gImages:
            name += image + ', '
            # if it's the first image we loaded from this group, just load it
            if img1 is None:
                img1 = cv2.imread(path + image)
                if img1 is None:
                    raise RuntimeError
            # if it's second or further image try to concat it with previous images
            else:
                # https://stackoverflow.com/a/24522170
                img2 = cv2.imread(path + image)
                h1, w1 = img1.shape[:2]
                h2, w2 = img2.shape[:2]
                # if the width of combined images would be greater than the width of the screen
                #   then break them apart
                if w1 + w2 > screen_widht:
                    name = name[:-2]
                    display_img(name, img1, False)
                    name = gHash + ': '
                    img1 = img2
                else:
                    # create empty matrix
                    vis = np.zeros((max(h1, h2), w1 + w2, 3), np.uint8)

                    # combine 2 images
                    vis[:h1, :w1, :3] = img1
                    vis[:h2, w1:w1 + w2, :3] = img2
                    img1 = vis

        name = name[:-2]
        display_img(name, img1, disp_single_groups)
        # cv2.namedWindow(name, cv2.WINDOW_NORMAL)
        # cv2.imshow(name, img1)
        # h1, w1 = img1.shape[:2]
        # cv2.resizeWindow(name, w1, h1)
        # if disp_single_groups:
        #     cv2.waitKey(0)

    if not disp_single_groups:
        cv2.waitKey(0)
    cv2.destroyAllWindows()


