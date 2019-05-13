# https://stackoverflow.com/a/33875233
def hamming_distance(a, b):
    if type(a) is not int:
        try:
            a = int(a, 16)
        except ValueError:
            raise RuntimeError(f"parameter a = {a} must be of int type or hex str not {type(a)}")
    if type(b) is not int:
        try:
            b = int(b, 16)
        except ValueError:
            raise RuntimeError(f"parameter a = {b} must be of int type or hex str not {type(b)}")
    return bin(a ^ b).count('1')


def hamming_distance_lists(a, b):
    if type(a) is not list:
        raise RuntimeError(f"parameter a = {a} must be of list not {type(a)}")
    if type(b) is not list:
        raise RuntimeError(f"parameter a = {b} must be of list type not {type(b)}")
    dist1 = 0
    for h1 in a:
        dist2 = 0
        for h2 in b:
            dist2 += hamming_distance(h1, h2)
        dist1 += dist2 / len(b)
    return dist1 / len(a)
