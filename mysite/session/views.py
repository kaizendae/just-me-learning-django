from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
def sessfun(request):
    return render(request, "session/sessfun.html")


def cookie(request):
    print(request.COOKIES)
    response = HttpResponse("Cookie Set")
    response.set_cookie("zap", "123456789")  # no expiration, delete on browser close
    response.set_cookie(
        "dj4e_cookie", "123456789", max_age=1000
    )  # delete after 1000 seconds
    return response


def theme_switcher(request):
    current_theme = request.COOKIES.get("theme", "light")

    if request.method == "POST":
        new_theme = "dark" if current_theme == "light" else "light"
        response = render(request, "session/theme.html", {"theme": new_theme})
        response = redirect(
            "session:theme_switcher"
        )  # HttpResponse("Theme switched to " + new_theme)
        response.set_cookie("theme", new_theme, max_age=60 * 60 * 24 * 365)
        return response
    else:
        return render(request, "session/theme.html", {"theme": current_theme})
