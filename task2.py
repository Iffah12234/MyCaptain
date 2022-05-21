filename =input("Input the filename: ")
x= filename.split(".")
f=x[-1]
print(f)


file_ext={
    "jsp":"java",
    "py":"Python",
    "pl":"pearl",
    "cpp":"c++"}

x= file_ext.get(f)
print("The extension of the file is: ",x)
