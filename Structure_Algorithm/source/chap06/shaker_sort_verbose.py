# [Do it! �ǽ� 6-5] ����Ŀ ���� �˰��� �����ϱ�(���� ������ ���)

from typing import MutableSequence

def shaker_sort_verbose(a: MutableSequence) -> None:
    """"����Ŀ ����(���� ������ ���)"""
    ccnt = 0  # �� Ƚ��
    scnt = 0  # ��ȯ Ƚ��
    left = 0
    n = len(a)
    right = len(a) - 1
    last = right
    i = 0
    while left < right:
        print(f'�н�{i + 1}')
        i += 1
        for j in range(right, left, -1):
            for m in range(0, n - 1):
               print(f'{a[m]:2}' + ('  ' if m != j - 1 else
                                    ' +' if a[j - 1] > a[j] else ' -'),
                     end='')
            print(f'{a[n - 1]:2}')
            ccnt += 1
            if a[j - 1] > a[j]:
                scnt += 1
                a[j - 1], a[j] = a[j], a[j - 1]
                last = j
        left = last
        for m in range(0, n - 1):
           print(f'{a[m]:2}', end='  ')
        print(f'{a[n - 1]:2}')

        if (left == right):
             break
        print(f'�н� {i + 1}')
        i += 1
        for j in range(left, right):
            for m in range(0, n - 1):
               print(f'{a[m]:2}' + ('  ' if m != j else
                                    ' +' if a[j] > a[j + 1] else ' -'),
                     end='')
            print(f'{a[n - 1]:2}')
            ccnt += 1
            if a[j] > a[j + 1]:
                scnt += 1
                a[j], a[j + 1] = a[j + 1], a[j]
                last = j
        right = last
        for m in range(0, n - 1):
           print(f'{a[m]:2}', end='  ')
        print(f'{a[n - 1]:2}')
    print(f'�񱳸� {ccnt}�� �߽��ϴ�.')
    print(f'��ȯ�� {scnt}�� �߽��ϴ�.')

if __name__ == '__main__':
    print('����Ŀ ������ �����մϴ�.')
    num = int(input('���� ���� �Է��ϼ���.: '))
    x = [None] * num  # ���� �� num�� �迭�� ����

    for i in range(num):
        x[i] = int(input(f'x[{i}] : '))

    shaker_sort_verbose(x)  # �迭 x�� �ܼ� ��ȯ ����

    print('������������ �����߽��ϴ�.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')
