# [Do it! �ǽ� 4-4] ���� ���� ť Ŭ����(FixedQueue)�� ����ϱ�

from enum import Enum
from fixed_queue import FixedQueue

Menu = Enum('Menu', ['��ť', '��ť', '��ũ', '�˻�', '����', '����'])

def select_menu() -> Menu:
    """�޴� ����"""
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep='   ', end='')
        n = int(input(': '))
        if 1 <= n <= len(Menu):
            return Menu(n)

q = FixedQueue(64)  # �ִ� 64���� ��ť�� �� �ִ� ť ����(���� ����)

while True:
    print(f'���� ������ ����: {len(q)} / {q.capacity}')
    menu = select_menu()   # �޴� ����

    if menu == Menu.��ť:  # ��ť
        x = int(input('��ť�� �����͸� �Է��ϼ���.: '))
        try:
            q.enque(x)
        except FixedQueue.Full:
            print('ť�� ���� á���ϴ�.')

    elif menu == Menu.��ť:  # ��ť
        try:
            x = q.deque()
            print(f'��ť�� �����ʹ� {x}�Դϴ�.')
        except FixedQueue.Empty:
            print('ť�� ��� �ֽ��ϴ�.')

    elif menu == Menu.��ũ:  # ��ũ
        try:
            x = q.peek()
            print(f'��ũ�� �����ʹ� {x}�Դϴ�.')
        except FixedQueue.Empty:
            print('ť�� ������ϴ�.')

    elif menu == Menu.�˻�:  # �˻�
        x = int(input('�˻��� ���� �Է��ϼ���.: '))
        if x in q:
            print(f'{q.count(x)}�� ���Եǰ�, �� ���� ��ġ�� {q.find(x)}�Դϴ�.')
        else:
            print('�˻����� ã�� �� �����ϴ�.')

    elif menu == Menu.����:  # ����
        q.dump()
    else:
        break
