# [Do it! �ǽ� 8-2] �����ͷ� �̿��� ���� ����Ʈ Ŭ���� LinkedList ����ϱ�

from enum import Enum
from linked_list import LinkedList

Menu = Enum('Menu', ['�Ӹ���������', '������������', '�Ӹ�������',
                     '����������', '�ָ������', '�ָ����̵�',
                     '�ָ������', '��������', '�˻�', '������Ǵ�',
                     '��������', '��ĵ', '����',])

def select_Menu() -> Menu:
    """�޴� ����"""
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep='  ', end='')
        n = int(input(': '))
        if 1 <= n <= len(Menu):
            return Menu(n)


lst = LinkedList()  # ���� ����Ʈ�� ����

while True:
    menu = select_Menu()  # �޴� ����

    if menu == Menu.�Ӹ���������:  # �� �տ� ��� ����
        lst.add_first(int(input('�Ӹ��� ���� ���� �Է��ϼ���.: ')))

    elif menu == Menu.������������:  # �� ���� ��� ����
        lst.add_last(int(input('������ ���� ���� �Է��ϼ���.: ')))

    elif menu == Menu.�Ӹ�������:  # �� �� ��� ����
        lst.remove_first()

    elif menu == Menu.����������:  # �� �� ��� ����
        lst.remove_last()

    elif menu == Menu.�ָ������:  # �ָ� ��� ���
        lst.print_current_node()

    elif menu == Menu.�ָ����̵�:  # �ָ� ��带 �� ĭ �ڷ� �̵�
        lst.next()

    elif menu == Menu.�ָ������:  # �ָ� ��� ����
        lst.remove_current_node()

    elif menu == Menu.��������:  # ��� ��带 ����
        lst.clear()

    elif menu == Menu.�˻�:  # ��带 �˻�
        pos = lst.search(int(input('�˻��� ���� �Է��ϼ���.: ')))
        if pos >= 0:
            print(f'�� ���� �����ʹ� {pos + 1}��°�� �ֽ��ϴ�.')
        else:
            print('�ش� �����Ͱ� �����ϴ�.')

    elif menu == Menu.������Ǵ�:  # ����� �Ǵ�
        print('�� ���� �����ʹ� ���ԵǾ�' + (' �ֽ��ϴ�.' if int(input('����� �Ǵ��� ���� �Է��ϼ���.: ')) in lst else ' ���� �ʽ��ϴ�.'))

    elif menu == Menu.��������:  # ��� ��� ���
        lst.print()

    elif menu == Menu.��ĵ:  # ��� ��� ��ĵ
        for e in lst:
            print(e)

    else:  # ����
        break
