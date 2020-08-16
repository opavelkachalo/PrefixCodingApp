# -*- encoding: utf-8 -*-
import random
import math
from prefixCoding.MinHeap import MinHeap, Node


def entropy(probabilities):
    """Returns entropy of given probabilities"""
    result = 0
    for i in probabilities:
        result -= i * math.log(i, 2)
    return result


def sorting_dict(proba_dict, reverse=True):
    """Sorts a dictionary by its values"""
    a = sorted(proba_dict, key=lambda x: proba_dict[x], reverse=reverse)
    b = sorted(list(proba_dict.values()), reverse=reverse)
    return {x: y for x, y in zip(a, b)}


def dividing(some_dict):
    """Divides dictionary of letters probabilities into two dictionaries and absolute difference between sum of
    values of these two dictionaries is minimal"""
    ps = list(some_dict.values())
    delta = abs(sum(ps[:1]) - sum(ps[1:]))
    delta_index = 1
    for i in range(2, len(ps)):
        delta_index = i - 1
        if abs(sum(ps[:i]) - sum(ps[i:])) < delta:
            delta = abs(sum(ps[:i]) - sum(ps[i:]))
        elif abs(sum(ps[:i]) - sum(ps[i:])) > delta:
            break
    keys1, keys2 = list(some_dict.keys())[:delta_index], list(some_dict.keys())[delta_index:]
    values1, values2 = list(some_dict.values())[:delta_index], list(some_dict.values())[delta_index:]
    return {i: j for i, j in zip(keys1, values1)}, {m: n for m, n in zip(keys2, values2)}


class ShannonFano:
    def __init__(self, proba_list, symbol_names=None):
        if symbol_names is None:
            self.probabilities = {'a' + str(i): x for i, x in enumerate(proba_list, 1)}
        else:
            self.probabilities = {i: j for i, j in zip(symbol_names, proba_list)}
        self.coded_alphabet = {i: '' for i in list(self.probabilities.keys())}

    def coding(self, proba_dict):
        """Returns coded alphabet using shannon-fano method. Takes probabilities dictionary as argument. It must be
        sorted using sorting_dict function"""
        if len(proba_dict) == 1:
            return
        seq1, seq2 = dividing(proba_dict)
        val1, val2 = random.choice([('0', '1'), ('1', '0')])
        for i in (seq1, seq2):
            for j in i:
                self.coded_alphabet[j] += val1 if i == seq1 else val2
        self.coding(seq1)
        self.coding(seq2)
        return self.coded_alphabet

    def mean_length(self):
        """Returns mean length of prefix code"""
        s = 0
        for i in self.coded_alphabet:
            s += len(self.coded_alphabet[i]) * self.probabilities[i]
        return s

    def entropy(self):
        """Returns entropy of alphabet frequencies"""
        result = 0
        for i in self.probabilities.values():
            result -= i * math.log(i, 2)
        return result


class Huffman(ShannonFano):
    def __init__(self, proba_list, symbol_names):
        """Creates nodes_array which will be used to build huffman tree"""
        ShannonFano.__init__(self, proba_list, symbol_names)
        self.nodes_array = []
        for i, j in zip(self.probabilities.keys(), self.probabilities.values()):
            self.nodes_array.append(Node(j))
            self.nodes_array[-1].key = i

    def build_huffman_tree(self):
        """Builds binary tree of huffman from a min-heap, which was built from nodes_array"""
        min_heap = MinHeap()
        min_heap.buildHeap(self.nodes_array)
        while min_heap.size > 1:
            left = min_heap.extract()
            right = min_heap.extract()
            node = Node(left.value + right.value)
            node.left = left
            node.right = right
            node.key = left.key + ', ' + right.key
            min_heap.insert(node)
        return min_heap.list[0]

    def coding(self, tree):
        """Returns coded alphabet using huffman tree. Must take huffman tree as argument"""
        if tree.left is None and tree.right is None:
            return
        for i in tree.left.key.split(', '):
            self.coded_alphabet[i] += '0'
        for i in tree.right.key.split(', '):
            self.coded_alphabet[i] += '1'
        self.coding(tree.left)
        self.coding(tree.right)
        return self.coded_alphabet
