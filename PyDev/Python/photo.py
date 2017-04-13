#-*- coding:utf-8 -*-
import urllib.request
import shutil
import sys
import imp
from bs4 import BeautifulSoup

if __name__ == "__main__":
    print("Hello World")
            
    req = urllib.request.Request("http://gall.dcinside.com/board/view/?id=kimsohye&no=630655&page=1");
    data = urllib.request.urlopen(req).read()

    bs = BeautifulSoup(data, 'html.parser')
    li = bs.find_all('li')

    for ele in li:
        val = ele.get('class')
        if val != None and val[0] == 'icon_pic':
            base_url = ele.a.get("href")
            rp_from = "http://image.dcinside.com/download.php"
            rp_to = "http://dcimg2.dcinside.com/viewimage.php"
            base_url = base_url.replace(rp_from, rp_to);
            print(base_url)
            f = open("./" + ele.a.contents[0], "wb");
            img_req = urllib.request.Request(base_url);
            f.write(urllib.request.urlopen(img_req).read())
            f.close()

'''
## 요구사항 3

오픈베이스 홈페이지의 PR센터>포토갤러리(http://openbase.co.kr/pr/gallery)에 있는 이미지 파일들을 추출해 저장하고 싶습니다.
1. URL의 요청 결과(html)를 문자열로 반환하는 함수를 구현해주세요.
2. 포토갤러리의 문자열을 분석(파싱)해 이미지들의 URL을 추출해보세요.
3. 추출한 이미지 URL을 이용해서 로컬 디스크에 이미지 파일들을 저장해보세요. 파일명은 URL에 명시된 명칭을 사용해주세요.
'''
