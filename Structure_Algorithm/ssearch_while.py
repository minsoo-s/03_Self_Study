# [Do it! �ǽ� 3-1] while ������ �ۼ��� ���� �˻� �˰���

from typing import Any, Sequence

def seq_search(a: Sequence, key: Any) -> int:
    """������ a���� key���� ���� ���Ҹ� ���� �˻�(while ��)"""
    i = 0

    while True:
        if i == len(a):
            return -1  # �˻��� �����Ͽ� -1�� ��ȯ
        if a[i] == key:
            return i   # �˻��� �����Ͽ� ���� ������ �迭�� �ε����� ��ȯ
        i += 1

if __name__ == '__main__':
    num = int(input('���� ���� �Է��ϼ���.: '))  # num ���� �Է�
    x = [None] * num                           # ���� ���� num�� �迭�� ����

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    ky = int(input('�˻��� ���� �Է��ϼ���.: '))  # �˻��� Ű ky�� �Է¹ޱ�

    idx = seq_search(x, ky)                     # ky�� ���� ���Ҹ� x���� �˻�

    if idx == -1:
        print('�˻����� ���� ���Ұ� �������� �ʽ��ϴ�.')
    else:
        print(f'�˻����� x[{idx}]�� �ֽ��ϴ�.')
