# [Do it! �ǽ� 1-9] a���� b���� ������ �� ���ϱ�(for ��)

print('a���� b������ ���� ���մϴ�.')
a = int(input('���� a�� �Է��ϼ���.: '))
b = int(input('���� b�� �Է��ϼ���.: '))

if a > b:
    a, b = b, a  # a�� b�� ������������ ����

sum = 0
for i in range(a, b + 1):
    sum += i  # sum�� i�� ����

print(f'{a}���� {b}���� ������ ���� {sum}�Դϴ�.')
