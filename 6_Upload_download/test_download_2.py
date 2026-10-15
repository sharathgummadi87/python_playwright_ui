from playwright.sync_api import sync_playwright, expect, Page
import os

def test_download_file(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/p/download-files_25.html")

    page.locator("#inputText").fill("welcome")
    page.locator("#generateTxt").click()  # this will generate a link to download file

    # # Appraoch 1: register an event
    # def handle_download(download):
    #     download.save_as("downloads/testfile.txt")
    #
    # page.on("download",handle_download)

    # Appraoch 2: lambda
    page.on("download",lambda download: download.save_as("downloads/testfile.txt"))

    page.locator("#txtDownloadLink").click()  # this will download the file

    page.wait_for_timeout(3000)

    if os.path.exists("downloads/testfile.txt"):
        print("File exists")
    else:
        print("File not exist")

