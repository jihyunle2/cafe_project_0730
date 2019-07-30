from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from . import models

def home(request):
    CafeObjectList = models.Cafe.objects
    context = {"CafeObjectList" : CafeObjectList}
    return render(request,'index.html',context)

def new(request):
    if request.user.is_authenticated: 
        return render(request, 'new.html')
    else:
        CafeObjectList = models.Cafe.objects
        context = {"CafeObjectList" : CafeObjectList,'error':'You have to login to make newpost'}
        return render(request, 'index.html', context)

def create(request):
    CafeObject = models.Cafe()
    CafeObject.title = request.POST['title']
    CafeObject.author= request.user
    CafeObject.address = request.POST['address']
    CafeObject.contact = request.POST['contact']
    CafeObject.image = request.FILES['image']
    CafeObject.pub_date = timezone.datetime.now()
    CafeObject.save()
    return redirect('home')

def cafeDetail(request,cafe_id):
    detailCafeObject = get_object_or_404(models.Cafe, pk=cafe_id)
    if request.method == 'POST':
        newCommentObject = models.Comment()
        newCommentObject.cafe = detailCafeObject 
        newCommentObject.comment_author = request.user
        newCommentObject.comment_title = request.POST['comment_title']
        newCommentObject.created_date = timezone.datetime.now()
        newCommentObject.comment_contents = request.POST['comment_contents']
        newCommentObject.save()
        return redirect('/cafeDetail/'+str(detailCafeObject.id))
    context = {"detailCafeObject" : detailCafeObject }
    return render(request, 'cafeDetail.html', context)

def update(request, cafe_id):
    updateCafeObject = get_object_or_404(models.Cafe, pk=cafe_id)
    if request.method == 'POST':
        updateCafeObject.title = request.POST['title']
        updateCafeObject.address = request.POST['address']
        updateCafeObject.contact = request.POST['contact']
        updateCafeObject.pub_date = timezone.datetime.now()
        #updateCafeObject.body = request.POST['body']
        updateCafeObject.save()
        return redirect('home')
        #return redirect('/cafeDetail/'+str(updateCafeObject.id))
    context = {"updateCafeObject" : updateCafeObject}
    return render(request, 'update.html', context)

def delete(request, cafe_id):
    deleteCafeObject = get_object_or_404(models.Cafe, pk=cafe_id)
    deleteCafeObject.delete()
    return redirect('home')

def commentDelete(request, cafe_id, comment_id):
    details = get_object_or_404(models.Cafe, pk=cafe_id)
    deleteCommentObject = get_object_or_404(models.Comment, pk=comment_id)
    deleteCommentObject.delete()
    return redirect('/cafeDetail/' + str(details.id))

















