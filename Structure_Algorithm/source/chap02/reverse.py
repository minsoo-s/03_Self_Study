# [Do it! �ǽ� 2-6] ���ͺ� ������ ���Ҹ� �������� ����

from typing import Any, MutableSequence

def reverse_array(a: MutableSequence) -> None:
    """���ͺ� �������� a�� ���Ҹ� �������� ����"""
    n = len(a)
    for i in range(n // 2):
         a[i], a[n - i - 1] = a[n - i - 1], a[i]

if __name__ == '__main__':
    print('�迭 ���Ҹ� �������� �����մϴ�.')
    nx = int(input('���� ���� �Է��ϼ���.: '))
    x = [None] * nx   # ���� ���� nx�� ����Ʈ�� ����

    for i in range(nx):
        x[i] = int(input(f'x[{i}] : '))

    reverse_array(x)  # x�� �������� ����

    print('�迭 ���Ҹ� �������� �����߽��ϴ�.')
    for i in range(nx):
        print(f'x[{i}] = {x[i]}')
