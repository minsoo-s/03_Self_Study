# [Do it! �ǽ� 2C-6] ����Ʈ�� ��� ���ڰ��� ������Ʈ�ϱ�

def change(lst, idx, val):
    """lst[idx]�� ���� val�� ������Ʈ"""
    lst [idx] = val

x = [11, 22, 33, 44, 55] # Ʃ��, str �� �̹��ͺ� ��ü�� ���� ���� �Ұ���.
print('x =', x)

index = int(input('������Ʈ�� �ε����� �����ϼ���.: '))
value = int(input('���ο� ���� �Է��ϼ���.: '))

change(x, index, value)
print(f'x = {x}')
