
def readBook(img_url):
    import cv2
    import pytesseract
    print(pytesseract.get_languages(config=''))

    import urllib.request
    import numpy as np

    import time
    import json
    from requests.auth import HTTPBasicAuth
    import requests

    #img_url = 'https://images-na.ssl-images-amazon.com/images/I/41g6oM5YU-S._SY498_BO1,204,203,200_.jpg'
    book_name = ''
    book_desc = ''
    print('image url: {}'.format(img_url))
    try:
        req = urllib.request.urlopen(img_url)
        arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
        img = cv2.imdecode(arr, -1)

        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        text = pytesseract.image_to_string(img, lang = "eng")
        print(text)

        book_name = text.replace('\n', ' ')
        book_name = book_name.strip()
        print('Book name: {}'.format(book_name))

        encode_book_name = book_name.replace(' ', '%20')
        url = 'https://api.jp-tok.discovery.watson.cloud.ibm.com/instances/afe5a60f-8b7f-419e-b2b3-a0ed4191eb2b/v1/environments/c92683c6-0bde-48a9-9a19-19f3685b338f/collections/468fe5d1-f3ad-4487-bc41-b1957db56a7a/query?version=2018-12-03&query=enriched_text.entities.text:{}'.format(encode_book_name)
        print('Search url: {}'.format(url))
        headers = {"Accept": "application/json", "Content-Type": "application/json"}
        auth = HTTPBasicAuth('apikey', 'AIcTyGcJFnppMttzvYVMwtxy5rP_ZyAszM1a_bGdTdWC')

        response=requests.get(url, headers=headers, auth=auth)
        if response.ok:
            values = dict(response.json())
            print('WD search outpu: {}'.format(values['results'][0]['text']))
            book_desc = values['results'][0]['text']
        else:
            print('Error: Can not search the book from Watson Discovery')

    except:
        print('Error: Someing went wrong on either retrieving image or search book!')
    
    return book_name, book_desc
