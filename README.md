# BingX-Client

BingX-Client is a powerful and flexible Python package that allows you to easily interact with the BingX API. The package currently supports the Spot API, Standard API, Perpetual Swap API Reference V1, and Perpetual Swap API Reference V2. With BingX-Client, you can retrieve real-time market data, manage your account, place trades, and more...

# Installation

To install BingX-Client, you can use pip:

```python
pip install bingx-client
```

# Usage

There are multiple ways to use BingX-Client, depending on your needs and preferences.

### Using BingXClient

The most straightforward way to use BingX-Client is by importing the `BingXClient` class and initializing it with your API key and secret key:

```python
from bingx_client import BingXClient

client = BingXClient(api_key="api_key", secret_key="secret_key")
```

Once you have initialized the client, you can call any of the available APIs, for example:

```python
# Call the Trade API of Perpetual V2
client.perpetual_v2.trade.trade_order()
```

### Using PerpetualV2

If you prefer to work with a specific API or version, you can import the relevant class and initialize it with your API key and secret key:

```python
from bingx_client.perpetual.v2 import PerpetualV2

client = PerpetualV2(api_key="api_key", secret_key="secret_key")
```

Once you have initialized the client, you can call any of the available APIs, for example:

```python
# Call the Trade API of Perpetual V2
client.trade.trade_order()
```

# Handling Responses

BingX-Client uses requests library to communicate with the API and returns the response in JSON format. You can easily handle the response by accessing the relevant key(s) in the dictionary, for example:

```python
# Get the symbol and last price of BTC/USDT
response = client.perpetual_v2.market.get_ticker("BTC-USDT")
symbol = response["symbol"]
last_price = response["lastPrice"]
```

# Error Handling

In case of errors or exceptions, BingX-Client will raise relevant exceptions with error message and error code. You can catch and handle the exceptions accordingly, for example:

```python
from bingx_client._exceptions import ClientError, ServerError

try:
    response = client.perpetual_v2.trade.create_order()
except (ClientError, ServerError) as e:
    error_code = e.error_code
    error_message = e.error_message
```

# Contributing

BingX-Client welcomes contributions from the community! If you'd like to contribute, please fork the repository, create a feature branch, make your changes, and submit a pull request. Before submitting, please ensure that your code follows the PEP 8 style guide and includes appropriate tests.

# License

BingX-Client is licensed under the MIT License. See the LICENSE file for more information.
