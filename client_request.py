import freecurrencyapi

from config import KEY_FOR_OUTER_API
def request_for_currency():
    try:
        client = freecurrencyapi.Client(KEY_FOR_OUTER_API)
        return str(round(client.latest(currencies=['ILS'])["data"]['ILS'], 2))

    except:
        return "Redirect is failed!"


def perfom_convert():
    try:
        request_for_currency()
    except:
        return "Redirect is failed!"