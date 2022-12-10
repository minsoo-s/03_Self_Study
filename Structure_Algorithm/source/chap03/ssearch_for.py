# [Do it! �ǽ� 3-2] for ������ �ۼ��� ���� �˻� �˰���

from typing import Any, Sequence

def seq_search(a: Sequence, key: Any) -> int:
    """������ a���� key���� ���� ��Ҹ� ���� �˻�(for ��)"""
    for i in range(len(a)):
        if a[i] == key:
            return i  # �˻� ����(�ε����� ��ȯ)
    return -1         # �˻� ����(-1�� ��ȯ)

if __name__ == '__main__':
    num = int(input('���� ���� �Է��ϼ���.: '))  # num ���� �Է�
    x = [None] * num                           # ���� ���� num�� �迭�� ����

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    ky = int(input('�˻��� ���� �Է��ϼ���.: '))  # �˻��� Ű ky�� �Է¹���

    idx = seq_search(x, ky)                     # ky�� ���� ���� ��Ҹ� x���� �˻�

    if idx == -1:
        print('�˻� ���� ���� ��Ұ� �������� �ʽ��ϴ�.')
    else:
        print(f'�˻� ���� x[{idx}]�� �ֽ��ϴ�.')
