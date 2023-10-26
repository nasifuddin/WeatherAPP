**APPROACH**

The goal of this project was to make an API that can predict the temperature of Dhaka for future dates and times.
This project was built by using Django as a basic API and neuralprophet as an LSTM time-series forecasting model.
Here are some basic breakdowns of approaching the problem:
- Collect, analyze, and clean the dataset
- Selecting the model that may perform the model
- Train and finetune the model
- Testing the model's performance based on future date and time
- Saving the model to use in API
- Extracting/filtering the exact value for a specific date and time
- Create a Django project and create a new app on the project
- Connecting the app to the actual project
- Creating basic API response for the app in a basic HTML page
- Building up the functions and responses in the API
- fixing the output result and response time



**INSTALLATION**

- Install Anaconda/miniconda on your device
- Create a virtual environment: conda create --name strativ python=3.9
- conda activate strativ
- Copy the link of this repo and clone this repo by using: git clone https://github.com/nasifuddin/WeatherAPP.git
- cd path/to/weatherapp/ 
- Install dependencies on terminal by: pip install django matplotlib numpy pandas neuralprophet or use pip install -r "requirements.txt"
- Start the server by running : python manage.py runserver (make sure that you are on the project directory)
- Go to browser and type: 127.0.0.1:8000 or ctrl+click on the link from terminal
- This model can predict the weather in Dhaka for next three months(Nov Dec Jan) in any given time on hourly interval.
So after the homepage is loaded give date and time as input. Predicted temperature will be shown.


![Capture1](https://github.com/nasifuddin/WeatherAPP/assets/125158930/1d7a9a61-51a2-45ad-be20-7a82ad304060)
![Capture2](https://github.com/nasifuddin/WeatherAPP/assets/125158930/a2dda5e9-acbb-4aba-8c60-2356c14ebf0e)
