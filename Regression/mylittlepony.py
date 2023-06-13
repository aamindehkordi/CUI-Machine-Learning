import re
if __name__ == '__main__':

    f = open('mlp.txt', 'r')
    script = f.read()
    matches = re.findall('[A-Z]+[A-Za-z ]*:', script)
    matches = set(matches)
    print(matches)
