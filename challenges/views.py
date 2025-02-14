from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
# Create your views here.

monthly_challenges = {
    "january": "Eat",
    "february": "Sleep",
    "march": "fuck",
    "april": "fucck april",
    "may": "fucck may",
    "june": "fucck june",
    "july": "fucck july",
    "august": "fucck august",
    "september": "fucck september",
    "october": "fucck  october",
    "november": "fucck november",
    "december": None
}


def index(request):
    list_item = ""
    months = list(monthly_challenges.keys())
    return render(request, "challenges/index.html", {
        "months": months
    })
    # for month in months:
    #     capitalized_month = month.capitalize()
    #     redirect_path = reverse(
    #         "month-challenge", args=[month])
    #     list_item += f"<li><a href='{redirect_path}'>{capitalized_month}</a></li>"
    # return HttpResponse(
    #     f"<ul>{list_item}</ul>"
    # )


def monthly_challenge_by_num(request, month):
    months = list(ly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")
    redirect_month = months[month - 1]
    redirect_path = reverse(
        "month-challenge", args=[redirect_month])  # /challenge/january
    print(redirect_path)
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        print(month)
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month_name": month
        })
    except:
        raise Http404()
