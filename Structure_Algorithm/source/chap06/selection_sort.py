# [Do it! �ǽ� 6-6] �ܼ� ���� ���� �˰��� ����

from typing import MutableSequence

def selection_sort(a: MutableSequence) -> None:
    """�ܼ� ���� ����"""
    n = len(a)
    for i in range(n - 1):
        min = i  # ���� �� �κп��� ���� ���� ������ �ε���
        for j in range(i + 1, n):
            if a[j] < a[min]:
                min = j
        a[i], a[min] = a[min], a[i]  # ���� �� �κп��� �� ���� ���ҿ� ���� ���� ���Ҹ� ��ȯ 

if __name__ == '__main__':
    print('�ܼ� ���� ������ �����մϴ�.')
    num = int(input('���� ���� �Է��ϼ���.: '))
    x = [None] * num  # ���� ���� num�� �迭�� ����

    for i in range(num):
        x[i] = int(input(f'x[{i}] : '))

    selection_sort(x)  # �迭 x�� �ܼ� ���� ����

    print('������������ �����߽��ϴ�.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')
