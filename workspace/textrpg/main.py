from village import enter_village
import time

def game_start():
    print("게임을 시작합니다!")
    print("=== 직업 선택 ===")
    print("1. 궁수")
    print("2. 마법사")

    while True:
        choice = input("직업을 선택하세요 : ")

        if choice == "1":
            player = {"직업": "궁수", "체력": 80, "공격력": 20}
            break    

        elif choice == "2":
            player = {"직업": "마법사", "체력": 60, "공격력": 35}
            break

        else:
            print("올바른 숫자를 입력하세요.")

    # 직업 선택 후 이름 입력
    name = input("이름을 입력하세요 : ")
    player["이름"] = name

    return player


def main():
    while True:
        print("=== 텍스트 RPG ===")
        print("1. 게임 시작")
        print("2. 게임 종료")

        choice = input("입력 : ")

        if choice == "1":
            player = game_start()  # 플레이어 정보 생성
            print(f"당신은 {player['이름']}({player['직업']}) 를 선택하였습니다!")
            time.sleep(1)
            print("... 마을로 이동합니다 ...")
            time.sleep(1)

            enter_village(player)
            break  

        elif choice == "2":
            print("게임을 종료합니다.")
            break  # 게임 종료

        else:
            print("올바른 숫자를 입력하세요.")


if __name__ == "__main__":
    main()
