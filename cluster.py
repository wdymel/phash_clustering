class Cluster:

    id = 0

    def __init__(self, names, hashes):
        """
        :param names: string bądź lista stringów, ścieżki do plików
        :param hashes: string bądź lista stringów, hashe plików
        """
        if type(names) == str and type(hashes) == str:
            # klaster składający się z jednego zdjęcia i hashu
            self.names = [names]
            self.hashes = [hashes]
            self.id = names
        elif type(names) == list and type(hashes) == list and len(names) == len(hashes):
            # klaster składający się z wielu zdjęć i hashy
            self.names = names
            self.hashes = hashes
            self.id = str(Cluster.id)
            Cluster.id += 1
        else:
            # źle dobrane dane
            raise RuntimeError(f"Both parameters must be of the same type, either string or same length list not\n"
                               f"\tnames: {type(names)}\n\thashes: {type(hashes)}")

    def __add__(self, other):
        if type(other) is not type(self):
            raise RuntimeError(f"Cluster can be added only to other clusters, not {type(other)}")
        return Cluster(self.names + other.names, self.hashes + other.hashes)

    def __repr__(self):
        return f"Cluster(id = {self.id})"

    # def __str__(self):
    #     return f"Cluster\n\tid = {self.id}\n\tnames = {self.names}\n\thashes = {self.hashes})"
    pass
