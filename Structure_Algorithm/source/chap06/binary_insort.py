# [Do it! �ǽ� 6C-2] ���� ���� ���� �˰����� ����(bisect.insort ���)

from typing import MutableSequence
import bisect

def binary_insertion_sort(a: MutableSequence) -> None:
    """���� ���� ����(bisect.insort�� ���)"""
    for i in range(1, len(a)):
        bisect.insort(a, a.pop(i), 0, i)

if __name__ == '__main__':
    print('���� ���� ������ �����մϴ�.')
    num = int(input('���� ���� �Է��ϼ���.: '))
    x = [None] * num            # ���� ���� num�� �迭�� ����

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    binary_insertion_sort(x)    # �迭 x�� ���� ���� ����

    print('������������ �����߽��ϴ�.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')
