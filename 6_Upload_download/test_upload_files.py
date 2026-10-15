from playwright.sync_api import expect, Page
import pytest


def test_upload_singlefile(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    filepath = 'C:\\Users\\shara\\PycharmProjects\\Python_Playwright\\6_Upload_download\\test1.txt'
    #uploading single file
    page.locator("//input[@id='singleFileInput']").set_input_files(filepath)
    page.locator("//button[normalize-space()='Upload Single File']").click()

    expect(page.locator("#singleFileStatus")).to_contain_text("test1.txt")
    print("File uplaod succesfull......")
    page.wait_for_timeout(5000)


def test_upload_multiplefiles(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    #uploading multiple files
    files=["C:\\Users\\shara\\PycharmProjects\\Python_Playwright\\6_Upload_download\\test1.txt",
           "C:\\Users\\shara\\PycharmProjects\\Python_Playwright\\6_Upload_download\\test2.txt"]

    page.locator("//input[@id='multipleFilesInput']").set_input_files(files)
    page.locator("//button[normalize-space()='Upload Multiple Files']").click()

    #validation
    msgloc=page.locator("//p[@id='multipleFilesStatus']")

    expect(msgloc).to_contain_text("test1.txt")
    expect(msgloc).to_contain_text("test2.txt")

    page.wait_for_timeout(5000)

    print("Multiple files are uploaded successfully.......")

