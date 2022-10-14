import os

key = os.environ.get('API_KEY_TRELLO')
token = os.environ.get('API_TOKEN_TRELLO')
user_id = os.environ.get('USER_ID_TRELLO')
board_id = os.environ.get('BOARD_ID_TRELLO')
list_id = os.environ.get('LIST_ID_TRELLO')
url = "https://api.trello.com/"

headers = {
   "Accept": "application/json"
}

query = {
   'key': key,
   'token': token
}
query_list = {
        'idBoard': "63446a765b4e5c00f5a24376",
        'key': key,
        'token': token
    }

print(key)
print(token)
print(board_id)
print(list_id)
print(user_id)
