from django.shortcuts import render, get_object_or_404
from .models import *
from .forms import *
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

# Create your views here.
'''
def home(request):
    context = {}
    return render(request, 'home.html', context)
'''

def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))

    liked = False
    if post.likes.filter(id = request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    
    return HttpResponseRedirect(reverse('blog_detail', args=[str(pk)]))


def CategoryView(request):
    return render(request, 'categories.html', {'categories':Category.objects.all()})

def BlogByCategoryView(request, cats):
    cat = Category.objects.filter(name=cats).first()
    blogs = cat.post_set.all()
    return render(request, 'category_posts.html', {'blogs':blogs})

#Class based view
class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-id','-publish_date'] #to order by creation without having a date in model use ['-id']
    
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)

        context['cat_menu'] = cat_menu
        return context


class BlogDetailView(DetailView):
    model = Post
    template_name= 'blog_detail.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(BlogDetailView, self).get_context_data(*args, **kwargs)
        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()

        liked = False
        if stuff.likes.filter(id = self.request.user.id).exists():
            liked = True

        context['liked'] = liked
        context['cat_menu'] = cat_menu
        context['total_likes'] = total_likes
        return context

class AddBlogView(CreateView):
    model = Post
    form_class = BlogForm
    template_name = 'addblog.html'
    #fields = '__all__' removed after adding form_class

class UpdateBlogView(UpdateView):
    model = Post
    template_name = 'updateblog.html'
    form_class = UpdateBlogForm

class DeleteBlogView(DeleteView):
    model = Post
    template_name = 'deleteblog.html'
    success_url = reverse_lazy('home')
