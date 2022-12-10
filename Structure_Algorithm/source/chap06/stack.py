# ���� ���� ���� Ŭ����(collections.deque�� ���) ���� ����

from typing import Any
from collections import deque

class Stack:
    """���� ���� ���� Ŭ����(collections.deque�� ���)"""

    def __init__(self, maxlen: int = 256) -> None:
        """�ʱ�ȭ ����"""
        self.capacity = maxlen
        self.__stk = deque([], maxlen)

    def __len__(self) -> int:
        """���ÿ� �׿��ִ� ������ ������ ��ȯ"""
        return len(self.__stk)

    def is_empty(self) -> bool:
        """������ ��� �ִ��� �Ǵ�"""
        return not self.__stk

    def is_full(self) -> bool:
        """������ ���� á���� �Ǵ�"""
        return len(self.__stk) == self.__stk.maxlen

    def push(self, value: Any) -> None:
        """���ÿ� value�� Ǫ��"""
        self.__stk.append(value)

    def pop(self) -> Any:
        """���ÿ��� �����͸� ��"""
        return self.__stk.pop()

    def peek(self) -> Any:
        """���ÿ��� �����͸� ��ũ"""
        return self.__stk[-1]

    def clear(self) -> None:
        """������ ���ϴ�"""
        self.__stk.clear()

    def find(self, value: Any) -> Any:
        """���ÿ��� value�� ã�� �ε���(������ -1)�� ��ȯ"""
        try:
            return self.__stk.index(value)
        except ValueError:
            return -1

    def count(self, value: Any) -> int:
        """���ÿ� ���Ե� value�� ������ ��ȯ"""
        return self.__stk.count(value)

    def __contains__(self, value: Any) -> bool:
        """���ÿ� value�� ���ԵǾ� �ִ��� �Ǵ�"""
        return self.count(value)

    def dump(self) -> int:
        """���� �ȿ� �ִ� ��� �����͸� ����"""
        print(list(self.__stk))
