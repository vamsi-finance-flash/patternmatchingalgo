from flask import Flask, render_template, request
from working import *
from ht import *

def funct(selected_option,selected_time_period):
    dat = 'D:/FInance Flash/application/csvdata/'+selected_option+".csv"
    tp = int(selected_time_period)

    return (dat,tp)

app = Flask(__name__)
# app = Flask(__name__, static_url_path='/static')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    # Get user input from the form
    selected_option = request.form['option']
    selected_time_period = request.form['time_period']

    # Process the input (replace this with your actual processing logic)
    dat, tp = funct(selected_option,selected_time_period)
    # processed_output = process_input(selected_option, selected_time_period)

    # Generating the graphs
    working_function(dat,tp)

    # # Get a list of image files in the folder
    # image_files = [f for f in os.listdir(image_folder) if f.endswith(".png")]

    # # Create a list of dictionaries containing image name and path
    # image_data = [{'name': image, 'path': image} for image in image_files]

    #Updating the result.html file
    time.sleep(5)
    work()
    time.sleep(2)
    return render_template('res.html',)

    # Render the output on a new page
    # return render_template('result.html', output=processed_output)


if __name__ == '__main__':
    app.run(debug=True)
