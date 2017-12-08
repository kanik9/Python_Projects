import requests
from bs4 import BeautifulSoup

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

def data():
    try:
        url = "https://timesofindia.indiatimes.com/"

        r = requests.get(url)
        """while True:
            if r.status_code != 200:
                break
            r = requests.get(url)"""

        soup = BeautifulSoup(r.text, 'html.parser')
        ele = soup.find_all('ul',{'class': {'list8', 'list_article', 'list2'}})

        i = 1

        for news in ele:
            print color.BLUE,color.UNDERLINE , "NEWS ",i, color.END, "\n"
            news1 = news.find_all('a')
            for num in news1:
                if num.text == "":
                    continue
                print u'\u2022'," ", num.text, "\n"
            print "\n"
            i+=1

    except Exception as e:
        print "ERROR Encountered"


def main():
    print "\t TODAY'S TOP NEWS\n"
    data()

if __name__ == '__main__':
    main()
