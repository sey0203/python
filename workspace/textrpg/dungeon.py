import time
import random

monsters = [
    {"이름":"머쉬맘", "체력":40, "공격력":20},
    {"이름":"골렘", "체력":60, "공격력":30},
    {"이름":"슬라임", "체력":40, "공격력":10}
]

def enter_dungeon(player):
    print("\n으스스한 기운이 느껴진다... 던전으로 이동 중...\n")
    time.sleep(1)
    print("\n=== 던전 입장 ===\n")
    time.sleep(1)

    monster = random.choice(monsters).copy()
    print(f"\n{monster['이름']}이(가) 등장했다!\n")
    time.sleep(1)


    battle(player, monster)

def battle(player, monster):
    while player['체력'] > 0 and monster['체력'] > 0:
        print(f"\n{player['이름']}이(가) {monster['이름']}을(를) 공격했다!\n")
        monster['체력'] -= player['공격력']
        print(f"{monster['이름']}의 체력: {max(monster['체력'], 0)}")

        if monster['체력'] <= 0:
            print(f"\n{monster['이름']}을(를) 처치했다!\n")
            break

        time.sleep(1)

        print(f"\n{monster['이름']}이(가) {player['이름']}을(를) 공격했다!\n")
        player['체력'] -= monster['공격력']
        print(f"현재 체력이 {max(player['체력'], 0)} 남았습니다.")
        

        if player['체력'] <= 0:
            print("\n전투에서 패배 하였습니다...\n")
            return
    
        time.sleep(1)

    print("\n...마을로 돌아갑니다...")
    time.sleep(2)