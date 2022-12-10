# [Do it! �ǽ� 3C-3] ���� �˻� �˰����� ���� ������ ���

from typing import Any, Sequence

def bin_search(a: Sequence, key: Any) -> int:
    """������ a���� key�� ��ġ�ϴ� ���Ҹ� ���� �˻�(���� ������ ���)"""
    pl = 0           # �˻� ���� �� �� ������ �ε���
    pr = len(a) - 1  # �˻� ���� �� �� ������ �ε���

    print('   |', end='')
    for i in range(len(a)):
        print(f'{i : 4}', end='')
    print()
    print('---+' + (4 * len(a) + 2) * '-')

    while True:
        pc = (pl + pr) // 2  # �߾� ������ �ε���

        print('   |', end='')
        if pl != pc:         # pl ���� ���� <-�� ���
            print((pl * 4 + 1) * ' ' + '<-' + ((pc - pl) * 4) * ' ' + '+', end='')
        else: 
            print((pc * 4 + 1) * ' ' + '<+', end='')
        if pc != pr:         # pr ���� ���� ->�� ���
            print(((pr - pc) * 4 - 2) * ' ' + '->')
        else:
            print('->')
        print(f'{pc:3}|', end='')
        for i in range(len(a)):
            print(f'{a[i]:4}', end='') 
        print('\n   |')

        if a[pc] == key:
            return pc    # �˻� ����
        elif a[pc] < key:
            pl = pc + 1  # �˻� ������ ������ �������� ����
        else:
            pr = pc - 1  # �˻� ������ ������ �������� ����
        if pl > pr:  
            break
    return -1            # �˻� ����

if __name__ == '__main__':
    num = int(input('���� ���� �Է��ϼ���.: '))
    x = [None] * num  # ���� ���� num�� �迭�� ����

    print('�迭 �����͸� ������������ �Է��ϼ���.')

    x[0] = int(input('x[0]: '))

    for i in range(1, num):
        while True:
            x[i] = int(input(f'x[{i}]: '))
            if x[i] >= x[i - 1]:
                 break

    ky = int(input('�˻��� ���� �Է��ϼ���.: '))  # �˻��� ky�� �Է�

    idx = bin_search(x, ky)                     # ky�� ���� ���� ���Ҹ� x���� �˻�

    if idx == -1:
        print('�˻����� ���� ���Ұ� �������� �ʽ��ϴ�.')
    else:
        print(f'�˻����� x[{idx}]�� �ֽ��ϴ�.')
