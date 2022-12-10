# [Do it! 4C-1] ���� ���� ���� Ŭ����(collections.deque)�� ����ϱ�

from enum import Enum
from stack import Stack

Menu = Enum('Menu', ['Ǫ��', '��', '��ũ', '�˻�', '����', '����'])

def select_menu() -> Menu:
    """�޴� ����"""
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep='  ', end='')
        n = int(input('��'))
        if 1 <= n <= len(Menu):
            return Menu(n)

s = Stack(64)  # �ִ� 64 ���� Ǫ���� �� �ִ� ����

while True:
    print(f'���� ������ ������{len(s)} / {s.capacity}')
    menu = select_menu()  # �޴� ����

    if menu == Menu.Ǫ��:  # Ǫ��
        x = int(input('�����ͣ�'))
        try:
            s.push(x)
        except IndexError:
            print('������ ���� á���ϴ�.')

    elif menu == Menu.��:  # ��
        try:
            x = s.pop()
            print(f'���� �����ʹ� {x}�Դϴ�.')
        except IndexError:
           print('������ ��� �ֽ��ϴ�.')

    elif menu == Menu.��ũ:  # ��ũ
        try:
            x = s.peek()
            print(f'��ũ�� �����ʹ� {x}�Դϴ�.')
        except IndexError:
           print('������ ��� �ֽ��ϴ�.')

    elif menu == Menu.�˻�:  # �˻�
        x = int(input('�˻� ���� �Է��ϼ��䣺'))
        if x in s:
            print(f'{s.count(x)} ���� �����ϰ�, �� ������ ��ġ�� {s.find(x)}�Դϴ�.')
        else:
            print('�˻� ���� ���ԵǾ� ���� �ʽ��ϴ�.')
            
    elif menu == Menu.����:  # ����
        s.dump()

    else:
        break
