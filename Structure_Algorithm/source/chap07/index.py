# ���ڿ��� ���ԵǾ� �ִ� ���ڿ��� �˻�(index �迭 �Լ�)

txt = input('���ڿ� txt: ')
ptn = input('���ڿ� ptn: ')

c = txt.count(ptn)

if c == 0:                                                  # ���Ե� ���ڰ� ����
    print('ptn�� txt�� ���ԵǾ� ���� �ʽ��ϴ�.')
elif c == 1:                                                # ���Ե� ���ڰ� ������ �ִ� ���
    print('ptn�� txt�� ���ԵǾ� �ִ� �ε���: ', txt.index(ptn))
else:                                                       # ���Ե� ���ڰ� 2�� �̻� �ִ� ���
    print('ptn�� txt�� ���ԵǾ� �ִ� �� �� �ε���: ', txt.index(ptn))
    print('ptn�� txt�� ���ԵǾ� �ִ� �� �� �ε���: ', txt.rindex(ptn))
