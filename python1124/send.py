from money import saved_money

def send(add_money):
    send_money = saved_money + add_money
    # print(send_money)
    return send

if __name__ == '__main__':
    send(1000)
    