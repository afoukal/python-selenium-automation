from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from selenium.webdriver.common.by import By

VIDEO_1 = (By.CSS_SELECTOR, ".style-scope ytd-rich-grid-renderer ytd-rich-item-renderer")
LIKE = (By.CSS_SELECTOR, "a.yt-simple-endpoint.style-scope.ytd-toggle-button-renderer")
LIKE_VIDEO = (By.XPATH, "//*[text()='Like this video?']")
PREMIUM_POPUP = (By.XPATH, "//*[text()='1 month free']")
#ADS = (By.ID, "preskip-component:n")
ADS = (By.CSS_SELECTOR, ".video-ads.ytp-ad-module")
SKIP = (By.CSS_SELECTOR, ".ytp-ad-skip-button.ytp-button")


@given('Open Youtube page')
def open_youtube(context):
    context.driver.get("https://www.youtube.com/")


@when("Click on the first video")
def choose_video(context):
    context.driver.find_element(*VIDEO_1).click()
    sleep(2)


@then("Click on Like")
def like_video(context):
    premium_popup = context.driver.find_elements(*PREMIUM_POPUP)
    ads = context.driver.find_elements(*ADS)
    if len(ads) > 0:
        if context.driver.find_element(*SKIP).text == 'Skip Ads':
            context.driver.find_element(*SKIP).click()
        elif context.driver.wait.until(EC.element_to_be_clickable(PREMIUM_POPUP)):
            premium_popup.click()
    else:
        context.driver.find_element(*LIKE).click()
    sleep(3)
    like_video_text = context.driver.find_element(*LIKE_VIDEO).text
    assert 'Like' in like_video_text, f'{like_video_text} displayed instead'



