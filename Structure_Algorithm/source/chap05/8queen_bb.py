# [Do it! �ǽ� 5-8] ��� ���� ���� 1�� ��ġ�ϴ� ������ ��������� �����ϱ�

pos = [0] * 8       # �� ������ ���� ��ġ
flag = [False] * 8  # �� �࿡ ���� ��ġ�ߴ��� üũ

def put() -> None:
    """�� ���� ���� ���� ��ġ�� ���"""
    for i in range(8):
        print(f'{pos[i]:2}', end='')
    print()

def set(i: int) -> None:
    """i ���� �˸��� ��ġ�� ���� ��ġ"""
    for j in range(8):
        if not flag[j]:  # j �࿡ ���� ��ġ���� �ʾ�����
            pos[i] = j   # ���� j �࿡ ��ġ
            if i == 7:   # ��� ���� ���� ��ġ�� �Ϸ�
                put()
            else:
                flag[j] = True
                set(i + 1)  # ���� ���� ���� ��ġ
                flag[j] = False

set(0)  # 0���� ���� ��ġ
