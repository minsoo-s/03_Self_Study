# [Do it! �ǽ� 1-18] 10~99 ������ ���� n�� �����ϱ�(13�� ������ �ߴ�)

import random

n = int(input('������ ������ �Է��ϼ���.: '))

for _ in range(n):
    r = random.randint(10, 99)
    print(r, end=' ')
    if r == 13:
        print('\n���α׷��� �ߴ��մϴ�.')
        break
else :
    print('\n���� ������ �����մϴ�.')
