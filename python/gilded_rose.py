# -*- coding: utf-8 -*-
from enum import Enum

MAX_QUALITY = 50
MIN_QUALITY = 0


class ItemType(Enum):
    AGED_BRIE = "Aged Brie"
    BACKSTAGE_PASSES = "Backstage passes to a TAFKAL80ETC concert"
    SULFURAS = "Sulfuras, Hand of Ragnaros"
    DEFAULT = None

    @classmethod
    def _missing_(cls, value):
        return cls.DEFAULT


class ItemQualityUpdater:
    @staticmethod
    def _update_quality(sell_in: int, quality: int) -> int:
        if sell_in >= 0:
            return quality - 1

        return quality - 2

    @classmethod
    def get_updated_quality(cls, sell_in: int, quality: int) -> int:
        updated_quality = cls._update_quality(sell_in, quality)

        if updated_quality >= MAX_QUALITY:
            return MAX_QUALITY

        if updated_quality < MIN_QUALITY:
            return MIN_QUALITY

        return updated_quality


class BackstagePassesUpdater(ItemQualityUpdater):
    @staticmethod
    def _update_quality(sell_in: int, quality: int) -> int:
        if sell_in == 0:
            return 0
        if sell_in <= 5:
            return quality + 3
        if sell_in <= 10:
            return quality + 2

        return quality + 1


class AgedBrieUpdater(ItemQualityUpdater):
    @staticmethod
    def _update_quality(sell_in: int, quality: int) -> int:
        return quality + 1


class SulfurasUpdater(ItemQualityUpdater):
    @classmethod
    def get_updated_quality(cls, sell_in: int, quality: int) -> int:
        return quality


MAP_ITEM_TYPE_TO_QUALITY = {
    ItemType.DEFAULT: ItemQualityUpdater,
    ItemType.BACKSTAGE_PASSES: BackstagePassesUpdater,
    ItemType.AGED_BRIE: AgedBrieUpdater,
    ItemType.SULFURAS: SulfurasUpdater,
}


class GildedRose:

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            item_type = ItemType(item.name)
            item.quality = MAP_ITEM_TYPE_TO_QUALITY[item_type].get_updated_quality(
                sell_in=item.sell_in, quality=item.quality
            )


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
