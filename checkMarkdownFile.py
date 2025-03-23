# 检查markdown文件是否有异常的
import os
import re

import chardet

def get_encoding(file):
    with open(file, 'rb') as f:
        result = chardet.detect(f.read())
        return result['encoding']
# (/assets/image/default/ea4327ee99d7e459665f4eacf4fda6a2.png) ,我检查图片是否存在，不存在就取消吧
pattern = f'\(/assets/image/default/[^)]*\)'
pattern2 = f'!\[\]'

flags = re.IGNORECASE | re.MULTILINE

script_dir = os.path.split(os.path.realpath(__file__))[0]
print(f'脚本所在的目录是:{script_dir}')

Post_dir = os.path.join(script_dir, '_posts')
print(f'博文所在的文件夹:{Post_dir}')

# 取得所有的文件
post_files = os.listdir(Post_dir)
post_files = [i for i in post_files if i.endswith('.md')]
print(f'一共有{len(post_files)}个markdown文件')

def check_markdown(file_name):
    file_path = os.path.join(Post_dir, file_name)
    encoding = get_encoding(file_path)
    with open(file_path, 'r', encoding=encoding) as f:
        content = f.read()
        # 这里进行解析无效的图片
        img_paths = re.findall(pattern, content, flags)
        if len(img_paths) >0:
            # 检查图片是否存在
            for img_name in img_paths:
                img_path = os.path.join(script_dir, img_name[1:-1])
                if not os.path.exists(img_path):
                    print(f'不存在:{img_name}')
                    # 然后这里进行删除
                    content = content.replace(img_name, '')
        # 图片中的alt为空
        content = content.replace('![]', '![no img]')
        # img_alt_paths = re.findall(pattern2, content, flags)
        # if len(img_alt_paths) >0:
        #     # 检查图片是否存在
        #     for img_name in img_alt_paths:
        #         content = content.replace(img_name, '![no img]')


            # 最后保存文件
    with open(file_path, 'w', encoding=encoding) as f:
            f.write(content)

for file_name in post_files:
    check_markdown(file_name)