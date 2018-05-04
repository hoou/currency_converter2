from flask import current_app
from forex_python.converter import CurrencyRates

from currency import Currency
from project.redis import redis

currency_rates = CurrencyRates()


def get_cached_output_rates(amount, input_currency: Currency, output_currency: Currency):
    if output_currency:
        rate = redis.hget(input_currency.code, output_currency.code)

        if rate:
            current_app.logger.info("from cache")
            rate = float(rate)
        else:
            rate = currency_rates.get_rate(input_currency.code, output_currency.code)
            redis.hset(input_currency.code, output_currency.code, rate)

        return {
            output_currency.code: rate * amount
        }

    else:
        latest_rates_for_input_currency = currency_rates.get_rates(input_currency.code)

        for code, rate in latest_rates_for_input_currency.items():
            redis.hset(input_currency.code, code, rate)
            latest_rates_for_input_currency[code] = rate * amount

        return latest_rates_for_input_currency
