
from time import sleep
from random import choice
import random


class Character:
    def __init__(self, name, hp, power):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.power = power

    def attack(self, other):
        damage = random.randint(self.power - 2, self.power + 2)
        other.hp = max(other.hp - damage, 0)
        print(f"{self.name}의 질문공격! {other.name}에게 {damage}의 데미지를 입혔습니다.")
        if other.hp == 0:
            print(f"{other.name}이(가) 더 이상 수업을 진행할 수 없습니다.")
        else:
            print(f"{other.name}이(가) 뇌에 과부하가 걸렸습니다..")


class Player(Character):
    def magic(self, other):
        print(f"{self.name}이(가) {other.name}에게 주말반납요청!")
        print(f"{other.name}에게 50만큼의 데미지!")
        other.hp = other.hp - 50
        if other.hp == 0:
            print(f"{other.name}이(가) 뇌에 과부하가 걸렸습니다..")
        else:
            print(f"{other.name}이(가) 더 이상 수업을 진행할 수 없습니다.")


class Monster(Character):
    def cure(self):
        self.hp = self.hp + 10
        print(f"{self.name}이(가) 체력을 10 회복했습니다!")

    def run(self):
        print(f"{self.name}이(가) 도망가다 잡혔습니다!")

        # @title

# 플레이어와 몬스터 스텟


def createobjects():
    Warrior = Player('매니저님', 100, 10)
    # 이름으로 해당 몬스터 인스턴스를 찾을 수 있도록, 딕셔너리 형태로 Monsters 를 묶어놓음
    Monsters = {}
    Monsters['교육생1'] = Monster('교육생1', 10, 10)
    Monsters['교육생2'] = Monster('교육생2', 20, 20)
    Monsters['교육생3'] = Monster('교육생3', 30, 30)
    return Warrior, Monsters


# 플레이어와 몬스터의 상태확인
def showinfo(self, other):
    print("\n--------------수업 시작---------------")
    print(f"{self.name}의 상태: HP {self.hp}/{self.max_hp}")
    for key, other in Monsters.items():
        print(f"{other.name}의 상태: HP {other.hp}")


def playerturn(Player, Monsters):
    print("\n--------------당신의 차례입니다--------------")

    command = input('교육하시겠습니까?(일반(개인과제)/마법(팀과제)) : ')
    target = input('누구에게 과제를 내시겠습니까?: ')
    if command == '일반':
        Player.attack(Monsters[target])
    elif command == '마법':
        Player.magic(Monsters[target])
    return Monsters


def check_mdead(Monsters):
    # 이번 턴에서 죽은 몬스터가 있는지 확인
    dead_monsters = []
    for key, value in Monsters.items():
        if value.hp <= 0:
            dead_monsters.append(key)
    # 죽은 몬스터는 몬스터 명단에서 삭제
    for i in dead_monsters:
        del Monsters[i]
    # 남은 몬스터가 없다면 승리 출력, 있다면 몬스터 그대로 리턴해주기
    if len(Monsters) <= 0:
        return Monsters, True
    else:
        return Monsters, False


def monsterturn(Player, Monsters):
    print("\n------------상대방의 차례입니다-----------")
    sleep(3)
    for key, value in Monsters.items():
        commands = ['cure', 'attack', 'run']
        command = choice(commands)
        if command == 'cure':
            value.cure()
        elif command == 'attack':
            value.attack(Player)
        elif command == 'run':
            value.run()
    return Player


def check_pdead(Player):
    if Player.hp <= 0:
        return True
    else:
        return False

    # @title
Warrior, Monsters = createobjects()

while True:
    showinfo(Warrior, Monsters)
    Monsters = playerturn(Warrior, Monsters)
    sleep(1)
    Monsters, ismdead = check_mdead(Monsters)
    if ismdead:
        print('\n승리!!!')
        break
    Warrior = monsterturn(Warrior, Monsters)
    ispdead = check_pdead(Warrior)
    if ispdead:
        print("\n패배!!!")
        break
    sleep(1)
