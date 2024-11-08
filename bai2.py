s1 = input("Nhập xâu s1 : ")
s2 = input("Nhập xâu s2 : ")
def tron_hai_xau(s1, s2):
    xau_s1 = [int(x) for x in s1.split(',')]
    xau_s2 = [int(x) for x in s2.split(',')]
    s3 = []
    len_s1 = len(xau_s1)
    len_s2 = len(xau_s2)
    max_len = max(len_s1, len_s2)
    for i in range(max_len):
        if i < len_s1:
            s3.append(xau_s1[i])
        if i < len_s2:
            s3.append(xau_s2[i])

    print(f"Kết quả: S3={s3}")

tron_hai_xau(s1, s2)
