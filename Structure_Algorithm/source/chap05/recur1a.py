# [Do it! �ǽ� 5-4] ��� �Լ��� ����(���� ��͸� ����)

def recur(n: int) -> int:
    """���� ��͸� ������ �Լ� recur"""
    while n > 0:
        recur(n - 1)
        print(n)
        n = n - 2
x = int(input('�������� �Է��ϼ���.: '))

recur(x)
