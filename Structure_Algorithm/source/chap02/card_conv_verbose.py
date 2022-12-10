# 10���� �������� �Է¹޾� 2~36������ ��ȯ�Ͽ� ����ϱ�(�ǽ� 2-7 ����)

def card_conv(x: int, r: int) -> str:
    """���� x�� r ������ ��ȯ�� �� �� ���� ��Ÿ���� ���ڿ��� ��ȯ"""

    d =  ''  # ��ȯ �� ���ڿ�
    dchar = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    n = len(str(x))  # ��ȯ�ϱ� ���� �ڸ���

    print(f'{r:2} | {x:{n}d}')
    while x > 0:
        print('   +' + (n + 2) * '-')
        if x // r:
            print(f'{r:2} | {x // r:{n}d} �� {x % r}')
        else:
            print(f'     {x // r:{n}d} �� {x % r}')
        d += dchar [x % r]  # �ش��ϴ� ���ڸ� ���� ����
        x //= r

    return d[::-1]  # �������� ��ȯ

# ���� Do it! �ǽ� 2-7 [B]�� ����

if __name__ == '__main__':
    print('10������ n������ ��ȯ�մϴ�.')

    while True:
        while True :  # ���� �ƴ� ������ �Է¹���
            no = int(input('��ȯ�� ������ ���� �ƴ� ������ �Է��ϼ���.: '))
            if no > 0:
                break

        while True :  # 2~36������ �������� �Է¹���
            cd = int(input('� ������ ��ȯ�ұ��?: '))
            if 2 <=  cd <=  36:
                break

        print(f'{cd}�����δ� {card_conv(no, cd)}�Դϴ�.')

        retry = input( "�� �� �� ��ȯ�ұ��?(Y �� ��/N �� �ƴϿ�) : ")
        if retry in {'N', 'n'}:
           break
