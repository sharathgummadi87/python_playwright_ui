from playwright.sync_api import Page


class CartPage:

    def __init__(self, page:Page):

        self.page = page



    def verify_product_name(self,product_name):

        verify_product = self.page.locator(f"//table[contains(@class,'table')]/tbody/tr/td[normalize-space()='{product_name}']")

        verify_product_text = verify_product.first.inner_text()
        print("The text of product is:", verify_product_text)
        if verify_product_text == 'Samsung galaxy s6':
            return verify_product.first
        else:
            return None

'''
# if text is matched, we are returning locator since in playwright assertion done 
# on locator objects rather than values "verify_product.first" ---> returns locator object    
'''



