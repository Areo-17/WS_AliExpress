from bs4 import BeautifulSoup
import requests
'''def url_searching():
    raw1_url = 'https://es.aliexpress.com/w/wholesale-'
    raw2_url = '.html?spm=a2g0o.home.search.0'
    searching = str(input('What do you want to find? '))
    url_req = "'" + raw1_url + searching + raw2_url + "'"
    return url_req'''

if __name__ == '__main__':
    #From this line, the script will find and give you the link of the desired page.
    raw1_url = 'https://es.aliexpress.com/w/wholesale-'
    raw2_url = '.html?spm=a2g0o.home.search.0'
    searching = str(input('What do you want to find? '))
    searching = searching.replace(' ', '-')
    url_req = raw1_url + searching + raw2_url
    print(url_req)
    result = requests.get(url_req)
    print(result.status_code)
    #Part of the code to find the number of page you want to go.
    page = str(input('What page do you want to go? '))
    raw3_url = '.html?page='
    raw4_url = '&g=y&SearchText='
    p_searching = raw1_url + searching + raw3_url + page + raw4_url + searching
    page_content = requests.get(p_searching)
    print(p_searching)
    #From this line, the script will take the html code of the desired number of page.
    content = page_content.text
    soup = BeautifulSoup(content, 'lxml')
    print(soup.prettify())
