#나정호_블랙잭 게임 풀이
import random

def play_blackjack():
    suits = ['spades', 'hearts', 'diamonds', 'clubs']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    # 덱 만들고 섞기
    deck = [{suit: rank} for suit in suits for rank in ranks]
    random.shuffle(deck)

    # 카드 분배
    dealer = [deck.pop(0), deck.pop(0)]
    player = [deck.pop(0), deck.pop(0)]

    # 점수 계산 함수
    def getScore(hand):
        score = 0
        ace = 0
        for card in hand:
            rank = list(card.values())[0]
            if rank in ['J', 'Q', 'K']:
                score += 10
            elif rank == 'A':
                score += 11
                ace += 1
            else:
                score += int(rank)
        while score > 21 and ace:
            score -= 10
            ace -= 1
        return score

    # 카드 보여주는 함수
    def showCards(name, hand):
        print(f"{name} 카드:")
        for card in hand:
            print(f"  {list(card.values())[0]} of {list(card.keys())[0]}")
        print(f"총점: {getScore(hand)}\n")

    # 플레이어 턴
    while True:
        showCards("플레이어", player)
        if getScore(player) >= 21:
            break
        choice = input("Hit 하시겠습니까? (y/n): ")
        if choice == 'y':
            player.append(deck.pop(0))
        else:
            break

    # 딜러 턴
    while getScore(dealer) < 17:
        dealer.append(deck.pop(0))

    # 결과 출력
    showCards("플레이어", player)
    showCards("딜러", dealer)

    player_score = getScore(player)
    dealer_score = getScore(dealer)

    # 승패 판단
    if player_score > 21:
        print("플레이어 Bust! 딜러 승리!\n")
    elif dealer_score > 21:
        print("딜러 Bust! 플레이어 승리!\n")
    elif player_score > dealer_score:
        print("플레이어 승리!\n")
    elif player_score < dealer_score:
        print("딜러 승리!\n")
    else:
        print("무승부!\n")

#게임 시작
print("==== 블랙잭 게임 시작 ====")
play_blackjack()