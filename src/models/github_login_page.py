from src.models.base_page import BasePage
from src.utils.locators import GitHubLoginPageLocators

class GitHubLoginManager(BasePage):

    def enter_creds(self, login, password):
        login_field = self.find_element(GitHubLoginPageLocators.LOGIN)
        login_field.click()
        login_field.send_keys(login)
        password_field = self.find_element(GitHubLoginPageLocators.PASSWORD)
        password_field.click()
        password_field.send_keys(password)
        return (login_field, password_field)

    def click_on_the_signin_button(self):
        return self.find_element(GitHubLoginPageLocators.SINGIN_BUTTON,time=2).click()
