# [Do it! �ǽ� 8-6] ���� ���� ���� ����Ʈ Ŭ���� DoubleLinkedList �����ϱ�

from enum import Enum
from double_list import DoubleLinkedList

Menu = Enum('Menu', ['�Ӹ���������', '������������', '�ָ���ٷεڻ���',
                     '�Ӹ�������', '����������', '�ָ������',
                     '�ָ����̵�', '�ָ��忪���̵�', '�ָ������',
                     '��������', '�˻�', '������Ǵ�', '��������',
                     '����忪�����', '����彺ĵ', '����忪����ĵ', '����'])

def select_Menu() -> Menu:
    """�޴� ����"""
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep = '  ', end='')
        n = int(input(': '))
        if 1 <= n <= len(Menu):
            return Menu(n)

lst = DoubleLinkedList()  # ����?���� ���� ����Ʈ ����

while True:
    menu = select_Menu()  # �޴� ����

    if menu == Menu.�Ӹ���������:  # �� �տ� ��� ����
        lst.add_first(int(input('�Ӹ� ��忡 ���� ���� �Է��ϼ���.: ')))

    elif menu == Menu.������������:  # �� ���� ��� ����
        lst.add_last(int(input('���� ��忡 ���� ���� �Է��ϼ���.: ')))

    elif menu == Menu.�ָ���ٷεڻ���:  # �ָ� ��� �ٷ� �ڿ� ����
        lst.add(int(input('�ָ� ��� �ٷ� �ڿ� ���� ���� �Է��ϼ��� : ')))

    elif menu == Menu.�Ӹ�������:  # �� �� ��� ����
        lst.remove_first()

    elif menu == Menu.����������:  # �� �� ��� ����
        lst.remove_last()

    elif menu == Menu.�ָ������:  # �ָ� ��� ���
        lst.print_current_node()

    elif menu == Menu.�ָ����̵�:  # �ָ� ��带 �� ĭ �ڷ� �̵�
        lst.next()

    elif menu == Menu.�ָ��忪���̵�:  # �ָ� ��带 �� ĭ ������ �̵�
        lst.prev()

    elif menu == Menu.�ָ������:  # �ָ� ��� ����
        lst.remove_current_node()

    elif menu == Menu.��������:  # ��� ����
        lst.clear()

    elif menu == Menu.�˻�:  # �˻�
        pos = lst.search(int(input('�˻��� ���� �Է��ϼ���.: ')))
        if pos >= 0:
            print(f'�� ���� �����ʹ� {pos + 1}��°�� �ֽ��ϴ�.')
        else:
            print('�ش� �����Ͱ� �����ϴ�.')

    elif menu == Menu.������Ǵ�:  # ����� �Ǵ�
        print('�� ���� �����ʹ� ���ԵǾ�'
              +(' �ֽ��ϴ�.' if int(input('�Ǵ��� ���� �Է��ϼ���.: ')) in lst else ' ���� �ʽ��ϴ�.'))

    elif menu == Menu.��������:  # ��� ��带 ���
        lst.print()

    elif menu == Menu.����忪�����:  # ��� ��� ���� ���
        lst.print_reverse()

    elif menu == Menu.����彺ĵ:  # ��� ��� ��ĵ
        for e in lst:
             print(e)

    elif menu == Menu.����忪����ĵ:  # ��� ��� ���� ��ĵ
        for e in reversed(lst):
             print(e)

    else:  # ����
        break
