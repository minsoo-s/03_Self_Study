# [Do it! �ǽ� 2-10] 1,000 ������ �Ҽ��� �����ϱ�(�˰��� ���� 2)

counter = 0           # ������ �������� ���� Ƚ��
ptr = 0               # �̹� ã�� �Ҽ��� ����
prime = [None] * 500  # �Ҽ��� �����ϴ� �迭

prime[ptr] = 2  # 2�� �Ҽ�
ptr += 1

prime[ptr] = 3  # 3�� �Ҽ�
ptr += 1

for n in range(5, 1001, 2):    # Ȧ������ ������� ����
    i = 1
    while prime[i] * prime[i] <=  n:
        counter += 2
        if n % prime[i] == 0:  # ������ �������Ƿ� �Ҽ��� �ƴ�
            break              # �ݺ� �ߴ�
        i += 1
    else:                      # ������ ������ �������� �ʾҴٸ�
        prime[ptr] = n         # �Ҽ��� �迭�� ���
        ptr += 1
        counter += 1

for i in range(ptr):  # ptr���� �Ҽ��� ���
    print(prime[i])
print(f'������ �������� ������ Ƚ��: {counter}')
