from lxml import html  
import csv,os,json
import requests
from exceptions import ValueError
from time import sleep


def AmzonParser(url):
    headers = {'User-Agent': 'Mozilla/5.0'}
    page = requests.get(url,headers=headers)
    while True:
        sleep(3)
        try:
            doc = html.fromstring(page.content)
            XPATH_NAME = '//div[@id="anonCarousel2"]//os@class='a-carousel']//li[contains(@class,'a-carousel-card')]//div[contains(@class,'a-section')]//div[contains(@class,'a-row')]//a[contains(@class,'a-link-child')]"'
            
            RAW_NAME = doc.xpath(XPATH_NAME)       
 
            NAME = ' '.join(''.join(RAW_NAME).split()) if RAW_NAME else None
 
            if not ORIGINAL_PRICE:
                ORIGINAL_PRICE = SALE_PRICE
 
            if page.status_code!=200:
                raise ValueError('captha')
            data = {
                    'NAME':NAME,
                    'URL':url,
                    }
 
            return data
        except Exception as e:
            print e
 
def ReadAsin():
    searchurl="https://www.amazon.co.jp/s?k=%E3%81%82%E3%81%84%E3%81%BF%E3%82%87%E3%82%93" 
    headers = {'User-Agent': 'Mozilla/5.0'}
    page = requests.get(searchurl,headers=headers)
    soup = Beautifulsoup(page.contains,"html.parser")
    #links = soup.find_all('a',href=True)
    links = []


    #fetch("https://www.amazon.co.jp/s?k=%E3%81%82%E3%81%84%E3%81%BF%E3%82%87%E3%82%93")
    #response.xpath("//div[@class='sg-col-inner']")
    #products = response.xpath("//div[@class='sg-col-inner']")
    for eachPart in soup.select('a[class *= "a-text-bold"]')
        print eachPart.get_text()
        if "CD" in  str(eachPart):
            #get all the CD link
           link = eachPart['href']
           links.append(link)

        elif "DVD" in str(eachPart):
            #get all the DVD link
            link = eachPart['href']
            links.append(link)
        else "Blu-ray" in str(eachPart):    
            #get all the Blu-ray link
            link = eachPart['href']
            links.append(link)

    for delink in links:
        searchASIN = re.search(r'B[A-Z0-9]{9}', delink)
        #print(searchASIN.group(0))
        AsinList = []
        AsinList.append(searchASIN.group(0))

        extracted_data = []
    for i in AsinList:
        url = "http://www.amazon.com/dp/"+i
        print "Processing: "+url
        extracted_data.append(AmzonParser(url))
        sleep(5)
    f=open('data.json','w')
    json.dump(extracted_data,f,indent=4)
 
 
if __name__ == "__main__":
    ReadAsin()