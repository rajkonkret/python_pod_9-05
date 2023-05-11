# argumenty słownikowe
def connect(**opcje):
    print(opcje)
    connect_param = {
        'host': '127.0.0.7',
        'port': '8080'
    }
    print(connect_param)
    # dodajemy klucz 'pwd' i nadajemy wartość {'a': 7}
    connect_param['pwd'] = opcje
    # {'host': '127.0.0.7', 'port': '8080', 'pwd': {'a': 7}}
    print(connect_param)
    # drugi sposób dodawania klucza i wartości do słownika
    connect_param.update({'pwd': opcje})
    # {'host': '127.0.0.7', 'port': '8080', 'pwd': {'a': 7}}
    # 'pwd': {'userr': '/home', 'root': '/', 'port': '9090'}}
    print(connect_param)


connect(a=7)
connect(user='/home')
# {'userr': '/home', 'root': '/', 'port': '9090'}
connect(userr='/home', root='/', port='9090')
# 8:30
