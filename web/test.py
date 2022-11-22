import os 
import json
pylint = os.popen('pylint ./app').read()
os.system('bandit -r ./app/ -o bandit.json -f json')

with open('bandit.json', 'r') as f:
    b = json.load(f)

if b['results'] or pylint:
    raise RuntimeError('Ошибки')