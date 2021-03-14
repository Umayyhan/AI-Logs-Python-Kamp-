import requests
import operator
from bs4 import BeautifulSoup

def sozlukolustur(tumkelimeler):
  kelimesayisi = {} #sozluk yapisi kullanildi
  for kelime in tumkelimeler:
    if kelime in kelimesayisi:
      kelimesayisi[kelime] +=1
    else:
      kelimesayisi[kelime]= 1
  return kelimesayisi


def sembolleritemizle(tumkelimeler):
  sembolsuzkelimeler =[]
  semboller = "1234567890!@$#%^*()_+{}\"<>?,./;'[]|-=´`:" + chr(775)# sayilari da ek olarak çikardim
  for kelime in tumkelimeler :
    for sembol in semboller:
      if sembol in kelime:
        kelime =kelime.replace(sembol,"")
    if(len(kelime) > 0):
      sembolsuzkelimeler.append(kelime)
  return sembolsuzkelimeler 



url ="https://www.ntv.com.tr/teknoloji/aziz-sancar-nobel-kimya-odulunu-aldi,F10C10YMBEaCIMqnra3I2w"

tumkelimeler = []
r = requests.get(url)
soup = BeautifulSoup(r.content,"html.parser")

for kelimegruplari in soup.find_all("p"):
#p etiketine sahip tum kelime gruplarını aliyoruz
  icerik = kelimegruplari.text
  kelimeler =icerik.lower().split() #lower ile kucuk harfe cevirdik split ile bosluklara gore ayirdik

  for kelime in kelimeler:
    tumkelimeler.append(kelime)

tumkelimeler = sembolleritemizle(tumkelimeler)
for kelime in tumkelimeler:
  print(kelime)# anahtar kelime oluşturmak için

kelimesayisi = sozlukolustur(tumkelimeler)

for anahtar,deger in sorted(kelimesayisi.items(),key = operator.itemgetter(1)): # 0 alfabetik sıraya gore, 1 degere gore siraliyacaktir
  print(anahtar,deger)