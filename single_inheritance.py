class Apple:
    manufacturer = 'Apple Inc.'
    contact_website = 'www.apple.com/contact'

    def contact_details(self):
        print(f'To contact us, please visit: {self.contact_website}')


class MacBook(Apple):
    def __init__(self):
        self.manufacturer_year = 2017

    def manufacturer_details(self):
        print(f'This MacBook was manufactored in the year {self.manufacturer_year}, by {self.manufacturer}')


macbook = MacBook()
macbook.manufacturer_details()
macbook.contact_details()