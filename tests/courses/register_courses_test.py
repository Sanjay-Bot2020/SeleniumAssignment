import unittest
import pytest
from pages.courses.register_courses_page import RegisterCoursesPage


@pytest.mark.usefixtures("init_driver")
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
    def test_verify_enroll_failed(self):
        errorMessage = self.rcp.verify_enroll_failed()
        assert errorMessage == "Your card number is invalid."


if __name__ == "__main__":
    unittest.main(verbosity=2)
