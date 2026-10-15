from playwright.sync_api import expect, Page
import re
import pytest



def test_flight_booking_app(page: Page):

    page.goto("https://blazedemo.com/")
    expect(page.locator("//div[@class='container']/h1")).to_be_visible()

    print("Selecting departure city:")
    source_city = page.locator("//select[@name='fromPort']")
    source_city.click()
    page.wait_for_timeout(3000)
    print("source city dropdown is clicked")

    # Get the options to be printed from dropdown

    drp_options = page.locator("//select[@name='fromPort']/option")

    count = drp_options.count()
    print("The total options count is:", count)

    for i in range(count):
        text = drp_options.nth(i).inner_text().strip()
        print(text)
        if text == 'San Diego':
            continue

    # step2 : selecting San Diego as source city

    page.locator("//select[@name='fromPort']").select_option(label='San Diego')
    print("Source city selected")


    # step3: selecting San Diego as source city and click on find flights

    page.locator("//select[@name='toPort']").select_option(label="Dublin")
    print("Destination city selected")
    page.wait_for_timeout(3000)

    page.locator("//div[@class='container']/input[@type='submit']").click()
    page.wait_for_timeout(1000)
    text_validation = page.locator("//div[@class='container']/h3")
    text_validation_text = text_validation.inner_text()
    print("The text is:", text_validation_text)

    expect(text_validation).to_contain_text(text_validation_text)

    page.wait_for_timeout(1000)


    #step 5: Try to print the table rows

    table = page.locator("//table[@class='table']")
    print("----> The table inner text is:\n--->", table.inner_text())

    #step6: Get the header and rows and store in variable

    headers = page.locator("//table[@class='table']/thead/tr/th").all_inner_texts()

    print("the headers:", headers)

    rows = page.locator("//table[@class='table']/tbody/tr")
    rows_texts = rows.all_inner_texts()
    print("the rows are:", rows_texts)

    count = rows.count()
    print("\nThe count is:\n", count)

    # step7: Find the Price column all <td> present in that column
    # Need to apply zip() method which takes zip(headers, values) followed by dict(zip(headers, values))

    l = []
    for i in range(count):
        # need to use rows in which locator "//table[@class='table']/tbody/tr",
          # here till we need to have <tr> only we should include <td> in locator above line 65
          # because it works like on specific row find all td's below line
        values = rows.nth(i).locator("td").all_inner_texts()
        row_data = dict(zip(headers, values))
        l.append(row_data['Price'])

    print("The list is:",l)

    price_data = [ele.replace('$', '') for ele in l]
    print(type(price_data))
    print("The price of flights::",price_data)

    # step8: count the total_value in the list
    total_value = 0
    for i in price_data:
        total_value = total_value+float(i)
    print(total_value)

    # Find the Flight column all <td> cells and add them in list

    # step1: Find all headers and apply all_inner_text()
    headers = page.locator("//table[@class='table']/thead/tr/th").all_inner_texts()

    rows = page.locator("//table[@class='table']//tbody/tr")

    count = rows.count()
    print("\nThe count is:", count)

    l3 = []
    for i in range(count):
        values = rows.nth(i).locator('td').all_inner_texts()
        row_data = dict(zip(headers, values))
        l3.append(row_data['Flight #'])

    print(l3)

    flight_data = [int(ele) for ele in l3]
    print("The flight numbers::",flight_data)


    # Now sort the prices and determine the flight with lowest price

    for i in range(count):
        latest_data = dict(zip(flight_data,price_data))

    print("This is the flight with price data:\n",latest_data)

    d3 = {}

    for i in range(count):
        flight_number = flight_data[i]
        flight_price =  price_data[i]
        d3[flight_number] = flight_price

    print("\nThis is the value of d3\n", d3)


    # Find the least price of the flight
    # One sentence to remember
    # min(d3, key=d3.get) = find the key whose value is the smallest.
    # tells Python:
    # "Don't decide based on the key. Use the value of each key to decide which is smallest."

    least_price = min(d3, key=d3.get)
    print("The least price of flight_name is:",least_price)  # returns the key i.e (flight_number)
    print("The price ",d3[least_price])  # returns value of key i.e d[key]

    '''
    If we want to apply loop rather than just using inbuilt apps like min() or max()
    use this below approach 
    This is the value 
    d3 = {43: '472.56', 234: '432.98', 9696: '200.98', 12: '765.32', 4346: '233.98'}
    lowest_price = float('inf') ===> inf means ====> infinite price 
    '''

    least_price_a = float('inf')
    least_flight_a = None

    for flight, price in d3.items():

        price = float(price)
        if price<least_price_a:
            least_price_a = price
            least_flight_a = flight

    print("The lowest flight is least_flight_a:", least_flight_a)
    print("The lowest price  is least_price_a:",least_price_a)
    to_enter = [least_flight_a]
    print("Found the lowest price of the fligt:---->",to_enter)

    #Now find the entire <tr> of which least price flight is presented --->to_enter = [least_flight_a]
    # Enter the price dynamically by using f-string and get the row

    rows_choose = page.locator(f"//table[@class='table']//tbody/tr/td[normalize-space()='{least_flight_a}']/parent::tr")

    print("the row inner text is:--->",rows_choose.inner_text())

    for i in to_enter:
        text_price = page.locator(f"//table[@class='table']//tbody/tr/td[normalize-space()='{i}']/parent::tr")
        print("The entire row:\n", text_price.inner_text())

    page.wait_for_timeout(2000)

    # once row is found,on this we need to have the column cell <td> which needed to perform action
    # for that first findcolumn header
    # and second apply preceding-sibling & count() method,
    # then find td[] of that row
    # so it has to be ----> row.locator(xpath://td[count()])

    choose_header = rows_choose.locator("xpath=.//td[count(//table[@class='table']//thead/tr/th[normalize-space()='Choose']/preceding-sibling::th) + 1]")

    print("The choose_column_header inner text:",choose_header.inner_text()) #return None it's form type

    # Find xpath to click by using locator chaining concept

    choose_this_flight = choose_header.locator("xpath=.//input[@type='submit']")

    choose_this_flight.click()
    print("choose_this_flight is clicked")

    page.wait_for_timeout(3000)

    expect(page.locator("//p[normalize-space()='Please submit the form below to purchase the flight.']")).to_be_visible()
    page.wait_for_timeout(2000)

    # input Name
    page.locator("//div[@class='control-group']//input[@id='inputName']").fill("kumar")
    print("Name is entered")

    # Address
    page.locator("//div[@class='control-group']//input[@id='address']").fill("75 street")
    print("Address is entered")

    # City
    page.locator("//div[@class='control-group']//input[@id='city']").fill("Dallas")
    print("City is entered")

    # State
    page.locator("//div[@class='control-group']//input[@id='state']").fill("TX")
    print("State is entered")

    # Zip Code
    page.locator("//div[@class='control-group']//input[@id='zipCode']").fill("7657")
    print("Zip Code is entered")

    # Credit Card Number
    page.locator("//div[@class='control-group']//input[@id='creditCardNumber']").fill("986798")
    print("Zip Code is entered")

    # Month
    page.locator("//div[@class='control-group']//input[@id='creditCardMonth']").fill("10")
    print("Month is entered")

    # Year
    page.locator("//div[@class='control-group']//input[@id='creditCardYear']").fill("2018")
    print("Year is entered")

    # Name on Card
    page.locator("//div[@class='control-group']//input[@id='nameOnCard']").fill("2018")
    print("Name on Card is entered")

    # Purchase Flight
    page.locator("//div[@class='control-group']/div/input[@type='submit']").click()
    print("Purchase Flight is clicked")

    page.wait_for_timeout(4000)

    expect(page.locator("//div[@class='container']//h1[normalize-space()='Thank you for your purchase today!']")).to_be_visible()
    print("It is verified")
    page.wait_for_timeout(2000)

    print("Ready to print the table--->>\n")
    table_confirm = page.locator("//table[@class='table']/tbody/tr")

    page.wait_for_timeout(4000)

    count = table_confirm.count()
    print("The row count is:",count)


    for i in range(count):
        confirm_text = table_confirm.nth(i).inner_text().strip()
        print(confirm_text)

    id_value = page.locator("//table[@class='table']/tbody/tr/td[starts-with(normalize-space(), '17')]")
    print("The id is:", id_value.inner_text())

    page.wait_for_timeout(5000)





    # # Now find the Airline column all <td>
    #
    # #Step1 : Find the header
    # airline_header = page.locator("//table[@class='table']/thead/tr/th").all_inner_texts()
    # print("the header is:",airline_header)
    #
    # #step2: Find all the rows
    # rows = page.locator("//table[@class='table']/tbody/tr")
    #
    # row_header = page.locator("//table[@class='table']/tbody/tr").all_inner_texts()
    # print(row_header)
    #
    # #step3: count()
    # count = rows.count()
    # print("The count:",count)
    #
    # #step4: apply loop by using range(count) and get each rows cells and extract values
    # l2 = []
    # for i in range(count):
    #     values = rows.nth(i).locator('td').all_inner_texts()  #return list of all <td> cells in a row
    #     row_data = dict(zip(airline_header,values))
    #     l2.append(row_data['Airline'])
    #
    # print(l2)
    # for i in l2:
    #     print(i)
    #
    #












































