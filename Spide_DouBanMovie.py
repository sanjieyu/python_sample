import requests
from bs4 import BeautifulSoup

class MovieTop(object):
    def __init__(self):
        self.start =  0
        self.param = '&filter='
        self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0'}
        self.movie_list = []
        self.file_path = 'D:\movie_spider.txt'

    def get_pages(self):
        for i in range(0,10):
            link = 'https://movie.douban.com/top250?start='+str(i*25)
            r = requests.get(link,headers=self.headers)
            print(str(i+1),"页相应代码：",r.status_code)
            # print(r.text)
            soup = BeautifulSoup(r.text,features='html.parser')
            div_list = soup.find_all('div',class_='hd')
            for each in div_list:
                movie = each.a.span.text.strip()
                self.movie_list.append(movie)
        # with open(r"D:\movie_spider.txt","w") as f:
        with open(self.file_path, "w") as f:
            for i in range(len(self.movie_list)):
                s = str(self.movie_list[i]).replace('[','').replace(']','') #去除[],这两行按数据不同，可以选择
                s = s.replace("'",'').replace(',','') + '\n' #去除单引号，逗号，每行末尾追加换行符
                f.write(s)
        return self.movie_list

if __name__ == '__main__':
    m = MovieTop()
    m.get_pages()
