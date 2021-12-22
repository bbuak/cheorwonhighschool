from django.shortcuts import render

# Create your views here.
from bs4 import BeautifulSoup
import requests
from django.http import HttpResponse


def score_board(request):
    response = requests.get('https://open.neis.go.kr/hub/hisTimetable?KEY=3ebf88a2ff0b418c89c5ee1af120cf84Type=&pIndex=1&pSize=100&ATPT_OFCDC_SC_CODE=K10&SD_SCHUL_CODE=7800090&ALL_TI_YMD=20211217&GRADE=2&CLASS_NM=4')
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    my_titles = soup.select('row > itrt_cntnt')
    subject = [ ]
    count = len(my_titles) #요소의 개수
    for i in range(count) :
       subject.append(str(my_titles[i]))
    return render(request, 'Hi.html', {'git' : subject})

def eating(request):
    url1 = "https://open.neis.go.kr/hub/mealServiceDietInfo?Type=json&pIndex=1&pSize=100&ATPT_OFCDC_SC_CODE=K10&SD_SCHUL_CODE=7800090&MMEAL_SC_CODE=2&MLSV_YMD=20211206"
    data1 = requests.get(url1).json()
    data1_rows = data1.get('mealServiceDietInfo', [])[1].get('row', [])
    for i in data1_rows :
        samples = i['DDISH_NM'].split('<br/>')
    new_samples = []
    last_samples = []
    for i in samples :
        new_samples.append(''.join([j for j in i if not j.isdigit()]))
    for i in new_samples :
        last_samples.append(''.join([char for char in i if char.isalnum() or char == '&']))
    print(last_samples)
    return render(request, 'home.html', {'rice' : last_samples})

def home(request):
    return render(request, 'home.html')

def regpg(request):
    grade = request.GET.get('grade')
    if grade == '1grade-1class':
        return render(request, '1-2.html')
    elif grade == '1grade-2class':
        return render(request, '1-3.html')
    return render(request, 'regpg.html')    

def onetwo(request):
    return render(request,'1-2.html')

