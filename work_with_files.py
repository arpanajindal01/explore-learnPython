my_file = open('text.txt', 'r')
print(my_file.read())
my_file.close()

my_file_1 = open('text2.txt', 'w')
my_file_1.write("Hello Learners, lets learn Python today..!!")
my_file_1.close()

# With relative file path
with open('input_files/some_text.txt', 'r') as my_file_3:
    print(my_file_3.read())

# with absolute file path, replacing backslashes with forward slashes in python
with open('C:/Users/arpanaji/PycharmProjects/pythonForTestersProject/input_files/some_text.txt', 'r') as my_file_4:
    print(my_file_4.read())

# Exception Handling with I/O operations in File handling
try:
    with open('text4.txt', 'r') as new_file:
        print(new_file.read())

except FileNotFoundError:
    print("The requested file, text4.txt is not found, Please check again")


