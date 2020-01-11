from django.shortcuts import render
from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup

def index(request):
    params = {
            'title' :'検索ページフロント',
            'msg':'山中検索',
            'goto':'search',
    }

    return render(request, 'hello/index.html', params)

def search(request):

    #Googleの検索画面から「NTTデータ」で検索したときのURL
    url = "https://www.google.com/search?q=ntt%E3%83%87%E3%83%BC%E3%82%BF&source=lnms&tbm=nws&sa=X&ved=2ahUKEwjNv8\
    ShtN_mAhWQBKYKHRtLDFYQ_AUoAXoECA0QAw&cshid=1577778876525367&biw=1608&bih=948"

    #検索した結果を格納
    r = requests.get(url)

    #BeautifulSoupメソッドを使用し、解析
    soup = BeautifulSoup(r.text, 'html.parser')

    #htmlの<a>タグのみを抽出
    elems = soup.find_all("a")
    elems_a = []
    elems_b = []

    #<a>タグから記事のタイトルを抽出
    for e in elems:
        elems_a.append(e.getText())
    for f in elems_a:
        if "NTTデータ" in f:
            elems_b.append(f)

    #print(elems_b)

    #elems_href = soup.get("href")
    #<a>タグからURLのみを抽出
    elems_c = []
    elems_d = []
    for g in elems:
        elems_c.append(g.get("href").replace('/url?q=',''))
        #elems_c.append(g.get("href"))
    for h in elems_c:
        if "https" in h:
            if "google" not in h:
                elems_d.append(h)
    print(elems_c)

    #返却するパラメータを設定
    params = {
            'title': '検索ページ結果',
            'msg': elems_b,
            'url_news': elems_d,
            'goto': 'index',
        }
    #結果を返却する
    return render(request, 'hello/search.html', params)

    '''params = {
        'title': '検索ページ結果',
        'msg': '鈴木検索',
        'goto': 'index',
    }
    return render(request, 'hello/index.html', params)'''

# Create your views here.

