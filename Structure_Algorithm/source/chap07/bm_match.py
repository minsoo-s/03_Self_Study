# [Do it! �ǽ� 7-3] ���̾� ��������� ���ڿ� �˻��ϱ�(0~255 ����)

def bm_match(txt: str, pat: str) -> int:
    """���̾� ������� ���� ���ڿ� �˻�"""
    skip = [None] * 256  # �ǳʶٱ� ǥ

    # �ǳʶٱ� ǥ �����
    for pt in range(256):
        skip[pt] = len(pat)
    for pt in range(len(pat)):
        skip[ord(pat[pt])] = len(pat) - pt - 1

    # �˻��ϱ�
    while pt < len(txt):
        pp = len(pat) - 1
        while txt[pt] == pat[pp]:
            if pp == 0:
                return pt
            pt -= 1
            pp -= 1
        pt += skip[ord(txt[pt])] if skip[ord(txt[pt])] > len(pat) - pp \
              else len(pat) - pp

    return -1

if __name__ == '__main__':
    s1 = input('�ؽ�Ʈ�� �Է��ϼ���.: ')  # �ؽ�Ʈ ���ڿ�
    s2 = input('������ �Է��ϼ���.: ')    # ���� ���ڿ�

    idx = bm_match(s1, s2)  # ���ڿ� s1~s2�� KMP������ �˻�

    if idx == -1:
        print('�ؽ�Ʈ �ȿ� ������ �������� �ʽ��ϴ�.')
    else:
        print(f'{(idx + 1)}��° ���ڿ��� ��ġ�մϴ�.')
