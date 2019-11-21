from core.extract import *
from core.load import *

if __name__ == "__main__":

    # Extract
    extract_swapi_data()
    extract_sws_data()

    ## Load
    load_swapi_data()
    load_sws_data()
