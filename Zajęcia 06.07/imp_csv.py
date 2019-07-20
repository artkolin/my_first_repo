import csv


if __name__ == "__main__":
    f = open('example.txt', 'r+')
    file_lines = f.readlines()
    print(file_lines)
    f.writelines(['line3\n'])