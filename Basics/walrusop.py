names = ["John", "Jane", "Jim"]

if (name := input("Enter a name: ")) in names:
    print(f"Hello, {name}!")
else:
    print("Name not found.")


names = ["harsh","pako","mako"]

if(name := input("Enter a name:")) in names:
    print(f"hello {name}")
else:
    print("Name not found") 