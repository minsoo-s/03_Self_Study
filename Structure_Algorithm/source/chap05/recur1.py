# [Do it! �ǽ� 5-3] ������ ��� �Լ� �����ϱ�

def recur(n: int) -> int:
    """������ ��� �Լ� recur�� ����"""
    if n > 0:
        recur(n - 1)
        print(n)
        recur(n - 2)

x = int(input('�������� �Է��ϼ���.: '))

recur(x)
