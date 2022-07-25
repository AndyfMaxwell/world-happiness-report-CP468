# world-happiness-report-CP468

Model Training/Running Instructions:

1. Download the relevant files and place into relevant directory: ladderscore-model.py, ladderscore-model - revised.py, world-happiness-report-2021.csv, requirements.txt
2. Create a virtual environment using Python -m venv ./venv
3. Enter your virtual environment with command: .\venv\Scripts\activate.bat
4. Install relevant packages with command: pip install -r requirements.txt
5. Executing either python file ('ladderscore-model.py' for the model that used all 6 features or 'ladderscore-model - revised.py' for the model which used the 3 most correlated features.) Will create and train a model, then test the model and print out the mean squared error of the model's performance. Feel free to repeat this step multiple times for different results.

Plot Generation Instructions:

1. Download the relevant files and place into relevant directory: plots.py, requirements.txt
2. Create a virtual environment using Python -m venv ./venv
3. Enter your virtual environment with command: .\venv\Scripts\activate.bat
4. Install relevant packages with command: pip install -r requirements.txt
5. Uncomment a preferred plot from the code to view it
6. Execute plots.py with the relevant plot uncommented will generate the plot you seek.
