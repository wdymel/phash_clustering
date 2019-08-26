from os import listdir
from os.path import isfile, join
from phash import p_hash
from hamming import hamming_distance_lists
from presentation import save_grouped_images
from cluster import Cluster

# path to directory with tested images
paths = ["Inputs/Krzesla/", "Inputs/KartyMicroSD/", "Inputs/Samochody/", "Inputs/Owoce/", "Inputs/Smartfony/"]
outputs_dir = "Outputs/"
# by how many bits can hashes differ to be considered similar
epsilon = 10

for path in paths:
    print(f"path {path}:")
    # get a list of all files in directory
    images = [f for f in listdir(path) if isfile(join(path, f))]
    # directory for grouping images
    #   uses hash of first image in group as key

    clusters = {}
    for image in images:
        h = p_hash(path + image)        # calc perceptual hash
        cluster = Cluster(image, h)     # wrap it in one-element cluster
        clusters[cluster] = None        # store it in a dictionary
        print(f"\t{image}:\t {h}")      # printout calculated hash

    # Hierarchical agglomerative clustering
    while True:
        minimum = float('inf')
        potential_pair = None
        for c1 in clusters:
            for c2 in clusters:
                if c1.id < c2.id:
                    distance = hamming_distance_lists(c1.hashes, c2.hashes)
                    if epsilon >= distance < minimum:
                        minimum = distance
                        potential_pair = (c1, c2)
        if minimum == float('inf'):     # przerwij jeżeli nie ma już par o różnicy mniejszej/równej epsilon
            break
        else:       # połącz znalezioną parę o największym prawodpodobieństwie w klaster
            new_cluster = potential_pair[0] + potential_pair[1]
            clusters[new_cluster] = None
            clusters.pop(potential_pair[0])
            clusters.pop(potential_pair[1])

    # print out groups
    print("Hierarchical agglomerative clustering:")
    for gHash, gImages in clusters.items():
        print(f"\t{gHash}: {gImages}")
    print("\n")

    # display grouped images
    # show_grouped_images(groups, path=paths[i])
    save_grouped_images(clusters, path=path, output_directory_name=join(outputs_dir, path))









