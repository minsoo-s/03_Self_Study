# [Do it! �ǽ� 1-12] +�� -�� ������ ����ϱ� 1

print('+�� -�� ������ ����մϴ�.')
n = int(input('�� ���� ����ұ��?: '))

for i in range(n):          # �ݺ� n��
    if i % 2:                 
        print('-', end='')  # Ȧ���� ��� - ���
    else:
        print('+', end='')  # ¦���� ��� + ���

print()
