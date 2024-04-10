# stockdatawrapper

This is a Python wrapper for the [stockdata.org](https://www.stockdata.org) API, allowing easy integration of the API functionalities into Python applications.

---

## Installation

## Usage

### Authentication

*stockdatawrapper* relies on the API token you can obtain from [their website](https://www.stockdata.org) for authentication. You can then either pass this token as a string when you intialize the `StockDataApiWrapper` object:

```
from stockdatawrapper import StockDataApiWrapper

wrapper = StockDataApiWrapper(key='API_TOKEN_STRING')
wrapper.get_stock_prices('AAPL')
```

or store the token as an environment variable and pass the name of the environment variable to the `StockDataApiWrapper` object:

```
from stockdatawrapper import StockDataApiWrapper

wrapper = StockDataApiWrapper(key_env_name='API_TOKEN_ENVIRONMENT_VARIABLE_NAME')
wrapper.get_stock_prices('AAPL')
```



### Making Requests

Once a `StockDataApiWrapper` object has been instantiated, you can use its built-in methods to make API calls. There is a method for each endpoint in the API documentation. Parameters listed as required in the documentation are mandatory in the associated methods. All others are passed as `**kwargs`. You can reference this for acceptable formats.


### Error Handling

This wrapper handles exceptions associated with incorrect datatypes of arguments passed to API get methods and will not perform an API request unless it passed validation. 

## Contributing

Contributions and constructive criticism are always welcome! Feel free to submit an issue or a pull request!
