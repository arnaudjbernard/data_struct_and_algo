
class Pair(object):
    def __init__(self, key, value):
        super(Pair, self).__init__()
        self.key = key
        self.value = value


class HashMap(object):

    def __init__(self, init_size=16, load_factor=0.75):
        super(HashMap, self).__init__()
        # init_size is a power of 2
        assert init_size & init_size-1 == 0
        assert load_factor > 0
        assert load_factor < 1
        self._size = 0
        self._load_factor = load_factor

        data = [[] for _ in xrange(init_size)]
        """:type : list[list[Pair]]"""
        self._data = data

    def insert(self, key, value):
        if (self._size + 1) * self._load_factor > len(self._data):
            self._double_size()
        self._insert(key, value)

    def _insert(self, key, value):
        self._size += 1
        key_hash = HashMap._compute_hash(key, len(self._data))
        for pair in self._data[key_hash]:
            if pair.key == key:
                pair.value = value
                return

        self._data[key_hash].append(Pair(key=key, value=value))

    def get(self, key, default_value=None):
        key_hash = HashMap._compute_hash(key, len(self._data))
        for pair in self._data[key_hash]:
            if pair.key == key:
                return pair.value
        return default_value

    def delete(self, key):
        self._delete(key)
        if self._size * self._load_factor < len(self._data) / 2:
            self._divide_size_by_two()

    def _delete(self, key):
        key_hash = HashMap._compute_hash(key, len(self._data))
        for pair in self._data[key_hash]:
            if pair.key == key:
                self._size -= 1
                self._data[key_hash].remove(pair)
                return

    def _divide_size_by_two(self):
        old_data = self._data
        self._size /= 2
        self._data = [[] for _ in xrange(self._size)]
        self._insert_data(old_data)

    def _double_size(self):
        old_data = self._data
        self._size *= 2
        self._data = [[] for _ in xrange(self._size)]
        self._insert_data(old_data)

    def _insert_data(self, data):
        for arr in data:
            for pair in arr:
                self._insert(pair.key, pair.value)

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        self._insert(key, value)

    def __delitem__(self, key):
        self.delete(key)

    def __len__(self):
        return self._size

    def keys(self):
        return [pair.key for arr in self._data for pair in arr]

    def values(self):
        return [pair.value for arr in self._data for pair in arr]

    @staticmethod
    def _compute_hash(key, size):
        return hash(key) % size


def main():
    hash_map = HashMap()

    hash_map.insert("bli", "bla")
    print hash_map.get("bli")

    hash_map["bli"] = "blu"
    print hash_map.get("bli")

    del hash_map["bli"]
    print hash_map.get("bli")


if __name__ == "__main__":
    main()
