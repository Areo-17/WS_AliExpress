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

## Importing libraries


