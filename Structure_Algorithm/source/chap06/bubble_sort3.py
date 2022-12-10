# [Do it! �ǽ� 6-4] ���� ���� �˰��� �����ϱ�(�˰����� ���� 2)

from typing import MutableSequence

def bubble_sort(a: MutableSequence) -> None:
    """���� ����(��ĵ ������ ����)"""
    n = len(a)
    k = 0
    while k < n - 1:
        last = n - 1
        for j in range(n - 1, k, -1):
            if a[j - 1] > a[j]:
                a[j - 1], a[j] = a[j], a[j - 1]
                last = j
        k = last

if __name__ == '__main__':
    print('���� ������ �մϴ�.')
    num = int(input('���ڼ��� �Է��ϼ���.: '))
    x = [None] * num    # ���ڼ� num�� �迭�� ����

    for i in range(num):
        x[i] = int(input(f'x[{i}] : '))

    bubble_sort(x)      # �迭 x�� ���� ����

    print('������������ �����߽��ϴ�.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')
