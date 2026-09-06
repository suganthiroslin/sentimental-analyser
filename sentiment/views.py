import json

from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt


# =========================================================
# HOME
# =========================================================

def home(request):
    return render(request, 'sentiment/home.html')


# =========================================================
# ABOUT
# =========================================================

def about(request):
    return render(request, 'sentiment/about.html')


# =========================================================
# REGISTER
# =========================================================

def register_view(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Check password
        if password != confirm_password:

            messages.error(
                request,
                "Passwords do not match."
            )

            return redirect('register')


        # Check username
        if User.objects.filter(username=username).exists():

            messages.error(
                request,
                "Username already exists."
            )

            return redirect('register')


        # Create user
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        user.save()


        messages.success(
            request,
            "Registration successful! Please login."
        )

        return redirect('login')


    return render(
        request,
        'sentiment/register.html'
    )


# =========================================================
# LOGIN
# =========================================================

def login_view(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')


        user = authenticate(
            request,
            username=username,
            password=password
        )


        if user is not None:

            login(request, user)

            return redirect('home')


        else:

            messages.error(
                request,
                "Invalid username or password."
            )

            return redirect('login')


    return render(
        request,
        'sentiment/login.html'
    )


# =========================================================
# LOGOUT
# =========================================================

def logout_view(request):

    logout(request)

    return redirect('home')


# =========================================================
# SENTIMENT ANALYSIS API
# =========================================================

@csrf_exempt
def analyze_api(request):

    # Only POST method allowed

    if request.method != 'POST':

        return JsonResponse(
            {
                'error': 'POST method required.'
            },
            status=405
        )


    # Read JSON data

    try:

        data = json.loads(request.body)

    except json.JSONDecodeError:

        return JsonResponse(
            {
                'error': 'Invalid JSON data.'
            },
            status=400
        )


    # Get text

    text = data.get('text', '').strip()


    # Check empty text

    if not text:

        return JsonResponse(
            {
                'error': 'Text is required.'
            },
            status=400
        )


    # =====================================================
    # TEMPORARY SENTIMENT ANALYSIS
    # =====================================================
    #
    # This is only for testing the connection between
    # Netlify and Django.
    #
    # Later we will replace this with your actual
    # NLP / Machine Learning model.
    # =====================================================

    positive_words = [
        'good',
        'great',
        'excellent',
        'amazing',
        'awesome',
        'happy',
        'love',
        'liked',
        'wonderful',
        'best',
        'fantastic',
        'nice',
        'enjoy',
        'enjoyed',
        'perfect'
    ]


    negative_words = [
        'bad',
        'worst',
        'terrible',
        'horrible',
        'sad',
        'hate',
        'dislike',
        'poor',
        'awful',
        'boring',
        'waste',
        'disappointed',
        'disappointing',
        'useless',
        'problem'
    ]


    # Convert text to lowercase

    words = text.lower().split()


    # Count words

    positive_count = 0
    negative_count = 0


    for word in words:

        # Remove punctuation

        clean_word = word.strip(
            ".,!?;:'\"()[]{}"
        )


        if clean_word in positive_words:

            positive_count += 1


        if clean_word in negative_words:

            negative_count += 1


    # Determine sentiment

    if positive_count > negative_count:

        sentiment = "Positive 😊"


    elif negative_count > positive_count:

        sentiment = "Negative 😞"


    else:

        sentiment = "Neutral 😐"


    # Return JSON response

    return JsonResponse(
        {
            'sentiment': sentiment
        }
    )
