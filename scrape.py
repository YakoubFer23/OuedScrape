from bs4 import BeautifulSoup
import requests
import re

response = requests.get('https://www.ouedkniss.com/emploi_offres').text
#response += requests.get('https://www.ouedkniss.com/emploi_offres/2').text

soup = BeautifulSoup(response,'lxml')

jobs = soup.find_all('div', class_ = 'annonce')

def Print():
    try:
        if ("minutes" in time.text):
            print(f'New Job Available: {title.text} in {wilaya.text} since {time.text} Email: {email} Phone: {phone}')
    except:
        pass



try:
    for job in jobs:
        time = job.find('p', class_= 'annonce_date')
        title = job.find('h2')
        wilaya = job.find('span', class_ = 'titre_wilaya')
        atag = job.find('a', href=True)
        link = 'https://www.ouedkniss.com/' + atag['href']
        res = requests.get(link).text
        annonce = BeautifulSoup(res,'lxml').find('div', id='Annonceur')
        hatif = BeautifulSoup(res,'lxml').find('p', class_='Phone')
        if (annonce.find('p', class_='Email') != None):
            email = annonce.find('p', class_='Email').text
        else:
            email = 'No Email'
        if (hatif.find('a') != None):
            phone = hatif.find('a')['href']
        else:
            phone = 'no phone'
        Print()
except:
    pass