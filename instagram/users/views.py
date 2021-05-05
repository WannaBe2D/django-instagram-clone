from django.shortcuts import render, get_object_or_404, redirect
from .forms import CustomUserCreationForm, CustomUserChangeForm, CustomProfileForm, CustomPost, CommentForm
from django.views import generic
from django.urls import reverse_lazy
from .models import Profile, Post, Comment
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'users/signup.html'


class EditUser(LoginRequiredMixin, generic.UpdateView):
    model = User
    fields = ('username', 'email')
    success_url = reverse_lazy('profile')
    template_name = 'users/edit_user.html'
    login_url = 'login'

    def get_object(self):
        return self.request.user


@login_required
def page_profile(request):
    post = Post.objects.filter(author=request.user)
    return render(request, 'insta/profile.html', {'post': post})


@login_required
def profile_follower(request, user_id):
    user = User.objects.get(pk=user_id)
    post = Post.objects.filter(author=user)
    return render(request, 'insta/follow_profile.html', {'post': post, 'follower': user})


@login_required
def page_follower(request):
    return render(request, 'insta/follower.html', {})


@login_required
def follower(request, user_id):
    user = User.objects.get(pk=user_id)
    return render(request, 'insta/follower.html', {'user': user})


@login_required
def page_following(request):
    return render(request, 'insta/following.html', {})


@login_required
def edit_profile(request):
    profile = Profile.objects.get(user=request.user)

    if request.method == "POST":
        form = CustomProfileForm(request.POST, request.FILES)
        if form.is_valid():
            avatar = form.cleaned_data.get('avatar')
            bio = form.cleaned_data.get('bio')
            if avatar:
                profile.avatar = avatar
                print(avatar)
            if bio:
                profile.bio = bio
                print(bio)
            profile.save()
            return redirect('profile')

    else:
        form = CustomProfileForm()
    return render(request, 'users/edit_profile.html', {'form': form})


@login_required
def following_in_user(request, follow_id):
    if request.method == "POST":

        following = User.objects.get(pk=follow_id)
        user = Profile.objects.get(user=request.user)
        user.following.add(following)
        user.save()
        return redirect('profile')


@login_required
def unfollow(request, follow_id):
    if request.method == "POST":

        following = User.objects.get(pk=follow_id)
        user = Profile.objects.get(user=request.user)
        user.following.remove(following)
        user.save()
        return redirect('profile')


@login_required
def view_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.method == "POST":
        post.likes.add(request.user)

    return render(request, 'insta/post_view.html', {'post': post})


@login_required
def like(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.likes.add(request.user)
    post.save()
    return redirect('view_post', post_id)


@login_required
def unlike(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.likes.remove(request.user)
    post.save()
    return redirect('view_post', post_id)


@login_required
def time_line(request):
    p = []
    for i in request.user.profile.following.all():
        for y in Post.objects.filter(author=i):
            p.append(y)
    return render(request, 'insta/time_line.html', {"li": p})


@login_required
def activity(request):
    a = [i for i in Post.objects.filter(author=request.user).order_by('-pub_date')]

    return render(request, 'insta/activity.html', {'a': a})


@login_required
def test_create_post(request):
    if request.method == "POST":
        form = CustomPost(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data.get('image')
            description = form.cleaned_data.get('description')
            post = Post.objects.create(author=request.user, image=image, description=description)
            post.save()
            return redirect('profile')
    else:
        form = CustomPost()

    return render(request, 'insta/create_post.html', {'form': form})


class DeletePost(LoginRequiredMixin, generic.DeleteView):
    model = Post
    login_url = 'login'
    success_url = reverse_lazy('profile')


@login_required
def search(request):
    return render(request, 'insta/find.html', {})


class SearchProfile(LoginRequiredMixin, generic.ListView):
    model = Profile
    template_name = 'insta/search_profile.html'
    login_url = 'login'

    def get_queryset(self):
        query = self.request.GET.get('q')
        print(query)
        object_list = User.objects.filter(username__startswith=query)
        return object_list


@login_required
def create_comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data.get('textCom')
            com = Comment.objects.create(author=request.user, post=post, text=text)
            com.save()
            return redirect('view_post', post_id)
    else:
        form = CommentForm()
    return render(request, 'insta/comments.html', {'form': form, 'post': post})
