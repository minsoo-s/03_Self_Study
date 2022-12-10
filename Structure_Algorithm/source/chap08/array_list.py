# [Do it! �ǽ� 8-3] Ŀ���� ���� ����Ʈ �����

from __future__ import annotations
from typing import Any, Type

Null = -1

class Node:
    """���� ����Ʈ�� ��� Ŭ����(�迭 Ŀ�� ����)"""

    def __init__(self, data = Null, next = Null, dnext = Null):
        """�ʱ�ȭ"""
        self.data  = data   # ������
        self.next  = next   # ����Ʈ�� ���� ������
        self.dnext = dnext  # ���� ����Ʈ�� ���� ������

class ArrayLinkedList:
    """���� ����Ʈ Ŭ����(�迭 Ŀ�� ����)"""

    def __init__(self, capacity: int):
        """�ʱ�ȭ"""
        self.head = Null                   # �Ӹ� ���
        self.current = Null                # �ָ� ���
        self.max = Null                    # ��� ���� �ǳ� ���ڵ�
        self.deleted = Null                # ���� ����Ʈ�� �Ӹ� ���
        self.capacity = capacity           # ����Ʈ�� ũ��
        self.n = [Node()] * self.capacity  # ����Ʈ ��ü
        self.no = 0


    def __len__(self) -> int:
        """���� ����Ʈ�� ��� ���� ��ȯ"""
        return self.no

    def get_insert_index(self):
        """������ ������ ���ڵ��� ÷�ڸ� ���մϴ�"""
        if self.deleted == Null:  # ���� ���ڵ�� �������� �ʽ��ϴ�
            if self.max+1 < self.capacity:
                self.max += 1
                return self.max   # �� ���ڵ带 ���
            else:
                return Null       # ũ�� �ʰ�
        else:
            rec = self.deleted                # ���� ����Ʈ����
            self.deleted = self.n[rec].dnext  # �� �� rec�� ������
            return rec

    def delete_index(self, idx: int) -> None:
        """���ڵ� idx�� ���� ����Ʈ�� ���"""
        if self.deleted == Null:      # ���� ���ڵ�� �������� �ʽ��ϴ�
            self.deleted = idx        # idx�� ���� ����Ʈ��
            self.n[idx].dnext = Null  # �� �տ� ���
        else:
            rec = self.deleted        # idx�� ���� ����Ʈ��
            self.deleted = idx        # �� �տ� ����
            self.n[idx].dnext = rec

    def search(self, data: Any) -> int:
        """data�� ���� ���� ��带 �˻�"""
        cnt = 0
        ptr = self.head             # ���� ��ĵ ���� ���
        while ptr != Null:
            if self.n[ptr].data == data:
                self.current = ptr
                return cnt          # �˻� ����
            cnt += 1
            ptr = self.n[ptr].next  # ���� ��忡 �ָ�
        return Null                 # �˻� ����

    def __contains__(self, data: Any) -> bool:
        """���� ����Ʈ�� data�� ���ԵǾ� �ִ��� Ȯ��"""
        return self.search(data) >= 0

    def add_first(self, data: Any):
        """�Ӹ� ��忡 ����"""
        ptr = self.head                     # �����ϱ� ���� �Ӹ� ���
        rec = self.get_insert_index()
        if rec != Null:
            self.head = self.current = rec  # rec��° ���ڵ忡 ����
            self.n[self.head] = Node(data, ptr)
            self.no += 1

    def add_last(self, data: Any) -> None:
        """���� ��忡 ����"""
        if self.head == Null:     # ����Ʈ�� ��� ������
            self.add_first(data)  # �� �տ� ��� ����
        else:
            ptr = self.head
            while self.n[ptr].next != Null:
                ptr = self.n[ptr].next
            rec = self.get_insert_index()

            if rec != Null:       # rec��° ���ڵ忡 ����
                self.n[ptr].next = self.current = rec
                self.n[rec] = Node(data)
                self.no += 1

    def remove_first(self) -> None:
        """�Ӹ� ��带 ����"""
        if self.head != Null:  # ����Ʈ�� ��� ������
            ptr = self.n[self.head].next
            self.delete_index(self.head)
            self.head = self.current = ptr
            self.no -= 1

    def remove_last(self) -> None:
        """���� ��带 ����"""
        if self.head != Null:
            if self.n[self.head].next == Null:  # ��尡 1�� ���̸�
                self.remove_first()             # �Ӹ� ��带 ����
            else:
                ptr = self.head                 # ��ĵ ���� ���
                pre = self.head                 # ��ĵ ���� ����� ���� ���

                while self.n[ptr].next != Null:
                    pre = ptr
                    ptr = self.n[ptr].next
                self.n[pre].next = Null  # pre�� ������ ���� ���� ���
                self.delete_index(ptr)
                self.current = pre
                self.no -= 1

    def remove(self, p: int) -> None:
        """���ڵ� p�� ����"""
        if self.head != Null:
            if p == self.head:       # p�� �Ӹ� ����
                self.remove_first()  # �Ӹ� ��带 ����
            else:
                ptr = self.head

                while self.n[ptr].next != p:
                    ptr = self.n[ptr].next
                    if ptr == Null:
                        return  # p�� ����Ʈ�� �������� ����
                #self.n[ptr].next = Null
                self.delete_index(p)
                self.n[ptr].next = self.n[p].next
                self.current = ptr
                self.no -= 1

    def remove_current_node(self) -> None:
        """�ָ� ��带 ����"""
        self.remove(self.current)

    def clear(self) -> None:
        """��� ��带 ����"""
        while self.head != Null:  # ����Ʈ ��ü�� �� ������
            self.remove_first()   # �Ӹ� ��带 ����
        self.current = Null

    def next(self) -> bool:
        """�ָ� ��带 �� ĭ �ڷ� ����"""
        if self.current == Null or self.n[self.current].next == Null:
            return False  # ������ �� ����
        self.current = self.n[self.current].next
        return True


    def print_current_node(self) -> None:
        """�ָ� ��带 ���"""
        if self.current == Null:
            print('�ָ� ��尡 �����ϴ�.')
        else:
            print(self.n[self.current].data)

    def print(self) -> None:
        """��� ��带 ���"""
        ptr = self.head

        while ptr != Null:
            print(self.n[ptr].data)
            ptr = self.n[ptr].next

    def dump(self) -> None:
        """�迭�� ����"""
        for i in self.n:
            print(f'[{i}]  {i.data} {i.next} {i.dnext}')

    def __iter__(self) -> ArrayLinkedListIterator:
        """���ͷ����͸� ��ȯ"""
        return ArrayLinkedListIterator(self.n, self.head)

class ArrayLinkedListIterator:
    """Ŭ���� ArrayLinkedList�� ���ͷ����Ϳ� Ŭ����"""

    def __init__(self, n: int, head: int):
        self.n = n
        self.current = head

    def __iter__(self) -> ArrayLinkedListIterator:
        return self

    def __next__(self) -> Any:
        if self.current == Null:
            raise StopIteration
        else:
            data = self.n[self.current].data
            self.current = self.n[self.current].next
            return data
