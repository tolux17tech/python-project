file=open("practise_python_log", "w+")
file.write("I love engineering")
file.close()

file=open("practise_python_log", "r+")
file_mi=file.read()
print(file_mi)
file.close