# [Do it! �ǽ� 6-10] �迭�� �� �׷����� ������

from typing import MutableSequence

def partition(a: MutableSequence) -> None:
    """�迭�� �����Ͽ� ���"""
    n = len(a)
    pl = 0         # ���� Ŀ��
    pr = n - 1     # ������ Ŀ��
    x = a[n // 2]  # �ǹ�(��� ����)

    while pl <= pr:
        while a[pl] < x: pl += 1
        while a[pr] > x: pr -= 1
        if pl <= pr:
            a[pl], a[pr] = a[pr], a[pl]
            pl += 1
            pr -= 1

    print(f'�ǹ��� {x}�Դϴ�.')

    print('�ǹ� ������ �׷��Դϴ�.')
    print(*a[0 : pl])           # a[0] ~ a[pl - 1]

    if pl > pr + 1:
        print('�ǹ��� ��ġ�ϴ� �׷��Դϴ�.')
        print(*a[pr + 1 : pl])  # a[pr + 1] ~ a[pl - 1]

    print('�ǹ� �̻��� �׷��Դϴ�.')
    print(*a[pr + 1 : n])       # a[pr + 1] ~ a[n - 1]

if __name__ == '__main__':
    print('�迭�� �����ϴ�.')
    num = int(input('���� ���� �Է��ϼ���.: '))
    x = [None] * num    # ���� ���� num�� �迭�� ����

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    partition(x)         # �迭 x�� ����� ���
