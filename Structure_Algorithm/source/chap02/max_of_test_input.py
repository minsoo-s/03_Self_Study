# [Do it! �ǽ� 2-3] �迭 ������ �ִ��� ���ؼ� ����ϱ�(���ڰ��� �Է¹���)

from max import max_of

print('�迭�� �ִ��� ���մϴ�.')
print('����: "End"�� �Է��ϸ� �����մϴ�.')

number = 0
x = []                  # �� ����Ʈ

while True:
    s = input(f'x[{number}]�� �Է��ϼ���.: ')
    if s == 'End':
        break
    x.append(int(s))    # �迭�� ���� �߰�
    number += 1

print(f'{number}���� �Է��߽��ϴ�.')
print(f'�ִ��� {max_of(x)}�Դϴ�.')
