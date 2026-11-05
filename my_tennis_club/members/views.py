from django.shortcuts import get_object_or_404, render

from .models import Member


def main(request):
    return render(request, "main.html", {"member_count": Member.objects.count()})


def members(request):
    query = request.GET.get("q", "").strip()
    queryset = Member.objects.all()
    if query:
        queryset = queryset.filter(firstname__icontains=query) | queryset.filter(lastname__icontains=query)
    return render(request, "all_members.html", {"mymembers": queryset, "query": query})


def details(request, id):
    return render(request, "details.html", {"mymember": get_object_or_404(Member, id=id)})
