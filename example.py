from pyson import Pyson


db = Pyson(__name__, True)


db.createlist('users')

db.lset('users', 'sarah')

if not db.lismember('users', 'sarah'):
    print('You have to create a new account.')
else:
    print('Logging in...')