# [Do it! �ǽ� 3C-1] seq_search() �Լ��� ����Ͽ� �Ǽ� �˻��ϱ�
from ssearch_while import seq_search

print('�Ǽ��� �˻��մϴ�.')
print('����: "End"�� �Է��ϸ� �����մϴ�.')

number = 0
x = []  # �� ����Ʈ x�� ����

while True:
    s = input(f'x[{number}]: ')
    if s == 'End':
        break
    x.append(float(s))  # �迭 �������� ���Ҹ� �߰�
    number += 1

ky = float(input('�˻��� ���� �Է��ϼ���.: '))  # �˻��� Ű ky�� �Է�

idx = seq_search(x, ky)  # ky�� ���� ���� ���Ҹ� x���� �˻�
if idx == -1:
    print('�˻����� ���� ���Ұ� �������� �ʽ��ϴ�.')
else:
    print(f'�˻����� x[{idx}]�� �ֽ��ϴ�.')
