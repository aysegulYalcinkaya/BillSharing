import random

print("Enter the number of friends joining (including you):")
number_of_friends = int(input())

friends = {}
if number_of_friends < 1:
    print("No one is joining for the party")
else:
    print("Enter the name of every friend (including you), each on a new line:")
    for _i in range(number_of_friends):
        name = input()
        friends[name] = 0
    print("Enter the total bill value:")
    bill = float(input())
    
    print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    lucky = input()
    if lucky == "Yes":
        lucky_person = random.choice([friend for friend in friends.keys()])
        print("{} is the lucky one!".format(lucky_person))
        
        share = round((bill / (number_of_friends - 1)),2)
        friends = {friend:share for friend in friends}
        friends[lucky_person] = 0
    
    else:
        print("No one is going to be lucky")
        share = round((bill / number_of_friends),2)
        friends = {friend:share for friend in friends}
    print(friends)
