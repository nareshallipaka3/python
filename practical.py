import requests
import pandas as pd
from bs4 import BeautifulSoup

response=requests.get("https://www.flipkart.com/tyy/4io/~cs-5ysprk7w3p/pr?sid=tyy%2C4io&collection-tab-name=Galaxy+S23+FE&param=4533&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InZhbHVlQ2FsbG91dCI6eyJtdWx0aVZhbHVlZEF0dHJpYnV0ZSI6eyJrZXkiOiJ2YWx1ZUNhbGxvdXQiLCJpbmZlcmVuY2VUeXBlIjoiVkFMVUVfQ0FMTE9VVCIsInZhbHVlcyI6WyJGcm9tIOKCuTMzLDk5OSoiXSwidmFsdWVUeXBlIjoiTVVMVElfVkFMVUVEIn19LCJ0aXRsZSI6eyJtdWx0aVZhbHVlZEF0dHJpYnV0ZSI6eyJrZXkiOiJ0aXRsZSIsImluZmVyZW5jZVR5cGUiOiJUSVRMRSIsInZhbHVlcyI6WyJTYW1zdW5nIFMyMyBGRSJdLCJ2YWx1ZVR5cGUiOiJNVUxUSV9WQUxVRUQifX0sImhlcm9QaWQiOnsic2luZ2xlVmFsdWVBdHRyaWJ1dGUiOnsia2V5IjoiaGVyb1BpZCIsImluZmVyZW5jZVR5cGUiOiJQSUQiLCJ2YWx1ZSI6Ik1PQkdWVEEyR1JWUlhWRlIiLCJ2YWx1ZVR5cGUiOiJTSU5HTEVfVkFMVUVEIn19fX19")
print(response)
soup=BeautifulSoup(response.content,'html.parser')
# print(soup)

names=soup.find_all('div',class_="KzDlHZ")
# print(names)
name=[]
for i in names[0:5]:
    d=i.get_text()
    name.append(d)
# print(name)

prices=soup.find_all('div',class_="Nx9bqj _4b5DiR")
price=[]
for i in prices[0:5]:
    v=i.get_text()
    price.append(i)
# print(price)

ratings=soup.find_all('div',class_="XQDdHH")
rating=[]
for i in ratings[0:5]:
    s=i.get_text()
    rating.append(i)
# print(rating)


images=soup.find_all("img",class_="DByuf4")
image=[]
for i in images[0:5]:
    f=i['src']
    image.append(i)
# print(image)


links=soup.find_all("a",class_="CGtC98")
link=[]
for i in links[0:5]:
    b="https://www.flipkart.com"+i['href']
    link.append(i)
# print(link)

df=pd.DataFrame()
df['Names']=name
df['Prices']=price
df['Ratings']=rating
df['Images']=image
df['Links']=link
print(df)

df.to_csv('mobiles.csv')
