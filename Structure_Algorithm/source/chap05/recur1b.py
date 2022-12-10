# [Do it! �ǽ� 5-5] �������� ��� �Լ� �����ϱ�(��͸� ����)

from stack import Stack  # stack.py�� Stack Ŭ������ ����Ʈ

def recur(n: int) -> int:
    """��͸� ������ �Լ� recur"""
    s = Stack(n)

    while True:
        if n > 0:
            s.push(n)         # n ���� Ǫ��
            n = n - 1
            continue
        if not s.is_empty():  # ������ ��� ���� ������
            n = s.pop()       # �����ϰ� �ִ� ���� n�� ��
            print(n)
            n = n - 2
            continue
        break

x = int(input('�������� �Է��ϼ���.: '))

recur(x)
