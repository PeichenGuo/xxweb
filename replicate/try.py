
import replicate
import os

def process_image(input_path, output_path):
    """
    图片处理逻辑：可以替换为你的实际处理逻辑。
    示例：添加模糊效果。
    """
    image = open(input_path, 'rb')
    output = replicate.run(
        "fofr/face-to-many:a07f252abbbd832009640b27f063ea52d87d7a23a185ca165bec23b5adc8deaf",
        input={
            "image":image,
            "style": "Video game",
            "prompt": "a person in a post apocalyptic war game",
            "negative_prompt": "",
            "prompt_strength": 4.5,
            "denoising_strength": 0.65,
            "instant_id_strength": 0.8
        }
    )
    # if output is None:
    #     print(f"{input_path} process failed")
    # Save the generated image
    with open(output_path, 'wb') as f:
        img = output[0]
        f.write(img.read())

def batch_process(input_folder, output_folder):
    """
    批量处理图片。
    :param input_folder: 输入文件夹路径
    :param output_folder: 输出文件夹路径
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for file_name in os.listdir(input_folder):
        input_path = os.path.join(input_folder, file_name)

        # 检查是否为图片文件（扩展名检查）
        if file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            output_path = os.path.join(output_folder, file_name)

            try:
                process_image(input_path, output_path)
                print(f"已处理: {file_name}")
            except Exception as e:
                print(f"处理失败: {file_name}, 错误信息: {e}")

# 输入和输出文件夹路径
input_folder = "input"  # 输入图片文件夹路径
output_folder = "output"  # 输出图片文件夹路径

batch_process(input_folder, output_folder)