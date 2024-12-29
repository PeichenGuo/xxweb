import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
import os

def process_image(input_path, output_path):
    """
    用于调用你已有的代码进行图片处理。
    此处是示例，替换为你的实际处理逻辑。
    """
    from PIL import ImageFilter  # 示例处理：添加模糊效果
    img = Image.open(input_path)
    processed_img = img.filter(ImageFilter.BLUR)
    processed_img.save(output_path)

def open_file():
    try:
        file_path = filedialog.askopenfilename(
            title="选择一张图片",
            filetypes=[("所有图片文件", "*.png;*.jpg;*.jpeg;*.bmp;*.gif"), ("所有文件", "*.*")]
        )
        if file_path:  # 确保用户选择了文件
            input_label.config(text=f"输入文件: {os.path.basename(file_path)}")
            global input_image_path
            input_image_path = file_path
            display_image(file_path, input_image_label)
    except Exception as e:
        messagebox.showerror("错误", f"无法选择图片: {e}")

def process_and_save():
    if not input_image_path:
        messagebox.showerror("错误", "请先选择一张图片！")
        return

    output_path = filedialog.asksaveasfilename(
        defaultextension=".png", filetypes=[("PNG Files", "*.png")]
    )
    if output_path:
        try:
            process_image(input_image_path, output_path)
            output_label.config(text=f"输出文件: {os.path.basename(output_path)}")
            display_image(output_path, output_image_label)
            messagebox.showinfo("成功", "图片处理完成！")
        except Exception as e:
            messagebox.showerror("错误", f"图片处理失败: {e}")

def display_image(image_path, label):
    img = Image.open(image_path)
    img.thumbnail((300, 300))  # 调整图片大小以适应 GUI
    img_tk = ImageTk.PhotoImage(img)
    label.config(image=img_tk)
    label.image = img_tk

# 初始化界面
root = tk.Tk()
root.title("图片处理工具")

# 输入图片部分
input_label = tk.Label(root, text="输入文件: 未选择")
input_label.pack()
input_image_label = tk.Label(root)
input_image_label.pack()
input_image_path = None

# 选择图片按钮
open_button = tk.Button(root, text="选择图片", command=open_file)
open_button.pack()

# 处理图片并保存
process_button = tk.Button(root, text="处理并保存", command=process_and_save)
process_button.pack()

# 输出图片部分
output_label = tk.Label(root, text="输出文件: 无")
output_label.pack()
output_image_label = tk.Label(root)
output_image_label.pack()

# 启动主循环
root.mainloop()
