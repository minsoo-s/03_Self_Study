# [Do it! �ǽ� 6C-3] �� ���� �˰��� ����(�迭�� ������ ���� ���)

from typing import MutableSequence

def qsort(a: MutableSequence, left: int, right: int) -> None:
    """a[left] ~ a[right]�� �� ����(�迭�� ������ ���� ���)"""
    pl = left                   # ���� Ŀ��
    pr = right                  # ������ Ŀ��
    x = a[(left + right) // 2]  # �ǹ�(��� ����)

    print(f'a[{left}] ~ a[{right}]: ', *a[left : right + 1])  # ���� �߰��� �κ�

    while pl <= pr:                     
        while a[pl] < x: pl += 1
        while a[pr] > x: pr -= 1
        if pl <= pr:                    
            a[pl], a[pr] = a[pr], a[pl]
            pl += 1
            pr -= 1

    if left < pr: qsort(a, left, pr)   
    if pl < right: qsort(a, pl, right)

def quick_sort(a: MutableSequence) -> None:
    """�� ����"""
    qsort(a, 0, len(a) - 1)

if __name__ == '__main__':
    print('�� ������ �����մϴ�(�迭�� ������ ���� ���).')
    num = int(input('���� ���� �Է��ϼ���.: '))
    x = [None] * num    # ���� ���� num�� �迭�� ����

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    quick_sort(x)       # �迭 x�� �� ����

    print('������������ �����߽��ϴ�.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')
