from utils import utils

def get_health_status(location,month,year):
    return utils.status_mapper('./config/health_status.csv','location',f"{month}/{year}",location,'status')