import readimg as readimg

def InsertIMG():
    count = 0
    with open('D:\Files\Desktop\live-news\scripts.js', 'r+') as js:
        lines = js.readlines()
        for line in lines:
            line = line.split('\n', 1)[0]
            to_write = line.replace('src=""',f'src="{readimg.Read(count)}"') #solution backslash /
            to_write = to_write.replace('\n','')
            print(to_write)
            js.write(f'\n{to_write}')
            count+=1
            


#InsertIMG()
        
        
