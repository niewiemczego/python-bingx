# Python-BingX

Python-bingx is a powerful and flexible Python package that allows you to easily interact with the BingX API. The package currently supports the Spot API, Standard API, Perpetual Swap API Reference V1, and Perpetual Swap API Reference V2. With python-bingx, you can retrieve real-time market data, manage your account, place trades, and more...

# Installation

To install python-bingx, you can use pip:

```python
pip install python-bingx
```

# Usage

There are multiple ways to use python-bingx, depending on your needs and preferences.

### Using BingX

The most straightforward way to use python-bingx is by importing the `BingX` class and initializing it with your API key and secret key:

```python
from bingX import BingX

bingx_client = BingX(api_key="api_key", secret_key="secret_key")
```

Once you have initialized the client, you can call any of the available APIs, for example:

```python
# Call the Trade API of Perpetual V2
bingx_client.perpetual_v2.trade.trade_order()
```

### Using PerpetualV2

If you prefer to work with a specific API or version, you can import the relevant class and initialize it with your API key and secret key:

```python
from bingX.perpetual.v2 import PerpetualV2

bingx_client = PerpetualV2(api_key="api_key", secret_key="secret_key")
```

Once you have initialized the client, you can call any of the available APIs, for example:

```python
# Call the Trade API of Perpetual V2
bingx_client.trade.trade_order()
```

# Handling Responses

Python-bingx uses requests library to communicate with the API and returns the response in JSON format. You can easily handle the response by accessing the relevant key(s) in the dictionary, for example:

```python
# Get the symbol and last price of BTC/USDT
response = bingx_client.perpetual_v2.market.get_ticker("BTC-USDT")
symbol = response["symbol"]
last_price = response["lastPrice"]
```

# Error Handling

In case of errors or exceptions, python-bingx will raise relevant exceptions with error message and error code. You can catch and handle the exceptions accordingly, for example:

```python
from bingX import ClientError, ServerError

try:
    response = bingx_client.perpetual_v2.trade.create_order()
except (ClientError, ServerError) as e:
    error_code = e.error_code
    error_message = e.error_message
```

# Contributing

Python-bingx welcomes contributions from the community! If you'd like to contribute, please fork the repository, create a feature branch, make your changes, and submit a pull request. Before submitting, please ensure that your code follows the PEP 8 style guide and includes appropriate tests.

# License

Python-bingx is licensed under the MIT License. See the LICENSE file for more information.
