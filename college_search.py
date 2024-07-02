#! /usr/bin/python3
from bs4 import BeautifulSoup
from colorama import Fore,Style
import sys
import requests
import json

class CollegeSearch:
    def __init__(self):
        self.urllist = []
        self.position = []
        self.collegesnames = []
        self.collegesfees = []
        self.header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}

    def search(self)-> str:
        try:
            self.url = f"https://collegedunia.com/{self.course}/{self.city}-colleges"
            self.response = requests.get(self.url,headers=self.header)
            self.response.raise_for_status()
            return self.response.text
        except:
            print("Some Error Occured During Connection...")
            sys.exit(1)

    def parser(self):
        self.html = self.search()
        self.soup = BeautifulSoup(self.html,"html.parser")

    def clglinks(self):
        try:
            links = self.soup.findAll("script")[2]
            for _ in links:
                json_content = links.string
                dict_data = json.loads(json_content)
                list1 = dict_data['itemListElement']
                for i in list1:
                    self.urllist.append(i['url'])
                    self.position.append(i['position'])
        except Exception as e:
            print(f"Some Error Occured...'\n'{e}")
            sys.exit(1)

    def clgname(self):
        for i in self.urllist:
            name = i.split('/')[-1]
            self.collegesnames.append(name.partition('-')[-1])

    def clgfees(self):
        td_tags = self.soup.find_all('td', class_='jsx-1948362374 col-fees')
        for i in td_tags:
            college_fees = i.find('a')
            if college_fees:
                college_fee = college_fees.get_text(strip=True)
            else:
                college_fee = 'N/A'
            self.collegesfees.append(college_fee)

    def savelinks(self):
        ask = input("Do You Want To Save Links y/N : ")
        if ask == 'y':
            try:
                with open("links.txt",'w') as f:
                    for i,links in enumerate(self.urllist):
                        f.write(f'{i}  {links}\n')
            except Exception as e:
                print(e)
                print('Unable To Save in File...')

    def colourline(self)-> str:
        i = "*" * 21
        l = ""
        for i in i[0::1]:
            l += Fore.CYAN + Style.BRIGHT + i
            l += Fore.RED + Style.BRIGHT + i
            l += Fore.GREEN + Style.BRIGHT + i
            l += Fore.BLUE + Style.BRIGHT + i
            l += Fore.YELLOW + Style.BRIGHT + i
            l += Fore.MAGENTA + Style.BRIGHT + i
        return l

    def run(self):
        self.city = input("Enter Your City Here:- ").lower().split()[0]
        self.course = input("Enter Your Course(BCA or Btech) Here:- ").lower().split()[0]
        self.parser()
        self.clglinks()
        self.clgname()
        self.clgfees()
        self.savelinks()
        colour = self.colourline()
        print(colour + Fore.GREEN + Style.BRIGHT)
        print('{:^5}{:<85}{:<20}'.format("Sn ", "Colleges-Name", "Colleges-Fees"))
        print(Fore.RESET + Style.BRIGHT)
        for i,j,k in zip(self.position,self.collegesnames,self.collegesfees):
            print('{:^5}{:<85}{:<20}'.format(i,j,k))
        print(colour + Fore.RESET + Style.RESET_ALL)

if __name__ == '__main__':
    obj = CollegeSearch()
    obj.run()