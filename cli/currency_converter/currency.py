from collections import namedtuple

import click
from forex_python.converter import CurrencyCodes

# Dictionary for converting currency symbols to codes
CURRENCY_SYMBOL_DICT = {
    u"$": u"USD",
    u"BGN": u"BGN",
    u"Fr.": u"CHF",
    u"Ft": u"HUF",
    u"HK$": u"HKD",
    u"Kr": u"DKK",
    u"Kč": u"CZK",
    u"L": u"RON",
    u"NZ$": u"NZD",
    u"R": u"ZAR",
    u"R$": u"BRL",
    u"RM": u"MYR",
    u"Rp": u"IDR",
    u"S$": u"SGD",
    u"TRY": u"TRY",
    u"W": u"KRW",
    u"kn": u"HRK",
    u"kr": u"NOK",
    u"zł": u"PLN",
    u"£": u"GBP",
    u"¥": u"CNY",
    u"฿": u"THB",
    u"₪": u"ILS",
    u"€": u"EUR",
    u"₱": u"PHP",
    u"₹": u"INR"
}

Currency = namedtuple('Currency', ['code', 'symbol'])


class CurrencyType(click.ParamType):
    name = 'currency'

    def convert(self, value, param, ctx):
        currency_codes = CurrencyCodes()

        try:
            # First, think of input currency argument as symbol and try to find it in dictionary
            code = CURRENCY_SYMBOL_DICT[value]

            # When symbol found in dictionary, we already saved its code, so now just setup symbol member field
            symbol = value

        except KeyError:
            # When symbol not found in dictionary, input currency argument is rather code
            code = value

            # Now try to get its symbol
            symbol = currency_codes.get_symbol(code)
            if not symbol:
                # When it cannot find its symbol, it must be invalid
                self.fail(f'\'{value}\' is not valid currency name or symbol', param, ctx)

        return Currency(code, symbol)
