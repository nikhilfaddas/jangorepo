import requests
from onlinestore.ConsumerInfo import Books


BASE_URI = 'http://localhost:8000/v1/book/'
value = 'Token eb7e18067fbd98f6316720e47d47c9be8a9de817'

'''
body_val = {
    "name": "captainAmerica-2",
    "author": "marvel",
    "price": 700,
    "qty": 3,
    "publication": "foxstar",
    "reviews": "superb in scifi action"
}
response = requests.get(BASE_URI+str(2),headers={'Authorization':value},json=body_val)
print(response.status_code)
print(response.json())
'''

def process_json_to_book(bookJson):
    libraries = []
    if type(bookJson)==list:
        for bk in bookJson:
             library = Books(bid=bk['id'],
                  bname=bk['name'],
                  bauth=bk['author'],
                  bprice=bk['price'],
                  bqty=bk['qty'],
                  bpub=bk['publication'],
                  brev=bk['reviews'])
             libraries.append(library)
        return libraries
    else:
        bk=bookJson
        library = Books(bid=bk['id'],
                        bname=bk['name'],
                        bauth=bk['author'],
                        bprice=bk['price'],
                        bqty=bk['qty'],
                        bpub=bk['publication'],
                        brev=bk['reviews'])
        return library


def get_books():
    response = requests.get(BASE_URI,headers={'Authorization':value})           #request.get-- fetch data from producer in json format
    if type(response.json())==list:
        return process_json_to_book(response.json()) #many
    else:
        return response.json()

def get_single_book(bid):
    response = requests.get(BASE_URI+str(bid),headers={'Authorization':value})
    #print(response.json().keys())
    # if "status" not in response.json().keys():
    #     return process_json_to_book(response.json()) #many
    # else:
    return response.json()

def delete_books(bid):
    response = requests.delete(BASE_URI+str(bid),headers={'Authorization':value})
    return response.json()

def update_books(bid,library):
    response = requests.put(BASE_URI+str(bid),headers={'Authorization':value},json=library.__dict__)
    #print(response.json())
    return response.json()

def add_books(library):
    # print(library.__dict__)
    library.__dict__.pop('id')
    # print(library.__dict__)ib
    response = requests.post(BASE_URI,headers={'Authorization':value},json=library.__dict__)  # requests.post--python into jason and send json format to producer to save
    # print(response.status_code)
    # print(response.json())
    return response.json()

if __name__ == '__main__':
    # lib = Books(bid=111, bname='shiv-tandav', bauth='nana', bprice=1000, bqty=1, bpub='pouranik', brev='informatics')
    # add_books(lib)
    # print(get_books())
    # print(get_single_book(24))
    delete_books(12)
    # update_books(24,lib)