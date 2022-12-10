# [Do it! �ǽ� 9C-1] ���� �˻� Ʈ�� Ŭ���� BinarySearchTree ����ϱ�(��������, ������������ ����)

from enum import Enum
from bst2 import BinarySearchTree

Menu = Enum('Menu', ['����', '����', '�˻�', '������������', '������������', 'Ű�ǹ���', '����'])

def select_Menu() -> Menu:
    """�޴� ����"""
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep = '  ', end='')
        n = int(input(' : '))
        if 1 <= n <= len(Menu):
            return Menu(n)

tree = BinarySearchTree()  # ���� �˻� Ʈ���� ����

while True:
    menu = select_Menu()  # �޴� ����

    if menu == Menu.����:  # ����
        key = int(input('������ Ű�� �Է��ϼ���.: '))
        val = input('������ ���� �Է��ϼ���.: ')
        if not tree.add(key, val):
            print('���Կ� �����߽��ϴ�!')

    elif menu == Menu.����:  # ����
        key = int(input('������ Ű�� �Է��ϼ���.: '))
        tree.remove(key)

    elif menu == Menu.�˻�:  # �˻�
        key = int(input('�˻��� Ű�� �Է��ϼ���.: '))
        t = tree.search(key)
        if t is not None:
            print(f'�� Ű�� ���� ���� {t}�Դϴ�.')
        else:
            print('�ش� �����Ͱ� �����ϴ�.')

    elif menu == Menu.������������:  # �������� ����
        tree.dump()


    elif menu == Menu.������������:  # �������� ����
        tree.dump(reverse = True)

    elif menu == Menu.Ű�ǹ��� :  # Ű�� ����(�ּڰ��� �ִ�)
        print(f'Ű�� �ּڰ��� {tree.min_key()}�Դϴ�.')
        print(f'Ű�� �ִ��� {tree.max_key()}�Դϴ�.')
        
    else:# ����
        break
