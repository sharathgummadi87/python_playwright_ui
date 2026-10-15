from playwright.sync_api import expect, Page
import re
import pytest

'''
Assignment Task 1 - Lab 1: Handling Dynamic Web Tables
file:///C:/Users/shara/Downloads/Day26-Tables-Lab+Assignment.pdf
"https://testautomationpractice.blogspot.com"
'''



# Test_1 Retrieve the CPU Load value for the Chrome process
def test_cpuload_chrome(page: Page):
    
    print(" Test_Case 1 :::: Retrieve the CPU Load value for the Chrome process ::::")
    page.goto("https://testautomationpractice.blogspot.com/")

    table = page.locator("//table[@id='taskTable']//tbody/tr")

    count = table.count()
    print("the count is:", count)

    print("the table is :",table)

    print("printing row one by one and get the text:\n")

    for i in range(count):
        text = table.nth(i).inner_text().strip()
        print("The text is:", text)

    page.wait_for_timeout(2000)

    # captured all names by myself and stored them in list collection so one by one i can iterate and apply
    Name = ['Chrome', 'System', 'Internet Explorer', 'Firefox']

    # step1: Get the name from list whichever we wanted to perform action
    for i in Name:
        name = page.locator(f"//table[@id='taskTable']//tbody/tr/td[normalize-space()='{i}']")
        text = name.inner_text().strip()
        print("The name is :", text)
        if text == 'Chrome':
            print("\n The text is matched")
            print("Trying to get the entire row:")

            # Finds the table header only
            # step2: Find the header only
            header = page.locator("//table[@id='taskTable']//thead/tr")
            print("----->The header is -------->\n",header.inner_text())

            # Finds the {i} -> row complete row
            # step3: Find the Firefox entire row
            name_row = page.locator(f"//table[@id='taskTable']//tbody/tr/td[normalize-space()='{i}']/parent::tr")
            print("----->The entire row is----->\n", name_row.inner_text())

            # step4: Find the CPU Load value, and it's preceding-sibling of that column & count() method
            # apply locator chaining concept of name_row.column
            # need to mention xpath=.//  otherwise playwright considers it as a CSS selector

            print("\n --->Trying to get CPU load of Chrome process:--->")
            print("Get the CPU% of", text,"is :----->")
            cpu_data = name_row.locator("xpath=.//td[count(//table[@id='taskTable']//thead/tr/th[normalize-space()='CPU (%)']/preceding-sibling::th) + 1]")
            cpu_value = cpu_data.inner_text()
            print("The cpu value is :", cpu_value)
            expect(name_row).to_contain_text(cpu_value)
            page.wait_for_timeout(2000)
            break

    page.wait_for_timeout(2000)


# Test case 2 : Verify Memory Size of Firefox process:
def test_memory_usage_firefox(page: Page):
    
    print(" Test_Case 2 :::: Verify Memory Size of Firefox process::::")
    page.goto("https://testautomationpractice.blogspot.com/")
    table = page.locator("//table[@id='taskTable']//tbody/tr")

    count = table.count()
    print("the count is:", count)

    print("printing row one by one and get the text:\n")

    for i in range(count):
        text = table.nth(i).inner_text().strip()
        print("The text is:", text)

    page.wait_for_timeout(2000)

    # captured all names by myself and stored them in list collection so one by one i can iterate and apply
    Name = ['Chrome', 'System', 'Internet Explorer', 'Firefox']

    # step1: Get the name from list whichever we wanted to perform action
    for i in Name:
        name = page.locator(f"//table[@id='taskTable']//tbody/tr/td[normalize-space()='{i}']")
        name_firefox = name.inner_text()
        if name_firefox == 'Firefox':
            print("Firefox is presented in the table-->")
            print("Now trying to get the header printed")

            # step2: Find the header only
            table_header = page.locator("//table[@id='taskTable']//thead/tr")
            print("The table header is:\n", table_header.inner_text())

            # step3: Find the Firefox entire row
            print("---->Now get the only firefox entire row ---->:\n")
            firefox_et_row = page.locator(f"//table[@id='taskTable']//tbody/tr/td[normalize-space()='{i}']/parent::tr")

            print("The entire Firefox row is\n:",firefox_et_row.inner_text())


            # step4: Find the Memory column header column, and it's preceding-sibling of that column & count() method
            # apply locator chaining concept of firefox_et_row.column
            # need to mention xpath=.//  otherwise playwright considers it as a CSS selector

            memory_mb = firefox_et_row.locator("xpath=.//td[count(//table[@id='taskTable']//thead/tr/th[normalize-space()='Memory (MB)']/preceding-sibling::th) + 1]")

            memory_mb_text = memory_mb.inner_text()
            print("The memory mb is:", memory_mb_text)

            # perform assert memory_mb of firefox against firefox_et_row  it is displayed on table
            # we should perform assertion on locator in playwright and not on the value
               # in the expect()  ---> statement

            expect(firefox_et_row).to_contain_text(memory_mb_text)

    page.wait_for_timeout(2000)


# Test 3 Verify Network speed of Chrome process
def test_network_speed_chrome(page: Page):
    print(" Test_Case 3 :::: Network speed of Chrome process::::")
    page.goto("https://testautomationpractice.blogspot.com/")
    table = page.locator("//table[@id='taskTable']//tbody/tr")

    count = table.count()
    print("the count is:", count)

    print("printing row one by one and get the text:\n")

    for i in range(count):
        text = table.nth(i).inner_text().strip()
        print("The text is:", text)

    page.wait_for_timeout(2000)

    # captured all names by myself and stored them in list collection so one by one i can iterate and apply
    Name = ['Chrome', 'System', 'Internet Explorer', 'Firefox']

    #step1: Get the name from list whichever we wanted to perform action
    for i in Name:
        chrome = page.locator(f"//table[@id='taskTable']//tbody/tr/td[normalize-space()='{i}']")
        text = chrome.inner_text()
        if text == 'Chrome':
            print("\nFound, and the inner text is:", text)

            #step2: Find the table header only
            table_header = page.locator(" //table[@id='taskTable']//thead/tr")
            print("\n The table header is:\n", table_header.inner_text())

            #step3 : Find the chrome entire row
                    # the below one returns playwright locator object
            chrome_a = page.locator("//table[@id='taskTable']//tbody/tr/td[normalize-space()='Chrome']/parent::tr")

            print("This is the chrome entire row:\n",chrome_a.inner_text())

            # step4: Find the Disk space column, and it's preceding-sibling of that column & count() method
                 # and we need apply locator chaining concept by using chrome_a entire row.column
                 # need to mention xpath=.//  otherwise playwright considers it as a CSS selector
            network_speed = chrome_a.locator("xpath=.//td[count(//table[@id='taskTable']//thead/tr/th[normalize-space()='Network (Mbps)']/preceding-sibling::th) +1 ]")

            network_text = network_speed.inner_text()
            print("The network speed of chroem is:",network_text)

            #step5: assertion
            expect(chrome_a).to_contain_text(network_text)

    page.wait_for_timeout(2000)


# Test 4 Verif Disk space of Firefox process
def test_disK_space_firefox(page: Page):
    print(" Test_Case 4 :::: Disk space of Firefox process ::::")
    page.goto("https://testautomationpractice.blogspot.com/")
    table = page.locator("//table[@id='taskTable']//tbody/tr")

    count = table.count()
    print("the count is:", count)

    print("printing row one by one and get the text:\n")

    for i in range(count):
        text = table.nth(i).inner_text().strip()
        print("The text is:", text)

    page.wait_for_timeout(2000)

    # captured all names by myself and stored them in list collection so one by one i can iterate and apply
    Name = ['Chrome', 'System', 'Internet Explorer', 'Firefox']

    # step1: Get the name from list whichever we wanted to perform action
    for i in Name:
        chrome = page.locator(f"//table[@id='taskTable']//tbody/tr/td[normalize-space()='{i}']")
        text = chrome.inner_text()
        if text == 'Firefox':
            print("\nFound, and the inner text is:", text)

            # step2: Find the header only

            t_header = page.locator(" //table[@id='taskTable']//thead/tr")
            print("The table header is\n:", t_header.inner_text())

            # step3: Find the Firefox entire row

            firefox_en_row = page.locator(f"//table[@id='taskTable']//tbody/tr/td[normalize-space()='{i}']/parent::tr")

            print("The firefox entire row is \n:",firefox_en_row.inner_text())

            # step4: Find the Disk space column, and it's preceding-sibling of that column & count() method
                    # apply locator chaining concept of firefox_en_row.column
                    # need to mention xpath=.//  otherwise playwright considers it as a CSS selector

            disk_space_colum = firefox_en_row.locator("xpath=.//td[count(//table[@id='taskTable']//thead/tr/th[normalize-space()='Disk (MB/s)']/preceding-sibling::th) +1]")

            disk_space_text = disk_space_colum.inner_text()
            print("---->The disk space of Firefox is ----->", disk_space_text )

            #step5: assertion
            expect(firefox_en_row).to_contain_text(disk_space_text)

    page.wait_for_timeout(2000)























