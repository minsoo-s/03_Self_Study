# [Do it! �ǽ� 6C-5] �� ���� �˰��� �����ϱ�(heapq.push�� heapq.pop�� ��룩

import heapq
from typing import MutableSequence

def heap_sort(a: MutableSequence) -> None:
    """�� ����(heapq.push�� heapq.pop�� ���)"""

    heap = []
    for i in a:
        heapq.heappush(heap, i)
    for i in range(len(a)):
        a[i] = heapq.heappop(heap)

if __name__ == '__main__':
    print('�� ������ �����մϴ�(heapq.push�� heapq.pop�� ���).')
    num = int(input('���� ���� �Է��ϼ���. : '))
    x = [None] * num    # ���� ���� num�� �迭�� ����

    for i in range(num):
        x[i] = int(input(f'x[{i}] : '))

    heap_sort(x)        # �迭 x�� �� ����

    print('������������ �����߽��ϴ�.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')
