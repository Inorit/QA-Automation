import unittest
from optparse import OptionParser
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy


capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='Android Emulator',
    appPackage='com.google.android.calculator',
    appActivity='com.android.calculator2.Calculator'
)

appium_server_url = 'http://localhost:4723'


class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote(appium_server_url, capabilities)


    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()


    def test_four_add_eight(self) -> None:
        self.driver.find_element(value='com.google.android.calculator:id/digit_4').click()
        self.driver.find_element(value='com.google.android.calculator:id/op_add').click()
        self.driver.find_element(value='com.google.android.calculator:id/digit_8').click()

        assert(self.driver.find_element(value='com.google.android.calculator:id/result_preview').text == '12')

        self.driver.find_element(value='com.google.android.calculator:id/eq').click()

        assert(self.driver.find_element(value='com.google.android.calculator:id/result_final').text == '12')


    def test_nine_div_three(self) -> None:
        self.driver.find_element(value='com.google.android.calculator:id/digit_9').click()
        self.driver.find_element(value='com.google.android.calculator:id/op_div').click()
        self.driver.find_element(value='com.google.android.calculator:id/digit_3').click()

        assert(self.driver.find_element(value='com.google.android.calculator:id/result_preview').text == '3')

        self.driver.find_element(value='com.google.android.calculator:id/eq').click()

        assert(self.driver.find_element(value='com.google.android.calculator:id/result_final').text == '3')


    def test_zero_div(self) -> None:
        self.driver.find_element(value='com.google.android.calculator:id/digit_9').click()
        self.driver.find_element(value='com.google.android.calculator:id/op_div').click()
        self.driver.find_element(value='com.google.android.calculator:id/digit_0').click()

        assert(self.driver.find_element(value='com.google.android.calculator:id/result_preview').text == '')

        self.driver.find_element(value='com.google.android.calculator:id/eq').click()

        assert(self.driver.find_element(value='com.google.android.calculator:id/result_preview').text == 'Can\'t divide by 0')


    def test_root_from_negative(self) -> None:
        self.driver.find_element(value='com.google.android.calculator:id/op_sqrt').click()
        self.driver.find_element(value='com.google.android.calculator:id/op_sub').click()
        self.driver.find_element(value='com.google.android.calculator:id/digit_5').click()

        assert(self.driver.find_element(value='com.google.android.calculator:id/result_preview').text == '')

        self.driver.find_element(value='com.google.android.calculator:id/eq').click()

        assert(self.driver.find_element(value='com.google.android.calculator:id/result_preview').text == 'Keep it real')


def get_options():
    parser = OptionParser()
    parser.add_option("--test_four_add_eight", action="store_true", dest="test_four_add_eight", default=False)
    parser.add_option("--test_nine_div_three", action="store_true", dest="test_nine_div_three", default=False)
    parser.add_option("--test_zero_div", action="store_true", dest="test_zero_div", default=False)
    parser.add_option("--test_root_from_negative", action="store_true", dest="test_root_from_negative", default=False)

    (options, _) = parser.parse_args()

    return options


def form_suite(options):
    suite = unittest.TestSuite()

    if options.test_four_add_eight:
        suite.addTest(TestAppium('test_four_add_eight'))
    if options.test_nine_div_three:
        suite.addTest(TestAppium('test_nine_div_three'))
    if options.test_zero_div:
        suite.addTest(TestAppium('test_zero_div'))
    if options.test_root_from_negative:
        suite.addTest(TestAppium('test_root_from_negative'))

    return suite


if __name__ == '__main__':
    suite = form_suite(get_options())
    unittest.TextTestRunner().run(suite)
