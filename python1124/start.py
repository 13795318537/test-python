import select
import send

def print_test():
    p_test = select.select()
    p = p_test
    print('发工资后:',p,sep="\t")
    return p

if __name__ == '__main__':
    send.print_send()
    print_test()
    