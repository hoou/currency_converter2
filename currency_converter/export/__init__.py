import json


def to_json(amount, input_currency, output_rates):
    return json.loads(
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
    )
