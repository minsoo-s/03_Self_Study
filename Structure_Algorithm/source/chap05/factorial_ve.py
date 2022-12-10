# [������� 5-1] ���� ������ ���丮�� ���ϱ�(n�� ������ ValueError ���� ó�� �߻�)

def factorial(n : int) -> int:
    """���� ���� n�� ���丮���� ��������� ����(n�� ������ ValueError ���� ó�� �߻�)"""
    if n > 0:
        return n * factorial(n - 1)
    elif n == 0:
        return 1
    else:
        raise ValueError

if __name__ == '__main__':
    n = int(input('����� ���丮�� ���� �Է��ϼ���.: '))
    try:
        print(f'{n}�� ���丮���� {factorial(n)}�Դϴ�.')
    except ValueError:
        print(f'{n}�� ���丮���� ���� �� �����ϴ�.')
