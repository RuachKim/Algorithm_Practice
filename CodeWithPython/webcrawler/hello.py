import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

baseurl = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query='
search = input('what do you want to search: ')
url = baseurl + urllib.parse.quote_plus(search)
#print(url)
html = urllib.request.urlopen(url).read()

soup = BeautifulSoup(html, 'html.parser')

# title = soup.find_all(class_ = 'sh_blog_title')

# for blog in title:
#     print(blog.attrs['title'])


img = soup.find_all(class_ = '_img')
print(img)
#print(img[0])
index = 1
for i in img:
    imgUrl = i['data-source']
    with urllib.request.urlopen(imgUrl) as f:
        with open( search + str(index) + '.jpg', 'wb') as h:
            img_dat = f.read()
            h.write(img_dat)
    index += 1


print('img download finished!!')
