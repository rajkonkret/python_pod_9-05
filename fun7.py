# argumenty słownikowe
def connect(**opcje):
    print(opcje)
    connect_param = {
        'host': '127.0.0.7',
        'port': '8080'
    }
    print(connect_param)
    connect_param['pwd'] = opcje
    print(connect_param)
    connect_param.update({'pwd': opcje})
    print(connect_param)


connect(a=7)
connect(user='/home')
connect(userr='/home', root='/', port='9090')
