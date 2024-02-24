from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import giamhieu as giamhieu_model
from .models import comments as comments_model
# Create your views here.
def get_home(request):
    giamhieu_list=giamhieu_model.objects.filter().order_by('giamhieu_id')
    return render(request,'home.html',{'giamhieu_list':giamhieu_list})
def get_gioithieu1(request):
    comments_list=comments_model.objects.filter().order_by('cmt_id')
    return render(request,'gioithieu1.html',{'comments_list':comments_list})
def get_gioithieu2(request):
    comments_list=comments_model.objects.filter().order_by('cmt_id')
    return render(request,'gioithieu2.html',{'comments_list':comments_list})
def get_gioithieu3(request):
    comments_list=comments_model.objects.filter().order_by('cmt_id')
    return render(request,'gioithieu3.html',{'comments_list':comments_list})
def get_gioithieu4(request):
    giamhieu_list=giamhieu_model.objects.filter().order_by('giamhieu_id')
    comments_list=comments_model.objects.filter().order_by('cmt_id')
    return render(request,'gioithieu4.html',{'giamhieu_list':giamhieu_list,'comments_list':comments_list})
def add_comments(request):
    if request.method == 'POST':
        ho_ten=request.POST['author']
        cmt=request.POST['comment']

        comment=comments_model.objects.create(cmt=cmt,ho_ten=ho_ten)
        comment.save()
    
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))