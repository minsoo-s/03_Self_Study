# ü�ι����� �ؽ� �Լ� �����ϱ�
# Do it! �ǽ� 3-5 [A]
from __future__ import annotations
from typing import Any, Type
import hashlib

class Node:
    """�ؽø� �����ϴ� ���"""

    def __init__(self, key: Any, value: Any, next: Node) -> None:
        """�ʱ�ȭ"""
        self.key   = key    # Ű
        self.value = value  # ��
        self.next  = next   # ���� ��带 ����

# Do it! �ǽ� 3-5 [B]
class ChainedHash:
    """ü�ι��� �ؽ� Ŭ���� ����"""

    def __init__(self, capacity: int) -> None:
        """�ʱ�ȭ"""
        self.capacity = capacity             # �ؽ� ���̺��� ũ�⸦ ����
        self.table = [None] * self.capacity  # �ؽ� ���̺�(����Ʈ)�� ����

    def hash_value(self, key: Any) -> int:
        """�ؽð��� ����"""
        if isinstance(key, int):
            return key % self.capacity
        return(int(hashlib.sha256(str(key).encode()).hexdigest(), 16) % self.capacity)

# Do it! �ǽ� 3-5[C]
    def search(self, key: Any) -> Any:
        """Ű�� key�� ���Ҹ� �˻��Ͽ� ���� ��ȯ"""
        hash = self.hash_value(key)  # �˻��ϴ� Ű�� �ؽð�
        p = self.table[hash]         # ��带 ���

        while p is not None:
            if p.key == key:
                 return p.value  # �˻� ����
            p = p.next           # ���� ��带 �ָ�

        return None              # �˻� ����

    def add(self, key: Any, value: Any) -> bool:
        """Ű�� key�̰� ���� value�� ���Ҹ� ����"""
        hash = self.hash_value(key)  # �����ϴ� Ű�� �ؽð�
        p = self.table[hash]         # �ָ��ϴ� ���

        while p is not None:
            if p.key == key:
                return False         # ���� ����
            p = p.next               # ���� ��忡 �ָ�

        temp = Node(key, value, self.table[hash])
        self.table[hash] = temp      # ��带 ����
        return True                  # ���� ����

# Do it! �ǽ� 3-5[D]
    def remove(self, key: Any) -> bool:
        """Ű�� key�� ���Ҹ� ����"""
        hash = self.hash_value(key)  # ������ Ű�� �ؽð�
        p = self.table[hash]         # �ָ��ϰ� �ִ� ���
        pp = None                    # �ٷ� �� �ָ� ���

        while p is not None:
            if p.key == key:  # key�� �߰��ϸ� �Ʒ��� ����
                if pp is None:
                    self.table[hash] = p.next
                else:
                    pp.next = p.next
                return True  # key ���� ����
            pp = p
            p = p.next       # ���� ��忡 �ָ�
        return False         # ���� ����(key�� �������� ����)

    def dump(self) -> None:
        """�ؽ� ���̺��� ����"""
        for i in range(self.capacity):
            p = self.table[i]
            print(i, end='')
            while p is not None:
                print(f'  �� {p.key} ({p.value})', end='')  # �ؽ� ���̺� �ִ� Ű�� ���� ���
                p = p.next
            print()
