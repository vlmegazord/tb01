# -*- coding: utf-8 -*-
from django.test import TestCase
from django.core.urlresolvers import reverse


class TestHomePage(TestCase):

    def test_uses_index_template(self):
        print('1')
        response = self.client.get(reverse("home"))
        print('response done')
        self.assertTemplateUsed(response, "taskbuster/index.html")

    def test_uses_base_template(self):
        print('2')
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "base.html")
