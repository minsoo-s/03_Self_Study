# [Do it! �ǽ� 6-14] ������ ��ģ �� �迭�� �����ϱ�

from typing import Sequence, MutableSequence

def merge_sorted_list(a: Sequence, b: Sequence, c: MutableSequence) -> None:
    """������ ��ģ �迭 a�� b�� �����Ͽ� c�� ����"""
    pa, pb, pc = 0, 0, 0                 # �� �迭�� Ŀ��
    na, nb, nc = len(a), len(b), len(c)  # �� �迭�� ���Ҽ� 

    while pa < na and pb < nb:  # pa�� pb�� ���Ͽ� ���� ���� pc�� ����
        if a[pa] <= b[pb]:
            c[pc] = a[pa]
            pa += 1
        else:
            c[pc] = b[pb]
            pb += 1
        pc += 1

    while pa < na:              # a�� ���� ���Ҹ� ����
        c[pc] = a[pa]
        pa += 1
        pc += 1

    while pb < nb:              # b�� ���� ���Ҹ� ����
        c[pc] = b[pb]
        pb += 1
        pc += 1

if __name__ == '__main__':
    a = [2, 4, 6, 8, 11, 13]
    b = [1, 2, 3, 4, 9, 16, 21]
    c = [None] * (len(a) + len(b))
    print('������ ��ģ �� �迭�� ������ �����մϴ�.')

    merge_sorted_list(a, b, c)  # �迭 a�� b�� �����Ͽ� c�� ����

    print('�迭 a�� b�� �����Ͽ� �迭 c�� �����Ͽ����ϴ�.')
    print(f'�迭 a: {a}')
    print(f'�迭 b: {b}')
    print(f'�迭 c: {c}')
