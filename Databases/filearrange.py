import os

path = os.chdir("C:\\Users\\mi\\Desktop\\upload")

ls = list()
for file in os.listdir(path):
    if len(file) == 71:
        file = file.split('-')
        new_name = file[1]
    else:
        file = file.split('.')
        new_name = "{}.{}.pdf".format(file[1], file[2])

    os.rename(file, new_name)

    