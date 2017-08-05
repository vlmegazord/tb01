# -*- coding: utf-8 -*-
from selenium import webdriver
from django.core.urlresolvers import reverse
# from django.contrib.staticfiles.testing import LiveServerTestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from datetime import date
from django.utils import formats
from django.utils.translation import activate

# class HomeNewVisitorTest(LiveServerTestCase):
class HomeNewVisitorTest(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def get_full_url(self, namespace):
        print("Live URL:", str(self.live_server_url))
        print("Namespace:", str(namespace))
        print("Reversed ns:", str(reverse(namespace)))
        return self.live_server_url + reverse(namespace)

    def test_home_title(self):
        self.browser.get(self.get_full_url("home"))
        self.assertIn("TaskBuster", self.browser.title)

    def test_h1_css(self):
        self.browser.get(self.get_full_url("home"))
        h1 = self.browser.find_element_by_tag_name("h1")
        self.assertEqual(h1.value_of_css_property("color"), "rgba(200, 50, 255, 1)")

    def test_home_files(self):
        self.browser.get(self.live_server_url + "/robots.txt")
        self.assertNotIn("Not Found", self.browser.title)
        self.browser.get(self.live_server_url + "/humans.txt")
        self.assertNotIn("Not Found", self.browser.title)

    def test_internationalization(self):
        texts = [( 'en', "Welcome to TaskBuster"), ('ru', "Добро пожаловать в ТаскБастер!")]
        for lang, h1_text in texts:
            activate(lang)
            self.browser.get(self.get_full_url("home"))
            h1 = self.browser.find_element_by_tag_name("h1")
            self.assertEqual(h1.text, h1_text)



    def test_localization(self):
        today = date.today()
        print("Today:", str(today))
        for lang in ['en', 'ru']:
            activate(lang)
            print("Language activated:", lang)
            self.browser.get(self.get_full_url('home'))
            local_date = self.browser.find_element_by_id("local-date")
            print("LOcal date:", str(local_date))
            non_local_date = self.browser.find_element_by_id("non-local-date")
            print("Non-lOcal date:", str(non_local_date))
            self.assertEqual(formats.date_format(today, use_l10n=True), local_date.text)
            self.assertEqual(today.strftime('%Y-%m-%d'), non_local_date.text)

    def test_tz(self):
        self.browser.get(self.get_full_url('home'))
        tz = self.browser.find_element_by_id('time-tz')
        utc = self.browser.find_element_by_id('time-utc')
        ny = self.browser.find_element_by_id('time-ny')
        self.assertNotEqual(tz, utc)
        self.assertNotIn(ny, [tz, utc])




# -*- coding: utf-8 -*-
# from selenium import webdriver
# import unittest
#

# class NewVisitorTest(unittest.TestCase):
#
#     def setUp(self):
#         self.browser = webdriver.Firefox()
#         self.browser.implicitly_wait(3)
#
#     def tearDown(self):
#         self.browser.quit()
#
#     def test_it_worked(self):
#         self.browser.get('http://localhost:8000')
#         self.assertIn('Welcome to Django', self.browser.title)
#
# if __name__ == '__main__':
#     unittest.main(warnings='ignore')
