#!/usr/bin/python3

"""
    Interview prepration exercise: Lock Boxes
"""


def canUnlockAll(boxes):
    """
        A method that determines if all boxes can be opened.
        Boxes is a list of lists.
        A key with the same number as a box opens that box.
        You can assume all keys will be positive integers.
        There can be keys that do not have boxes.
        The first box boxes[0] is unlocked.
        Return True if all boxes can be opened, else return False.
    """
    length = len(boxes)
    keys = set()
    opened = []
    i = 0

    while i < length:
        temp = i
        opened.append(i)
        keys.update(boxes[i])
        for key in keys:
            if key != 0 and key < length and key not in opened:
                i = key
                break
        if temp == i:
            break

    for i in range(length):
        if i not in opened and i != 0:
            return False
    return True
