def is_valid(username, password):
    if username == 'admin' or (username == 'user' and password == 'qweasd'):
        return True
    else: 
        return False