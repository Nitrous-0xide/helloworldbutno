import os

def read_comment():
    # Get the filename of the current script
    filename = os.path.basename(__file__)
    
    with open(filename, 'r') as file:
        for line in file:
            if line.strip().startswith("# HelloWorld:"):
                return line.split(":", 1)[1].strip()

def print_message():
    message = read_comment()
    if message:
        print(message)
    else:
        print("No HelloWorld comment found.")

if __name__ == "__main__":
    print_message()

# HelloWorld: Hello, World!
