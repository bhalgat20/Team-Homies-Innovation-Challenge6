from src.api.utils import utils

def get_population_density(location):
    return utils.mapper('./config/population_density.csv','location',location,'density')
