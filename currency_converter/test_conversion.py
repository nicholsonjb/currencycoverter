from currency_converter import convert_currency

def test_convert_currency():
    assert convert_currency(1, "USD", "EUR") == 0.85
    assert convert_currency(10, "JPY", "USD") == 0.09
    assert convert_currency(100, "GBP", "EUR") == 117.28
    assert convert_currency(1000, "KRW", "JPY") == 7.78
