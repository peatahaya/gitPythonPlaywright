This project is focused on automated testing using Python, Playwright and Pytest. Instruction below will guide you how to install all required modules and how to start testing process.

1. First we have to create new project in our IDE (Pycharm, VSCode, etc.)
2. Now we have to create specific folder structure. It is important because Page Object Model requires separeting page objects from tests.
   
![image](https://github.com/user-attachments/assets/2590fd16-53d4-4af6-89d5-34aef706c623)


3. Remember that:<br>
   -tests have to be in 'tests' folder<br>
   -name of the test file should start with 'test_'<br>
   -test function name inside test file should start with 'test_'<br>
4. Now we have to install required modules via command line:<br>
   pip install pytest-playwright<br>
   playwright install<br>
   pip install pytest<br>
   pip install RandomUser (We will use this module to generate random user data)<br>
5. After successful instalations we can write our code
6. To test our funcionalities we use commands below in terminal:<br>
   
   pytest -s --headed --slowmo=1000 (this command will run tests in headed mode. It means our browser will open and we will see all the actions that playwright does according to our instructions. 'slowmo=1000' means, there will be 1000ms delay in playwright actions on page. Results of tests will appear in terminal.)<br>

   pytest test_example_name.py (this command will run tests inside test_example_name.py file only without opening a browser. Results will also appear in terminal.)<br>

   pytest /tests (this command runs all tests inside 'tests' folder without opening a browser)<br>

   pytest test_example_name.py::test_func_name (this command runs single function from 'test_example_name.py' file without opening a browser)
