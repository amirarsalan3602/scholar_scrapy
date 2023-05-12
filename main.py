import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook
from urllib.parse import quote_plus
from time import sleep
import random
workbook = Workbook()  # create a new exel file

sheet = workbook.active  # create a new sheet

header = {
   # 'Cookie': '1P_JAR=2023-05-11-20; AEC=AUEFqZfNUjj55dRukdioVVp7vrMR3npE3kbviCLC4CAO_9YjwqluN8vYFQ; NID=511=OsY3Auqn86oNeawW0qKdkREJWIUt9145Ld8OwhlzDf53YZ9pfGU3GBPWvAceGpBvsAWrg864gFYwB7KyybSrx16f_FxrdySHmCHnnWFgAQs1jNs4UTMjBxIpLp6WZUryYUHA4uu3POLwwN2Jzyba7vlyvndePAPjNNXlpwoPEEM; GSP=LM=1683836743:S=mXXUyXv9SKeiE-9N',
    'Sec-Ch-Ua': '"Chromium";v="109", "Not_A Brand";v="99"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': "Linux",
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5414.75 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'X-Client-Data': 'CIXxygE=',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Referer': 'https://scholar.google.com/',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9',
}


def curling(query: str):
    query = quote_plus(query)
    url_counter = 0
    counter = 1
    while True:
        url = f"https://scholar.google.com/scholar?start={url_counter}&q={query}&hl=en&as_sdt=0,5"
        #sleep(random.randint(15,60))
        response = requests.get(url, headers=header)
        print(f'status : {response.status_code} ')
        content = BeautifulSoup(response.text, 'html.parser')
        sub = content.find_all('div', attrs={'class': 'gs_ri'})
        for i in sub:
            sheet[f'A{counter}'] = i.find('span', attrs={'dir': 'rtl'}).text  # wright a title on cell
            sheet[f'B{counter}'] = i.find('div', attrs={'class': 'gs_a'}).text  # wright a publisher on cell
            sheet[f'C{counter}'] = i.find('a').get('href')  # wright a url on cell
            workbook.save(filename='example.xlsx')  # save exel file
            counter += 1
            print(counter)
        url_counter += 10


curling('خشونت خانگی')