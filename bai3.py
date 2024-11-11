class SinhVien:
    def nhap_thong_tin(self):
        self.ho_ten = input("Nhập họ tên sinh viên (để dừng, nhấn Enter): ")
        if not self.ho_ten:
            return False

        self.diem_tin = float(input("Nhập điểm Tin đại cương: "))
        self.diem_c = float(input("Nhập điểm C: "))
        return True

    def in_thong_tin(self):
        print(f"Họ tên: {self.ho_ten}")
        print(f"Tin học Đại cương: {self.diem_tin}")
        print(f"LT C: {self.diem_c}")
        print("")

def main():
    danh_sach_sinh_vien = []

    while True:
        sv = SinhVien()
        if not sv.nhap_thong_tin():
            break
        danh_sach_sinh_vien.append(sv)

    print("\nThông tin sinh viên:")
    for sinh_vien in danh_sach_sinh_vien:
        sinh_vien.in_thong_tin()

if __name__ == "__main__":
    main()
