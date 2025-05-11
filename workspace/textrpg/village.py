import time
from dungeon import enter_dungeon

def enter_village(player):
    print("마을에 입장하였습니다.")

    while True:
        print("\n=== 마을 ===")
        print("1. 이장님과 대화")
        print("2. 던전으로 이동")
        print("3. 마을에서 나가기")

        choice = input("입력 :")

        if choice == "1":
            dialogue_village_chief()

        elif choice == "2":
            enter_dungeon(player) 

        elif choice == "3":
            print("마을을 떠납니다.")
            break

        else:
            print("올바른 숫자를 입력하세요.")


def dialogue_village_chief():
    print("이장님: 우리 마을에 온 것을 환영하네")
    time.sleep(1)
    print("이장님: 요즘 몬스터들이 기승을 부리는데 몬스터를 잡을 수 있는 사람이 적어서 고민이야")
    time.sleep(1)
    print("이장님: 자네가 몬스터들을 최대한 많이 잡아준다면 고맙겠어")
    time.sleep(1)
