# [Do it! �ǽ� 1-13] +�� -�� ������ ����ϱ� 2(range()�Լ� ����)

print('+�� -�� ������ ����մϴ�.')
n = int(input('�� ���� ����ұ��?: '))

for _ in range(1, n // 2 + 1):
    print('+-', end='')  # n // 2���� +-�� ���
    
if n % 2:
    print('+', end='')  # n�� Ȧ���� ���� +�� ���
    
    
    
for _ in range(1, n//2+1):
    print('+-',end="")
if n%2:
    print('+')
