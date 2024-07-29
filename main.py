import httpx
from bs4 import BeautifulSoup
url='https://www.houseoffraser.co.uk/women/tops'
headers={
    "User-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
}

def main():
    response=httpx.get(url,headers=headers)
    response_html=response.text

    soup=BeautifulSoup(response_html,'html.parser')
    print(soup.get_text())
    print(soup.title)

# <title>The Dormouse's story</title>

    print(soup.title.name)
# u'title'

    print(soup.title.string)
# u'The Dormouse's story'

    print(soup.title.parent.name)
# u'head'

    print(soup.p)
# <p class="title"><b>The Dormouse's story</b></p>

    print(soup.p['class'])
# u'title'

    print(soup.a)
# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>

    print(soup.find_all('a'))
    # [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

    print(soup.find(id="link3"))    

if __name__ == '__main__':
    main()
