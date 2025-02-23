filename = "example.txt"

with open(filename, "w", encoding="utf-8") as file:
    file.write("Hello World!")

with open(filename, "r", encoding="utf-8") as file:
    content = file.read()
    print(content)
