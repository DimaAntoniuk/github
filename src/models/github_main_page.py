import uuid
from src.models.base_page import BasePage
from src.utils.locators import GitHubMainPageLocators

class GitHubMainManager(BasePage):

    def create_new_repo(self):
        self.find_element(GitHubMainPageLocators.CREATE_MENU,time=2).click()
        self.find_element(GitHubMainPageLocators.NEW_REPO,time=2).click()

    def get_profile(self):
        self.find_element(GitHubMainPageLocators.PROFILE_MENU,time=2).click()
        profile = self.find_element(GitHubMainPageLocators.PROFILE,time=2)
        return profile.text