# [Do it! �ǽ� 5-6] �ϳ����� ž �����ϱ�

def move(no: int, x: int, y: int) -> None:
    """������ no���� x ��տ��� y ������� �ű�"""
    if no > 1:
        move(no - 1, x, 6 - x - y)

    print(f'���� [{no}]��(��) {x}��տ��� {y}������� �ű�ϴ�.')

    if no > 1:
        move(no - 1, 6 - x - y, y)

print('�ϳ����� ž�� �����ϴ� ���α׷��Դϴ�.')
n = int(input('������ ������ �Է��ϼ���.: '))

move(n, 1, 3)
