#! /usr/bin/env python
import sys


# pep8 & google python style


class Node(object):
    def __init__(self, idx, value):
        self.left = None
        self.right = None
        self.parent = None
        self.idx = idx
        self.value = value
        self.path = [self.idx]  # [].append(self.idx)
        pass

    def check(self, arr):
        pass

    # build binary tree based on 'arr'
    def build(self, node):
        pass

    def findpath(self, start, end, arr):
        pass

    pass


def findpath(arr, start, end):
    first, last = 1, len(arr)
    iterator_list, enque_list = [start], [start]

    while len(enque_list) > 0:
        current = enque_list.pop(0)
        current_step = arr[current - 1]

        left_idx = current + current_step
        if left_idx <= last:
            left_node = Node(left_idx, arr[left_idx - 1])
            if left_idx not in iterator_list:
                enque_list.append(left_idx)
                iterator_list.append(left_idx)
                tree.append(left_node)

        right_idx = current - current_step
        if right_idx > first - 1:
            right_node = Node(right_idx, arr[right_idx - 1])
            if right_idx not in iterator_list:
                enque_list.append(right_idx)
                iterator_list.append(right_idx)
                tree.append(right_node)
        pass
    if end in iterator_list:
        print iterator_list
    else:
        print 'path not exist'
    pass


if __name__ == '__main__':
    level = [1, 2, 3, 4, 5]
    step_arr = [2, 1, 1, 4, 3]
    start, end = 1, 5
    root = Node(start, step_arr[start - 1])
    tree = [root]
    findpath(step_arr, start, end)

    step_arr = [2, 1, 2, 3, 3]
    start, end = 1, 5
    findpath(step_arr, start, end)