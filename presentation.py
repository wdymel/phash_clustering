import cv2.cv2 as cv2
import os
import errno


def save_grouped_images(clusters, path, output_directory_name):
    for c in clusters:                                          # dla każdego klastra
        directory = output_directory_name + c.id + "/"          # utwórz osobny katalog
        if not os.path.exists(os.path.dirname(directory)):
            try:
                os.makedirs(os.path.dirname(directory))
            except OSError as exc:  # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise
        for image_name, image_hash in zip(c.names, c.hashes):   # równolegle idź po 2 listach, nazwach plików i hashach
            filename, file_extension = os.path.splitext(image_name)
            name = filename + "_" + image_hash + file_extension
            img1 = cv2.imread(path + image_name)
            cv2.imwrite(directory + name, img1)


