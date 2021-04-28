from file import *
from menu import *
from operate import *


info = []
while True:
    menu()
    num = input()
    if num == '1':
        add(info)
    elif num == '2':
        show(info)
    elif num == '3':
        delete(info)
    elif num == '4':
        update(info)
    elif num == '5':
        sort(info)
    elif num == '6':
        save(info)
    elif num == '7':
        read(info)
    elif num == 'quit':
        break

