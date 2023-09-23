# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose, MIN_QUALITY, MAX_QUALITY


class GildedRoseTest(unittest.TestCase):
    def test_minimal_quality(self):
        items = [Item("foo", 0, MIN_QUALITY)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("foo", items[0].name)
        self.assertEquals(MIN_QUALITY, items[0].quality)

    def test_maximal_quality(self):
        items = [Item("Aged Brie", 5, MAX_QUALITY)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("Aged Brie", items[0].name)
        self.assertEquals(MAX_QUALITY, items[0].quality)

    def test_decrease(self):
        items = [Item("foo", 1, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("foo", items[0].name)
        self.assertEquals(9, items[0].quality)

    def test_aged_brie(self):
        items = [Item("Aged Brie", 3, 12)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("Aged Brie", items[0].name)
        self.assertEquals(13, items[0].quality)


if __name__ == '__main__':
    unittest.main()
