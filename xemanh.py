import numpy as np
from tkinter import filedialog, Tk, Label, Button
from PIL import Image, ImageTk, ImageOps

# Tạo một cửa sổ chính
root = Tk()
root.title("Xem Anh")

# Khởi tạo biến toàn cục
image = None
img_label = None

# Hàm mở file ảnh
def open_image():
    global image, img_label
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.png;*.jpeg")])
    if file_path:
        image = Image.open(file_path)
        img = ImageTk.PhotoImage(image)
        
        if img_label is None:
            img_label = Label(root, image=img)
            img_label.image = img
            img_label.grid(row=0, column=0, columnspan=4)
        else:
            img_label.configure(image=img)
            img_label.image = img

# Hàm lưu ảnh
def save_image():
    global image
    if image:
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg")])
        if file_path:
            image.save(file_path)

# Hàm phóng to ảnh
def zoom_in():
    global image, img_label
    if image:
        width, height = image.size
        image_resized = image.resize((int(width * 1.2), int(height * 1.2)))
        img = e(ImageTk.PhotoImagimage_resized)
        img_label.configure(image=img)
        img_label.image = img

# Hàm thu nhỏ ảnh
def zoom_out():
    global image, img_label
    if image:
        width, height = image.size
        image_resized = image.resize((int(width * 0.8), int(height * 0.8)))
        img = ImageTk.PhotoImage(image_resized)
        img_label.configure(image=img)
        img_label.image = img

# Hàm cân bằng lược đồ xám
def equalize_histogram():
    if image:
        gray_image = image.convert("L")
        equalized_image = ImageOps.equalize(gray_image)
        img = ImageTk.PhotoImage(equalized_image)
        img_label.configure(image=img)
        img_label.image = img
        image.paste(equalized_image)

# Các nút chức năng
open_btn = Button(root, text="Open Image", command=open_image)
open_btn.grid(row=1, column=0)

save_btn = Button(root, text="Save Image", command=save_image)
save_btn.grid(row=1, column=1)

zoom_in_btn = Button(root, text="Zoom In", command=zoom_in)
zoom_in_btn.grid(row=2, column=0)

zoom_out_btn = Button(root, text="Zoom Out", command=zoom_out)
zoom_out_btn.grid(row=2, column=1)

equalize_btn = Button(root, text="Equalize Histogram", command=equalize_histogram)
equalize_btn.grid(row=3, column=0, columnspan=2)

# Chạy vòng lặp giao diện
root.mainloop()

