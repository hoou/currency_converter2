from flask_api import status


def test_get(client):
    r = client.get('/currency_converter/?amount=100&input_currency=EUR&output_currency=CZK')
    payload = r.json

    assert r.status_code == status.HTTP_200_OK
    assert payload['input']['amount'] == 100
    assert payload['input']['currency'] == 'EUR'
    assert len(payload['output']) == 1
    assert payload['output']['CZK']


def test_get_lowercase(client):
    r = client.get('/currency_converter/?amount=100&input_currency=eur&output_currency=czk')
    payload = r.json

    assert r.status_code == status.HTTP_200_OK
    assert payload['input']['amount'] == 100
    assert payload['input']['currency'] == 'EUR'
    assert len(payload['output']) == 1
    assert payload['output']['CZK']


def test_get_input_symbol(client):
    r = client.get('/currency_converter/?amount=0.9&input_currency=¥&output_currency=AUD')
    payload = r.json

    assert r.status_code == status.HTTP_200_OK
    assert payload['input']['amount'] == 0.9
    assert payload['input']['currency'] == 'CNY'
    assert len(payload['output']) == 1
    assert payload['output']['AUD']


def test_get_no_output(client):
    r = client.get('/currency_converter/?amount=10.92&input_currency=£')
    payload = r.json

    assert r.status_code == status.HTTP_200_OK
    assert payload['input']['amount'] == 10.92
    assert payload['input']['currency'] == 'GBP'
    assert len(payload['output']) > 1


def test_get_missing_amount(client):
    r = client.get('/currency_converter/?input_currency=EUR&output_currency=CZK')
    payload = r.json

    assert r.status_code == status.HTTP_400_BAD_REQUEST
    assert payload['errors']['amount'] == 'Missing required parameter in the query string'
    assert payload['message'] == 'Input payload validation failed'


def test_get_missing_input(client):
    r = client.get('/currency_converter/?amount=100&output_currency=CZK')
    payload = r.json

    assert r.status_code == status.HTTP_400_BAD_REQUEST
    assert payload['errors']['input_currency'] == 'Missing required parameter in the query string'
    assert payload['message'] == 'Input payload validation failed'


def test_get_invalid_input(client):
    r = client.get('/currency_converter/?amount=100&input_currency=blabla&output_currency=CZK')
    payload = r.json

    assert r.status_code == status.HTTP_400_BAD_REQUEST
    assert 'is not valid currency name or symbol' in payload['errors']['input_currency']
    assert payload['message'] == 'Input payload validation failed'


def test_get_invalid_output(client):
    r = client.get('/currency_converter/?amount=100&input_currency=EUR&output_currency=blabla')
    payload = r.json

    assert r.status_code == status.HTTP_400_BAD_REQUEST
    assert 'is not valid currency name or symbol' in payload['errors']['output_currency']
    assert payload['message'] == 'Input payload validation failed'
