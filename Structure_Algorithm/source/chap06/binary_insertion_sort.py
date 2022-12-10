# [Do it! �ǽ� 6C-1] ���� ���� ���� �˰��� �����ϱ�

from typing import MutableSequence

def binary_insertion_sort(a: MutableSequence) -> None:
    """���� ���� ����"""
    n = len(a)
    for i in range(1, n):
        key = a[i]
        pl = 0      # �˻� ������ �� �� ���� �ε���
        pr = i - 1  # �˻� ������ �� �� ���� �ε���

        while True:
            pc = (pl + pr) // 2  # �˻� ������ �߾� ���� �ε���
            if a[pc] == key:     # �˻� ����
                break
            elif a[pc] < key:
                pl = pc + 1
            else:
                pr = pc - 1
            if pl > pr:
                break
    
        pd = pc + 1 if pl <= pr else pr + 1  # ������ ��ġ�� �ε���

        for j in range(i, pd, -1):
            a[j] = a[j - 1]
        a[pd] = key

if __name__ == "__main__":
    print("���� ���� ������ �����մϴ�.")
    num = int(input("���� ���� �Է��ϼ���.: "))
    x = [None] * num          # ���� ���� num�� �迭�� ����

    for i in range(num):
        x[i] = int(input(f"x[{i}]: "))

    binary_insertion_sort(x)  # �迭 x�� ���� ���� ����

    print("������������ �����߽��ϴ�.")
    for i in range(num):
        print(f"x[{i}] = {x[i]}")
