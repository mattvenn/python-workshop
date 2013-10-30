#library for printing the time
import datetime

#global variables
balance = 0
return_price = 5
single_price = 3

#print the ticket
def printTicket(ticket_type,cost,travellers):
    #print date, ticket type, cost and num travellers
    print "date:",datetime.datetime.now()
    print "ticket:",ticket_type
    print "cost:",cost*travellers
    print "travellers:",travellers

#allow the user to top up
def topup():
    #we need to use the global balance variable
    global balance
    print "topup"
    extra_credit = input("how much extra credit?")
    #check it's not too much
    if balance + extra_credit > 30:
        print "too much credit"
        return
    else:
        #otherwise we can increase credit
        balance += extra_credit

#let's us buy all the ticket types
def buy(ticket_type):
    global balance
    print "ticket:", ticket_type
    travellers = input("how many travellers?")
    if travellers < 0:
        print "not enough travellers!"
        return

    if ticket_type == 'single':
        if balance < single_price*travellers:
            print "too little credit - top up!"
            return
        else:
            balance -=single_price*travellers
            printTicket(ticket_type,single_price,travellers)
            return
    if ticket_type == 'return':
        if balance < return_price*travellers:
            print "too little credit - top up!"
            return
        else:
            balance -=return_price*travellers
            printTicket(ticket_type,return_price,travellers)
            return

while True:
    print "you have credit:", balance
    print "codes:"
    print "1 top up"
    print "2 single"
    print "3 return"
    code = input("type code:")
    if code == 1:
        topup()
    elif code == 2:
        buy('single')
    elif code == 3:
        buy('return')
    else:
        print "invalid code"
