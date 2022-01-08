from utils import utils

def get_location(store_id):
    return utils.mapper('./config/locations.csv','store_id',store_id,'location')
