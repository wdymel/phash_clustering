from phash import p_hash

images = ["krzeslo1.png", "krzeslo1.png", "krzeslo1a.png", "krzeslo2.png"]
for image in images:
    h = p_hash("data\\" + image)
    print(f"{image}:\t {h}")


