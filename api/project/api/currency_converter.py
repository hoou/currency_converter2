from flask import current_app
from flask_restplus import Resource
from flask_restplus.reqparse import RequestParser

from project.api import api

ns = api.namespace('currency_converter')

currency_converter_parser: RequestParser = api.parser()
currency_converter_parser.add_argument('amount', required=True, type=float, location='args')
currency_converter_parser.add_argument('input_currency', required=True, location='args')
currency_converter_parser.add_argument('output_currency', location='args')


@ns.route('/')
@ns.expect(currency_converter_parser)
class CurrencyConverter(Resource):
    def get(self):
        args = currency_converter_parser.parse_args()

        amount = args['amount']
        input_currency = args['input_currency']
        output_currency = args['output_currency']

        current_app.logger.info(amount)
        current_app.logger.info(input_currency)
        current_app.logger.info(output_currency)
