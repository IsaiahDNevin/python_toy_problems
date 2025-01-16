
with open('alice_in_wonderland.txt', 'r', encoding='utf-8') as f:
    print(f.tell())
    one_line = f.readline()
    while one_line:
        print(one_line[:-1], f.tell())
        one_line = f.readline()

def read_file(file_path):
    try:
        with open('alice_in_wonderland.txt', 'r', encoding='utf-8') as file:
            content = file.read()
        return content
    except FileNotFoundError:
         return "File not found. Please check the file path."
    except Exception as e:
         return f"An error occured: {e}"
    

def main():
    file_path = "alice_in_wonderland.txt"
    content = read_file(file_path)

    print(content)

if __name__ == "__main__":
    main()  