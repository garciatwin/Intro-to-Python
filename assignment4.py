import random

def deal_card():
    #returns a random card from 1 to 10
    return random.randint(1,10)

def calculate_score(cards):
    #calculates the total value of a list of cards
    score = sum(cards)
    if 11 in cards and score > 21:
        cards.remove(11)
        cards.append(1)
        score = sum(cards)
    return score

def compare_scores(player_score, dealer_score):
    #compares the scores of the user and dealer and returns the winner
    if player_score == dealer_score:
        return "It's a tie!"
    elif dealer_score == 21:
        return "Dealer wins with a Blackjack!"
    elif player_score == 21:
        return "Player wins with a Blackjack!"
    elif player_score > 21:
        return "Player busts, dealer wins!"
    elif dealer_score > 21:
        return "Dealer busts, player wins!"
    elif player_score > dealer_score:
        return "Player wins!"
    else:
        return "Dealer wins!"

def play_game():
    #plays a game of blackjack
    print("Welcome to Blackjack!")

    player_cards = [deal_card(), deal_card()]
    dealer_cards = [deal_card(), deal_card()]

    player_score = calculate_score(player_cards)
    dealer_score = calculate_score(dealer_cards)

    print(f"Your cards: {player_cards}, current score: {player_score}")
    print(f"Dealer's first card: {dealer_cards[0]}")

    game_over = False
    while not game_over:
        player_choice = input("Do you want to hit or stay? Type 'hit' or 'stay': ").lower()
        if player_choice == 'hit':
            player_cards.append(deal_card())
            player_score = calculate_score(player_cards)
            print(f"Your cards: {player_cards}, current score: {player_score}")
            if player_score > 21:
                print("You went over 21. Dealer wins!")
                game_over = True
        else:
            game_over = True

    if not game_over:
        while dealer_score < 17:
            dealer_cards.append(deal_card())
            dealer_score = calculate_score(dealer_cards)
            print(f"Dealer's cards: {dealer_cards}, current score: {dealer_score}")
            if dealer_score > 21:
                print("Dealer went over 21. Player wins!")
                game_over = True

    if not game_over:
        print(compare_scores(player_score, dealer_score))

    play_again = input("Do you want to play again? Type 'y' or 'n': ").lower()
    if play_again == 'y':
        play_game()
    else:
        print("Thanks for playing!")
#call the function
play_game()




