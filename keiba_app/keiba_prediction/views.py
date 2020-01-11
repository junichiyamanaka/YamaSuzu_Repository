from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .form import KeibaForm
from bs4 import BeautifulSoup
import urllib.request as req
from .models import Horse
from .form import KeibaCreateForm
from django.shortcuts import redirect
import ssl
import re



# Create your views here.

class KeibaView(TemplateView):

    def __init__(self):
        self.paramas = {
            'title': '鈴木の競馬サイト',
            'message': 'your data:',
            'form': KeibaForm(),
            'text': '馬名'

        }

    def get(self,request):
        return render(request, 'keiba_prediction/index.html', self.paramas)

    def post(self, request):
        msg = '日付：<b>' + request.POST['date'] +\
            '</b><br>レース<b>' + request.POST['choice'] +\
            '</b> です。'
        ssl._create_default_https_context = ssl._create_unverified_context
        url = "http://race.netkeiba.com/?pid=race&id=c201806040711&mode=shutuba"
        res = req.urlopen(url)
        soup = BeautifulSoup(res, "html.parser")
        #馬名を取得
        h_name = soup.find_all(class_="h_name")
        name_list = []
        for i in h_name:
            name_list.append(i.get_text())
        #性齢を取得
        h_age = soup.find_all(class_="txt_smaller")
        age_list = []
        for i in h_age:
            age_list.append(i.get_text())
        #結合
        k = 1
        for j in age_list:
            name_list.insert(k, j)
            k = k + 2


        self.paramas['message'] = msg
        self.paramas['form'] = KeibaForm(request.POST)
        self.paramas['name_list'] = name_list
        #self.paramas['age_list'] = age_list
        #self.paramas['text'] = text
        return render(request, 'keiba_prediction/index.html', self.paramas)

def horse_db(request):
    data = Horse.objects.all()
    params = {
        'title': 'Keiba',
        'message': 'all Horse',
        'data': data,
    }

    return render(request, 'keiba_prediction/horse.html', params)

def create(request):
    params = {
        'title': 'Keiba',
        'form': KeibaCreateForm(),
    }

    if (request.method == 'POST'):
        horse = request.POST['horse']
        f_horse = request.POST['f_horse']
        m_horse = request.POST['m_horse']
        ff_horse = request.POST['ff_horse']
        fm_horse = request.POST['fm_horse']
        mf_horse = request.POST['mf_horse']
        mm_horse = request.POST['mm_horse']
        age = request.POST['age']
        keiba = Horse(horse=horse,f_horse=f_horse,m_horse=m_horse,ff_horse=ff_horse,
                      fm_horse=fm_horse,mf_horse=mf_horse,mm_horse=mm_horse,age=age)
        keiba.save()
        return redirect(to='/keiba_prediction/index')
    return render(request, 'keiba_prediction/create.html',params)

def edit(request, num):
    obj = Horse.objects.get(id=num)
    print(obj)
    if (request.method == 'POST'):
        horse = KeibaCreateForm(request.POST, instance=obj)
        horse.save()
        return redirect(to='/keiba_prediction/index')
    params = {
        'title': 'Keiba',
        'id':num,
        #'form': KeibaCreateForm(instance=obj),
        'form': KeibaCreateForm(obj),
    }
    return render(request, 'keiba_prediction/edit.html', params)

'''def index(request):
    #return HttpResponse("Hello World")
    params = {
        'title':'Hello/Index',
        'msg':'これは、サンプルで作ったページです。',
        'goto':'next',
        'form':KeibaForm()
    }
    if (request.method == 'POST'):
        params['message'] = '名前：' + request.POST['name']\
        + '<br>メール：' + request.POST['mail']\
        + '<br>年齢：' + request.POST['age']
        params['form'] = KeibaForm(request.POST)
    return render(request, 'keiba_prediction/index.html', params)


def next(request):
    params = {
            'title':'Hello/Next',
            'msg':'これはもう１つのページです。',
            'goto':'index',
    }
    return render(request,  'keiba_prediction/index.html', params)

def form(request):
    msg = request.POST['msg']
    params = {
        'title':'Hello/From',
        'msg':'こんにちは' + msg + 'さん。',

    }
    return render(request, 'keiba_prediction/index.html', params)'''