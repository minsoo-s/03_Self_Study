# [Do it! �ǽ� 4C-2] ���ϴ� ����(n)��ŭ ���� �Է¹޾� ������ n���� ����

n = int(input('������ �� �� �����ұ��? : '))
a = [None] * n  # �Է� ���� ���� �����ϴ� �迭

cnt = 0         # �Է� ���� ����
while True:
    a[cnt % n] = int(input((f'{cnt + 1} ��° ������ �Է��ϼ���.: ')))
    cnt += 1

    retry = input(f'��� �ұ��?(Y ... Yes / N ... No) : ')
    if retry in {'N', 'n'}:
        break

i = cnt - n
if i < 0: i = 0

while i < cnt:
    print(f'{i + 1}��° = {a[i % n]}')
    i += 1
