# ������ ��ģ �� �迭�� ���� (heapq.merege ��룩

import heapq

a = [2, 1, 6, 8, 11, 13]
b = [1, 2, 3, 4, 9, 16, 21]
c = list(heapq.merge(a, b))  # �迭 a�� b�� �����Ͽ� c�� ����

print('�迭 a�� b�� �����Ͽ� �迭 c�� �����Ͽ����ϴ�.')
print(f'�迭 a: {a}')
print(f'�迭 b: {b}')
print(f'�迭 c: {c}')
