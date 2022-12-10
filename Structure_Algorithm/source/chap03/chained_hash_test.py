# [Do it! �ǽ� 3-6] ü�ι��� �����ϴ� �ؽ� Ŭ���� ChainedHash�� ���

from enum import Enum
from chained_hash import ChainedHash

Menu = Enum('Menu', ['�߰�', '����', '�˻�', '����', '����'])  # �޴��� ����

def select_menu() -> Menu:
    """�޴� ����"""
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep = '   ', end='')
        n = int(input(': '))
        if 1 <=  n <=  len(Menu):
            return Menu(n)

hash = ChainedHash(13)     # ũ�Ⱑ 13�� �ؽ� ���̺��� ����

while True:
    menu = select_menu()   # �޴� ����

    if menu == Menu.�߰�:  # �߰�
        key = int(input('�߰��� Ű�� �Է��ϼ���.: '))
        val = input('�߰��� ���� �Է��ϼ���.: ')
        if not hash.add(key, val):
            print('�߰��� �����߽��ϴ�!')

    elif menu == Menu.����:  # ����
        key = int(input('������ Ű�� �Է��ϼ���.: '))
        if not hash.remove(key):
            print('������ �����߽��ϴ�!')

    elif menu == Menu.�˻�:  # �˻�
        key = int(input('�˻��� Ű�� �Է��ϼ���.: '))
        t = hash.search(key)
        if t is not None:
            print(f'�˻��� Ű�� ���� ���� {t}�Դϴ�.')
        else:
            print('�˻��� �����Ͱ� �����ϴ�.')

    elif menu == Menu.����:  # ����
        hash.dump()

    else:  # ����
        break
