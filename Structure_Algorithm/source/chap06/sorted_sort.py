# [Do it! �ǽ� 6C-4] sorted() �Լ��� ����Ͽ� �����ϱ�

print('sorted() �Լ��� ����Ͽ� �����մϴ�.')
num = int(input('���� ���� �Է��ϼ���.: '))
x = [None] * num    # ���� ���� num�� �迭�� ����

for i in range(num):
    x[i] = int(input(f'x[{i}]: '))

# �迭 x�� ������������ ����
x = sorted(x)
print('������������ �����߽��ϴ�.')
for i in range(num):
    print(f'x[{i}] = {x[i]}')

# �迭 x�� ������������ ����
x = sorted(x, reverse = True)
print('������������ �����߽��ϴ�.')
for i in range(num):
    print(f'x[{i}] = {x[i]}')
