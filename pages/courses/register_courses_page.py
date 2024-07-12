from base.selenium_driver import SeleniumDriver
import time



class RegisterCoursesPage(SeleniumDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Login Locators
    _link_SignIn = "//a[@class='dynamic-link'][text()='Sign In']"
    _textbox_Email = "//input[@class='form-control input-md'][@name='email']"
    _textbox_Password = "//input[@class='form-control input-md'][@name='password']"
    _button_Login = "//button[@id='login']"
    _banner_MyCourses = "//h1[text()='My Courses ']"

    # Register courses locators
    _search_box = "//input[@placeholder='Search Course']"
    _button_search = "//i[@class='fa fa-search']"
    _course = "//h4[contains(text(), '{0}')]"
    _link_All_courses = "//a[text()='ALL COURSES']"
    _button_enroll = "//button[contains(text(), 'Enroll in Course')]"
    _textbox_cc_num = "//input[@aria-label='Credit or debit card number']"
    _textbox_cc_exp = "//input[@placeholder='MM / YY']"
    _textbox_cc_cvv = "//input[@placeholder='Security Code']"
    # _button_Buy = "//button[@type='button']/i[@class='fa fa-arrow-right']"
    _enroll_error_message = "//li[@class='card-no text-danger']/span"
    _Iframe_Name = "__privateStripeFrame9253"

    def click_on_SignIn(self):
        self.elementClick("xpath", self._link_SignIn)

    def enter_email(self, email):
        self.sendKeys(email, "xpath", self._textbox_Email)

    def enter_password(self, password):
        self.sendKeys(password, "xpath", self._textbox_Password)

    def click_on_Login(self):
        self.elementClick("xpath", self._button_Login)

    def verify_for_presence_of_mycourse_banner(self):
        return self.isElementPresent("xpath", self._banner_MyCourses)

    def verify_valid_login(self, email, password):
        self.click_on_SignIn()
        self.enter_email(email)
        self.enter_password(password)
        self.click_on_Login()
        result = self.verify_for_presence_of_mycourse_banner()
        return result

    def clickOnAllCourses(self):
        self.elementClick("xpath", self._link_All_courses)

    def searchCourseName(self, name):
        self.sendKeys(name, "xpath", self._search_box)
        self.elementClick("xpath", self._button_search)
        time.sleep(1)

    def selectCourseToEnroll(self, fullCourseName):
        whichCourse = self._course.format(fullCourseName)
        self.elementClick("xpath", whichCourse)

    def enrollCourse(self):
        self.elementClick("xpath", self._button_enroll)

    def scrollingDown(self):
        innerHeight = self.getInnerHeight()
        self.scrollDown(innerHeight-200)

    def enterCardNum(self, num):
        self.switchToIFrameByLoopingAllIFrames("xpath", self._textbox_cc_num)
        self.sendKeys(num, "xpath", self._textbox_cc_num)
        self.switchTodefaultContent()

    def enterExp(self, exp):
        self.switchToIFrameByLoopingAllIFrames("xpath", self._textbox_cc_exp)
        self.sendKeys(exp, "xpath", self._textbox_cc_exp)
        self.switchTodefaultContent()

    def enterCvv(self, cvv):
        self.switchToIFrameByLoopingAllIFrames("xpath", self._textbox_cc_cvv)
        self.sendKeys(cvv, "xpath", self._textbox_cc_cvv)
        self.switchTodefaultContent()

    def enterCreditCardInformation(self, num, exp, cvv):
        self.enterCardNum(num)
        self.enterExp(exp)
        self.enterCvv(cvv)

    def verify_for_appearnce_of_error_message(self):
        errorMessage = self.getElement("xpath", self._enroll_error_message)
        errorMessageText = errorMessage.text
        return errorMessageText

    def verify_enroll_failed(self, course, ccNum, ccExp, ccCVV):
        self.clickOnAllCourses()
        self.searchCourseName(course)
        self.selectCourseToEnroll(course)
        self.enrollCourse()
        self.scrollingDown()
        self.enterCreditCardInformation(ccNum, ccExp, ccCVV)
        time.sleep(4)
        result = self.verify_for_appearnce_of_error_message()
        assert result == 'Your card number is invalid.'
        self.clickOnAllCourses()
        # return result
