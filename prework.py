def hello_name(User_name):
    """ User Name """
    usr_name = User_name
    return usr_name

def first_odds():
    """ Odds From 1-100 """
    nw_num= [x + 1 for x in range(100) if x % 2 == 0] 
    print(nw_num)  

def max_num_in_list(a_list):
    """ Max Number in List """
    A_list = a_list
    return A_list

def is_leap_year(a_year):
    """ Checking Leap Year """
    year = a_year
    return year

def is_consecutive(a_list):
    """ Checking If List Is Consecutive """
    nu_list = a_list
    return nu_list

    
    



while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")
 
    us_name = input('type username: ')
    if us_name == "q":
        break

    usr_name = hello_name(us_name)
    print('\nAnswer 1:\nhello ' + usr_name + '!\n')

    print('\nAnswer 2:')
    odds = first_odds()

    print('\nAnswer 3:')
    numb = [1, 2, 3, 4, 5]
    numb.sort
    A_list = (numb[-1]) 
    print(A_list)

    print('\nAnswer 4:\n')
    leap_years = list(range(0,4000,4))
    input_year = input('\nPlease enter a year from 0 - 4000: ')
    if int(input_year) in leap_years:
        print(True)
    else:
        print(False)
    
    print('\nAnswer 5:\n')
    l = [1, 2, 3, 4, 5]
    print(sorted(l) == list(range(min(l), max(l)+1)))

    


