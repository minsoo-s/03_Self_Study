# [Do it! �ǽ� 1-12] +�� -�� ������ ����ϱ� 1(for �� ����)

print('+�� -�� ������ ����մϴ�.')
n = int(input('�� ���� ����ұ��?: '))

for i in range(1, n + 1):  
    if i % 2:              # Ȧ��
        print('+', end='')
    else:                  # ¦��
        print('-', end='')
        
print()
