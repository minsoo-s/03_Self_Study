# ���ͺ� ������ ���Ҹ� �������� ����(n�� ������� ����)

from typing import Any, MutableSequence

def reverse_array(a: MutableSequence) -> None:
    """���ͺ� �������� a�� ���Ҹ� �������� ����"""
    for i in range(len(a) // 2):
         a[i], a[len(a) - i - 1] = a[len(a) - i - 1], a[i]

if __name__ == '__main__':
    print('�迭 ���Ҹ� �������� �����մϴ�.')
    nx = int(input('���� ���� �Է��ϼ���.: '))
    x = [None] * nx   # ���� ���� nx�� ����Ʈ�� ����

    for i in range(nx):
        x[i] = int(input(f'x[{i}]��'))

    reverse_array(x)  # x�� �������� ����

    print('�迭 ���Ҹ� �������� �����߽��ϴ�.')
    for i in range(nx):
        print(f'x[{i}]��{x[i]}')
