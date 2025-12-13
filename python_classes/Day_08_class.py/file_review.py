# create a file 
# with open("new-file.txt", "x") as f:
#     print(f.name, f.mode)


# with open("review.txt", "w") as f:
#     f.write("This is file that i created \n")
#     f.write("This is second line i created \n")
    

# with open("review.txt", "a") as f:
#     f.write("the is recentely added text")


# with open("newfile.txt", "r") as f:
#     data = f.read()
#     print(data)

with open("resized.jpg", "rb") as f:
    data = f.read()
    print(data)

with open("resized_copy.jpg", "wb") as f:
    data1 = f.write(data)
    print(data1)