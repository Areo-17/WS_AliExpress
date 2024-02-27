# **MercadoLibre Web scrapper**

Hello! Welcome to the our web scrapper project.
MercadoLibre is an online shopping webpage that offers a variety of products of many categories, such as technology, clothing, supermarket, pets, etc.
The main objective of our web scrapper is to offer a web app that allows the user enter a word, wich will be browsed on MercadoLibre website, and returns the multiple products that are related with that search on the website, showing the price, name, description and images of the product.

## Where will the scrapper be developed?
The application will be developed on Python language, for this, please install [Visual Studio Code](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwiF1fa1uMqEAxVLIEQIHTcjBNEQFnoECAwQAQ&url=https%3A%2F%2Fcode.visualstudio.com%2F&usg=AOvVaw15O90sm1ios8AUpw56hCml&opi=89978449)

## Adapting the work environment
First of all, create the folder in which you will be working the project, you have to create this from the file explorer of your OS. After this, open Visual Studio Code and choose the created folder.

### Creating a virtual environment
Once you have opened the folder, create a virtual environment. For this, open the terminal in Visual studio code with the command ``ctrl+` ``, or `ctrl+ñ` if you have a keyboard with the "ñ" letter.
With the opened termninal, navigate to the path of your folder (Usually, once you open the terminal it is on the path of your active folder) just as the image.
![Captura de pantalla (3419)](https://github.com/Areo-17/WS_MercadoLibre/assets/144394013/6ca9e5d6-7a3b-443b-a573-38d396c43c6f)
Now that you are on the selected path, write the following command ` python -m venv venv` on the terminal and press the  enter button. 
![Captura de pantalla (3420)](https://github.com/Areo-17/WS_MercadoLibre/assets/144394013/c500bbde-3859-45a8-bd10-37c4c8cca11d)
The execution of the previous command will create you a folder that contains your virtual environment. Inside this folder you can find 3 other folders that are "Include", "Lib", and "Scripts". Do not modify any of these folders.
![Captura de pantalla (3421)](https://github.com/Areo-17/WS_MercadoLibre/assets/144394013/f0db3b2f-c6bb-4e06-a2bb-f3302a724821)
The purpose of creating a virtual environment is to work under specific libraries (that we are going to install later) and control the versions of our app, avoiding conflicts with other versions and also indicating which libraries and their versions we are using for the project.

### Activating and deactivating the virtual environment
To work propperly in our project we have to activate the virtual environment. To achieve this, write the command `venv\Scripts\activate` on the terminal and press the enter button. Make sure that you are in the path in which the virtual environment was created.
![Captura de pantalla (3423)](https://github.com/Areo-17/WS_MercadoLibre/assets/144394013/49cea558-b4a7-4f37-8d48-7e56e3967d9d)
![Captura de pantalla (3426)](https://github.com/Areo-17/WS_MercadoLibre/assets/144394013/b75aa288-ac54-4d20-9b16-331a703c2db2)

If `(venv)` shows up to the left of your path in the terminal the virtual environment has been activated successfully. You have to keep it activated until you close the file.

To deactivate the virtual environment, write the command `venv\Scripts\deactivate` on the terminal and press the enter button. You should do this everytime you are going to stop working on your code.
![Captura de pantalla (3425)](https://github.com/Areo-17/WS_MercadoLibre/assets/144394013/96ce4d73-2880-4759-a766-68912e2e11b9)

If `(venv)` dissapears from left of your path in the terminal, then the virtual environment has been deactivated successfully.

## Installing libraries

In programming, libraries (also known as modules) are sets of predefined functions, classes and constants that provide specific functionality that can be reused by other programs. They offer a wide range of tools to perform various tasks without having to write all the code from scratch. In a few words, libraries help us to develop a more efficient code through special function (methonds).
For this project, we are going to install "bs4", "requests", and "Flask". In Python, the libraries are installed with the `pip install` command. On your active virtual environment, install the already mentioned libraries with the following commands:
```
pip install bs4
pip install lxml
pip install requests
pip install Flask
```
You have to do it one by one, take a look of the following example:
![Captura de pantalla (3427)](https://github.com/Areo-17/WS_MercadoLibre/assets/144394013/6a0a9479-dd8d-4b3e-8b30-4361046c0d25)

***NOTE: Before install them in your virtual environment, you have to install these libraries (in the same way) on your global Python. Open the cmd of your PC and install them.***
![Captura de pantalla (3428)](https://github.com/Areo-17/WS_MercadoLibre/assets/144394013/851dbf0f-e05c-4d49-b82f-965a5ca78a6a)

## Starting to code

Create a Python file by right-clicking on the venv folder and choosing the option "New File...", it will automatically create a file, name it as *"Product_scrapper.py"*.
And now we have the first Python file in which we will be working on. Let's start importing the libraries on the first three lines of code.
![Captura de pantalla (3429)](https://github.com/Areo-17/WS_MercadoLibre/assets/144394013/dfb383bb-b476-4e18-a412-4778a79a2439)

Before continuing, let's see why we are using these libraries.
**bs4:** Extracts elements of HTML web pages.
**lxml:** It offers a wide range of functions for efficient parsing, manipulation, searching and generation of XML/HTML documents.
**requests:** Send and receive HTTP requests.
**time:** Used to measure times.
**json:** Encodes and decodes JSON data.

The next step is to declare our class. A class serves as a template for defining the properties (attributes) and behaviors (methods) that objects of that class will have.
The first function will be the initialization of recurring variables.
![Captura de pantalla (3430)](https://github.com/Areo-17/WS_MercadoLibre/assets/144394013/41a9fe46-f354-4838-8587-0c45225677b4)

`Class Scrapper`: declares a new class named Scrapper.

`def __init__(self, URL: str, verbose: bool = False, daemon: bool = False)`: defines the constructor method using the __init__ special method, which is called whenever a new instance of the class is created.

`self` refers to the current object instance. This method takes three parameters: 
**URL**: A required string parameter representing the URL to be scraped.
**verbose**: An optional boolean parameter (default: False), indicating whether verbose logging messages should be printed.
**daemon**: An optional boolean parameter (default: False), determining whether the class should behave as a daemon (explained later).

The triple-quoted strings (''') before the code block define the docstring, which provides a brief description of the class and its parameters. It improves code readability and understanding.

`self.URL = URL`: Assigns the provided URL parameter to the instance attribute self.URL for storage within the object.
This is repeated for `verbose` and `daemon`, creating instance attributes associated with the respective parameters' values.

`self.__inform("Class initialized correctly...")`: This line calls a private method (`__inform`) within the class, potentially to print a message indicating successful class initialization. The 
double underscores (__) before the method name convention in Python make this method private, meaning it can only be accessed directly within the class and not from external code.

`if self.daemon`: checks if the daemon parameter is set to True. If so, the code block within the if statement executes:

`self.load_soup()`: This line calls another method, load_soup, within the class, to load the content from the URL and parse it using a web scraping library like BeautifulSoup (not shown in this code snippet).

Let's continue with the private and public methods that were mentioned in the previous explanation.
![Captura de pantalla (3431)](https://github.com/Areo-17/WS_MercadoLibre/assets/144394013/b485aebf-6fce-4c65-bfa8-a073fb429083)

`def __inform(self, message: str)`: declares a private method named __inform.

`message: str` is a required parameter of type str, representing the message to be printed.

`if self.verbose`: checks if the instance attribute self.verbose is set to True. If True, the code inside the if block executes: `print(message)` prints the provided message to the console.

`def load_soup(self)`: declares a public method named load_soup.

`execution_time = time.time()`: measures the current time using the time.time() function and stores it in the execution_time variable.

`response = requests.get(self.URL)` sends a GET request to the self.URL attribute (an URL) using the requests library and stores the response object in response.

`if response.status_code == 200`: checks if the response status code is 200 (indicating success). If True, the code inside the if block executes:

`html = response.text`: extracts the text content from the response and stores it in html.

`self.soup = BeautifulSoup(html, 'lxml')` parses the html content using the BeautifulSoup library and the lxml parser, and sets the result as the soup attribute of the object.

`else:` (if the status code isn't 200):

`self.soup = None` sets the soup attribute to None to indicate that no soup (parsed content) was created.

`self.__inform(f"Execution time for generating soup: {time.time() - execution_time}")` calls the private  `__inform` method and prints a message to the console (if verbose is True) showing the time taken to generate the soup.

The following step is to start to do the functions for the products characteristics that we are going to extract:
![Captura de pantalla (3432)](https://github.com/Areo-17/WS_MercadoLibre/assets/144394013/74293519-fa36-4e61-b580-2b4126b6f353)

`#name function extracts the name of the product.` This is a line comment and does not affect the code's execution. It describes the purpose of the following function.

`def name(self)`: defines a function named name within the class.

`attributes1 = self.soup.find('div', class_= 'ui-pdp-container__col col-2 mr-32')` searches within the soup attribute (a BeautifulSoup object)for the first <div> element with the class names 'ui-pdp-container__col', 'col-2', and 'mr-32'. This element corresponds to the product information section based on the CSS selectors of the HTML code of MercadoLibre. The result is stored in the variable `attributes1`.

`nm = attributes1.find('h1', class_ = 'ui-pdp-title')` searches within the previously found element (attributes1) for the first <h1> element with the class name 'ui-pdp-title'. This the product name element. The result is stored in the variable `nm`.

`if nm`: checks if the nm variable contains a value (meaning the product name element was found). If True, the code block within the if statement executes:

`self.nametxt = nm.get_text()` extracts the text content of the product name element and assigns it to the nametxt attribute of the object.

`else:` (if the product name element wasn't found) then it executes:

`print('The product name was not found.')` which prints an error message to the console.

