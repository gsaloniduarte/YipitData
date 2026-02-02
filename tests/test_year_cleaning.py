from src.cleaning.year import clean_year

def test_year_extraction():
    assert clean_year("Released in 1999") == 1999
    assert clean_year("October\u00a08,\u00a01968 ( 1968-10-08 )") ==  1968
