import unittest
import pytest
from pages.courses.register_courses_page import RegisterCoursesPage
from ddt import data, unpack, ddt


@pytest.mark.usefixtures("init_driver")
@ddt
class Test_Register_Courses(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetUp(self, init_driver, request):
        self.rcp = RegisterCoursesPage(self.driver)

    @pytest.mark.run(order=1)
    def test_verify_valid_login(self):
        email = "Sanjay.Joshi2020@gmail.com"
        password = "Phase3@1980"
        result = self.rcp.verify_valid_login(email, password)
        assert result == True

    @pytest.mark.run(order=2)
    @data(("JavaScript for beginners", "5546370221081234", "0710", "321"),
          ("Learn Python 3 from scratch", "5546370221085678", "0711", "456"),
          ("Selenium WebDriver 4 With Python", "5546370221085678", "0711", "456"))
    @unpack
    def test_verify_enroll_failed(self, course, ccNum, ccExp, ccCVV):
        # errorMessage = self.rcp.verify_enroll_failed()
        self.rcp.verify_enroll_failed(course, ccNum, ccExp, ccCVV)
        # assert errorMessage == "Your card number is invalid."


if __name__ == "__main__":
    unittest.main(verbosity=2)
