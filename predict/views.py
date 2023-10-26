from django.shortcuts import render
from django.http import JsonResponse
from neuralprophet import NeuralProphet
import pickle
import pandas as pd

m = NeuralProphet()

# load the model
with open("dhaka_forecast.pkl", "rb") as f:
    m = pickle.load(f)


# Create your views here.
def predict(request):
    return render(request, "index.html")


def User(request):
    date_time = request.GET["input"]

    # load dataframe
    df = pd.read_csv("data.csv")
    print("dataframe loaded")

    # prediction
    future = m.make_future_dataframe(df, periods=2400)
    m.restore_trainer()
    forecast = m.predict(future)
    print("forecast succeed")

    # filtering temp
    filtered_df = forecast.loc[(forecast["ds"] == date_time)]
    predicted_temp = round(filtered_df["yhat1"].values[0], 2)
    print(predicted_temp)
    return render(
        request, "user.html", {"date_time": date_time, "predicted_temp": predicted_temp}
    )
