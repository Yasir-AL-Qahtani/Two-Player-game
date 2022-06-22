import random

user1 = {
    "name": input("whats ur name Fighter: "), "hp": 100, "defence": 0.2
}
user2 = {
    "name": input("whats ur name Fighter: "), "hp": 100, "defence": 0.2
}


def move(attacker, defender):

    while True:
        usermove = input(f"whats your move {attacker['name']} (kick or punch or defend): ")
        if not (usermove=="defend" and attacker["defence"]==0.5):
            break
        print("okay ur defend lvl max ")

    if usermove == "kick":
        if random.random() > defender["defence"]:
            damge = random.randint(20, 35)
            defender["hp"] = defender["hp"] - damge
            if defender["hp"] <0:
                defender['hp']=0

            print(f"WOW NICE KICK {attacker['name']} the damge is {damge}"
                  f" and the {defender['name']} hp is {defender['hp']}")
        else:
            print("lol noob")



    elif usermove == "punch":
        damge = random.randint(1, 20)
        defender["hp"] = defender["hp"] - damge
        if defender["hp"] < 0:
            defender['hp'] = 0
        print(f"WOW NICE PUCNCH {attacker['name']} the damge is {damge} and the {defender['name']} hp is {defender['hp']}")


    else:
        attacker["defence"] = attacker["defence"] + 0.1
        print("denfend upgrade")


    return defender["hp"] ==0

List=[user1,user2]
turn=random.randint(0,1)
while True:
    if move(List[turn],List[(turn+1)%2]):
        print(f"GG You won {List[turn]['name']}")
        break
    turn=(turn+1)%2









