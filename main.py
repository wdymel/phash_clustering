from os import listdir
from os.path import isfile, join
from phash import p_hash
from hamming import hamming_distance
from presentation import show_grouped_images

# path to directory with tested images
paths = ["Krzesla/", "KartyMicroSD/"]

for i in range (0, len(paths)):
        # get a list of all files in directory
        images = [f for f in listdir(paths[i]) if isfile(join(paths[i], f))]
        # directory for grouping images
        #   uses hash of first image in group as key
        groups = {}
        # by how many bits can hashes differ to be considered similar
        threshold = 10

        for image in images:
            h = p_hash(paths[i] + image)     # calc perceptual hash
            print(f"{image}:\t {h}")

            # try to group current images with previous
            added_to_group = False
            for gHash, gImages in groups.items():
                if hamming_distance(h, gHash) <= threshold:
                    groups[gHash].append(image)
                    added_to_group = True
                    break
            # if not matched with any existing group, create a new one
            if not added_to_group:
                groups[h] = [image]

        # print out groups
        print("\nProste grupowanie:")
        for gHash, gImages in groups.items():
            print(f"{gHash}: {gImages}")

        # display grouped images
        show_grouped_images(groups, path=paths[i])









