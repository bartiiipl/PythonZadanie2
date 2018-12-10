#!/usr/bin/env python3


class Flower:
    pass


flower = Flower()

print(flower)
print(isinstance(flower, Flower))
print(isinstance(flower, object))


class PottedFlower(Flower):
    pass


class Orchid(PottedFlower):
    pass


potted_flower = PottedFlower()
orchid = Orchid()

print(potted_flower)
print(isinstance(potted_flower, Flower))
print(isinstance(potted_flower, PottedFlower))
print(isinstance(potted_flower, object))

print(orchid)
print(isinstance(orchid, Flower))
print(isinstance(orchid, Orchid))
print(isinstance(orchid, object))

print(isinstance(potted_flower, Orchid))
print(isinstance(orchid, PottedFlower))
