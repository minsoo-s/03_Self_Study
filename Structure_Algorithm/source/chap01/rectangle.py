# [Do it! �ǽ� 1-17] ���� ���ΰ� �����̰� ���̰� area�� ���簢������ ���� ���̸� �����ϱ�

area = int(input('���簢���� ���̸� �Է��ϼ���.: '))

for i in range(1, area + 1):  # 1���� �簢���� ���� ���
    if i * i > area: break
    if area % i: continue
    print(f'{i} �� {area // i}')
