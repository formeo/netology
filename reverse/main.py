"""
Домашнее задание для лекции "Задачки на собеседованиях для продвинутых,
с тонкостями языка"

Описание
    1. Перестроить заданный связанный список (LinkedList) в обратном порядке.
    Для этого использовать метод `LinkedList.reverse()`, представленный
    в данном файле.
    2. Определить сложность алгоритма.
    3. Определить потребление памяти в big-O notation.

Примечание
    Проверить работоспособность решения можно при помощи тестов,
    которые можно запустить следующей командой:

    python3 -m unittest linked_list_reverse.py
"""

import unittest

from typing import Iterable

from memory_profiler import profile


class LinkedListNode:

    def __init__(self, data):
        self.data = data
        self.next = None  # type: LinkedListNode


class LinkedList:

    def __init__(self, values: Iterable):
        previous = None
        self.head = None
        for value in values:
            current = LinkedListNode(value)
            if previous:
                previous.next = current
            self.head = self.head or current
            previous = current

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next
    @profile
    def reverse(self):
        # задача сводится к перенаправлению указателе на предыдущие значения
        # сложность O(n)
        # если пустой или один элемент
        if not self.head or not self.head.next:
            return
        node = self.head
        while node.next.next:
            node = node.next
        last_node = node.next
        node.next = None
        self.reverse()
        last_node.next = self.head
        self.head = last_node

class LinkedListTestCase(unittest.TestCase):

    def test_reverse(self):
        cases = dict(
            empty=dict(
                items=[],
                expected_items=[],
            ),
            single=dict(
                items=[1],
                expected_items=[1],
            ),
            double=dict(
                items=[1, 2],
                expected_items=[2, 1],
            ),
            triple=dict(
                items=[1, 2, 3],
                expected_items=[3, 2, 1],
            ),
        )
        for case, data in cases.items():
            with self.subTest(case=case):
                linked_list = LinkedList(data['items'])
                linked_list.reverse()
                self.assertListEqual(
                    data['expected_items'],
                    list(linked_list),
                )
# ,
#             single=dict(
#                 items=[1],
#                 expected_items=[1],
#             ),
#             double=dict(
#                 items=[1, 2],
#                 expected_items=[2, 1],
#             ),
#             triple=dict(
#                 items=[1, 2, 3],
#                 expected_items=[3, 2, 1],
#             ),