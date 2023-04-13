from PIL import Image,ImageFilter
import sys
import os

input_folder = sys.argv[1]#you take two folder name in terminal
output_folder = sys.argv[2]#1 for jpg folder 1 for png folder
if not os.path.exists((output_folder)):
    os.makedirs(output_folder)
    print('hello')

for filename in os.listdir(input_folder):
    img = Image.open(f'{input_folder}{filename}')
    clean_name = os.path.splitext(filename)[0]
    img.save(f'{output_folder}{clean_name}.png','png')
    print('done!')
     