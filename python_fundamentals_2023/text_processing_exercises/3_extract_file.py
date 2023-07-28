input_str = input()
file = input_str.split('\\')[-1]
filename, extension = file.split(".")
print(f"File name: {filename}")
print(f"File extension: {extension}")