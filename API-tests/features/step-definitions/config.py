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
   'key': 'APIKey',
   'token': 'APIToken'
}
query_list = {
        'idBoard': config.board_id,
        'key': config.key,
        'token': config.token
    }