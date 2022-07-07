import os

file_path = 'C:/Users/me/Desktop/졸과'
file_names = os.listdir(file_path)
file_names

for name in file_names:
    number = name[4:-3]
    print(number)
