# [Do it! �ǽ� 2-2] ������ ������ �ִ� ����ϱ�

from typing import Any, Sequence

def max_of(a: Sequence) -> Any:
    """�������� a ����� �ִ��� ��ȯ"""
    maximum = a[0]
    for i in range(1, len(a)):
        if a[i] > maximum: 
            maximum = a[i]
    return maximum

if __name__ == '__main__':
    print('�迭�� �ִ��� ���մϴ�.')
    num = int(input('���� ���� �Է��ϼ��� : '))
    x = [None] * num    # ���� ���� num�� ����Ʈ�� ����

    for i in range(num):
        x[i] = int(input(f'x[{i}]�� �Է��ϼ���.: '))

    print(f'�ִ��� {max_of(x)}�Դϴ�.')
