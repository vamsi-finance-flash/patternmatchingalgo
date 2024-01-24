# patternmatchingalgo

# `application` folder contains all the files of the project

your_project/
├── app.py
├── templates/
│   └── result.html
└── static/
    └── images/
        ├── image1.png
        ├── image2.png
        └── ...


## How to execute: 
To run this app, we have to run the `app.py` file in the application folder.

Then a link will be printed in the terminal, by opening the link in a browser, it will be taken to the `index.html` page

in the `index.html` page, there you will be asked to enter inputs, such as the stock name and hodling period, 

based on the `stock name`, the data will be retrieved from the offline csv file. 
based on the `holding period` the window size will be taken by the program.

nextly, the code from `working.py` file will be executed, and then `graphs` will be generated and saved into the templates folder

then `h2.py` file is called to create a html file to show the saved graphs.
here a file named `res.html` is created and it contains all the images to show.

lastly, `result.html` file will be called by the flask framework, to show the output
