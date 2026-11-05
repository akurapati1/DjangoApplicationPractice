from datetime import date

from django.test import TestCase
from django.urls import reverse

from .models import Member


class MemberTests(TestCase):
    def setUp(self):
        self.ann = Member.objects.create(firstname="Ann", lastname="Lee", phone="555-1", joined_date=date(2024, 1, 5))
        Member.objects.create(firstname="Bob", lastname="Stone")

    def test_str_and_ordering(self):
        self.assertEqual(str(self.ann), "Ann Lee")
        self.assertEqual([m.lastname for m in Member.objects.all()], ["Lee", "Stone"])

    def test_home_shows_member_count(self):
        response = self.client.get(reverse("main"))
        self.assertContains(response, "<strong>2</strong> members")

    def test_member_list_and_search(self):
        self.assertContains(self.client.get(reverse("members")), "Bob Stone")
        filtered = self.client.get(reverse("members"), {"q": "ann"})
        self.assertContains(filtered, "Ann Lee")
        self.assertNotContains(filtered, "Bob Stone")

    def test_empty_search_result(self):
        self.assertContains(self.client.get(reverse("members"), {"q": "zzz"}), "No members found")

    def test_details_and_404(self):
        self.assertContains(self.client.get(reverse("details", args=[self.ann.id])), "555-1")
        self.assertEqual(self.client.get(reverse("details", args=[9999])).status_code, 404)
