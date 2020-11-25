from money import saved_money

def send(add_money):
    send_money = saved_money + add_money
    sm = send_money
    return sm

def print_send():
    print(f'发工资前:\t{saved_money}')


if __name__ == '__main__':
    print_send()
    send(1000)
    