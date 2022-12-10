# [Do it! �ǽ� 6-9] �� ���� �˰��� �����ϱ�(h * 3 + 1�� ���� ���)

from typing import MutableSequence

def shell_sort(a: MutableSequence) -> None:
    """�� ����(h * 3 + 1�� ���� ���)"""
    n = len(a)
    h = 1

    while h < n // 9:
        h = h * 3 + 1

    while h > 0:
        for i in range(h, n):
            j = i - h
            tmp = a[i]
            while j >= 0 and a[j] > tmp:
                a[j + h] = a[j]
                j -= h
            a[j + h] = tmp
        h //= 3

if __name__ == '__main__':
    print('�� ������ �����մϴ�(h * 3 + 1�� ���� ���).')
    num = int(input('���� ���� �Է��ϼ���.: '))
    x = [None] * num  # ���� ���� num�� �迭�� ����

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    shell_sort(x)  # �迭 x�� �� ����

    print('������������ �����߽��ϴ�.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')
