# �� �������� �Է¹޾� �߾Ӱ��� ���ϱ� 2

def med3(a, b, c):
    """a, b, c�� �߾Ӱ��� ���Ͽ� ��ȯ(�ٸ� ���)"""
    if (b >= a and c <= a) or (b <= a and c >= a):
        return a
    elif (a > b and c < b) or (a < b and c > b):
        return b
    return c

print('�� ������ �߾Ӱ��� ���մϴ�.')
a = int(input('���� a�� ���� �Է��ϼ���.: '))
b = int(input('���� b�� ���� �Է��ϼ���.: '))
c = int(input('���� c�� ���� �Է��ϼ���.: '))

print(f'�߾Ӱ��� {med3(a, b, c)}�Դϴ�.')
