import uuid
from src.models.base_page import BasePage
from src.utils.locators import GitHubRepoPageLocators

class GitHubRepoManager(BasePage):

    def fill_in_repo_data(self, name=repr(uuid.uuid4()), description='My new repo'):
        name_field = self.find_element(GitHubRepoPageLocators.NAME)
        name_field.click()
        name_field.send_keys(name)
        description_field = self.find_element(GitHubRepoPageLocators.DESCRIPTION)
        description_field.click()
        description_field.send_keys(description)
        return (name_field, description_field)

    def check_repo_options_section(self):
        all_list = self.find_elements(GitHubRepoPageLocators.OPTIONS,time=2)
        options = [x.text for x in all_list if len(x.text) > 0]
        return options