# [Do it! �ǽ� 6-12] �� ���� �˰��� ����(��������� �� ����)

from stack import Stack  # �ǽ� 4C-1�� ���� import
from typing import MutableSequence

def qsort(a: MutableSequence, left: int, right: int) -> None:
    """a[left] ~ a [right]�� �� ����(����� ����)"""
    range = Stack(right - left + 1)  # ���� ����

    range.push((left, right))

    while not range.is_empty():
        pl, pr = left, right = range.pop()  # ����, ������ Ŀ���� ����
        x = a[(left + right) // 2]          # �ǹ�(�߾� ���)

        while pl <= pr:
            while a[pl] < x: pl += 1
            while a[pr] > x: pr -= 1
            if pl <= pr:                        # �ǽ� 6-10, �ǽ� 6-11�� ����
                a[pl], a[pr] = a[pr], a[pl]
                pl += 1
                pr -= 1

        if left < pr: range.push((left, pr))    # ���� �׷��� Ŀ���� ����
        if pl < right: range.push((pl, right))  # ������ �׷��� Ŀ���� ����

def quick_sort(a: MutableSequence) -> None:
    """�� ����"""
    qsort(a, 0, len(a) - 1)

if __name__ == '__main__':
    print('��������� �� ����')
    num = int(input('���� ���� �Է��ϼ���.: '))
    x = [None] * num    # ���� ���� num�� �迭�� ����

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    quick_sort(x)       # �迭 x�� �� ����

    print('������������ �����߽��ϴ�.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')
