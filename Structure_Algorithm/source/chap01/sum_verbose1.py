# [Do it! �ǽ� 1-10] a���� b���� ������ �� ���ϱ� 1

print('a���� b������ ���� ���մϴ�.')
a = int(input('���� a�� �Է��ϼ���.: '))
b = int(input('���� b�� �Է��ϼ���.: '))

if a > b:
    a, b = b, a

sum = 0
for i in range(a, b + 1):  # b - a�� �ݺ�
    if i < b:              # i�� b���� ������ ���� ���ϴ� ������ ���
        print(f'{i} + ', end='')
    else:                  # i�� b���� ũ�ų� ������ ������ ����� ���� i =�� ���
        print(f'{i} = ', end='')
    sum += i               # sum�� i�� ����

print(sum)
