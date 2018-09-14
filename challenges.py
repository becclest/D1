from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)


# Task 2 : Dynamic URLS
# edit the view function to display 'Welcome to <course_name>' on localhost:5000/course/<course>
@app.route('/course/<course_name>')
def courseView(course_name):
    return '<h1>Welcome to {}</h1>'.format(course_name)


# Task 3.1 Basic HTML Form
    # Set the method and action of the HTML form, such that form data is sent to /result using POST method
    # The form should have a text field in which you can enter an ingredient (milk, eggs, etc)
@app.route('/form')
def formView():
    html_form = '''
    <html>
    <body><form action="http://localhost:5000/result" method='POST'>
    <label>
    <input type="text" name="ingredient" value="Milk"><br>
    <input type="submit" value="Submit">
    </form>
    </body>
    </html>
    '''
    return html_form

# Task 3.2 : Processing Form Data


@app.route('/result', methods=['GET', 'POST'])
def resultView():
    # Make an API request to Recipe API for the ingredient entered in the form and display the recipe results
    # Step 1 : Receive the ingredient from the form if request type is POST
    if request.method == "POST":
        ingredient = request.form.get('ingredient', '')
        print (ingredient)
    # Step 2 : Create paramaters JSON with the ingredient received in step 1 in the form required by http://www.recipepuppy.com/about/api/
    params = {}
    params["i"] = ingredient
    api_url_base = 'http://www.recipepuppy.com/api/'
    # Step 3 : Make an API request to Recipe API and parameters in Step 2
    response = requests.get(api_url_base, params=params)
    # Step 4 : Parse the response from API request in JSON
    data = json.loads(response.text)
    # Step 5 : Display the response in browser (remember : HTML takes only strings)
    data_str = str(data)
    return (data_str)


if __name__ == '__main__':
    app.run(debug=True)
