from django.shortcuts import render, redirect
from  django.http import HttpResponse
from .models import *
from django.contrib import messages

def index(request):
    myposts = Blogpost.objects.all()
    return render(request,"blog/index.html", {'myposts': myposts})

def blogpost(request, id):
    post = Blogpost.objects.filter(post_id = id)[0]
    print(post)
    return render(request,"blog/blogpost.html", {'post':post})

def search(request):
    params = {}
    query=request.GET['query']
    if len(query)>78:
        allPosts=Blogpost.objects.none()
    else:
        allPostsTitle= Blogpost.objects.filter(title__icontains=query)
        allPostsHead0= Blogpost.objects.filter(head0__icontains=query)
        allPostsCHead0 =Blogpost.objects.filter(chead0__icontains=query)
        allPostsHead1= Blogpost.objects.filter(head1__icontains=query)
        allPostsCHead1 =Blogpost.objects.filter(chead1__icontains=query)
        allPostsHead2= Blogpost.objects.filter(head2__icontains=query)
        allPostsCHead2 =Blogpost.objects.filter(chead2__icontains=query)
        allPosts=  allPostsTitle.union(allPostsTitle, allPostsHead0, allPostsCHead0, allPostsHead1, allPostsCHead1, allPostsHead2, allPostsCHead2)
    if allPosts.count()==0:
        messages.warning(request, "No search results found. Please refine your query.")
    else:
        params={'allPosts': allPosts, 'query': query}
        messages.info(request, "Search query results found..")
    return render(request, 'blog/search.html', params)



