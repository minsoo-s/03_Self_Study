# [Do it! �ǽ� 2-9] 1,000 ������ �Ҽ��� �����ϱ�(�˰��� ���� 1)

counter = 0           # ������ Ƚ��
ptr = 0               # �̹� ã�� �Ҽ��� ����
prime = [None] * 500  # �Ҽ��� �����ϴ� �迭

prime[ptr] = 2        # 2�� �Ҽ��̹Ƿ� �ʱ갪���� ����
ptr += 1

for n in range(3, 1001, 2):  # Ȧ������ ������� ����
    for i in range(1, ptr):  # �̹� ã�� �Ҽ��� ����
        counter += 1
        if n % prime[i] == 0:  # ������ �������� �Ҽ��� �ƴ�
            break              # �ݺ� �ߴ�
    else:                      # ������ ������ �������� �ʾҴٸ�
        prime[ptr] = n         # �Ҽ��� �迭�� ���
        ptr += 1

for i in range(ptr):  # ptr�� �Ҽ��� ���
    print(prime[i])
print(f'�������� ������ Ƚ��: {counter}')
