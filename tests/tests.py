from src.models.google import GooglePageManager

def test_google_search(browser):
    google_main_page = GooglePageManager(browser, "https://google.com/")
    google_main_page.go_to_site()
    google_main_page.enter_word("Hello")
    google_main_page.click_on_the_search_button()
    elements = google_main_page.check_navigation_bar()
    assert "test" in elements