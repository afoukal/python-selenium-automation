from time import sleep

from behave import given, when, then
from selenium.webdriver.common.by import By

VIDEO_1 = (By.CSS_SELECTOR, ".style-scope ytd-rich-grid-renderer ytd-rich-item-renderer")
LIKE = (By.CSS_SELECTOR, "a.yt-simple-endpoint.style-scope.ytd-toggle-button-renderer")
LIKE_VIDEO = (By.CSS_SELECTOR, "yt-formatted-string#title")
PREMIUM_POPUP = (By.XPATH, "//*[text()='1 month free']")


@given('Open Youtube page')
def open_youtube(context):
    context.driver.get("https://www.youtube.com/")


@when("Click on the first video")
def choose_video(context):
    context.driver.find_element(*VIDEO_1).click()
    sleep(2)


@when("Click on Like")
def like_video(context):
    premium_popup = context.driver.find_elements(*PREMIUM_POPUP)
    if len(premium_popup) > 0:
        premium_popup.click()
    else:
        context.driver.find_element(*LIKE).click()
    sleep(3)


@then("{like_video} text is displayed")
def like_this_text(context, like_video):
    like_video_text = context.driver.find_element(*LIKE_VIDEO).text
    assert like_video in like_video_text, f'{like_video_text} displayed instead of {like_video}'




