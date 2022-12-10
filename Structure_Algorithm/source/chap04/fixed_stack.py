# ���� ���� ���� Ŭ���� FixedStack �����ϱ�
# Do it! �ǽ� 4-1 [A]
from typing import Any

class FixedStack:
    """���� ���� ���� Ŭ����"""

    class Empty(Exception):
        """��� �ִ� FixedStack�� pop �Ǵ� peek�� ȣ���� �� �������� ���� ó��"""
        pass

    class Full(Exception):
        """���� �� FixedStack�� push�� ȣ���� �� �������� ���� ó��"""
        pass

    def __init__(self, capacity: int = 256) -> None:
        """�ʱ�ȭ"""
        self.stk = [None] * capacity  # ���� ��ü
        self.capacity = capacity      # ������ ũ��
        self.ptr = 0                  # ���� ������

    def __len__(self) -> int:
        """���ÿ� �׿��ִ� ������ ������ ��ȯ"""
        return self.ptr

    def is_empty(self) -> bool:
        """������ ��� �ִ°�?"""
        return self.ptr <= 0

    def is_full(self) -> bool:
        """������ ���� á�°�?"""
        return self.ptr >= self.capacity

# Do it! �ǽ� 4-1 [B]
    def push(self, value: Any) -> None:
        """���ÿ� value�� Ǫ��"""
        if self.is_full():              # ������ ���� ��
            raise FixedStack.Full
        self.stk[self.ptr] = value
        self.ptr += 1

    def pop(self) -> Any:
        """���ÿ��� �����͸� ��(����� �����͸� ����)"""
        if self.is_empty():             # ������ ��� ����
             raise FixedStack.Empty
        self.ptr -= 1
        return self.stk[self.ptr]

    def peek(self) -> Any:
        """���ÿ��� �����͸� ��ũ(����� �����͸� �鿩�� ��)"""
        if self.is_empty():             # ������ ��� ����
            raise FixedStack.Empty
        return self.stk[self.ptr - 1]

    def clear(self) -> None:
        """������ ���(��� �����͸� ����)"""
        self.ptr = 0

# Do it! �ǽ� 4-1 [C]
    def find(self, value: Any) -> Any:
        """���ÿ��� value�� ã�� ÷��(������ -1)�� ��ȯ"""
        for i in range(self.ptr - 1, -1, -1):  # ����� �ʺ��� ���� �˻�
            if self.stk[i] == value:
                return i  # �˻� ����
        return -1         # �˻� ����

    def count(self, value: Any) -> bool:
        """���ÿ� ���ԵǾ��ִ� value�� ������ ��ȯ"""
        c = 0
        for i in range(self.ptr):  # �ٴ� �ʺ��� ���� �˻�
            if self.stk[i] == value:
                c += 1             # ��� ����
        return c

    def __contains__(self, value: Any) -> bool:
        """���ÿ� value�� �ִ°�?"""
        return self.count(value)

    def dump(self) -> None:
        """����(���� ���� ��� �����͸� �ٴں��� ����� ������ ���)"""
        if self.is_empty():  # ������ ��� ����
            print('������ ��� �ֽ��ϴ�.')
        else:
            print(self.stk[:self.ptr])
