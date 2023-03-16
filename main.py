import requests
import pandas as pd
from datetime import datetime 


#below you can change the mylong and mylat variables to the longitude and latitude of your preference
mylong = -48.00
mylat = -26.00

parameters = {
    "lat": mylat,
    "long": mylong,
    "formatted":0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params= parameters)

response.raise_for_status()

data = response.json()
sunrise_hour = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunrise_minutes = data["results"]["sunrise"].split("T")[1].split(":")[1]
sunrise_seconds = data["results"]["sunrise"].split("T")[1].split(":")[2].split("+")[0]
sunrise_time = sunrise_hour + ":" + sunrise_minutes + ":" + sunrise_seconds

sunset_hour = data["results"]["sunset"].split("T")[1].split(":")[0]
sunset_minutes = data["results"]["sunset"].split("T")[1].split(":")[1]
sunset_seconds = data["results"]["sunset"].split("T")[1].split(":")[2].split("+")[0]
sunset_time = sunset_hour + ":" + sunset_minutes + ":" + sunset_seconds



df = pd.DataFrame(data)

timenow = str(datetime.now())
timenow_hour = timenow.split(" ")[1].split(":")[0]
timenow_minutes = timenow.split(" ")[1].split(":")[1]
timenow_seconds = timenow.split(" ")[1].split(":")[2].split(".")[0]
timenow_time = timenow_hour + ":" + timenow_minutes + ":" + timenow_seconds

print(f"The sunrise time is {sunrise_time}\nThe sunset time is {sunset_time}\nand the Time Now is {timenow_time}")
