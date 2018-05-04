from forex_python.converter import CurrencyRates


def get_output_rates(amount, input_currency, output_currency):
    currency_rates = CurrencyRates()

    if output_currency:
        if input_currency == output_currency:
            converted_amount = amount
        else:
            converted_amount = currency_rates.convert(input_currency.code, output_currency.code, amount)
        output = {
            output_currency.code: converted_amount
        }
    else:
        latest_rates_for_input_currency = currency_rates.get_rates(input_currency.code)

        for code, value in latest_rates_for_input_currency.items():
            latest_rates_for_input_currency[code] = value * amount

        output = latest_rates_for_input_currency

    return output
