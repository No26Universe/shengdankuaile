from django.shortcuts import render
from django.http import HttpResponse
from .models import UserInfo

def toLogin_view(requset):
    return render(requset,'login.html')


def Login_view(requset):

    u = requset.POST.get("user",'')
    p = requset.POST.get("pwd",'')

    if u and p:
        c=UserInfo.objects.filter(name=u,password=p).count()
        if c >=1:
            return HttpResponse("登陆成功!")
        else:
            return HttpResponse("登陆失败!")
    else:
        return HttpResponse("请输入正确账户和密码")

#渲染注册界面
def toregister_view(requset):
    return render(requset,"register.html")

#注册后的逻辑推理
def Register_view(requset):
    u = requset.POST.get("user",'')
    p = requset.POST.get("pwd",'')
    e = requset.POST.get("ema",'')
    if u and p and e:
        USER=UserInfo(name=u,password=p,email=e)
        USER.save()
        return HttpResponse("注册成功")
    else:
        return HttpResponse("请输入完整的账户和密码")

def bgm(request):
    return render(request,"bgm.html")