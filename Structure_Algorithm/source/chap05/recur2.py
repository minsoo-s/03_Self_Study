# recur �Լ��� �Ųٷ� ���(Do it! �ǽ� 5-3 ����)

def recur(n: int) -> int:
    """������ ��� �Լ� recur�� ����(�Ųٷ� ���)"""
    if n > 0:
        recur(n - 2)
        print(n)
        recur(n - 1)

x = int(input('�������� �Է��ϼ���.: '))

recur(x)
