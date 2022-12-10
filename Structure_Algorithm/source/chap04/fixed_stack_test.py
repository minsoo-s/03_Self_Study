# [Do it! �ǽ� 4-2] ���� ���� ���� FixedStack�� ����ϱ�

from enum import Enum
from fixed_stack import FixedStack

Menu = Enum('Menu', ['Ǫ��', '��', '��ũ', '�˻�', '����', '����'])

def select_menu() -> Menu:
    """�޴� ����"""
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep = '   ', end='')
        n = int(input(': '))
        if 1 <= n <= len(Menu):
            return Menu(n)

s = FixedStack(64)  # �ִ� 64���� Ǫ���� �� �ִ� ����

while True:
    print(f'���� ������ ����: {len(s)} / {s.capacity}')
    menu = select_menu()  # �޴� ����
    
    if menu == Menu.Ǫ��:  # Ǫ��
        x = int(input('�����͸� �Է��ϼ���.: '))
        try:
            s.push(x)
        except FixedStack.Full:
            print('������ ���� �� �ֽ��ϴ�.')

    elif menu == Menu.��:  # ��
        try:
            x = s.pop()
            print(f'���� �����ʹ� {x}�Դϴ�.')
        except FixedStack.Empty:
            print('������ ��� �ֽ��ϴ�.')

    elif menu == Menu.��ũ:  # ��ũ
        try:
            x = s.peek()
            print(f'��ũ�� �����ʹ� {x}�Դϴ�.')
        except FixedStack.Empty:
            print('������ ��� �ֽ��ϴ�.')

    elif menu == Menu.�˻�:  # �˻�
        x = int(input('�˻��� ���� �Է��ϼ���.: '))
        if x in s:
            print(f'{s.count(x)}�� ���Եǰ�, �� ���� ��ġ�� {s.find(x)}�Դϴ�.')
        else:
            print('�˻����� ã�� �� �����ϴ�.')

    elif menu == Menu.����:  # ����
        s.dump()

    else:
        break
