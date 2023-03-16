# BingX-Client

BingX-Client is a Python package for interacting with the BingX API. It currently supports the Spot API, Standard API, Perpetual Swap API Reference V1, and Perpetual Swap API Reference V2.

# Installation

To install BingX-Client, you can use pip:

```python
pip install bingx-client
```

# Usage

I keep in mind that there are many different developers here, so I make 2 ways how you can use this package.

### Using BingXClient

To use the BingXClient class, simply import it and initialize it with your API key and secret key:

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

Alternatively, you can import the PerpetualV2 class from the appropriate subpackage and initialize it with your API key and secret key:

```python
from bingx_client.perpetual.v2 import PerpetualV2

client = PerpetualV2(api_key="api_key", secret_key="secret_key")
```

Once you have initialized the client, you can call any of the available APIs, for example:

```python
# Call the Trade API of Perpetual V2
client.trade.trade_order()
```

# Contributing

If you'd like to contribute to BingX-Client, feel free to submit a pull request! Please ensure that your code follows the PEP 8 style guide and includes appropriate tests.

# License

BingX-Client is licensed under the MIT License. See the LICENSE file for more information.
