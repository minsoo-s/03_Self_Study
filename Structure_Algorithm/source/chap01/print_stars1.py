# [Do it! �ǽ� 1-14] *�� n�� ����ϵ� w������ �ٹٲ��ϱ� 1

print('*�� ����մϴ�.')
n = int(input('�� ���� ����ұ��? : '))
w = int(input('�� ������ �ٹٲ��ұ��? : '))

for i in range(n):      # n�� �ݺ�
    print('*', end='')
    if i % w == w - 1:  # n�� �Ǵ�
        print()         # �ٹٲ�

if n % w:
    print()             # �ٹٲ�
