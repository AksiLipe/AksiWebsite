from django.shortcuts import render


def track_list(request):
    return render(request, "track_list.html")


def beat_list(request):
    return render(request, "beat_list.html")
