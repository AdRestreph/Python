def exchange_money(budget:float, exchange_rate:float)->float:
    """
    :param budget: float - amount of money you are planning to exchange.
    :param exchange_rate: float - unit value of the foreign currency.
    :return: float - exchanged value of the foreign currency you can receive.
    """
    result = budget/exchange_rate
    return result

#print(exchange_money(127.5,1.2))

def get_change(budget:float, exchanging_value:float)->float:
    """
    :param budget: float - amount of money you own.
    :param exchanging_value: float - amount of your money you want to exchange now.
    :return: float - amount left of your starting currency after exchanging.
    """
    result = budget - exchanging_value
    return result

#print(get_change(127.5,120))

def get_value_of_bills(denomination:int, number_of_bills:int)->int:
    """
    :param denomination: int - the value of a bill.
    :param number_of_bills: int - total number of bills.
    :return: int - calculated value of the bills.
    """
    result = denomination * number_of_bills
    return int(result)

#print(get_value_of_bills(5,128))

def get_number_of_bills(amount:float, denomination:int)->int:
    """
    :param amount: float - the total starting value.
    :param denomination: int - the value of a single bill.
    :return: int - number of bills that can be obtained from the amount.
    """
    result = amount//denomination
    return int(result)

#print(get_number_of_bills(127.5,5))

def get_leftover_of_bills(amount:float, denomination:int)->float:
    """

    :param amount: float - the total starting value.
    :param denomination: int - the value of a single bill.
    :return: float - the amount that is "leftover", given the current denomination.
    """
    result = amount % denomination
    return result

#print(get_leftover_of_bills(127.5,20))

def exchangeable_value(budget:float, exchange_rate:float, spread:int, denomination:int)->int:
    """
    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int - maximum value you can get.
    """
    rate = exchange_rate *((spread/100))
    newexch = exchange_rate + rate
    change = budget/newexch
    bills = change % denomination
    result = change - bills
    return int(result)

#print(exchangeable_value(127.25, 1.20, 10, 20))