
def Read(count):
    with open('img.txt') as imgfile:
        lines = imgfile.readlines()
        return lines[count]
