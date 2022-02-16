from flask import Flask, render_template, request
import calculator as cal

Flask_App = Flask(__name__) # Creating our Flask Instance

@Flask_App.route('/', methods=['GET'])
def index():
    """ Displays the index page accessible at '/' """

    return render_template('index.html')

@Flask_App.route('/operation_result/', methods=['POST'])
def operation_result():
    """Route where we send calculator form input"""
    # request.form looks for:
    # html tags with matching "name= "
    first_input = request.form['Input1']  
    second_input = request.form['Input2']
    operation = request.form['operation']

    try:
        input1 = int(first_input)
        input2 = int(second_input)
        if input1 < 0:
            return render_template(
            'index.html',
            result= "Bad Input",
            calculation_success=False,
            error="Cannot perform numeric operations with provided input")
        
        if input2 <0:
            return render_template(
            'index.html',
            result= "Bad Input",
            calculation_success=False,
            error="Cannot perform numeric operations with provided input")
            
            
        # On default, the operation on webpage is addition
        if operation == "+":
            result = cal.add(input1,input2)

        elif operation == "-":
            result = cal.subtract(input1,input2)

        elif operation == "*":
            result = cal.multiply(input1,input2)

        return render_template(
            'index.html',
            input1=input1,
            input2=input2,
            operation=operation,
            result=result,
            calculation_success=True
        )
    
    except ValueError:
        return render_template(
            'index.html',
            input1=first_input,
            input2=second_input,
            operation=operation,
            result= "Bad input",
            calculation_success=False,
            error="Cannot perform numeric operations with provided input"
        )

if __name__ == '__main__':
    Flask_App.debug = True
    Flask_App.run()

