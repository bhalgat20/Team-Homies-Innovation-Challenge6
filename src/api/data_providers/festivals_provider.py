from utils import utils

def get_festivals(location,month,year):
    return utils.status_mapper('./config/festivals_data.csv','location',f"{month}/{year}",location,'festivals')
