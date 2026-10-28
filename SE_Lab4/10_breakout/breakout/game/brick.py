"""Brick types and their hit durability."""

import pygame


class Brick:
    TYPES = {
        "normal": {"hits": 1, "color": (200, 90, 90)},
        "strong": {"hits": 3, "color": (235, 155, 55)},
        "unbreakable": {"hits": None, "color": (115, 145, 175)},
    }

    def __init__(self, x, y, width, height, brick_type="normal"):
        if brick_type not in self.TYPES:
            raise ValueError(f"Unknown brick type: {brick_type}")

        settings = self.TYPES[brick_type]
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.brick_type = brick_type
        self.hits_remaining = settings["hits"]
        self.color = settings["color"]

    def get_rect(self):
        return pygame.Rect(int(self.x), int(self.y), self.width, self.height)
