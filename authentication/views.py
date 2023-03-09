import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.http.multipartparser import MultiPartParser
from .models import User, Product, Message, MessageResponse, Profile
from .forms import SignupForm, LoginForm
from django.contrib import auth
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.conf import settings
from django.contrib.auth import logout
from datetime import date
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.http import QueryDict
from django.views.decorators.http import require_http_methods


def health(request):
    """Takes an request as a parameter and gives the count of pageview objects as reponse"""
    return HttpResponse(Product.objects.count())

@csrf_exempt
def registerPage(request: HttpRequest) -> HttpResponse:
    """
    Signup function
    Users creating an account
    """

    form = SignupForm()

    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]

            # create a new user
            new_user = User.objects.create(username=username, email=email)
            # set user's password
            new_user.set_password(password)
            new_user.save()
            subject = f'Hello {username}!'
            message = f'Thank you for registering with us, {username}'
            recipient_list = [email]
            send_mail( subject, message, 'uwais_i@outlook.com', recipient_list,fail_silently=False)
            # when a user register, a profile for that user needs to be created
            # a profile must have an email, a DoB and a photograph
            # the photograph and DoB needs to be added by the user - email is set
            new_profile = Profile.objects.create(email=email)
            new_profile.user_acc = new_user
            new_profile.save()

            # authenticate user
            # establishes a session, will add user object as attribute
            # on request objects, for all subsequent requests until logout
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                # to be forwarded to the main page - front-end - maybe profile
                return redirect("http://localhost:5173/shop")

    return render(request, "authentication/auth/register.html", {"form": SignupForm})


@csrf_exempt
def loginPage(request: HttpRequest) -> HttpResponse:
    """
    Login function
    Users logging into the app
    """

    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            # authenticate user to the backend
            user = auth.authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect("http://localhost:5173/shop")

                # forward to main page of the application - front-endop")

            # failed authentication
            return render(
                request, "error.html", {"error": "User not registered. Sign up first."}
            )

        # invalid form
        return render(request, "authentication/login.html", {"form": form})

    return render(request, "authentication/auth/login.html", {"form": form})


def logout(request: HttpRequest) -> HttpResponse:
    """
    View that can be used for a user to logout
    If the user is authenticated -> They can logout
    """
    if not request.user.is_authenticated:
        return redirect("%s?next=%s" % (settings.LOGIN_URL, request.path))
    else:
        auth.logout(request)
        return redirect("%s?next=%s" % (settings.LOGIN_URL, request.path))


@csrf_exempt
@require_http_methods(['GET', 'POST'])
def products_api(request: HttpRequest) -> HttpResponse:
    """
    Main page - Display all items -> GET, POST
    """

    # check all products
    for product in Product.objects.all():
        # if the auction for the product finished, an email is sent to the user
        if product.finish_date <= date.today():
            product.active = False
            if product.bid_on:
                subject = f'You won {product.title}!'
                message = f'Hi {product.highest_bidder.username}, thank you for purchasing {product.title}.'
                recipeint = product.highest_bidder
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [recipeint.email]
                send_mail( subject, message, 'uwais_i@outlook.com', recipient_list,fail_silently=False)
            isnt = Product.objects.get(id=product.id)
            isnt.delete()
        
    # GET request to display all products on the main page
    if request.method == "GET":
        return JsonResponse(
            {
                "products": [
                    # Transform all items to dictionary Json objects
                    product.to_dict()
                    for product in Product.objects.all()
                ]
            }
        )

    if request.method == "POST":
        # Create new product and return it as JsonResponse
        # Load Json data sent from frontend
        title = request.POST.get("title")
        description = request.POST.get("description")
        starting_price = request.POST.get("starting_price")
        
        finish_date = request.POST.get("finish_date")

        user = User.objects.get(pk=request.user.id)
        # Update DB with the new created team
        product = Product.objects.create(
            title=title,
            description=description,
            highest_bidder=user,
            owner=user,
            active=True,
            starting_price=starting_price,
            finish_date=finish_date,
        )
        if request.FILES.get("picture")!=None:
            picture = request.FILES.get("picture")
            product.picture=picture


        # product is then saved
        product.save()
  
        # all items are then transformed into JSonResponses and sent to the frontend
        return JsonResponse(
            {
                "products": [
                    # Transform all items to dictionary Json objects
                    product.to_dict()
                    for product in Product.objects.all()
                ]
            }
        )


@csrf_exempt
@require_http_methods(['PUT'])
def product_api(request: HttpRequest, product_id) -> HttpResponse:
    """
    View that handles a product's bid
    It answer a PUT request when a bidder bids for an item
    """

    if request.method == "PUT":
        product = get_object_or_404(Product, id=product_id)

        # Bidder of the item
        bidding_user = User.objects.get(username=request.user)

        data = MultiPartParser(request.META, request, request.upload_handlers).parse()[
            0
        ]

        product.starting_price = data["bid"]
        product.highest_bidder = bidding_user   
        if not product.bid_on:
            product.bid_on=True
        # product with its updated details is then saved
        product.save()

        return JsonResponse(
            {
                "products": [
                    # Transform all products to dictionary Json objects
                    product.to_dict()
                    for product in Product.objects.all()
                ]
            }
        )


@csrf_exempt
@require_http_methods(['GET', 'POST'])
def messages_api(request: HttpRequest) -> HttpResponse:
    """
    View that handles the messages posted for a product
    Methods used: - GET - lists all the messages for a product
                  - POST - post a new message
    """

    # lists all messages for a product
    if request.method == "GET":
        return JsonResponse(
            {
                "messages": [
                    # Transform all items to dictionary Json objects
                    message.to_dict()
                    for message in Message.objects.all()
                ]
            }
        )

    # upload a message for a product
    user=request.user
    if request.method == "POST":
        if user.is_authenticated:
            sender_id = user.id
            text = request.POST.get("text")
            product_id = request.POST.get("productId")

            if text!='':
            # Update DB with the new created message
                now = datetime.now()

                # get logged in user
                sender = User.objects.get(id=sender_id)  
                prod = Product.objects.get(id=product_id)

                message = Message.objects.create(
                    sender=sender,
                    product=prod,
                    message_response=MessageResponse.objects.get(
                        id=1
                    ),  
                    text=text,
                    time=now,
                )
                message.save()

        return JsonResponse(
            {
                "messages": [
                    # Transform all items to dictionary Json objects
                    messageE.to_dict() for messageE in Message.objects.all()
                ]
            }
        )


@csrf_exempt
@require_http_methods(['GET', 'POST'])
def responses_api(request: HttpRequest) -> HttpResponse:
    """
    View that handles the replies to the messages for products
    It responds to: - GET - display the reply for a message
                    - POST - post a reply to a message
    """

    # print the reply to products
    if request.method == "GET":
        return JsonResponse(
            {
                "responses": [
                    # Transform all responses to dictionary Json objects
                    response.to_dict()
                    for response in MessageResponse.objects.all()
                ]
            }
        )

    # post a reply to a message
    if request.method == "POST":
        text = request.POST.get("text")
        message_id = request.POST.get("messageId")

        if text != "":
        # Update DB with the new created reply
            now = datetime.now()
            message = Message.objects.get(id=message_id)
            response= MessageResponse.objects.get(id=message.message_response.id)
            if message.message_response.text != 'Default':
                response.delete()

            response = MessageResponse.objects.create(
                text=text
            )

            # save the message/response
            response.save()
            message.message_response = response
            message.save()

        return JsonResponse(
            {
                "responses": [
                    # Transform all responses to dictionary Json objects
                    responseE.to_dict() for responseE in MessageResponse.objects.all()
                ]   
            }
        )


@csrf_exempt
@require_http_methods(['GET'])
def profile(request: HttpRequest) -> HttpResponse:
    """
    User page - display details of user
    It handles GET request to display user's profile page
    """

    user = request.user
    if user.is_authenticated:

        if request.method == "GET":
            profile = get_object_or_404(Profile, email=user.email)

            return JsonResponse(
                {
                    "logged_in": True,
                    "username": user.username,
                    "profile": profile.to_dict(),
                }
            )
    else:
        # user is not logged in
        return JsonResponse({"logged_in": False})


@csrf_exempt
@require_http_methods(['PUT'])
def profile_api(request: HttpRequest, profile_id: int) -> HttpResponse:
    """
    Method that handles PUT requests for updating profile details
    """
    # Fetch the details of the profile
    profile = get_object_or_404(Profile, id=profile_id)
    user = profile.user_acc
    print("USER", user.email)

    print("PROFILE", profile.email)

    if request.method == 'PUT':
        if request.content_type.startswith('multipart'):
            put, files = request.parse_file_upload(request.META, request)
            request.FILES.update(files)
            request.PUT = put.dict()
    
        else:
            request.PUT = QueryDict(request.body).dict()

        # update DB with the new created team
        # Get the team's details
 

        profile.email = request.PUT["email"]
        user.email = request.PUT["email"]
        user.username = request.PUT["username"]
        profile.date_of_birth = request.PUT["date_of_birth"]
        
        if len(request.FILES.keys())!=0:
            img_data = request.FILES['profile_picture']
            if img_data is not None:
                

                profile.profile_picture=img_data
        user.save()
        # profile.date_of_birth = data["date"]
        profile.save()
        
        return JsonResponse(
            {
                "logged_in": True,
                "username": user.username,
                "profile": profile.to_dict(),
            }
        )

