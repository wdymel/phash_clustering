# https://stackoverflow.com/a/33875233
def hamming_distance(a, b):
    if type(a) is not int:
        try:
            a = int(a, 16)
        except ValueError:
            raise RuntimeError(f"parameter a = {a} is of type {type(a)} instead of int")
    if type(b) is not int:
        try:
            b = int(b, 16)
        except ValueError:
            raise RuntimeError(f"parameter a = {b} is of type {type(b)} instead of int")
    return bin(a ^ b).count('1')
