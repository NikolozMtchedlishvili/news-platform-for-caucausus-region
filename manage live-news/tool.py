#import urllib.request
#import webbrowser
#from simplified_scrapy import Spider, SimplifiedDoc, SimplifiedMain, utils
#import os
from serpapi import GoogleSearch

def main(query):
    params = {
        "q": f"{query}",
        "tbm": "isch",
        "ijn": "0",
        "api_key": "8f9e84bbbf4e0aed1c76dff99def29f5de9c0af412f6c21d11b9bd8f359a6857"
    }

    search = GoogleSearch(params)
    results = search.get_dict()
    images_results = results["images_results"]
    x = images_results[0]
    link = x['thumbnail'] 
    
    
    with open('img.txt', 'a+') as imgfile:
        imgfile.write(f'{link}\n')
    #one way to download X second to pull by url V
    #urllib.request.urlretrieve(link, "D:\Files\Desktop\live-news\img")


'''
def main():
    class ImageSpider(Spider):
        name = 'archillect'
        start_urls = [""]
        def afterResponse(self, response, url, error=None, extra=None):
            try:
                # Create file name
                end = url.find('?') if url.find('?')>0 else len(url)
                name = 'data'+url[url.rindex('/',0,end):end]
                # save image
                if utils.saveResponseAsFile(response,name,'image'):
                    return None 
                else:
                    return Spider.afterResponse(self, response, url, error)
            except Exception as err:
                print (err)
        def extract(self,url,html,models,modelNames):
            doc = SimplifiedDoc(html)
            urls = doc.listImg(url=url.url)
            return {'Urls':urls} 
    SimplifiedMain.startThread(ImageSpider()) # Start
'''