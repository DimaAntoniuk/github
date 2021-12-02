from selenium.webdriver.common.by import By

class GitHubLoginPageLocators:
    LOGIN = (By.ID, 'login_field')
    PASSWORD = (By.ID, 'password')
    SINGIN_BUTTON = (By.CSS_SELECTOR, 'input.btn.btn-primary.btn-block.js-sign-in-button')

class GitHubMainPageLocators:
    PROFILE_MENU = (By.XPATH, "//summary[@aria-label='View profile and more']")
    CREATE_MENU = (By.XPATH, "//summary[@aria-label='Create new…']")
    PROFILE = (By.CSS_SELECTOR, 'div.header-nav-current-user a.user-profile-link')
    NEW_REPO = (By.XPATH, "//a[@href='/new']")

class GitHubRepoPageLocators:
    NAME = (By.CSS_SELECTOR, '.js-repo-name')
    DESCRIPTION = (By.ID, 'repository_description')
    OPTIONS = (By.CSS_SELECTOR, 'div.js-repository-auto-init-options div.form-checkbox label')
