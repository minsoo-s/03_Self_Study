# [Do it! �ǽ� 7-2] KMP������ ���ڿ� �˻��ϱ�

def kmp_match(txt: str, pat: str) -> int:
    """KMP���� ���� ���ڿ� �˻�"""
    pt = 1  # txt�� ���󰡴� Ŀ��
    pp = 0  # pat�� ���󰡴� Ŀ��
    skip = [0] * (len(pat) + 1)  # �ǳʶٱ� ǥ

    # �ǳʶٱ� ǥ �����
    skip[pt] = 0
    while pt != len(pat):
        if pat[pt] == pat[pp]:
            pt += 1
            pp += 1
            skip[pt] = pp
        elif pp == 0:
            pt += 1
            skip[pt] = pp
        else:
            pp = skip[pp]

    # �˻��ϱ�
    pt = pp = 0
    while pt != len(txt) and pp != len(pat):
        if txt[pt] == pat[pp]:
            pt += 1
            pp += 1
        elif pp == 0:
            pt += 1
        else:
            pp = skip[pp]

    return pt - pp if pp == len(pat) else -1

if __name__ == '__main__':
    s1 = input('�ؽ�Ʈ�� �Է��ϼ���.: ')  # �ؽ�Ʈ�� ���ڿ�
    s2 = input('������ �Է��ϼ���.: ')    # ���Ͽ� ���ڿ�

    idx = kmp_match(s1, s2)  # ���ڿ� s1~s2�� KMP������ �˻�

    if idx == -1:
        print('�ؽ�Ʈ �ȿ� ������ �������� �ʽ��ϴ�.')
    else:
        print(f'{(idx + 1)}��° ���ڿ��� ��ġ�մϴ�.')
