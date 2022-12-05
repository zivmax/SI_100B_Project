import os


def main():

     file = "D:\\python\\cache"
     mkdir(file)


def mkdir(path):     # os.path.exists 函数判断文件夹是否存在

     folder = os.path.exists(path)      # 判断是否存在文件夹如果不存在则创建为文件夹

     if not folder:         # os.makedirs 传入一个path路径，生成一个递归的文件夹；如果文件夹存在，就会报错,因此创建文件夹之前，需要使用os.path.exists(path)函数判断文件夹是否存在；
         os.makedirs(path)  # makedirs 创建文件时如果路径不存在会创建这个路径
         print('Folder has been created successfully.')
         print("PATH:", path)
     else:
         print('Folder already existed.')
         print("PATH:", path)


if __name__ == "__main__":
     main()
