#! /usr/bin/env python3.6

import fire


def run(amount, input_currency, output_currency="ALL"):
    print(amount, input_currency, output_currency)


if __name__ == '__main__':
    fire.Fire(run)
