# [Do it! �ǽ� 8-1] �����ͷ� ���� ����Ʈ �����

from __future__ import annotations
from typing import Any, Type

class Node:
    """���� ����Ʈ�� ��� Ŭ����"""

    def __init__(self, data: Any = None, next: Node = None):
        """�ʱ�ȭ"""
        self.data = data  # ������
        self.next = next  # ���� ������

# Do it! �ǽ� 8-1 [B]
class LinkedList:
    """���� ����Ʈ Ŭ����"""

    def __init__(self) -> None:
        """�ʱ�ȭ"""
        self.no = 0          # ����� ����
        self.head = None     # �Ӹ� ���
        self.current = None  # �ָ� ���

    def __len__(self) -> int:
        """���� ����Ʈ�� ��� ������ ��ȯ"""
        return self.no

# Do it! �ǽ� 8-1 [C]
    def search(self, data: Any) -> int:
        """data�� ���� ���� ��带 �˻�"""
        cnt = 0
        ptr = self.head
        while ptr is not None:
            if ptr.data == data:
                self.current = ptr
                return cnt
            cnt += 1
            ptr = ptr.next
        return -1

    def __contains__(self, data: Any) -> bool:
        """���� ����Ʈ�� data�� ���ԵǾ� �ִ°�?"""
        return self.search(data) >= 0

# Do it! �ǽ� 8-1 [D]
    def add_first(self, data: Any) -> None:
        """�� �տ� ��带 ����"""
        ptr = self.head  # ���� ���� �Ӹ� ���
        self.head = self.current = Node(data, ptr)
        self.no += 1

# Do it! �ǽ� 8-1 [E]
    def add_last(self, data: Any):
        """�� ���� ��带 ����"""
        if self.head is None :    # ����Ʈ�� ��� ������
            self.add_first(data)  # �Ǿտ� ��� ����
        else:
            ptr = self.head
            while ptr.next is not None:
                ptr = ptr.next  # while���� ������ �� ptr�� ���� ��带 ����
            ptr.next = self.current = Node(data, None)
            self.no += 1

# Do it! �ǽ� 8-1 [F]
    def remove_first(self) -> None:
        """�Ӹ� ��带 ����"""
        if self.head is not None:  # ����Ʈ�� ��� ������
            self.head = self.current = self.head.next
        self.no -= 1

# Do it! �ǽ� 8-1 [G]
    def remove_last(self):
        """���� ��� ����"""
        if self.head is not None:
            if self.head.next is None :  # ��尡 1�� ���̶��
                self.remove_first()      # �Ӹ� ��带 ����
            else:
                ptr = self.head  # ��ĵ ���� ���
                pre = self.head  # ��ĵ ���� ����� ���� ���

                while ptr.next is not None:
                    pre = ptr
                    ptr = ptr.next # while�� ����� ptr�� ���� ��带 �����ϰ� pre�� �ǳ����� �� ��° ��带 ����
                pre.next = None  # pre�� ���� �� ���� ���
                self.current = pre
                self.no -= 1

# Do it! �ǽ� 8-1 [H]
    def remove(self, p: Node) -> None:
        """��� p�� ����"""
        if self.head is not None:
            if p is self.head:       # p�� �Ӹ� ??����̸�
                self.remove_first()  # �Ӹ� ��带 ����
            else:
                ptr = self.head

                while ptr.next is not p:
                    ptr = ptr.next
                    if ptr is None:
                        return  # ptr�� ����Ʈ�� �������� ����
                ptr.next = p.next
                self.current = ptr
                self.no -= 1

    def remove_current_node(self) -> None:
        """�ָ� ��带 ����"""
        self.remove(self.current)

    def clear(self) -> None:
        """��ü ��带 ����"""
        while self.head is not None:  # ��ü�� ��� �ְ� �� ������
            self.remove_first()       # �Ӹ� ��带 ����
        self.current = None
        self.no = 0

    def next(self) -> bool:
        """�ָ� ��带 �� ĭ �ڷ� ����"""
        if self.current is None or self.current.next is None:
            return False  # ������ �� ����
        self.current = self.current.next
        return True

# Do it! �ǽ� 8-1 [I]
    def print_current_node(self) -> None:
        """�ָ� ��带 ���"""
        if self.current is None:
            print('�ָ� ��尡 �������� �ʽ��ϴ�.')
        else:
            print(self.current.data)

    def print(self) -> None:
        """��� ��带 ���"""
        ptr = self.head

        while ptr is not None:
            print(ptr.data)
            ptr = ptr.next

# Do it! �ǽ� 8-1 [J]
    def __iter__(self) -> LinkedListIterator:
        """���ͷ�����(�ݺ���)�� ��ȯ"""
        return LinkedListIterator(self.head)

class LinkedListIterator:
    """Ŭ���� LinkedList�� ���ͷ�����(�ݺ���)�� Ŭ����"""

    def __init__(self, head: Node):
        self.current = head

    def __iter__(self) -> LinkedListIterator:
        return self

    def __next__(self) -> Any:
        if self.current is None:
            raise StopIteration
        else:
            data = self.current.data
            self.current = self.current.next
            return data
