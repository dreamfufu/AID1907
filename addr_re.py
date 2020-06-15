import re

def get_address(file):
    port = input('端口:')
    while True:
        data = ''
        for line in file:
            if line == '\n':
                break
            data += line
        obj = re.match(port,data)
        if obj:
            print(data)

if __name__ == '__main__':
    f = open('exc.txt')
    print(get_address(f.read()))