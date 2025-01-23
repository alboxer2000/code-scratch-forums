# write to file:
with open("file.txt", "w") as f:
    f.write("I wrote something to a file!!! YAY!!!")
#
#
# append to file (add more stuff to the end of a file):
with open("file.txt", "a") as f:
    f.write("I appended something! :D")
#
#
# read file:
with open("file.txt", "r") as f:
    print(f.read())
