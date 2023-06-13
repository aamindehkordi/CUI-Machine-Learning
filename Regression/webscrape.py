from urllib import request
import re
from bs4 import BeautifulSoup
def employee_Scraper(url):
    req = request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    content = request.urlopen(req).read().decode('UTF-8')
    
    full_matches = re.findall('<td>.*</td>', content)
    names = []
    namePatt = '[A-Za-z]*, [A-Za-z]*'
    numbers = []
    numbPatt = '\d\d\d-\d\d\d-\d\d\d\d'
    emails = []
    n = 2
    for match in full_matches:
        if n == 2:
            names.append(re.search(namePatt, match)[0])
            n -= 1
        elif n == 1:
            num = re.search(numbPatt, match)
            if num:
                num = num[0]
            else:
                numbers.append('None')
                continue
            numbers.append(f'({num[:3]}) {num[4:]}')
            n -= 1
        else:
            emails.append('Encrypted')
            n = 2
    print('(Names, Numbers, Emails) of CUI Employees:',list(zip(names, numbers, emails)))
    
    soup = BeautifulSoup(content, 'html.parser')
    print(soup.get_text()[790:-900])

if __name__ == '__main__':

    f = open('mlp.txt', 'r')
    script = f.read()
    pattern = '[A-Z]+[A-Za-z ]*:'
    matches = re.findall(pattern, script)
    matches = set(matches)
    print(matches, '\n')
    employee_Scraper('https://www.cui.edu/hr/employee-directory')