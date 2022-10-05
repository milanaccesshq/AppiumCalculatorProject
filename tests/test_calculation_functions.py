from unittest import TestCase
import time
import random


class CalculatorTest(TestCase):
    def test_calculator_test(self):
        # Sets a counter to start upon running the test
        counter = time.time()
        # Sets a separate counter in local time format
        t = time.localtime()
        # Converts that time to human-readable to be printed later
        start = time.asctime(t)
        # List of the different operators (do not change)
        operators = ["add", "sub", "mul", "div"]
        # List of the expected result for each operator (do not change)
        results = ["16", "8", "48", "3"]
        # List of numbers to be randomised, each linked to the above operators (do not change)
        options = [0, 1, 2, 3]
        # Number of times the test will be run (can change)
        repeats = 2
        # List to store each individual iteration's runtime
        iteration_msg: list = [""]*repeats
        # Variables to count each time the operator is used
        add = sub = mul = div = 0
        # Importing the calculation function from calculation_functions.py
        from functions.calculator_functions import calculation
        for i in range(repeats):
            # Starts a counter for the iteration
            iteration_counter = time.time()
            x = random.choice(options)
            self.assertEqual(calculation("12", "4", operators[x]), results[x])
            if x == 0:
                add += 1
            if x == 1:
                sub += 1
            if x == 2:
                mul += 1
            if x == 3:
                div += 1
            if i < repeats-1:
                time.sleep(5)
            # Gets the runtime of the current iteration and assigns it to the final message
            iterations = time.time() - iteration_counter
            iteration_msg[i] = str(i+1) + ": " + str(iterations) + " seconds"
        # Gets the length of the entire test
        counter = time.time() - counter
        # Gets the end time of the test in local time and converts it to human-readable
        t = time.localtime()
        end = time.asctime(t)
        # Creates the html file named tet.html that prints the data
        file_html = open("tet.html", "w")
        file_html.write('''<html>
        <head>
        <title>Test Execution Time</title>
        <body>
        <h1>Test Execution Time</h1>
        <p>The time taken to execute the calculator test was ''' + str(counter) + ''' seconds.</p>
        <p>The test began at '''+str(start)+''' and finished at '''+str(end)+'''.</p>
        <p>'''+str(repeats)+''' tests were run at random providing the following results.</p>
        <p>Time taken for iteration:</p>
        <p>'''+", ".join(iteration_msg)+'''</p>
        <p>Addition: '''+str(add)+'''</p>
        <p>Subtraction: '''+str(sub)+'''</p>
        <p>Multiplication: '''+str(mul)+'''</p>
        <p>Division: '''+str(div)+'''</p>
        </body>
        </html>''')
        file_html.close()

