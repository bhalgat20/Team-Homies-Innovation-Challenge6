from utils import utils

def get_weather(month):
    return utils.mapper('./config/weather_data.csv','month',month,'weather')
