# [Do it! �ǽ� 1C-2] �� �������� �Է¹޾� �߾Ӱ��� ���ϱ� 1

def med3(a, b, c):
    """a, b, c�� �߾Ӱ��� ���Ͽ� ��ȯ"""
    if a >= b: 
        if b >= c: 
            return b
        elif a <= c: 
            return a
        else:
            return c
    elif a > c: 
        return a
    elif b > c: 
        return c
    else:
        return b

print('�� ������ �߾Ӱ��� ���մϴ�.')
a = int(input('���� a�� ���� �Է��ϼ���.: '))
b = int(input('���� b�� ���� �Է��ϼ���.: '))
c = int(input('���� c�� ���� �Է��ϼ���.: '))

print(f'�߾Ӱ��� {med3(a, b, c)}�Դϴ�.')
