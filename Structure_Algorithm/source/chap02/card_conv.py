# Do it! �ǽ� 2-7 [A] 10���� �������� �Է¹޾� 2~36������ ��ȯ�Ͽ� ����ϱ�

def card_conv(x: int, r: int) -> str:
    """���� x�� r ������ ��ȯ�� �� �� ���� ��Ÿ���� ���ڿ��� ��ȯ"""

    d = ''  # ��ȯ �� ���ڿ�
    dchar = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    while x > 0:
        d += dchar [x % r]  # �ش��ϴ� ���ڸ� ���� ����
        x //= r

    return d[::-1]          # �������� ��ȯ

# Do it! �ǽ� 2-7 [B]

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

        retry = input( "�� �� �� ��ȯ�ұ��?(Y ... ��/N ... �ƴϿ�): ")
        if retry in {'N', 'n'}:
           break
