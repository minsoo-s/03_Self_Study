# [Do it! �ǽ� 7-1] ���Ʈ ���������� ���ڿ� �˻��ϱ�

def bf_match(txt: str, pat: str) -> int:
    """���Ʈ ���������� ���ڿ� �˻�"""
    pt = 0  # txt(�ؽ�Ʈ)�� ���󰡴� Ŀ��
    pp = 0  # pat(����)�� ���󰡴� Ŀ��

    while pt != len(txt) and pp != len(pat):
        if txt[pt] == pat[pp]:
            pt += 1
            pp += 1
        else:
            pt = pt - pp + 1
            pp = 0

    return pt - pp if pp == len(pat) else -1

if __name__ == '__main__':
    s1 = input('�ؽ�Ʈ�� �Է��ϼ���.: ')  # �ؽ�Ʈ�� ���ڿ�
    s2 = input('������ �Է��ϼ���.: ')    # ���Ͽ� ���ڿ�

    idx = bf_match(s1, s2)  # ���ڿ� s1~s2�� ���Ʈ ���������� �˻�

    if idx == -1:
        print('�ؽ�Ʈ �ȿ� ������ �������� �ʽ��ϴ�.')
    else:
        print(f'{(idx + 1)}��° ���ڿ��� ��ġ�մϴ�.')
