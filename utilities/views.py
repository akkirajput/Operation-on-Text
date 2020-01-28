from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.
def index(request):
    date=datetime.datetime.now().time()
    return render(request,'react/index.html',{'today':date})

def process(request):
    if request.method == 'POST':
        texts = request.POST['text']
        
    return HttpResponse(texts.title()+'''<br><br><a href='https://www.google.com/'>Google</a><br>
    <a href='https://www.youtube.com/'>Youtube</a><br><a href='https://www.hackerrank.com/'>Hackerrank</a><br><a href='..'>Home</a>''')
    
    # THIS CODE IS FOR WHEN WE TAKE CHECKBOX FOR DIFFERENT OPERATION TO BE PERFORMED
def analyze(request):
    texts= request.POST.get('text','default')
    original=texts
    removeana=""
    spaceana=""
    uppercase=""
    newline=""
    charcount=""
    if request.POST.get('removepun')=='on':
        punctuation = '''!()-[]{};:'"\/,<>.?/@#$%^&*_~'''
        analyzed=""
        for char in texts:
            if char not in punctuation:
                analyzed=analyzed+char
        removeana=analyzed        
        param={'purpose':"Remove Punctuation",'intial':original,'analyzed':analyzed,'removepun':removeana,'spaceremove':spaceana,'upperana':uppercase,'newlineana':newline,'charana':charcount }
        texts=analyzed    

    if request.POST.get('spaceremove')=='on':
        analyzed=texts.replace(" ","")
        spaceana=analyzed
        param={'purpose':"Space Remove",'intial':original,'analyzed':analyzed,'spaceremove':spaceana,'removepun':removeana ,'upperana':uppercase,'newlineana':newline,'charana':charcount}              
        texts=analyzed

    if request.POST.get('uppercase')=='on':
        analyzed=texts.upper()
        uppercase=analyzed
        param={'purpose':"Upper Case",'intial':original,'analyzed':analyzed,'upperana':uppercase,'removepun':removeana,'spaceremove':spaceana,'newlineana':newline,'charana':charcount}
        texts=analyzed
    if request.POST.get('newline')=='on':
        analyzed=""
        for char in texts:
            if char !="\n" and char!="\r":
                analyzed+=char
        newline=analyzed
        param={'purpose':"New Line",'intial':original,'analyzed':analyzed,'newlineana':newline,'removepun':removeana,'spaceremove':spaceana,'upperana':uppercase,'charana':charcount}
        texts=analyzed
    if request.POST.get('charcount')=='on':
        analyzed=len(texts)
        charcount=analyzed
        param={'purpose':"Char Count",'intial':original,'analyzed':analyzed,'charana':charcount,'removepun':removeana,'spaceremove':spaceana,'upperana':uppercase,'newlineana':newline}
       

    return render(request,'react/analyze.html',param)

