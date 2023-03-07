from InstagramAPI import InstagramAPI

username = 'Your Instagram Username'
password = 'Your Instagram Password'

api = InstagramAPI(username, password)
api.login()

user_id = input('Enter User ID: ')

api.searchUsername(user_id)
result = api.LastJson

if 'user' in result:
    user = result['user']
    print('User ID:', user['pk'])
    print('Description:', user['biography'])
else:
    print('User not found')
