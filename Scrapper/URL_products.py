from bs4 import BeautifulSoup
import requests
import time
import json
import asyncio

class Scrapper:
    
    # =============== CONSTRUCTOR ===============
    def __init__(self,URL:str,verbose:bool = False, daemon:bool = False):
        '''
        '''
        # Defining the variables
        self.URL     = URL
        self.verbose = verbose
        self.daemon  = daemon
        self.__inform("Class initialized correctly...")

        # If class instanced as a daemon, loads soup automatically
        if self.daemon:
            self.load_soup()
        
    # =============== PRIVATE METHODS ===============
    def __inform(self,message:str):
        '''
        Method used to print messages in console depending on `verbose` flag.

        ### Args:
        * message (str): The message to be printed in console
        '''
        if self.verbose: print(message)

    # =============== PUBLIC METHODS ===============
    def load_soup(self):
        '''
        Method created to declare the soup as an attribute of the class.

        ### Notes:
        * This method generates an attribute called `soup`, which can take 2 values: BeautifulSoup object | None
        '''
        execution_time = time.time()
        
        response = requests.get(self.URL)
        if response.status_code == 200:
            html = response.text
            self.soup = BeautifulSoup(html,'lxml')
        else:
            self.soup = None

        self.__inform(f"Execution time for generating soup: {time.time() - execution_time}")


    #product function extracts all the products' URL of the current page of the browsed product.
    """def product(self):
        products = self.soup.find_all('li', class_='ui-search-layout__item')
        products_urls = []
        for purl in products:
            prdct_url = purl.find_all('a')
            product_url = prdct_url[0]['href']
            products_urls.append(product_url)
        #return print(products_urls)"""
    
    #name function extracts the name of the product.
    def name(self):
        attributes1 = self.soup.find('div', class_= 'ui-pdp-container__col col-2 mr-32')
        nm = attributes1.find('h1', class_ = 'ui-pdp-title')
        nonfound = 0
        if nm:
            self.nametxt = nm.get_text()
        else:
            print('The product name was not found.')

    #price function extracts the price of the product.
    def price(self):
        attributes2 = self.soup.find('div', class_= 'ui-pdp-container__col col-2 mr-32')
        pr = attributes2.find('span', class_ = 'andes-money-amount__fraction')
        if pr:
            self.prices = pr.get_text()
        else:
            print('The product price was not found.')

    #price function extracts the price of the product.
    def description(self):
        attributes3 = self.soup.find('p', class_= 'ui-pdp-description__content')
        #dscrp = attributes3.find('p', class_= 'ui-pdp-description__content') I haven't delated this one because I have some doubts.
        if attributes3:
            self.descriptions = attributes3.get_text()
        else:
            print('The product description was not found.')
    
    #image function extracts all the URLs of the images of the product.
    def image(self):
        img_tags = self.soup.select('div[class*="ui-pdp-gallery"] span[class*="ui-pdp-gallery"] figure[class*="ui-pdp-gallery"] img')
        self.images = []
        for im in img_tags:
            img = im.get('data-zoom')
            self.images.append(img)
    
    #all_attributes function recieves all the extracted characteristics of the product and prints them.
    def all_attributes(self):
        start_time = time.time()
        self.name()
        self.price()
        self.description()
        self.image()
        all_def = {
            "name": self.nametxt,
            "price": self.prices,
            "description": self.descriptions,
            "images": self.images
        }
        json_result = json.dumps(all_def, indent = 2)
        end_time = time.time()
        self.time2 = end_time - start_time
        print(f'The execution time of the product attributes is {self.time2} seconds.')
        return json_result
    
    #timer function is used just to measure the time of the 'requests' method. It's not useful for the Scrapper itself.
    '''CODERNOTE: I made this function because when I put the time1 and time 2 in a single function it caused problems
    (arguments conflicts) and it was easier for me doing a function just for the request time (time1).'''
    def timer(self):
        return (f'The execution time of the request is {self.time1} seconds.')



# =============== DEBUGGING ===============
if __name__ == '__main__':
    start_time = time.time()
    
    #Test for the products' URL extraction
    link1 = 'https://listado.mercadolibre.com.mx/laptops#D[A:laptops]'
    
    test1 = Scrapper(
        URL     = link1,
        verbose = True,
        daemon  = True,
    )

    

    #Test for the products attributes
    link2 = 'https://www.mercadolibre.com.mx/laptop-lenovo-ideapad-156-ryzen-3-7320u-8gb-256gb-ssd/p/MLM21816271?pdp_filters=category:MLM1652#searchVariation=MLM21816271&position=3&search_layout=stack&type=product&tracking_id=dd9d1c17-227c-4f8d-87e6-09b3c7969cad'
    
    test2 = Scrapper(
        URL     = link2,
        verbose = True,
        daemon  = True,
    )