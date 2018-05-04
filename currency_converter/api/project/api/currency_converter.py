import os

from flask_restplus import Resource
from flask_restplus.reqparse import RequestParser

from converter import get_output_rates
from currency import Currency
from export import to_json
from project.business import get_cached_output_rates
from . import api

ns = api.namespace('currency_converter')

USE_CACHE = os.environ['USE_CACHE'] == "1"

currency_converter_parser: RequestParser = api.parser()
currency_converter_parser.add_argument('amount', required=True, type=float, location='args')
currency_converter_parser.add_argument('input_currency', required=True, type=Currency, location='args')
currency_converter_parser.add_argument('output_currency', type=Currency, location='args')


@ns.route('/')
@ns.expect(currency_converter_parser)
class CurrencyConverter(Resource):
    def get(self):
        args = currency_converter_parser.parse_args()

        if USE_CACHE:
            output_rates = get_cached_output_rates(**args)
        else:
            output_rates = get_output_rates(**args)

        return to_json(args['amount'], args['input_currency'], output_rates)
