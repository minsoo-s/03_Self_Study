# ���� ���� �˰��� �����ϱ�(heapq.merge�� ���)

from typing import MutableSequence
import heapq

def merge_sort(a: MutableSequence) -> None:
    """���� ����(heapq.merge�� ���)"""
    atype = type(a)

    def _merge_sort(a: MutableSequence, left: int, right: int) -> None:
        """a[left]��a[right]�� ��������� ���� ����"""
        if left < right:
            center = (left + right) // 2

            _merge_sort(a, left, center)            # �պκ� �迭�� ���� ����
            _merge_sort(a, center + 1, right)       # �޺κ� �迭�� ���� ����

            buff = atype(heapq.merge(a[left: center+1], a[center + 1: right+1]))
            for i in range(len(buff)):
                a[left + i] = buff[i]

    _merge_sort(a, 0, len(a))       # �迭 ��ü�� ���� ����

if __name__ == '__main__':
    print('���� ������ �����մϴ�(heapq.merge�� ���).')
    num = int(input('���� ���� �Է��ϼ���.: '))
    x = [None] * num    # ���� ���� num�� �迭�� ����

    for i in range(num):
        x[i] = int(input(f'x[{i}] : '))

    merge_sort(x)       # �迭 x�� ���� ����

    print('������������ �����߽��ϴ�.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')
