# *�� n�� ����ϵ� w������ �ٹٲ��ϱ� 2

print('*�� ����մϴ�.')
n = int(input('�� ���� ����ұ��?: '))
w = int(input('�� ������ �ٹٲ��ұ��?: '))

for _ in range(n // w):  # �ݺ� n // w�� �ݺ�
    print('*' * w)

rest = n % w
if rest:
    print('*' * rest)  # if �� 1�� �Ǵ�
