import pytest
from playwright.sync_api import sync_playwright, expect,Page

@pytest.mark.skip
def test_frames_1(page: Page):
    page.goto("https://ui.vision/demo/webtest/frames/")

    frames = page.frames
    print("Number of frames:", len(frames))

    frame1 = page.frame(url = 'https://ui.vision/demo/webtest/frames/frame_1')
    inputbox = frame1.locator("//input[@name='mytext1']")
    inputbox.fill("Focus on one thing")
    page.wait_for_timeout(2000)

@pytest.mark.skip
def test_frames_2(page: Page):
    page.goto("https://ui.vision/demo/webtest/frames/")

    frames = page.frames
    print("no of frames:", len(frames))
    frame2 = page.frame(url='https://ui.vision/demo/webtest/frames/frame_2')
    print("navigated to frame2")
    input_box2 = frame2.locator("//input[@name='mytext2']")
    input_box2.fill("Concentrate")
    page.wait_for_timeout(2000)
    page.wait_for_load_state()


# https://ui.vision/demo/webtest/frames/frame_3
def test_frames_3(page: Page):
    page.goto("https://ui.vision/demo/webtest/frames/")

    frames = page.frames
    print("no of frames:", len(frames))
    frame3 = page.frame(url='https://ui.vision/demo/webtest/frames/frame_3')
    print("navigated to frame3")

    input3 = frame3.locator("//input[@name='mytext3']")
    input3.fill("Focus is the KEY")
    print("Navigated and entered in frame3")

    # can access frame within the frame by using child_frames
    child_frames=frame3.child_frames
    print("no of child frames:",len(child_frames))
    innerframe = child_frames[0]
    radio = innerframe.locator("//div[@id='i9' and @role='radio']")
    radio.check()
    expect(radio).to_be_checked()
    print("radio button checked")

    page.wait_for_timeout(3000)
    checkbox = innerframe.locator("//div[@role='checkbox' and @aria-label='General Web Automation']")
    page.wait_for_timeout(2000)
    checkbox.check()
    page.wait_for_timeout(2000)
    print("checkbox is checked")
    expect(checkbox).to_be_checked()
    page.wait_for_timeout(3000)
    next_button = innerframe.locator("//span[normalize-space()='Next']/parent::div[@role='button']")
    print("text is:",next_button.inner_text())
    next_button.click()
    print("Next button is clicked")
    page.wait_for_timeout(3000)

    inputbox = innerframe.locator("//div[@class='Xb9hP']/input[@type='text']")
    inputbox.fill("Give your best")
    page.wait_for_timeout(3000)
    submit_button = innerframe.locator("//span[normalize-space()='Submit']/parent::div[@aria-label='Submit']")
    submit_button.click()
    print("submit button is clicked")
    page.wait_for_timeout(3000)
    text_verify = innerframe.locator("//div[@class='vHW8K']")
    expect(text_verify).to_contain_text("Thank you for testing the UI.")
    page.wait_for_timeout(3000)



