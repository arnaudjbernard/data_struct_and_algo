

class DisjointSet(object):
    """
    Keeps track of disjoint sets by linking each element of a set to the root of this set.
    The root is an arbitrary element of the set.
    """

    def __init__(self):
        self.parents_map = {}

    def make_set(self, x):
        """
        Creates a new set containing x
        """
        self.parents_map[x] = x

    def find(self, x):
        """
        Finds the root of an element.
        """
        parent_of_x = self.parents_map[x]
        if parent_of_x != x:
            #recusively find the root and update it
            parent_of_x = self.find(parent_of_x)
            self.parents_map[x] = parent_of_x
        return parent_of_x

    def union(self, x, y):
        """
        Merge the set containing x with the set containing y
        """
        x_root = self.find(x)
        y_root = self.find(y)

        self.parents_map[y_root] = x_root

    def __repr__(self):
        res = ""
        roots = [x for x, y in self.parents_map.iteritems() if x == y]
        for root in roots:
            children = [str(x) for x in self.parents_map.keys() if self.find(x) == root]
            res += str(root) + ": " + " ".join(children) + "\n"
        return res


def main():
    disjoint_set = DisjointSet()
    print disjoint_set

    for i in xrange(10):
        disjoint_set.make_set(i)
    print disjoint_set

    for i in xrange(0, 9, 3):
        disjoint_set.union(i, i+1)
    print disjoint_set

    for i in xrange(0, 8, 4):
        disjoint_set.union(i, i+2)
    print disjoint_set

if __name__ == "__main__":
    main()