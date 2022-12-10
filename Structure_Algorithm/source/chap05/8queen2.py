# [Do it! �ǽ� 5-9] 8�� ���� �˰��� �����ϱ�(���� ���� ��Ȳ�� �׸�� ǥ��)

pos = [0] * 8          # �� ���� ��ġ�� ���� ��ġ
flag_a = [False] * 8   # �� �࿡ ���� ��ġ�ߴ��� üũ
flag_b = [False] * 15  # �밢�� ����(�ע�)���� ���� ��ġ�ߴ��� üũ
flag_c = [False] * 15  # �밢�� ����( �٢�)���� ���� ��ġ�ߴ��� üũ

def put() -> None:
    """���� ���� ��Ȳ�� ��� ��� ���"""
    for j in range(8):
        for i in range(8):
            print('��' if pos[i] == j else '��', end='')
        print()
    print()

def set(i: int) -> None:
    """i ���� �˸��� ��ġ�� ���� ����"""
    for j in range(8):
        if(     not flag_a[j]           # j �࿡ ���� ���� ���� �ʾ�����
            and not flag_b[i + j]       # �밢�� ����(�ע�)���� ���� ��ġ ���� �ʾҴٸ�
            and not flag_c[i - j + 7]): # �밢�� ����( �٢�)���� ���� ��ġ ���� �ʾҴٸ�
            pos[i] = j          # ���� j �࿡ ����
            if i == 7:          # ��� ���� ���� ��ġ�ϴ� ���� �Ϸ�
                put()
            else:
                flag_a[j] = flag_b[i + j] = flag_c[i - j + 7] = True
                set(i + 1)      # ���� ���� ���� ����
                flag_a[j] = flag_b[i + j] = flag_c[i - j + 7] = False

set(0)          # 0 ���� ���� ����
