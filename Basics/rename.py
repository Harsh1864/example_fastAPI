import os

file = os.listdir("png")
i=1
for files in file:
    if files.endswith(".jpeg"):
        os.rename(f"png/{files}",f"png/{i}.png")
        i=i+1
    # print(files)
