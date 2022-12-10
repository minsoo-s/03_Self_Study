# [Do it! �ǽ� 6-1] ���� ���� �˰��� �����ϱ�

from typing import MutableSequence

def bubble_sort(a: MutableSequence) -> None:
    """���� ����"""
    n = len(a)
    for i in range(n - 1):
        for j in range(n - 1, i, -1):
            if a[j - 1] > a[j]:
                a[j - 1], a[j] = a[j], a[j - 1]

if __name__ == '__main__':
    print('���� ������ �����մϴ�.')
    num = int(input('���� ���� �Է��ϼ���.: '))
    x = [None] * num  # ���� ���� num�� �迭�� ����

    for i in range(num):
        x[i] = int(input(f'x[{i}] : '))

    bubble_sort(x)  # �迭 x�� ���� ����

    print('������������ �����߽��ϴ�.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')
