
st1 = input("Nhập xâu St1: ")
st2 = input("Nhập xâu St2: ")
def kiem_tra_xau(st1, st2):
    #a.	Kiểm tra xem xâu St2 có nằm trong St1 hay không?
    if st2 in st1:
        print("a. Xâu St2 nằm trong St1")
        #b.	Nếu có thì St2 xuất hiện mấy lần?
        print(f"b. Số lần xuất hiện của St2 trong St1 là: {st1.count(st2)}")
        #c.	Nếu st2 có xuất hiện trong st1 thì chỉ tính số lần xuất hiện không chồng chéo lên nhau.
        index = 0
        count = 0
        while (index := st1.find(st2, index)) != -1:
            count += 1
            index += len(st2)
        
        print(f"c. Số lần xuất hiện không chồng chéo của St2 trong St1 là: {count}")
    else:
        print("a. Xâu St2 không nằm trong St1")

kiem_tra_xau(st1, st2)
