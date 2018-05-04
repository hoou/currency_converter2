import click

from currency import Currency


class CurrencyType(click.ParamType):
    name = 'currency'

    def convert(self, value, param, ctx):
        try:
            return Currency(value)
        except ValueError as e:
            self.fail(e, param, ctx)
