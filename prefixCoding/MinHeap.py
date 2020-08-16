# -*- encoding: utf-8 -*-
class MinHeap:
    """MinHeap's elements are objects of Node class"""
    def __init__(self):
        self.list = []
        self.size = 0

    def insert(self, element):
        """Inserts an element into the min-heap"""
        self.list.append(element)
        self.size += 1
        i = self.size - 1
        parent = (i - 1) // 2
        while i > 0 and self.list[parent].value > self.list[i].value:
            self.list[parent], self.list[i] = self.list[i], self.list[parent]
            i = parent
            parent = (i - 1) // 2

    def heapify(self, i):
        """Heapifies min-heap when its main feature is broken"""
        while True:
            left_child = 2 * i + 1
            right_child = 2 * i + 2
            smallest_child = i
            if left_child < self.size and self.list[left_child].value < self.list[smallest_child].value:
                smallest_child = left_child
            if right_child < self.size and self.list[right_child].value < self.list[smallest_child].value:
                smallest_child = right_child
            if smallest_child == i:
                break
            self.list[smallest_child], self.list[i] = self.list[i], self.list[smallest_child]
            i = smallest_child

    def extract(self):
        """Extracts minimal (root) element of min-heap"""
        result = self.list[0]
        self.list[0] = self.list[self.size - 1]
        del self.list[self.size - 1]
        self.size -= 1
        self.heapify(0)
        return result

    def buildHeap(self, array):
        """Builds min-heap from given array"""
        self.list = array
        self.size = len(self.list)
        for i in range(self.size // 2, -1, -1):
            self.heapify(i)


class Node:
    """Binary tree's node"""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.key = None

    def __repr__(self):
        return f'({self.left}, {self.value}, {self.right})'
