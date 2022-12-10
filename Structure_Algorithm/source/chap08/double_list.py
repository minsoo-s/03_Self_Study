# ���� ���� ���� ����Ʈ �����ϱ�
# Do it! �ǽ� 8-5 [A] 
from __future__ import annotations
from typing import Any, Type

class Node:
    """���� ���� ���� ����Ʈ�� ��� Ŭ����"""

    def __init__(self, data: Any = None, prev: Node = None,
                       next: Node = None) -> None:
        """�ʱ�ȭ"""
        self.data = data          # ������
        self.prev = prev or self  # ���� ������
        self.next = next or self  # ���� ������

class DoubleLinkedList:
    """���� ���� ���� ����Ʈ Ŭ����"""

    def __init__(self) -> None:
        """�ʱ�ȭ"""
        self.head = self.current = Node()  # ���� ��带 ����
        self.no = 0

    def __len__(self) -> int:
        """���� ����Ʈ�� ��� ���� ��ȯ"""
        return self.no

    def is_empty(self) -> bool:
        """����Ʈ�� ��� �ִ°�?"""
        return self.head.next is self.head  

# Do it! �ǽ� 8-5 [B]
    def search(self, data: Any) -> Any:
        """data�� ���� ���� ��带 �˻�"""
        cnt = 0
        ptr = self.head.next  # ���� ��ĵ ���� ���
        while ptr is not self.head:
            if data == ptr.data:
                self.current = ptr
                return cnt  # �˻� ����
            cnt += 1
            ptr = ptr.next  # ���� ��忡 �ָ�
        return -1           # �˻� ����

    def __contains__(self, data: Any) -> bool:
        """���� ����Ʈ�� data�� ���ԵǾ� �ִ°�?"""
        return self.search(data) >= 0

# Do it! �ǽ� 8-5 [C]
    def print_current_node(self) -> None:
        """�ָ� ��带 ���"""
        if self.is_empty():
            print('�ָ� ���� �����ϴ�.')
        else:
            print(self.current.data)

    def print(self) -> None:
        """��� ��带 ���"""
        ptr = self.head.next  # ���� ����� ���� ���
        while ptr is not self.head:
            print(ptr.data)
            ptr = ptr.next

    def print_reverse(self) -> None:
        """��� ��带 �������� ���"""
        ptr = self.head.prev  # ���� ����� ���� ���
        while ptr is not self.head:
            print(ptr.data)
            ptr = ptr.prev

    def next(self) -> bool:
        """�ָ� ��带 �� ĭ �ڷ� �̵�"""
        if self.is_empty() or self.current.next is self.head:
            return False  # �̵��� �� ����
        self.current = self.current.next
        return True

    def prev(self) -> bool:
        """�ָ� ��带 �� ĭ ������ �̵�"""
        if self.is_empty() or self.current.prev is self.head:
            return False  # �̵��� �� ����
        self.current = self.current.prev
        return True

# Do it! �ǽ� 8-5[D]
    def add(self, data: Any) -> None:
        """�ָ� ����� �ٷ� �ڿ� ��带 ����"""
        node = Node(data, self.current, self.current.next)
        self.current.next.prev = node
        self.current.next = node
        self.current = node
        self.no += 1

    def add_first(self, data: Any) -> None:
        """�� �տ� ��带 ����"""
        self.current = self.head  # ���� ��� head�� �ٷ� �ڿ� ����
        self.add(data)

    def add_last(self, data: Any) -> None:
        """�� �ڿ� ��带 ����"""
        self.current = self.head.prev  # ���� ��� head.prev�� �ٷ� �ڿ� ����
        self.add(data)

# Do it! �ǽ� 8-5[E]
    def remove_current_node(self) -> None:
        """�ָ� ��� ����"""
        if not self.is_empty():
            self.current.prev.next = self.current.next
            self.current.next.prev = self.current.prev
            self.current = self.current.prev
            self.no -= 1
            if self.current is self.head:
                self.current = self.head.next

    def remove(self, p: Node) -> None:
        """��� p�� ����"""
        ptr = self.head.next

        while ptr is not self.head:
            if ptr is p:  # p�� �߰�
                self.current = p
                self.remove_current_node()
                break
            ptr = ptr.next

    def remove_first(self) -> None:
        """�Ӹ� ��� ����"""
        self.current = self.head.next  # �Ӹ� ��� head.next�� ����
        self.remove_current_node()

    def remove_last(self) -> None:
        """���� ��� ����"""
        self.current = self.head.prev  # ���� ��� head.prev�� ����
        self.remove_current_node()

    def clear(self) -> None:
        """��� ��带 ����"""
        while not self.is_empty():  # ����Ʈ ��ü�� �� ������
            self.remove_first()  # �Ӹ� ��带 ����
        self.no = 0

# Do it! �ǽ� 8-5[F]
    def __iter__(self) -> DoubleLinkedListIterator:
        """�ݺ��ڸ� ��ȯ"""
        return DoubleLinkedListIterator(self.head)

    def __reversed__(self) -> DoubleLinkedListReverseIterator:
        """�������� �ݺ��ڸ� ��ȯ"""
        return DoubleLinkedListReverseIterator(self.head)

class DoubleLinkedListIterator:
    """DoubleLinkedList�� �ݺ��ڿ� Ŭ����"""

    def __init__(self, head: Node):
        self.head = head
        self.current = head.next

    def __iter__(self) -> DoubleLinkedListIterator:
        return self

    def __next__(self) -> Any:
        if self.current is self.head:
            raise StopIteration
        else:
            data = self.current.data
            self.current = self.current.next
            return data

class DoubleLinkedListReverseIterator:
    """DoubleLinkedList�� �������� �ݺ��ڿ� Ŭ����"""

    def __init__(self, head: Node):
        self.head = head
        self.current = head.prev

    def __iter__(self) -> DoubleLinkedListReverseIterator:
        return self

    def __next__(self) -> Any:
        if self.current is self.head:
            raise StopIteration
        else:
            data = self.current.data
            self.current = self.current.prev
            return data
