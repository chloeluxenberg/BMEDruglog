from uuid import uuid4


def create_user(data):
    name = input('Enter new user name: ').strip()
    if not name:
        print('Name cannot be empty.')
        return
    user_id = uuid4().hex[:8]
    data['users'][user_id] = {'name': name, 'medications': []}
    print(f'Created {name} (ID: {user_id})')


def select_user(data):
    if not data['users']:
        print('No users yet. Create one first.')
        return None
    for user_id, user in data['users'].items():
        print(f'{user_id}: {user["name"]}')
    user_id = input('Enter user ID: ').strip()
    if user_id not in data['users']:
        print('User not found.')
        return None
    return user_id
