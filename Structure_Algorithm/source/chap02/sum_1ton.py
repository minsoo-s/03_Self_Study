# [Do it! �ǽ� 2C-5] 1���� n���� ������ �� ���ϱ�

def sum_1ton(n):
    """1���� n���� ������ ��"""
    s = 0
    while n > 0:
        s += n
        n -= 1
    return s

x = int(input('x�� ���� �Է��ϼ���.: '))
print(f'1���� {x}���� ���� {sum_1ton(x)}�Դϴ�.')
