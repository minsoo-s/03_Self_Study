# [Do it! �ǽ� 6-16] �� ���� �˰��� �����ϱ�

from typing import MutableSequence

def heap_sort(a: MutableSequence) -> None:
    """�� ����"""

    def down_heap(a: MutableSequence, left: int, right: int) -> None:
        """a[left] ~ a[right]�� ������ �����"""
        temp = a[left]      # ��Ʈ

        parent = left
        while parent < (right + 1) // 2:
            cl = parent * 2 + 1     # ���� �ڽ�
            cr = cl + 1             # ������ �ڽ�
            child = cr if cr <= right and a[cr] > a[cl] else cl  # ū ���� �����մϴ�.
            if temp >= a[child]:
                break
            a[parent] = a[child]
            parent = child
        a[parent] = temp

    n = len(a)

    for i in range((n - 1) // 2, -1, -1):   # a[i] ~ a[n-1]�� ������ �����
        down_heap(a, i, n - 1)

    for i in range(n - 1, 0, -1):
        a[0], a[i] = a[i], a[0]     # �ִ��� a[0]�� ������ ���� a[i]�� ��ȯ
        down_heap(a, 0, i - 1)      # a[0] ~ a[i-1]�� ������ �����

if __name__ == '__main__':
    print('�� ������ �����մϴ�.')
    num = int(input('���� ���� �Է��ϼ���. : '))
    x = [None] * num    # ���� ���� num�� �迭�� ����

    for i in range(num):
        x[i] = int(input(f'x[{i}] : '))

    heap_sort(x)        # �迭 x�� �� ����

    print('������������ �����߽��ϴ�.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')
