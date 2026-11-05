from django.contrib import admin

from .models import Member


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ("firstname", "lastname", "phone", "joined_date")
    search_fields = ("firstname", "lastname", "phone")
    list_filter = ("joined_date",)
