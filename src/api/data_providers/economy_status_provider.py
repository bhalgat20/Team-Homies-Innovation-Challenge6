from utils import utils

def get_economy_status(location,month,year):
    return utils.status_mapper('./config/economy_status.csv','location',f"{month}/{year}",location,'status')
