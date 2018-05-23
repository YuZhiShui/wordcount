from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

"""
通过URl传值
1."get"
? 表示我要传值了：
a=1 
& 并且还有这样的内容
b=2

2.非"get" -url传值
"""
"""
def firstpageindex(request):#,a,b):
    
    c = int(a)+int(b)  #接收的都是string类型

    d = request.GET.get("d")
    e = request.GET.get("d")

    f = int(d) + int(e)

    
    #return render(request,'First_test.html',locals()) #locals将前台数据返回出去
    return render(request,'First_test.html')
"""

def home(request):
    return render(request,'home.html')

def count(request):

    user_text = request.GET['text']
    total_count = len(user_text)

    word_dict = {}
    for word in user_text:
        if word not in word_dict:
            word_dict[word] = 1
        else:
            word_dict[word] += 1
    sorted_dict = sorted(word_dict.items(),key=lambda w:w[1],reverse=True)

    return render(request,'count.html',
                  {'count': total_count,'text': user_text,'word_count': word_dict,'sorted_dict': sorted_dict})

def about(request):
    return render(request,'about.html')