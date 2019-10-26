import json

import bricklink


auth = json.load(open('auth.json', 'r'))

client = bricklink.ApiClient(**auth)

print(client.catalog.getItem('MINIFIG', 'cty0859'))
