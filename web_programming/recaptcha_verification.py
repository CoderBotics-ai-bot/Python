"""
Recaptcha is a free captcha service offered by Google in order to secure websites and
forms.  At https://www.google.com/recaptcha/admin/create you can create new recaptcha
keys and see the keys that your have already created.
* Keep in mind that recaptcha doesn't work with localhost
When you create a recaptcha key, your will get two separate keys: ClientKey & SecretKey.
ClientKey should be kept in your site's front end
SecretKey should be kept in your site's  back end

# An example HTML login form with recaptcha tag is shown below

    <form action="" method="post">
        <h2 class="text-center">Log in</h2>
        {% csrf_token %}
        <div class="form-group">
            <input type="text" name="username" required="required">
        </div>
        <div class="form-group">
            <input type="password" name="password" required="required">
        </div>
        <div class="form-group">
            <button type="submit">Log in</button>
        </div>
        <!-- Below is the recaptcha tag of html -->
        <div class="g-recaptcha" data-sitekey="ClientKey"></div>
    </form>

    <!-- Below is the recaptcha script to be kept inside html tag -->
    <script src="https://www.google.com/recaptcha/api.js" async defer></script>

Below a Django function for the views.py file contains a login form for demonstrating
recaptcha verification.
"""
import requests


from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login


from typing import HttpRequest, HttpResponse

try:
    from django.contrib.auth import authenticate, login
    from django.shortcuts import redirect, render
except ImportError:
    authenticate = login = render = redirect = print

def login_using_recaptcha(request: HttpRequest) -> HttpResponse:
    """
    Attempt to log a user in using Google's reCAPTCHA for added security.

    This function will initially check if the request method is a POST. If it
    isn't, then it will render the login page.

    If the request method is POST, the function will attempt to verify the
    reCAPTCHA response using Google's reCAPTCHA API.

    If the reCAPTCHA is successfully verified, the function will attempt to
    authenticate the user. If the user is authenticated successfully, the
    user is logged in and redirected to another webpage.
    If the reCAPTCHA isn't verified or user can't be authenticated, the login page is rendered again.

    Args:
        request (HttpRequest): The request instance sent from the user's browser.

    Returns:
        HttpResponse: An HttpResponse object which either renders a webpage or redirects to another webpage.

    Side Effects:
        An HttpRequest object is modified in this function. If the user is authenticated, they are logged in.
    """
    if request.method != "POST":
        return render(request, "login.html")

    is_recaptcha_verified = verify_recaptcha(request)

    if is_recaptcha_verified:
        user_in_database = authenticate(
            request,
            username=request.POST.get("username"),
            password=request.POST.get("password"),
        )
        if user_in_database:
            login(request, user_in_database)
            return redirect("/your-webpage")

    return render(request, "login.html")


def verify_recaptcha(request: HttpRequest) -> bool:
    """Verify the recaptcha response with Google's recaptcha API and return the verification result."""
    secret_key = "secretKey"
    url = "https://www.google.com/recaptcha/api/siteverify"
    client_key = request.POST.get("g-recaptcha-response")
    response = requests.post(url, data={"secret": secret_key, "response": client_key})
    return response.json().get("success", False)
