# Currency Coverter
Sure! Here's a guide for using the Currency Converter program:

1. Install Python 3 on your computer if you haven't already. You can download it from the official Python website: https://www.python.org/downloads/

2. Install the requests library by running the following command in your terminal or command prompt:

   ```
   pip install requests
   ```

3. Download the `currency_converter` directory and navigate to it in your terminal or command prompt.

4. To convert currencies, run the following command:

   ```
   python run.py
   ```

   This will open a graphical user interface (GUI) where you can enter the amount, "from" currency, and "to" currency that you want to convert.

5. Enter the amount you want to convert in the "Amount" field.

6. Select the currency you want to convert from in the "From" dropdown menu.

7. Select the currency you want to convert to in the "To" dropdown menu.

8. Click the "Convert" button to perform the conversion. The converted amount will be displayed in the "Result" field.

9. If you want to clear the input fields, click the "Clear" button.

That's it! You can use this program to convert currencies as many times as you want.

# Currency Coverter Testing

Sure, here's a guide for how to run the tests using pytest:

1. Install pytest: If you haven't already installed pytest, you can do so by running the following command in your terminal: `pip install pytest`

2. Create a test file: Create a new file in the same directory as your code file and name it `test_[your_code_file_name].py`. For example, if your code file is called `currency_converter.py`, then your test file should be named `test_currency_converter.py`.

3. Write your test cases: In your test file, import the necessary modules and write your test cases using the pytest framework. Make sure to cover as many edge cases as possible.

4. Run the tests: To run the tests, navigate to the directory where your test file is located and run the command `pytest`. pytest will automatically search for all files with the name `test_*.py` and run all the tests in them.

5. View the test results: pytest will print the results of the tests in your terminal. If any of the tests fail, pytest will provide information on which test failed and why.

Here's an example test case for the `convert_currency` function in `currency_converter.py`:

```
import currency_converter

def test_convert_currency():
    assert currency_converter.convert_currency(100, "USD", "EUR") == 84.17
    assert currency_converter.convert_currency(50, "GBP", "JPY") == 6921.54
    assert currency_converter.convert_currency(0, "USD", "EUR") == 0.0
    assert currency_converter.convert_currency(-100, "USD", "EUR") == None
```

This test case tests the `convert_currency` function with different input values and expected output values. If all the tests pass, pytest will print a message indicating that all the tests passed. If any of the tests fail, pytest will print a message indicating which test(s) failed and why.
