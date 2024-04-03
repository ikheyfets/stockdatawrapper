import os
import requests
import warnings

from dotenv import load_dotenv

from wrapper.validation import RequestValidator
from wrapper.endpoints import Endpoint


class StockDataApiWrapper():
    def __init__(self, key=None, key_env_name=None) -> None:
        if key == None and key_env_name == None:
            raise Exception(f"You have to specify either the key or its environment variable name")
        if key != None and key_env_name != None:
            warnings.warn("Looks like you provided both the key and it's environment variable. In this case we are proceeding with the key.")

        if key:
            self.key = key
        else:
            load_dotenv()
            self.key = os.environ.get(key_env_name)
        self.validator = RequestValidator()
        self.url = "https://api.stockdata.org/v1/"
    
    def get_stock_prices(self, symbols, **kwargs):
        new_kwargs = {"api_token": self.key, "symbols": symbols}
        new_kwargs.update(kwargs)
        endpoint = Endpoint(type='Stock prices', kwargs=new_kwargs)
        self.validator.validate(endpoint=endpoint)
        return endpoint.call()

    def get_intraday_data(self, symbols, adjusted=False, **kwargs):
        if adjusted:
            endpoint_type = 'Instraday data (adjusted)'
        else:
            endpoint_type = 'Instraday data (unadjusted)'
        new_kwargs = {"api_token": self.key, "symbols": symbols}
        new_kwargs.update(kwargs)
        endpoint = Endpoint(type=endpoint_type, kwargs=new_kwargs)
        self.validator.validate(endpoint=endpoint)
        return endpoint.call()
    
    def get_eod_historical_data(self, symbols, **kwargs):
        new_kwargs = {"api_token": self.key, "symbols": symbols}
        new_kwargs.update(kwargs)
        endpoint = Endpoint(type='End-of-day historical data', kwargs=new_kwargs)
        self.validator.validate(endpoint=endpoint)
        return endpoint.call()