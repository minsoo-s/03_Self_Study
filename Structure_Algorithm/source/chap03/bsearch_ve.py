# ���� �˻� �˰���(�˻��� ������ �� ValueError�� ��������

from typing import Any, Sequence

def bin_search(a: Sequence, key: Any) -> int:
    """������ a���� key�� ��ġ�ϴ� ��Ҹ� ���� �˻�"""
    pl = 0           # �˻� ���� �� �� ����� �ε���
    pr = len(a) - 1  # �˻� ���� �� �� ����� �ε���

    while True:
        pc = (pl + pr) // 2  # �߾� ����� �ε���
        if a[pc] == key:
            return pc  # �˻� ����
        elif a[pc] < key:
            pl = pc + 1  # �˻� ������ ���� �������� ����
        else:
            pr = pc - 1  # �˻� ������ ���� �������� ����
        if pl > pr:
            break
    raise ValueError  # �˻� ����

if __name__ == '__main__':
    num = int(input('���� ���� �Է��ϼ���.: '))
    x = [None] * num  # ���� �� num�� �迭�� ����

    print('������������ �Է��ϼ���.')

    x[0] = int(input('x[0] : '))

    for i in range(1, num):
        while True:
            x[i] = int(input(f'x[{i}] : '))
            if x[i] >= x[i - 1]:
                 break

    ky = int(input('�˻��� ���� �Է��ϼ���.: '))  # Ű ky�� �Է¹���

    try:
        idx = bin_search(x, ky)                 # ky�� ���� ���� ��Ҹ� x���� �˻�
    except ValueError:
        print('�˻����� ���� ��Ұ� �������� �ʽ��ϴ�.')
    else:
        print(f'�˻����� x[{idx}]�� �ֽ��ϴ�.')
