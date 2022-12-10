# [Do it! �ǽ� 6-3] ���� ���� �˰��� �����ϱ�(�˰����� ���� 1) - ���� ������ ���

from typing import MutableSequence

def bubble_sort2_verbose(a: MutableSequence) -> None:
    """���� ����(��ȯ Ƚ���� ���� �ߴ�)"""
    ccnt = 0  # �� Ƚ��
    scnt = 0  # ��ȯ Ƚ��
    n = len(a)
    for i in range(n - 1):
        print(f"�н� {i + 1}")
        exchng = 0  # �н������� ��ȯ Ƚ��
        for j in range(n - 1, i, -1):
            for m in range(0, n - 1):
                print(
                    f"{a[m]:2}"
                    + ("  " if m != j - 1 else " +" if a[j - 1] > a[j] else " -"),
                    end="",
                )
            print(f"{a[n - 1]:2}")
            ccnt += 1
            if a[j - 1] > a[j]:
                scnt += 1
                a[j - 1], a[j] = a[j], a[j - 1]
                exchng += 1
        for m in range(0, n - 1):
            print(f"{a[m]:2}", end="  ")
        print(f"{a[n - 1]:2}")
        if exchng == 0:  # ��ȯ�� ������� �ʾ����� �۾��� �ߴ�
            break
    print(f"�񱳸� {ccnt}�� �߽��ϴ�.")
    print(f"��ȯ�� {scnt}�� �߽��ϴ�.")

if __name__ == "__main__":
    print("���� ������ �����մϴ�")
    num = int(input("���� ���� �Է��ϼ���.: "))
    x = [None] * num        # ���� ���� num�� �迭�� ����

    for i in range(num):
        x[i] = int(input(f"x[{i}]: "))

    bubble_sort2_verbose(x)  # �迭 x�� ���� ����

    print("������������ �����߽��ϴ�.")
    for i in range(num):
        print(f"x[{i}] = {x[i]}")
