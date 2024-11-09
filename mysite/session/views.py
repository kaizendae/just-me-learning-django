from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
def sessfun(request):
    visits_count = request.session.get("visits_count", 0) + 1
    request.session["visits_count"] = visits_count
    if visits_count > 5:
        del request.session["visits_count"]
    return HttpResponse("You have visited this page " + str(visits_count) + " times")


def inc_dec_card(request):
    try:
        card_count = int(request.session.get("card_count", 0))
    except (ValueError, TypeError):
        card_count = 0

    if request.method == "POST":
        print("POST data:", request.POST)
        if request.POST.get("inc", False) and card_count < 10:
            card_count += 1
        elif request.POST.get("dec", False) and card_count > 0:
            card_count -= 1

        request.session["card_count"] = card_count

    return render(request, "session/card.html", {"card_count": card_count})


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
