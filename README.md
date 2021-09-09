To download dependencies listed in the requirements file you’ll need to execute the ‘pip’ command:
pip install -r requirements.txt

Inside the virtual environment you can now run the unit-tests in the test_main.py’ file:
python -m pytest -v tests/test_generator.py