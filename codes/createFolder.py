import os


def main():

     file = "./test_createFoler"
     mkdir(file)


def mkdir(path):

     folder = os.path.exists(path)

     if not folder:
         os.makedirs(path)
         print('Folder has been created successfully.')
         print("PATH:", path)
     else:
         print('Folder already existed.')
         print("PATH:", path)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit()
