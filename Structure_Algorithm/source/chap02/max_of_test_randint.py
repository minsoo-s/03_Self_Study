 # [Do it! �ǽ� 2-4] �迭 ������ �ִ��� ���ؼ� ����ϱ�(���ڰ��� ������ ����)

import random
from max import max_of

print('������ �ִ��� ���մϴ�.')
num = int(input('������ ������ �Է��ϼ���.: '))
lo = int(input('������ �ּڰ��� �Է��ϼ���.: '))
hi = int(input('������ �ִ��� �Է��ϼ���.: '))
x = [None] * num        # ���� �� num�� ����Ʈ�� ����

for i in range(num):
    x[i] = random.randint(lo, hi)

print(f'{(x)}')
print(f'�� ��� �ִ��� {max_of(x)}�Դϴ�.')
