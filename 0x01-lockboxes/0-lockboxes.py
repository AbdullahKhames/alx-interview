#!/usr/bin/python3
"""
function that solves the lockboxes problem
"""


def canUnlockAll(boxes):
    """
    function to check if all boxes can be unlocked
    :param boxes: list of lists
    :return:true if all boxes can be opened else false
    """
    boxes_count = len(boxes)
    keys = {0}
    keys.update(boxes[0])
    temp = set()
    for key in keys:
        if key < len(boxes):
            temp.update(boxes[key])
    keys.update(temp)

    for i in range(boxes_count):
        if i in keys:
            keys.update(boxes[i])

    # filter any number out of the set if it is less than zero or more than len boxes
    filtered = [x for x in keys if checkNum(x, boxes_count)]
    return boxes_count == len(filtered)


def checkNum(num, max_range):
    """
    function to check if num is within accepted range 0 - max_range
    :param num: number to be checked
    :param max_range: range
    :return:true if all boxes can be opened else false
    """
    return 0 <= num <= max_range
