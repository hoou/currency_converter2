## Description

This is simple currency converter using [forex-python](https://pypi.python.org/pypi/forex-python) package.

Converter can run as CLI application or web API application.

## Usage

### CLI
#### Using public repository from Docker Hub (Recommended)
```
$ docker run hoouhoou/currency-converter [--help] --amount AMOUNT --input_currency INPUT_CURRENCY
                          [--output_currency OUTPUT_CURRENCY]
```
- --amount - amount which we want to convert - float
- --input_currency - input currency - 3 letters name or currency symbol
- --output_currency - requested/output currency - 3 letters name or currency symbol

#### Building docker image yourself
```
$ git clone https://github.com/hoou/currency_converter2.git
$ cd currency_converter2
$ docker build -f Dockerfile-cli -t currency_converter .
$ docker run --name currency_converter currency_converter [--help] --amount AMOUNT --input_currency INPUT_CURRENCY
                          [--output_currency OUTPUT_CURRENCY]
```

### Web API
#### Via docker-compose (Recommended and the only way)
```
$ git clone https://github.com/hoou/currency_converter2.git
$ cd currency_converter2
$ docker-compose -f docker-compose-api.yml up --build -d
```


### Currency codes supported:
EUR, IDR, BGN, ILS, GBP, DKK, CAD, JPY, HUF, RON, MYR, SEK, SGD, HKD, AUD, CHF, KRW, CNY, TRY, HRK, NZD, THB, USD, NOK, RUB, INR, MXN, CZK, BRL, PLN, PHP, ZAR

### Currency symbols supported:
$, BGN, Fr., Ft, HK$, Kr, Kč, L, NZ$, R, R$, RM, Rp, S$, TRY, W, kn, kr, zł, £, ¥, ฿, ₪, €, ₱, ₹

## Examples
### CLI
Basic usage:
```
$ docker run hoouhoou/currency-converter --amount 100 --input_currency EUR --output_currency USD
{
    "input": {
        "amount": 100.0,
        "currency": "EUR"
    },
    "output": {
        "USD": 119.69
    }
}
```

Symbols support:
```
$ docker run hoouhoou/currency-converter --amount 50 --input_currency $ --output_currency EUR
{
    "input": {
        "amount": 50.0,
        "currency": "USD"
    },
    "output": {
        "EUR": 41.77
    }
}
```

No output currency specified (list all of them):

```
$ docker run hoouhoou/currency-converter --amount 66.64 --input_currency GBP
{
    "input": {
        "amount": 66.64,
        "currency": "GBP"
    },
    "output": {
        "AUD": 120.2,
        "BGN": 147.71,
        "BRL": 320.58,
        "CAD": 116.39,
        "CHF": 90.25,
        "CNY": 574.85,
        "CZK": 1926.1,
        "DKK": 562.61,
        "EUR": 75.52,
        "HKD": 709.58,
        "HRK": 559.19,
        "HUF": 23705.18,
        "IDR": 1263561.04,
        "ILS": 327.34,
        "INR": 6044.11,
        "ISK": 9228.97,
        "JPY": 9846.06,
        "KRW": 97301.06,
        "MXN": 1731.64,
        "MYR": 355.98,
        "NOK": 728.38,
        "NZD": 128.9,
        "PHP": 4671.06,
        "PLN": 321.31,
        "RON": 352.1,
        "RUB": 5700.85,
        "SEK": 798.48,
        "SGD": 120.55,
        "THB": 2870.58,
        "TRY": 384.9,
        "USD": 90.4,
        "ZAR": 1141.48
    }
}
```

### Web API
Basic usage:
```
GET /currency-converter?amount=100&input_currency=EUR&output_currency=USD HTTP/1.1
{
    "input": {
        "amount": 100.0,
        "currency": "EUR"
    },
    "output": {
        "USD": 119.69
    }
}
```

Symbols support:
```
GET /currency-converter?amount=50&input_currency=$&output_currency=EUR HTTP/1.1
{
    "input": {
        "amount": 50.0,
        "currency": "USD"
    },
    "output": {
        "EUR": 41.77
    }
}
```

No output currency specified (list all of them):

```
GET /currency-converter?amount=66.64&input_currency=GBP HTTP/1.1
{
    "input": {
        "amount": 66.64,
        "currency": "GBP"
    },
    "output": {
        "AUD": 120.2,
        "BGN": 147.71,
        "BRL": 320.58,
        "CAD": 116.39,
        "CHF": 90.25,
        "CNY": 574.85,
        "CZK": 1926.1,
        "DKK": 562.61,
        "EUR": 75.52,
        "HKD": 709.58,
        "HRK": 559.19,
        "HUF": 23705.18,
        "IDR": 1263561.04,
        "ILS": 327.34,
        "INR": 6044.11,
        "ISK": 9228.97,
        "JPY": 9846.06,
        "KRW": 97301.06,
        "MXN": 1731.64,
        "MYR": 355.98,
        "NOK": 728.38,
        "NZD": 128.9,
        "PHP": 4671.06,
        "PLN": 321.31,
        "RON": 352.1,
        "RUB": 5700.85,
        "SEK": 798.48,
        "SGD": 120.55,
        "THB": 2870.58,
        "TRY": 384.9,
        "USD": 90.4,
        "ZAR": 1141.48
    }
}
```

## Cache using Redis
Application is by default using redis server as cache. It can be turned off by setting ENV variable USE_CACHE to 0 in docker-compose-api.yml.

Rates stored in cache expire after 30 minutes.

## Contributors

Tibor Mikita

## License

MIT
