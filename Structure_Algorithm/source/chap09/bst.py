# [Do it! �ǽ� 9-1] ���� �˻� Ʈ���� ����

from __future__ import annotations
from typing import Any, Type

class Node:
    """���� �˻� Ʈ���� ���"""
    def __init__(self, key: Any, value: Any, left: Node = None,
                 right: Node = None):
        """������"""
        self.key = key      # Ű
        self.value = value  # ��
        self.left = left    # ���� ������(���� �ڽ� ����)
        self.right = right  # ������ ������(������ �ڽ� ����)

class BinarySearchTree:
    """���� �˻� Ʈ��"""

    def __init__(self):
        """�ʱ�ȭ"""
        self.root = None  # ��Ʈ

# Do it! �ǽ� 9-1[B]
    def search(self, key: Any) -> Any:
        """Ű key�� ���� ��带 �˻�"""
        p = self.root           # ��Ʈ�� �ָ�
        while True:
            if p is None:       # �� �̻� ������ �� ������
                return None     # �˻� ����
            if key == p.key:    # key�� ��� p�� Ű�� ������
                return p.value  # �˻� ����
            elif key < p.key:   # key ���� ������
                p = p.left      # ���� ���� Ʈ������ �˻�
            else:               # key ���� ũ��
                p = p.right     # ������ ���� Ʈ������ �˻�

# Do it! �ǽ� 9-1[C]
    def add(self, key: Any, value: Any) -> bool:
        """Ű�� key�̰�, ���� value�� ��带 ����"""

        def add_node(node: Node, key: Any, value: Any) -> None:
            """node�� ��Ʈ�� �ϴ� ���� Ʈ���� Ű�� key�̰�, ���� value�� ��带 ����"""
            if key == node.key:
                return False  # key�� �����˻�Ʈ���� �̹� ����
            elif key < node.key:
                if node.left is None:
                    node.left = Node(key, value, None, None)
                else:
                    add_node(node.left, key, value)
            else:
                if node.right is None:
                    node.right = Node(key, value, None, None)
                else:
                    add_node(node.right, key, value)
            return True

        if self.root is None:
            self.root = Node(key, value, None, None)
            return True
        else:
            return add_node(self.root, key, value)

# # Do it! �ǽ� 9-1[D]
    def remove(self, key: Any) -> bool:
        """Ű�� key�� ��带 ����"""
        p = self.root           # ��ĵ ���� ���
        parent = None           # ��ĵ ���� ����� �θ� ���
        is_left_child = True    # p�� parent�� ���� �ڽ� ������� Ȯ��

        while True:
            if p is None:       # �� �̻� ������ �� ������
                return False    # �� Ű�� �������� ����

            if key == p.key:    # key�� ��� p�� Ű�� ������
                break           # �˻� ����
            else:
                parent = p                  # ������ �������� ���� �θ� ����
                if key < p.key:             # key ���� ������
                    is_left_child = True    # ���⼭ �������� ���� ���� �ڽ�
                    p = p.left              # ���� ���� Ʈ������ �˻�
                else:                       # key ���� ũ��
                    is_left_child = False   # ���⼭ �������� ���� ������ �ڽ�
                    p = p.right             # ������ ���� Ʈ������ �˻�

        if p.left is None:                  # p�� ���� �ڽ��� ������
            if p is self.root:
                self.root = p.right
            elif is_left_child:
                parent.left = p.right       # �θ��� ���� �����Ͱ� ������ �ڽ��� ����Ŵ
            else:
                parent.right = p.right      # �θ��� ������ �����Ͱ� ������ �ڽ��� ����Ŵ
        elif p.right is None:               # p�� ������ �ڽ��� ������
            if p is self.root:
                self.root = p.left
            elif is_left_child:
                parent.left = p.left        # �θ��� ���� �����Ͱ� ���� �ڽ��� ����Ŵ
            else:
                parent.right = p.left       # �θ��� ������ �����Ͱ� ���� �ڽ��� ����Ŵ
        else:
            parent = p
            left = p.left                   # ���� Ʈ�� �ȿ��� ���� ū ���
            is_left_child = True
            while left.right is not None:   # ���� ū ��� left�� �˻�
                parent = left
                left = left.right
                is_left_child = False

            p.key = left.key                # left�� Ű�� p�� �̵�
            p.value = left.value            # left�� �����͸� p�� �̵�
            if is_left_child:
                parent.left = left.left     # left�� ����
            else:
                parent.right = left.left    # left�� ����
        return True

# Do it! �ǽ� 9-1[E]
    def dump(self) -> None:
        """����(��� ��带 Ű�� ������������ ���)"""

        def print_subtree(node: Node):
            """node�� ��Ʈ�� �ϴ� ���� Ʈ���� ��带 Ű�� ������������ ���"""
            if node is not None:
                print_subtree(node.left)            # ���� ���� Ʈ���� ������������ ���
                print(f'{node.key}  {node.value}')  # node�� ���
                print_subtree(node.right)           # ������ ���� Ʈ���� ������������ ���

        print_subtree(self.root)

# Do it! �ǽ� 9-1[F]
    def min_key(self) -> Any:
        """���� ���� Ű"""
        if self.root is None:
            return None
        p = self.root
        while p.left is not None:
            p = p.left
        return p.key

    def max_key(self) -> Any:
        """���� ū Ű"""
        if self.root is None:
            return None
        p = self.root
        while p.right is not None:
            p = p.right
        return p.key
