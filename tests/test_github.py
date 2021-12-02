import config
import uuid

from src.models.github_main_page import GitHubMainManager
from src.models.github_repo_page import GitHubRepoManager
from src.models.github_login_page import GitHubLoginManager


def test_github_login(browser):
    github_login_page = GitHubLoginManager(browser, config.GITHUB_LOGIN_URL)
    github_login_page.go_to_site()
    github_login_page.enter_creds(config.LOGIN, config.PASSWORD)
    github_login_page.click_on_the_signin_button()
    github_main_page = GitHubMainManager(browser, browser.driver.current_url)
    profile = github_main_page.get_profile()
    assert config.LOGIN in profile
    

def test_create_new_repo(browser):
    github_main_page = GitHubMainManager(browser, browser.driver.current_url)
    github_main_page.go_to_site()
    github_main_page.create_new_repo()
    github_repo_page = GitHubRepoManager(browser, browser.driver.current_url)
    github_repo_page.go_to_site()
    github_repo_page.fill_in_repo_data(repr(uuid.uuid4())[6:-2], 'Custom description')
    options = github_repo_page.check_repo_options_section()
    assert 'Add .gitignore' in options
