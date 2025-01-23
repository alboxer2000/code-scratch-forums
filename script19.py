def read(filepath):
    file = open(filepath, 'r')
    content = file.read() # we have to do this instead of return file.read because we need to close the file
    file.close()
    return content
def write(filepath, content): # This appends onto the end of the file, if you want it to delete the file then write instead, change the a in "file = open(file, 'a')" to a w.
    file = open(file, 'a')
    file.write(content)
    file.close()
# How to use these functions
# If boring_folder/boring_file.txt contained "boring text", the below would print boring_folder/boring_file.txt to the terminal:
print(read("boring_folder/boring_file.txt"))
# And the below would write "this aint boring no more" to boring_folder/boring_file.txt
write("boring_folder/boring_file.txt", "this aint boring no more")
