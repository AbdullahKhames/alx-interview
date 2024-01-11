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

    return boxes_count == len(keys)


if __name__ == '__main__':
    boxes = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes))

    boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes))

    boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes))
