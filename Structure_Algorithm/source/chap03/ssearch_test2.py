# [Do it! �ǽ� 3C-2] seq_search() �Լ��� ����Ͽ� Ư�� �ε��� �˻��ϱ�

from ssearch_while import seq_search

t = (4, 7, 5.6, 2, 3.14, 1)
s = 'string'
a = ['DTS', 'AAC', 'FLAC']

print(f'{t}���� 5.6�� �ε����� {seq_search(t, 5.6)}�Դϴ�.')
print(f'{s}���� "n"�� �ε����� {seq_search(s, "n")}�Դϴ�.')
print(f'{a}���� "DTS"�� �ε����� {seq_search(a, "DTS")}�Դϴ�.')
