# [Do it! �ǽ� 6-13] �� ���� �˰��� �����ϱ�(���� ���� 9�� �̸��� ��� �ܼ� ���� ����)

from typing import MutableSequence

def sort3(a: MutableSequence, idx1: int, idx2: int, idx3: int):
    """a[idx1], a[idx2], a[idx3]�� ������������ �����ϰ� ��� ���� �ε����� ��ȯ"""
    if a[idx2] < a[idx1]: a[idx2], a[idx1] = a[idx1], a[idx2]
    if a[idx3] < a[idx2]: a[idx3], a[idx2] = a[idx2], a[idx3]
    if a[idx2] < a[idx1]: a[idx2], a[idx1] = a[idx1], a[idx2]
    return idx2

def insertion_sort(a: MutableSequence, left: int, right: int) -> None:
    """a[left] ~ a[right]�� �ܼ� ���� ����"""
    for i in range(left + 1, right + 1):
        j = i
        tmp = a[i]
        while j > 0 and a[j - 1] > tmp:
            a[j] = a[j - 1]
            j -= 1
        a[j] = tmp

def qsort(a: MutableSequence, left: int, right: int) -> None:
    """a[left] ~ a[right]�� �� ����"""
    if right - left < 9:            # ���� ���� 9�� �̸��̸� �ܼ� ���� ������ ȣ��
        insertion_sort(a, left, right)
    else:                           # ���� ���� 9�� �̻��̸� �� ������ ����
        pl = left                   # ���� Ŀ��
        pr = right                  # ������ Ŀ��
        m = sort3(a, pl, (pl + pr) // 2, pr)
        x = a[m]

        a[m], a[pr - 1] = a[pr - 1], a[m]
        pl += 1
        pr -= 2
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
    print('�� ������ �մϴ�(���� ���� 9�� �̸��̸� �ܼ� ���� ����).')
    num = int(input('���� ���� �Է��ϼ���.: '))
    x = [None] * num    # ���� ���� num�� �迭�� ����

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    quick_sort(x)       # �迭 x�� �� ����

    print('������������ �����߽��ϴ�.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')
