with open("logging_python_log", "r+") as file: 
    x=file.read()
with open("logging_python_log", "w+") as file:
    x=x.replace('cloud','engine')
    file.write(x)