# [Do it! �ǽ� 5-1] ���� ������ ���丮�� ���ϱ�

def factorial(n: int) -> int:
    """���� ���� n�� ���丮���� ���ϴ� ����"""
    if n > 0:
        return n * factorial(n - 1)
    else:
        return 1

if __name__ == '__main__':
    n = int(input('����� ���丮�� ���� �Է��ϼ���.: '))
    print(f'{n}�� ���丮���� {factorial(n)}�Դϴ�.')
