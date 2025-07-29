# Bitcoin Price Index 📈

Bitcoin is a form of digital currency, otherwise known as cryptocurrency. Rather than rely on a central authority like a bank, Bitcoin instead relies on a distributed network, otherwise known as a blockchain, to record transactions.

Because there’s demand for Bitcoin (i.e., users want it), users are willing to buy it, as by exchanging one currency (e.g., USD) for Bitcoin.

In a file called `bitcoin.py`, implement a program that:

- Expects the user to specify as a command-line argument the number of Bitcoins, $n$, that they would like to buy. If that argument cannot be converted to a `float`, the program should exit via `sys.exit` with an error message.

- Queries the API for the CoinCap Bitcoin Price Index at https://rest.coincap.io/v3/assets/bitcoin?apiKey=`YourApiKey`. You should replace `YourApiKey` with the actual API key you obtained from your CoinCap account dashboard, which returns a JSON object, among whose nested keys is the current price of Bitcoin as a `float`. Be sure to catch any [exceptions](https://requests.readthedocs.io/en/latest/api/#exceptions), as with code like:

```python
import requests

try:
    ...
except requests.RequestException:
    ...
```

- Outputs the current cost of $n$ Bitcoins in USD to four decimal places, using `,` as a thousands separator.
