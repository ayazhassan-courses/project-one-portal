import requests as req
from bs4 import BeautifulSoup as bs
from lxml import html

credentials = {
    'eid': 'mt05491',
    'pw': 'MyDearUni3',
    'submit': 'Log In',
    'as_sfid': 'AAAAAAXRdeC7EXCWXHi-J4dpRI40KIqnkAPLqb-nooczj4n13U6HPMg5o1mgPD1ZIuFUka7PbPoRBBCfrInwHST45t24KU0rAFvaInVYx4-WHm9wTXijXc5hUEVbTU9VT9vNXmg=',
    'as_fid': '39056eeac91de7e8b2ba67a4c97b9f75c0e4c5bc'
}

login_url = "https://lms.habib.edu.pk/portal"

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'}

S = req.session()
result = S.get(login_url)

result = S.post(login_url, data = credentials, headers = headers)
data = bs(result.content, 'lxml')
# import pickle
print(data)
# pickle.dump(data, open('index.html', 'wb'))