import click
from forex_python.converter import CurrencyRates

from currency import Currency
from currency_type import CurrencyType

CURRENCY = CurrencyType()


@click.command()
@click.option('--amount', required=True, type=float,
              help='amount which we want to convert - float')
@click.option('--input_currency', type=CURRENCY, required=True,
              help='input currency - 3 letters name or currency symbol')
@click.option('--output_currency', type=CURRENCY, default=None,
              help='requested/output currency - 3 letters name or currency symbol')
def main(amount, input_currency: Currency, output_currency: Currency):
    output_rates = get_output_rates(amount, input_currency, output_currency)

    print_output_json(amount, input_currency, output_rates)


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


def print_output_json(amount, input_currency, output_rates):
    import json

    print(
        json.dumps(
            json.loads(
                json.dumps(
                    {
                        "input": {
                            "amount": amount,
                            "currency": input_currency.code
                        },
                        "output": output_rates
                    }
                ),
                parse_float=lambda x: round(float(x), 2)
            ),
            indent=4
        )
    )


if __name__ == '__main__':
    main()
