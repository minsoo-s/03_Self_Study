# [Do it! �ǽ� 6-17] ���� ���� �˰��� �����ϱ�

from typing import MutableSequence

def fsort(a: MutableSequence, max: int) -> None:
    """���� ����(�迭 ���ڰ��� 0 �̻� max ����)"""
    n = len(a)           # ������ �迭 a
    f = [0] * (max + 1)  # ���� ���� ����ǥ �迭 f
    b = [0] * n          # �۾��� �迭 b

    for i in range(n):              f[a[i]] += 1                     # [1�ܰ�]
    for i in range(1, max + 1):     f[i] += f[i - 1]                 # [2�ܰ�]
    for i in range(n - 1, -1, -1):  f[a[i]] -= 1; b[f[a[i]]] = a[i]  # [3�ܰ�]
    for i in range(n):              a[i] = b[i]                      # [4�ܰ�]

def counting_sort(a: MutableSequence) -> None:
    """���� ����"""
    fsort(a, max(a))

if __name__ == '__main__':
    print('���� ������ �մϴ�.')
    num = int(input('���� ���� �Է��ϼ���. : '))
    x = [None] * num  # ���� ���� num�� �迭�� ����

    for i in range(num):  # ����� �Է¹���
        while True:
            x[i] = int(input(f'x[{i}] : '))
            if x[i] >= 0: break

    counting_sort(x)  # �迭 x�� ���� ����

    print('������������ �����߽��ϴ�.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')
