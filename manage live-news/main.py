import os
import webscraper_sites as sites
import split as spl
import insert as ins

def scrape():
    sites.scrape()


def opendata():
    temp = open('D:\Files\Desktop\live-news\scripts.js', 'w')
    temp.close()
    with open('data.txt', 'r+') as datafile:
        lines = datafile.readlines()
        datafile.seek(0)
        datafile.truncate()
        datafile.writelines(lines[1:])
        datafile.close()
        with open('data.txt') as datafile2:
            for lines in datafile2:
                x = lines.strip()
                array = []
                array.append(x)
                for data in array: 
                    info = data.replace("'","")
                    with open('D:\Files\Desktop\live-news\scripts.js', 'a+') as js: # yuradgeba
                        content = f"""document.getElementById('div2').innerHTML += '<div><ul><li style="list-style-type: square;"><a href="" style="padding-top: 3%; text-decoration: none; font-size: 220%; color: black;">{info}</a></ul><ul><img src="" alt="Image not loading" class="responsive"></ul></li></div>';\n"""
                        js.write(content)                                
                                
    
# do: find new API, changing system (how I change URL of image), sorting system
            

if __name__ == '__main__':
    scrape()
    opendata()
    spl.Split()
    spl.Generate()
    ins.InsertIMG()
    os.remove('scripts.js')

# datafile.close()
# datafile2.close()
# js.close()


'''
if ' - Liveuamap' in info:
    src = 'https://caucasus.liveuamap.com' # {src}
    content = f"""\n\ndocument.getElementById('div2').innerHTML += '<div><ul><li style="list-style-type: square;"><a href="" style="padding-top: 3%; text-decoration: none; font-size: 220%; color: black;">{info}</a></ul><ul><img src="{}" alt="Image not loading" class="responsive"></ul></li></div>';"""
    js.write(content)
elif ' - Radio Free' in info:
    src = 'https://www.rferl.org/p/5498.html' # {src}
    content2 = f"""\n\ndocument.getElementById('div2').innerHTML += '<div><ul><li style="list-style-type: square;"><a href="" style="padding-top: 3%; text-decoration: none; font-size: 220%; color: black;">{info}</a></ul><ul><img src="{}" alt="Image not loading" class="responsive"></ul></li></div>';"""
    js.write(content2)
'''