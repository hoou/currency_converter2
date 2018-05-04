import click
from currency import CurrencyType, Currency

CURRENCY = CurrencyType()


@click.command()
@click.option('--amount', required=True, type=float,
              help='amount which we want to convert - float')
@click.option('--input_currency', type=CURRENCY, required=True,
              help='input currency - 3 letters name or currency symbol')
@click.option('--output_currency', type=CURRENCY, default=None,
              help='requested/output currency - 3 letters name or currency symbol')
def main(amount, input_currency: Currency, output_currency: Currency):
    print(amount, input_currency, output_currency)


if __name__ == '__main__':
    main()
