from playwright.sync_api import expect,Page
import pytest

'''
Refer ::::: Notes1 and ::::: Notes2  ::::: Below test cases 
to understand how to find table xpaths dynamically 
'''
# Test1
# This is the best practice for xpath tables by using dynamic xpath
def test_pagination_table_office(page: Page):
    print("\n Test case 1::find the employee office city name where the employee name is Cara Stevens ")

    page.goto("https://datatables.net/examples/basic_init/zero_configuration.html")

    name = "Cara Stevens"
    '''
    # It finds entire Cara Stevens row and see difference between this two xpaths
    #//table[@id='example']//tbody/tr/td[normalize-space()='Cara Stevens']-> finds only cara stevens name.
    #//table[@id='example']//tbody/tr[td[normalize-space()='Cara Stevens']]-> finds entire row where cara stevens name presents.
       or 
    # f"//table[@id='example']//tbody/tr/td[normalize-space()='{name}']/parent::tr" -> traversing approach,
                this one also finds entire row where cara stevens name presents
    '''

    # Find the Name of the employee
    cara_name = page.locator(f"//table[@id='example']//tbody/tr/td[normalize-space()='{name}']")
    print("The name of employee is:", cara_name.inner_text())

    # Find entire row the Name of the employee
    cara_row = page.locator(f"//table[@id='example']//tbody/tr/td[normalize-space()='{name}']/parent::tr")

    print("\nThe employee row is:\n", cara_row.inner_text())

    page.wait_for_timeout(3000)

    '''

    # Finding Office column header on cara stevens row 
    # because we need to have td[coulum number]  or td[i] in below line 
    # //table[@id='example']//tbody/tr/td[normalize-space()='Cara Stevens']/td[i]
    # so far found Cara Stevens row and need to find column that has to be dyamic one only 

    '''
    # Find office city name of the employee by using locator chaining concept
    # example instead writing of cara_row locator above just use that variable locator object

    city = cara_row.locator(
        "xpath=.//td[count(//table[@id='example']//thead/tr/th[normalize-space()='Office']/preceding-sibling::th) + 1]")

    print("The office is :", city.inner_text())

    page.wait_for_timeout(3000)



# Test2
# This is the best practice for xpath tables by using dynamic xpath
def test_pagination_table_name(page: Page):
    print("\n Test case::find the employee name where the office name is Edinburgh ")
    page.goto("https://datatables.net/examples/basic_init/zero_configuration.html")

    office = "Edinburgh"

    # Find the Name of the employee
    emp_office = page.locator(f"//table[@id='example']//tbody/tr/td[normalize-space()='{office}']")
    print("The employee office name is:", emp_office.inner_text())

    # this will finds office row of the employee which we want to find the employee name
    office_row = page.locator(f"//table[@id='example']//tbody/tr/td[normalize-space()='{office}']/parent::tr")

    print("\nThe office row is:\n", office_row.inner_text())

    page.wait_for_timeout(3000)

    # Find name of employee using locator chaining concept
    # example instead writing of office_row locator above just use that variable locator object

    emp_name = office_row.locator(
        "xpath=.//td[count(//table[@id='example']//thead/tr/th[normalize-space()='Name']/preceding-sibling::th) + 1]")
    print("The name of employee is :", emp_name.inner_text())

    page.wait_for_timeout(3000)



"""

::::: Notes1  :::::

Here is a revision-friendly note for everything we discussed about dynamic table XPath in Playwright, especially the important preceding-sibling concept.

📘 Playwright Dynamic Table XPath — Revision Notes
1. Basic table DOM structure

Imagine this table:

<table id="example">

    <thead>
        <tr>
            <th>Name</th>
            <th>Position</th>
            <th>Office</th>
            <th>Age</th>
            <th>Start date</th>
            <th>Salary</th>
        </tr>
    </thead>

    <tbody>
        <tr>
            <td>Cara Stevens</td>
            <td>Sales Assistant</td>
            <td>New York</td>
            <td>46</td>
            <td>2011-12-06</td>
            <td>$145,600</td>
        </tr>
    </tbody>

</table>

Think of it as:

              TABLE
                |
        +-------+-------+
        |               |
      THEAD           TBODY
        |               |
       TR             TR
        |               |
      THs             TDs
2. Find a cell using its text

For example, find Cara Stevens:

//table[@id='example']//tbody/tr/td[normalize-space()='Cara Stevens']

This finds:

<td>Cara Stevens</td>
Important

This is a cell, not the complete row.

3. Find the complete row

Use:

//table[@id='example']//tbody/tr/td[normalize-space()='Cara Stevens']/parent::tr

Or:

//table[@id='example']//tbody/tr[td[normalize-space()='Cara Stevens']]

I prefer the second form because it directly says:

Find the tr that contains a td with Cara Stevens.

4. Dynamic value

Don't hardcode the name.

Use a Python variable:

name = "Cara Stevens"

row = page.locator(
    f"//table[@id='example']//tbody/tr[td[normalize-space()='{name}']]"
)

This is reusable.

You can change:

name = "Cedric Kelly"

without changing the XPath.

5. Finding a row based on Office

Suppose:

office = "Edinburgh"

Use:

office_row = page.locator(
    f"//table[@id='example']//tbody/tr[td[normalize-space()='{office}']]"
)

This finds:

Cedric Kelly
Senior Javascript Developer
Edinburgh
22
2012-03-29
$433,060
Mental model
Find Edinburgh
      ↓
Find its <td>
      ↓
Find the <tr> containing that <td>
      ↓
Now we have the complete employee row
6. Locator chaining

This is VERY important in Playwright.

If:

office_row = page.locator(...)

then:

employee_name = office_row.locator(...)

means:

Search inside office_row.

Conceptually:

PAGE
 |
 +-- TABLE
      |
      +-- TBODY
           |
           +-- TR  ← office_row
                |
                +-- TD
                +-- TD
                +-- TD
                +-- TD

Then:

office_row.locator(...)

searches inside that TR.

7. Locator vs Element
Locator
row = page.locator("...")

row is a Playwright Locator.

It represents a way to find an element.

Think:

Locator
   ↓
"How can I find this element?"
DOM element

The actual HTML is:

<tr>...</tr>

Think:

Locator → finds → DOM element

So:

row.inner_text()

asks Playwright to find the element represented by the locator and retrieve its text.

8. Why td[1] is not ideal

You could write:

//tr[td[normalize-space()='Edinburgh']]/td[1]

This assumes:

Name = column 1

But what if the application changes the table to:

Position | Name | Office | Age | Start date | Salary

Now Name is column 2.

Your:

td[1]

would return:

Position

❌ Not good for a dynamic-table interview question.

9. Dynamic column identification using the header

Instead of saying:

Name is column 1

we say:

Find the Name header and determine its position.

The important XPath is:

//th[normalize-space()='Name']/preceding-sibling::th
preceding-sibling

Means:

Find sibling elements that appear before the current element.

Example:

<th>Name</th>
<th>Position</th>
<th>Office</th>
<th>Age</th>

For Office:

//th[normalize-space()='Office']/preceding-sibling::th

returns:

Name
Position

So:

count(
    //th[normalize-space()='Office']/preceding-sibling::th
)

returns:

2

Then:

2 + 1 = 3

Therefore Office is column 3.

10. The important dynamic XPath

For finding the Name corresponding to an employee whose Office is Edinburgh:

//table[@id='example']//tbody/tr[
    td[normalize-space()='Edinburgh']
]/td[
    count(
        //table[@id='example']//thead/tr/th[
            normalize-space()='Name'
        ]/preceding-sibling::th
    ) + 1
]
Break it down

First:

//table[@id='example']//tbody/tr[
    td[normalize-space()='Edinburgh']
]

Means:

Find the employee row containing Edinburgh.

Then:

//th[normalize-space()='Name']

Means:

Find the Name header.

Then:

/preceding-sibling::th

Means:

Find the headers before Name.

Then:

count(...)

Counts them.

Then:

+ 1

Converts the count into the column position.

11. Example with Name

Current table:

Name | Position | Office | Age | Start date | Salary
  ↑

Headers before Name:

0

Therefore:

0 + 1 = 1

So XPath dynamically resolves to:

td[1]
12. If columns change

Suppose application changes to:

Position | Name | Office | Age | Start date | Salary

Now:

Position
   ↓
Name

Headers before Name:

1

Therefore:

1 + 1 = 2

So XPath dynamically resolves to:

td[2]

That's why this is better than hardcoding:

td[1]
13. Very important mistake to avoid

Don't overwrite your Python value with a Locator.

❌ Don't do:

office = "Edinburgh"

office = page.locator(
    f"//td[normalize-space()='{office}']"
)

Now office has changed from:

"Edinburgh"

to:

Locator(...)

Use different variable names.

✅ Better:

office = "Edinburgh"

office_cell = page.locator(
    f"//td[normalize-space()='{office}']"
)

Use:

office
    ↓
Python string

office_cell
    ↓
Playwright Locator
14. Another common mistake

❌ Don't put a Locator inside another XPath:

office = page.locator(
    "//td[normalize-space()='Edinburgh']"
)

row = page.locator(
    f"//td[normalize-space()='{office}']/parent::tr"
)

This produces something like:

normalize-space()='<Locator frame=...>'

❌ Invalid XPath.

If you need the text, use:

office_text = office.inner_text()

But normally you don't need to do that. Just keep:

office = "Edinburgh"

as your string.

15. Recommended code pattern

For this type of interview question, remember this structure:

def test_dynamic_table(page: Page):

    page.goto(
        "https://datatables.net/examples/basic_init/zero_configuration.html"
    )

    office = "Edinburgh"

    # Find employee row using business value
    employee_row = page.locator(
        f"//table[@id='example']//tbody/tr"
        f"[td[normalize-space()='{office}']]"
    )

    # Find Name column dynamically using Name header
    employee_name = employee_row.locator(
        "xpath=.//td[count("
        "//table[@id='example']//thead/tr/th"
        "[normalize-space()='Name']/preceding-sibling::th"
        ") + 1]"
    )

    print("Employee name:", employee_name.inner_text())

Expected:

Employee name: Cedric Kelly
🧠 Quick Revision Cheat Sheet
Requirement	XPath
Find text cell	//td[normalize-space()='Edinburgh']
Find complete row	//tr[td[normalize-space()='Edinburgh']]
Go from cell to row	//td[normalize-space()='Edinburgh']/parent::tr
Find header	//th[normalize-space()='Name']
Find columns before header	//th[normalize-space()='Name']/preceding-sibling::th
Count columns before header	count(//th[normalize-space()='Name']/preceding-sibling::th)
Calculate column position	count(...) + 1
Search inside a Playwright locator	row.locator("xpath=.//td[...]")
⭐ Interview Answer to Remember

If interviewer asks:

"How would you find an employee's name based on their office without hardcoding the column number?"

You can say:

"First, I locate the row using the unique business value such as the Office name. Then I locate the required column dynamically using its header and preceding-sibling, rather than hardcoding a column index. Finally, I use Playwright locator chaining to search within that row."

That's the core concept you should remember:

BUSINESS VALUE
      ↓
FIND ROW
      ↓
FIND COLUMN HEADER
      ↓
preceding-sibling
      ↓
CALCULATE COLUMN POSITION
      ↓
LOCATOR CHAINING
      ↓
GET REQUIRED CELL
🔥 Most important 5 things to memorize
1. td[text]             → find cell
2. td[text]/parent::tr  → find row
3. preceding-sibling    → find elements before current element
4. count(...) + 1       → dynamically calculate column position
5. row.locator(...)     → search inside that row

If you understand those five, dynamic HTML table questions in Selenium/Playwright become much easier.

"""




"""

::::: Notes2  :::::

Locator = Playwright object used to identify and interact with element(s).

In Selenium:

element = driver.find_element(...)

WebElement = Selenium object representing the found webpage element.

Interview answer

If an interviewer asks "What is the difference between an element and a locator?", you can answer:

An element is the actual HTML object present in the DOM, such as an input, button, or table row. A locator is the mechanism or Playwright Locator object used to identify that element so that we can perform actions or validations on it. In Playwright, page.locator() returns a Locator, whereas Selenium's find_element() returns a WebElement.


Selenium                             vs                             Playwright
Concept	                    Selenium	                            Playwright
Find something	            find_element()	                        locator()
Multiple elements	        find_elements()                         locator() matching multiple elements
Returned object             WebElement	                            Locator
Example	            driver.find_element(By.ID, "user")	            page.locator("#user")
Fill	                element.send_keys()	                        locator.fill()
Click	                element.click()	                            locator.click()
Text	                element.text	                            locator.inner_text()
Multiple elements	    find_elements()                         	locator() matching multiple elements
nth item	            list indexing[] commonly used	            .nth()
"""

