from proccessor import clean_id
def test_clean_id():
    assert clean_id("cc-1.055.754.628")=="1055754628"

def merge_name():
    assert merge_name("Mariana","Villegas")=="Mariana Villegas"
    