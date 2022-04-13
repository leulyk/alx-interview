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
    unlocked = [False for i in range(len(boxes))]
    unlocked[0] = True
    for idx in range(len(boxes)):
        if unlocked[idx]:
            for key in boxes[idx]:
                unlocked[key] = True
                for discovered_key in boxes[key]:
                    unlocked[discovered_key] = True
    return all(unlocked)
