# Do it! �ǽ� 3-7 ���� �ּҹ����� �ؽ��Լ� �����ϱ�

from __future__ import annotations
from typing import Any, Type
from enum import Enum
import hashlib

# ��Ŷ�� �Ӽ�
class Status(Enum):
    OCCUPIED = 0  # �����͸� ����
    EMPTY = 1     # ��� ����
    DELETED = 2   # ���� �Ϸ�

class Bucket:
    """�ؽø� �����ϴ� ��Ŷ"""

    def __init__(self, key: Any = None, value: Any = None,
                       stat: Status = Status.EMPTY) -> None:
        """�ʱ�ȭ"""
        self.key = key      # Ű
        self.value = value  # ��
        self.stat = stat    # �Ӽ�

    def set(self, key: Any, value: Any, stat: Status) -> None:
        """��� �ʵ忡 ���� ����"""
        self.key = key      # Ű
        self.value = value  # ��
        self.stat = stat    # �Ӽ�

    def set_status(self, stat: Status) -> None:
        """�Ӽ��� ����"""
        self.stat = stat

class OpenHash:
    """���� �ּҹ��� �����ϴ� �ؽ� Ŭ����"""

    def __init__(self, capacity: int) -> None:
        """�ʱ�ȭ"""
        self.capacity = capacity                 # �ؽ� ���̺��� ũ�⸦ ����
        self.table = [Bucket()] * self.capacity  # �ؽ� ���̺�

    def hash_value(self, key: Any) -> int:
        """�ؽð��� ����"""
        if isinstance(key, int):
            return key % self.capacity
        return(int(hashlib.md5(str(key).encode()).hexdigest(), 16)
                % self.capacity)

    def rehash_value(self, key: Any) -> int:
        """���ؽð��� ����"""
        return(self.hash_value(key) + 1) % self.capacity

    def search_node(self, key: Any) -> Any:
        """Ű�� key�� ��Ŷ�� �˻�"""
        hash = self.hash_value(key)  # �˻��ϴ� Ű�� �ؽð�
        p = self.table[hash]         # ��Ŷ�� �ָ�

        for i in range(self.capacity):
            if p.stat == Status.EMPTY:
                break
            elif p.stat == Status.OCCUPIED and p.key == key:
                return p
            hash = self.rehash_value(hash)  # ���ؽ�
            p = self.table[hash]
        return None

    def search(self, key: Any) -> Any:
        """Ű�� key�� ���� ���Ҹ� �˻��Ͽ� ���� ��ȯ"""
        p = self.search_node(key)
        if p is not None:
            return p.value  # �˻� ����
        else:
            return None     # �˻� ����

    def add(self, key: Any, value: Any) -> bool:
        """Ű�� key�̰� ���� value�� ��Ҹ� �߰�"""
        if self.search(key) is not None:
            return False             # �̹� ��ϵ� Ű

        hash = self.hash_value(key)  # �߰��ϴ� Ű�� �ؽð�
        p = self.table[hash]         # ��Ŷ�� �ָ�
        for i in range(self.capacity):
            if p.stat == Status.EMPTY or p.stat == Status.DELETED:
                self.table[hash] = Bucket(key, value, Status.OCCUPIED)
                return True
            hash = self.rehash_value(hash)  # ���ؽ�
            p = self.table[hash]
        return False                        # �ؽ� ���̺��� ���� ��

    def remove(self, key: Any) -> int:
        """Ű�� key�� ���� ��Ҹ� ����"""
        p = self.search_node(key)  # ��Ŷ�� �ָ�
        if p is None:
            return False           # �� Ű�� ��ϵǾ� ���� ����
        p.set_status(Status.DELETED)
        return True

    def dump(self) -> None:
        """�ؽ� ���̺��� ����"""
        for i in range(self.capacity):
            print(f'{i:2} ', end='')
            if self.table[i].stat == Status.OCCUPIED:
                print(f'{self.table[i].key} ({self.table[i].value})')
            elif self.table[i].stat == Status.EMPTY:
                print('-- �̵�� --')
            elif self.table[i] .stat == Status.DELETED:
                print('-- ���� �Ϸ� --')
