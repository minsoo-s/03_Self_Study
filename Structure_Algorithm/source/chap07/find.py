# ���ڿ��� ���ԵǾ� �ִ� ���ڿ��� �˻�(find �迭 �Լ���

txt = input('���ڿ� txt: ')  # ���ڿ� ����
ptn = input('���ڿ� ptn: ')  # �˻��� ����

c = txt.count(ptn)

if c == 0:                                                  # ���Ե� ���ڰ� ����
    print('ptn�� txt�� ���ԵǾ� ���� �ʽ��ϴ�.')
elif c == 1:                                                # ���Ե� ���ڰ� ������ �ִ� ���
    print('ptn�� txt�� ���ԵǾ� �ִ� �ε���: ', txt.find(ptn))
else:                                                       # ���Ե� ���ڰ� 2�� �̻� �ִ� ���
    print('ptn�� txt�� ���ԵǾ� �ִ� �� �� �ε���: ', txt.find(ptn))
    print('ptn�� txt�� ���ԵǾ� �ִ� �� �� �ε���: ', txt.rfind(ptn))
