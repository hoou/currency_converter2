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


class Currency:
    def __init__(self, value):
        self.__check_format(value)

    def __check_format(self, value):
        from forex_python.converter import CurrencyCodes
        currency_codes = CurrencyCodes()

        try:
            # First, think of input currency argument as symbol and try to find it in dictionary
            self.code = CURRENCY_SYMBOL_DICT[value]

            # When symbol found in dictionary, we already saved its code, so now just setup symbol member field
            self.symbol = value

        except KeyError:
            # When symbol not found in dictionary, input currency argument is rather code
            self.code = value

            # Now try to get its symbol
            self.symbol = currency_codes.get_symbol(self.code)
            if not self.symbol:
                # When it cannot find its symbol, it must be invalid
                raise ValueError(f'\'{value}\' is not valid currency name or symbol')

    def __eq__(self, other):
        return self.code == other.code
