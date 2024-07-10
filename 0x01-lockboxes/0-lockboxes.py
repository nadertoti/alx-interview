#!/usr/bin/python3
"""
Module to determine if all boxes can be opened.
Using the function prototype: def canUnlockAll(boxes)
"""

def canUnlockAll(boxes):
    """
    Determine if all boxes can be unlocked
    """
    unlocked = [False] * len(boxes)
    unlocked[0] = True  # The first box is always unlocked
    keys = [0]  # Start with the keys from the first box

    while keys:
        new_keys = []
        for key in keys:
            for new_key in boxes[key]:
                if new_key < len(boxes) and not unlocked[new_key]:
                    unlocked[new_key] = True
                    new_keys.append(new_key)
        keys = new_keys

    return all(unlocked)
