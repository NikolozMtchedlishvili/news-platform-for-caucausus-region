from bs4 import BeautifulSoup
import requests
# add sites in test.py
def scrape():
    open('data.txt', 'w').close()
    open('scripts.js', 'w').close()
    url = "https://caucasus.liveuamap.com/en"
    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')
    array = ['cat7', 'cat2', 'cat1', 'cat6']
    for cat in array:
        lists = soup.find_all('div', class_=f"event {cat} sourcees")#cat7 cat2 cat1 cat6 
        with open('data.txt', 'a+', encoding='utf8', newline='') as f: # yuradgeba

            for list in lists:

                title = list.find('div', class_="title").text.replace('\n', '')
                time = list.find('span', class_="date_add").text.replace('\n', '')

                info = (title + '  ' + time + ' - Liveuamap')
                f.write(f'\n{info}')
        f.close()

    url2 = "https://www.rferl.org/p/5498.html"
    page2 = requests.get(url2)

    soup2 = BeautifulSoup(page2.content, 'html.parser')
    lists2 = soup2.find_all('li', class_="col-xs-12 col-sm-6 col-md-6 col-lg-6 mb-grid")
    with open('data.txt', 'a+', encoding='utf8', newline='') as f2:

        for list2 in lists2:

            title2 = list2.find('h4', class_="media-block__title").text.replace('\n', '')
            info2 = (title2 + '.' + ' - Radio Free')
            f2.write(f'\n{info2}')
    f2.close()
    '''
    url3 = "https://eurasianet.org/region/caucasus"
    page3 = requests.get(url3)
    soup3 = BeautifulSoup(page3.content, 'html.parser')
    lists3 = soup3.find_all('div', class_="views-view-sidebar__content")
    with open('data.txt', 'a+', encoding='utf8', newline='') as f3:

        for list3 in lists3:

            title3 = list3.find('h2', class_="teaser__title").text.replace('\n', '')
            info3 = (title3 + '.' + ' - Eurasianet')
            f3.write(f'\n{info3}')
    f3.close()
    '''
