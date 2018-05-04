import click

from converter import get_output_rates
from currency import Currency
from currency_type import CurrencyType
from export import to_json

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


def print_output_json(amount, input_currency, output_rates):
    import json

    print(
        json.dumps(
            to_json(amount, input_currency, output_rates),
            indent=4
        )
    )


if __name__ == '__main__':
    main()
