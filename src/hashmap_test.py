import unittest
from hashmap import HashMap

class TestHashMapFunctions(unittest.TestCase):

    def setUp(self):
        self._ref = {}
        self._map = HashMap()

    def add(self, key, value):
        self._ref[key] = value
        self._map[key] = value

    def delete(self, key, value):
        del self._ref[key]
        del self._map[key]

    def test_add(self):
        for i in xrange(100):
            self.add("key_"+str(i), "value_"+str(i))
        self.assert_ref_equals_map()

    def test_delete(self):
        for i in xrange(100):
            self.add("key_"+str(i), "value_"+str(i))
        for i in xrange(0, 100, 2):
            self.delete("key_"+str(i), "value_"+str(i))
        self.assert_ref_equals_map()

    def test_get(self):
        for i in xrange(100):
            self.add("key_"+str(i), "value_"+str(i))
        for i in xrange(100):
            self.assertEqual(self._ref["key_"+str(i)], self._map["key_"+str(i)])

    def test_random(self):
        import random
        for i in xrange(10000):
            r = random.randint(0, 2)
            key = "key_"+str(random.randint(0, 9))
            value = "value_"+str(random.randint(0, 9))
            if r == 0:
                self.add(key, value)
            elif r == 1 and self._ref.get(key, None) is not None:
                self.delete(key, value)
            else:
                self.assertEqual(self._ref.get(key, None), self._map.get(key, None))



    def assert_ref_equals_map(self):
        self.assertItemsEqual(self._ref.keys(), self._map.keys())
        self.assertItemsEqual(self._ref.values(), self._map.values())

if __name__ == '__main__':
    unittest.main()