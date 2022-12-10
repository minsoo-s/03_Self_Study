# [Do it! �ǽ� 6-7] �ܼ� ���� ���� �˰��� �����ϱ�

from typing import MutableSequence

def insertion_sort(a: MutableSequence) -> None:
    """�ܼ� ���� ����"""
    n = len(a)
    for i in range(1, n):
        j = i
        tmp = a[i]
        while j > 0 and a[j - 1] > tmp:
            a[j] = a[j - 1]
            j -= 1
        a[j] = tmp

if __name__ == '__main__':
    print('�ܼ� ���� ������ �����մϴ�.')
    num = int(input('���� ���� �Է��ϼ���.: '))
    x = [None] * num  # ���� ���� num�� �迭�� ����

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    insertion_sort(x)  # �迭 x�� �ܼ� ���� ����

    print('������������ �����߽��ϴ�.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')
