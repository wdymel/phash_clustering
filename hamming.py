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
