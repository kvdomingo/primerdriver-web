from django.test import TestCase, LiveServerTestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.firefox.options import Options
from percy import percySnapshot


PERCY_BS_WIDTHS = [576, 768, 992, 1200]

class WebTestCase(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        options = Options()
        options.headless = True
        cls.selenium = WebDriver(options=options)
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_landing(self):
        self.selenium.get(self.live_server_url)
        self.selenium.execute_script('window.scrollTo(0, 100)')
        percySnapshot(browser=self.selenium, name='homepage', widths=PERCY_BS_WIDTHS)
