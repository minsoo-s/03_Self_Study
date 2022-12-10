# [Do it! �ǽ� 3-3] ���� �˻� �˰���(�ǽ� 3-1)�� ���ʹ����� ����

from typing import Any, Sequence
import copy

def seq_search(seq: Sequence, key: Any) -> int:
    """������ seq���� key�� ��ġ�ϴ� ���Ҹ� ���� �˻�(���ʹ�)"""
    a = copy.deepcopy(seq)  # seq�� ����
    a.append(key)           # ���� key�� �߰�
 
    i = 0
    while True:
        if a[i] == key: 
            break  # �˻��� �����ϸ� while ���� ����
        i += 1
    return -1 if i == len(seq) else i

if __name__ == '__main__':
    num = int(input('���� ���� �Է��ϼ���.: '))  # num ���� �Է�
    x = [None] * num                           # ���� ���� num�� �迭�� ����

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    ky = int(input('�˻��� ���� �Է��ϼ���.: '))  # �˻��� Ű ky�� �Է¹ޱ�

    idx = seq_search(x, ky)                     # ky���� ���� ���Ҹ� x���� �˻�

    if idx == -1:
         print('�˻����� ���� ���Ұ� �������� �ʽ��ϴ�.')
    else:
        print(f'�˻����� x[{idx}]�� �ֽ��ϴ�.')
