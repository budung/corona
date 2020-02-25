from bs4 import BeautifulSoup
import requests
import os
path = os.path.join(os.path.dirname(__file__), 'index.html')
self.response.out.write(template.render(path, template_values))

r1 = requests.get('https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=%EC%BD%94%EB%A1%9C%EB%82%9819')
html = r1.text
soup = BeautifulSoup(html,'html.parser')
a=soup.select('strong[class="num"]')
hw="확진자: "+str(a[0].text)
wa="완치자: "+str(a[1].text)
gu="검사중: "+str(a[2].text)
sa="사망자: "+str(a[3].text)

# hw 확진자
# wa 완치자
# gu 검사중
# sa 사망자