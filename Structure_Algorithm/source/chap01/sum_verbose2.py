# [Do it! �ǽ� 1-11] a���� b���� ������ �� ���ϱ� 2

print('a���� b���� ������ ���� ���մϴ�.')
a = int(input('���� a�� �Է��ϼ���.: '))
b = int(input('���� b�� �Է��ϼ���.: '))

if a > b :
    a, b = b, a

sum = 0
for i in range(a, b):
    print(f'{i} + ', end='')
    sum += i  # sum�� i�� ����

print(f'{b} = ', end ='')
sum += b      # sum�� b�� ����

print(sum)
