from django.shortcuts import render
from .models import Tweet
from .forms import TweetForm, UserRegistrationForm
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
# Create your views here.

def index(request):
  return render(request, 'index.html')  # (give request, template to load)


def tweet_list(request):
  tweets = Tweet.objects.all().order_by('-created_at')
  return render(request, 'tweet_list.html', {'tweets':tweets})

@login_required
def tweet_create(request):
  if request.method == 'POST':
    form = TweetForm(request.POST , request.FILES)       # optional accepeting the file 
    if form.is_valid():
      tweet = form.save(commit=False)                    # saving the form but not commiting in DB 
      tweet.user = request.user                          # User doesn't cum from forms it always comes by request default so we are appending it by tweet
      tweet.save()                                       # Now it will commit in DB 
      return redirect('tweet_list')                      # We are re-directing to tweet_list() 
  else:
    form = TweetForm()                                   # Giving user empty form
  return render(request, 'tweet_form.html', {'form': form})

@login_required
def tweet_edit(request , tweet_id):
  tweet = get_object_or_404(Tweet, pk=tweet_id , user = request.user)       # From Tweet-model find with help of primary key:tweet_id / the user who has logged-in he only can edit the tweet for own
  if request.method == 'POST':
    form = TweetForm(request.POST , request.FILES , instance = tweet) 
    if form.is_valid():
      tweet = form.save(commit=False)
      tweet.user = request.user
      tweet.save()
      return redirect('tweet_list')
  else:
    form = TweetForm(instance=tweet)
  return render(request, 'tweet_form.html', {'form': form})

@login_required
def tweet_delete(request , tweet_id):
  tweet = get_object_or_404(Tweet, pk=tweet_id , user = request.user)
  if request.method == 'POST':
    tweet.delete()
    return redirect('tweet_list')
  return render(request, 'tweet_confirm_delete.html', {'tweet': tweet})

def register(request):
  if request.method == 'POST':
    form = UserRegistrationForm(request.POST)
    if form.is_valid():
      user = form.save(commit=False)
      user.set_password(form.cleaned_data['password1'])
      user.save()
      login(request, user)                                   # after register user can login 
      return redirect('tweet_list')
  else:
    form = UserRegistrationForm()
    
  return render(request, 'registration/register.html', {'form': form})

  
