import random
from datetime import datetime
import os

def save_memory(name, money, last_login, loan_amount, loan_days):
    try:
        with open("player_data.txt", "w") as f:
            f.write(name + "\n")
            f.write(str(money) + "\n")
            f.write(last_login + "\n")
            f.write(str(loan_amount) + "\n")
            f.write(str(loan_days) + "\n")
    except PermissionError:
        print("\n⚠️  WARNING: Cannot save game data!")
        print("Please close 'player_data.txt' if it's open in another program.")
        print("Your progress will not be saved until the file is available.")
    except Exception as e:
        print(f"\n⚠️  Error saving game data: {e}")
        print("Your progress may not be saved.")

def read_player_data():
    try:
        with open("player_data.txt", "r") as f:
            lines = f.readlines()
            name = lines[0].strip()
            money = float(lines[1].strip())
            last_login = lines[2].strip()
            loan_amount = float(lines[3].strip())
            loan_days = int(lines[4].strip())
            return name, money, last_login, loan_amount, loan_days
    except:
        return None

def create_new_player():
    print("\n=== Welcome to the Casino Game! ===")
    name = input("Enter your name: ")
    money = 100.0
    today = datetime.now().strftime("%Y-%m-%d")
    loan_amount = 0.0
    loan_days = 0
    save_memory(name, money, today, loan_amount, loan_days)
    print(f"\nWelcome {name}! You start with ${money}")
    print("You earn $40,000 per year and can save $10 per day.")
    print("Bank gives 10% interest per day on positive balances!")
    return name, money, today, loan_amount, loan_days

def calculate_days_difference(last_date_str, current_date_str):
    last_date = datetime.strptime(last_date_str, "%Y-%m-%d")
    current_date = datetime.strptime(current_date_str, "%Y-%m-%d")
    return (current_date - last_date).days

def apply_daily_benefits(money, days_passed):
    if days_passed > 0:
        print(f"\n{'='*50}")
        print(f"{days_passed} day(s) have passed since your last login!")
        print(f"{'='*50}")
        
        salary = days_passed * 10
        print(f"💰 Daily savings: ${salary}")
        
        if money > 0:
            interest = money * 0.10 * days_passed
            print(f"🏦 Bank interest (10% per day): ${interest:.2f}")
            money = money + interest
        
        money = money + salary
        print(f"✅ Total money after benefits: ${money:.2f}")
        print(f"{'='*50}\n")
    
    return money

def check_loan_status(name, money, loan_amount, loan_days, last_login):
    if loan_amount > 0 and loan_days > 0:
        today = datetime.now().strftime("%Y-%m-%d")
        days_passed = calculate_days_difference(last_login, today)
        
        if days_passed > 0:
            # Calculate daily payment: $100 per day
            daily_payment = 100.0
            
            # Calculate total payment needed
            if days_passed <= loan_days:
                # Within loan period: pay $100 per day
                total_payment = days_passed * daily_payment
                # Don't pay more than the remaining loan
                total_payment = min(total_payment, loan_amount)
            else:
                # Past due date: full remaining loan is due
                total_payment = loan_amount
            
            print(f"\n{'='*60}")
            print(f"💳 LOAN PAYMENT - {days_passed} day(s) passed")
            print(f"{'='*60}")
            print(f"Amount due: ${total_payment:.2f}")
            
            if money >= total_payment:
                print(f"✅ Automatically paying ${total_payment:.2f}")
                money -= total_payment
                loan_amount -= total_payment
                loan_days -= days_passed
                
                # Ensure loan_days doesn't go negative
                if loan_days < 0:
                    loan_days = 0
                
                if loan_amount <= 0:
                    loan_amount = 0
                    loan_days = 0
                    print(f"🎉 Loan fully paid off!")
                else:
                    print(f"Remaining loan: ${loan_amount:.2f}")
                    if loan_days > 0:
                        print(f"Days remaining: {loan_days}")
                    else:
                        print(f"⚠️  Loan is overdue!")
                
                print(f"💰 New balance: ${money:.2f}")
                print(f"{'='*60}\n")
            else:
                # Can't pay the daily installment
                print(f"❌ BANKRUPTCY! You cannot pay ${total_payment:.2f}")
                print(f"Your balance is only ${money:.2f}")
                print(f"Remaining loan: ${loan_amount:.2f}")
                print("Game Over - You are bankrupt!")
                if os.path.exists("player_data.txt"):
                    os.remove("player_data.txt")
                exit()
    
    return money, loan_amount, loan_days

def casino(name, money, last_login, loan_amount, loan_days):
    print("\n" + "="*60)
    print("🎰 CASINO GAMES MENU 🎰")
    print("="*60)
    print("(Easiest to Hardest - Returns from 10% to 100%)")
    print("1. War (10% return)")
    print("2. Craps (20% return)")
    print("3. Sic Bo (30% return)")
    print("4. Blackjack (40% return)")
    print("5. Baccarat (50% return)")
    print("6. Roulette (60% return)")
    print("7. Wheel of Fortune (70% return)")
    print("8. Poker (80% return)")
    print("9. Slot Machine (90% return)")
    print("10. Keno (100% return)")
    print("11. Side Quest (Special Challenge)")
    print("="*60)
    
    choice = int(input("Enter choice (1-11): "))
    
    if choice == 11:
        money, loan_amount, loan_days = side_quest(name, money, last_login, loan_amount, loan_days)
        return money, loan_amount, loan_days
    
    bet = float(input(f"How much do you bet? (Balance: ${money:.2f}): $"))
    while bet > money or bet <= 0:
        print("❌ Invalid bet amount!")
        bet = float(input(f"How much do you bet? (Balance: ${money:.2f}): $"))
    
    if choice == 1:
        print("\n🎴 WAR")
        print("High card wins!")
        
        player_card = random.randint(2, 14)
        dealer_card = random.randint(2, 14)
        
        print(f"Your card: {player_card}")
        print(f"Dealer card: {dealer_card}")
        
        if player_card > dealer_card:
            print("✅ You win!")
            money += bet * 0.10
            print(f"Won: ${bet * 0.10:.2f}")
        elif player_card < dealer_card:
            print("❌ Dealer wins!")
            money -= bet
            print(f"Lost: ${bet:.2f}")
        else:
            print("🔄 War! Tie - no money lost")
        
    elif choice == 2:
        print("\n🎲 CRAPS")
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        total = dice1 + dice2
        
        print(f"Dice: {dice1} + {dice2} = {total}")
        
        if total in [7, 11]:
            print("✅ Natural! You win!")
            money += bet * 0.20
            print(f"Won: ${bet * 0.20:.2f}")
        elif total in [2, 3, 12]:
            print("❌ Craps! You lose!")
            money -= bet
            print(f"Lost: ${bet:.2f}")
        else:
            print(f"Point is {total} - No change")
        
    elif choice == 3:
        print("\n🎲 SIC BO")
        bet_choice = input("Bet on (small/big): ").lower()
        
        dice = [random.randint(1, 6) for _ in range(3)]
        total = sum(dice)
        
        print(f"Dice: {dice} = {total}")
        
        if (bet_choice == "small" and 4 <= total <= 10) or (bet_choice == "big" and 11 <= total <= 17):
            print("✅ You win!")
            money += bet * 0.30
            print(f"Won: ${bet * 0.30:.2f}")
        else:
            print("❌ You lose!")
            money -= bet
            print(f"Lost: ${bet:.2f}")
        
    elif choice == 4:
        print("\n🃏 BLACKJACK")
        player = [random.randint(1, 11), random.randint(1, 11)]
        dealer = [random.randint(1, 11), random.randint(1, 11)]
        
        print(f"Your cards: {player} = {sum(player)}")
        print(f"Dealer shows: {dealer[0]}")
        
        while sum(player) < 21:
            action = input("Hit or Stand? (h/s): ").lower()
            if action == 'h':
                player.append(random.randint(1, 11))
                print(f"Your cards: {player} = {sum(player)}")
            else:
                break
        
        while sum(dealer) < 17:
            dealer.append(random.randint(1, 11))
        
        p_val = sum(player)
        d_val = sum(dealer)
        
        print(f"Dealer cards: {dealer} = {d_val}")
        
        if p_val > 21:
            print("❌ Bust! You lose!")
            money -= bet
            print(f"Lost: ${bet:.2f}")
        elif d_val > 21 or p_val > d_val:
            print("✅ You win!")
            money += bet * 0.40
            print(f"Won: ${bet * 0.40:.2f}")
        elif p_val == d_val:
            print("🔄 Push! Tie")
        else:
            print("❌ Dealer wins!")
            money -= bet
            print(f"Lost: ${bet:.2f}")
        
    elif choice == 5:
        print("\n🎴 BACCARAT")
        bet_choice = input("Bet on (player/banker/tie): ").lower()
        
        player_hand = (random.randint(0, 9) + random.randint(0, 9)) % 10
        banker_hand = (random.randint(0, 9) + random.randint(0, 9)) % 10
        
        print(f"Player: {player_hand}, Banker: {banker_hand}")
        
        if player_hand > banker_hand:
            winner = "player"
        elif banker_hand > player_hand:
            winner = "banker"
        else:
            winner = "tie"
        
        print(f"Winner: {winner}")
        
        if bet_choice == winner:
            print("✅ You win!")
            money += bet * 0.50
            print(f"Won: ${bet * 0.50:.2f}")
        else:
            print("❌ You lose!")
            money -= bet
            print(f"Lost: ${bet:.2f}")
        
    elif choice == 6:
        print("\n🎡 ROULETTE")
        number = random.randint(0, 36)
        color = "green" if number == 0 else ("red" if number % 2 == 0 else "black")
        
        print(f"Roulette spins... {number} ({color})")
        bet_choice = input("Bet on (number/red/black/even/odd): ").lower()
        
        won = False
        if bet_choice == str(number):
            print("✅ Direct hit! You win!")
            money += bet * 0.60
            print(f"Won: ${bet * 0.60:.2f}")
            won = True
        elif bet_choice == color:
            print("✅ Color match!")
            money += bet * 0.60
            print(f"Won: ${bet * 0.60:.2f}")
            won = True
        elif (bet_choice == "even" and number % 2 == 0 and number != 0):
            print("✅ Even wins!")
            money += bet * 0.60
            print(f"Won: ${bet * 0.60:.2f}")
            won = True
        elif (bet_choice == "odd" and number % 2 == 1):
            print("✅ Odd wins!")
            money += bet * 0.60
            print(f"Won: ${bet * 0.60:.2f}")
            won = True
        
        if not won:
            print("❌ Lost!")
            money -= bet
            print(f"Lost: ${bet:.2f}")
        
    elif choice == 7:
        print("\n🎰 WHEEL OF FORTUNE")
        segments = [1, 5, 10, 20, 50, 0, 0, 0]
        result = random.choice(segments)
        
        print(f"Wheel spins... {result}!")
        
        if result == 0:
            print("❌ Bankrupt!")
            money -= bet
            print(f"Lost: ${bet:.2f}")
        else:
            print("✅ You win!")
            money += bet * 0.70
            print(f"Won: ${bet * 0.70:.2f}")
        
    elif choice == 8:
        print("\n🃏 POKER (5-Card Draw)")
        suits = ['♠', '♥', '♦', '♣']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        
        hand = [f"{random.choice(ranks)}{random.choice(suits)}" for _ in range(5)]
        print(f"Your hand: {', '.join(hand)}")
        
        rank_list = [card[:-1] for card in hand]
        unique_ranks = len(set(rank_list))
        
        if unique_ranks <= 3:
            print("✅ Good hand! You win!")
            money += bet * 0.80
            print(f"Won: ${bet * 0.80:.2f}")
        elif unique_ranks == 4:
            print("✅ One Pair!")
            money += bet * 0.80
            print(f"Won: ${bet * 0.80:.2f}")
        else:
            print("❌ High Card - No win")
            money -= bet
            print(f"Lost: ${bet:.2f}")
        
    elif choice == 9:
        print("\n🎰 SLOT MACHINE")
        symbols = ['🍒', '🍋', '🍊', '🍓', '💎', '7️⃣']
        reels = [random.choice(symbols) for _ in range(3)]
        print(f"Slots: {' | '.join(reels)}")
        
        if reels[0] == reels[1] == reels[2]:
            print("✅ JACKPOT! All three match!")
            money += bet * 0.90
            print(f"Won: ${bet * 0.90:.2f}")
        elif reels[0] == reels[1] or reels[1] == reels[2]:
            print("✅ Two match! Small win!")
            money += bet * 0.10
            print(f"Won: ${bet * 0.10:.2f}")
        else:
            print("❌ No match!")
            money -= bet
            print(f"Lost: ${bet:.2f}")
        
    elif choice == 10:
        print("\n🎱 KENO")
        print("Pick 5 numbers between 1-40")
        player_picks = []
        for i in range(5):
            num = int(input(f"Pick #{i+1}: "))
            while num < 1 or num > 40:
                print("❌ Invalid! Must be 1-40")
                num = int(input(f"Pick #{i+1}: "))
            player_picks.append(num)
        
        drawn = random.sample(range(1, 41), 20)
        matches = len(set(player_picks) & set(drawn))
        
        print(f"Drawn: {sorted(drawn)}")
        print(f"Your picks: {player_picks}")
        print(f"Matches: {matches}")
        
        if matches >= 2:
            print("✅ You win!")
            money += bet * 1.0
            print(f"Won: ${bet * 1.0:.2f}")
        else:
            print("❌ You lose!")
            money -= bet
            print(f"Lost: ${bet:.2f}")
    
    print(f"\n💰 Current balance: ${money:.2f}")
    save_memory(name, money, last_login, loan_amount, loan_days)
    return money, loan_amount, loan_days

def side_quest(name, money, last_login, loan_amount, loan_days):
    print("\n" + "="*60)
    print("🎯 CASINO SIDE QUEST - THE BIG CHALLENGE 🎯")
    print("="*60)
    print("The Casino Manager approaches you with a special deal...")
    print("\n📋 THE CHALLENGE:")
    print("Play 10 games and win at least 7 of them!")
    print("\n🎁 REWARDS:")
    print("✅ Win 7+ games: $1,000 loan with 0% interest!")
    print("❌ Win less than 7: $1,000 loan but casino takes $900,")
    print("   leaving you with $100 and full interest (20%)")
    
    accept = input("\nAccept the challenge? (yes/no): ").lower()
    if accept != "yes":
        print("Maybe next time!")
        return money, loan_amount, loan_days
    
    print("\n" + "="*60)
    print("Starting the challenge...")
    print("="*60)
    
    wins = 0
    games = ["War", "Craps", "Sic Bo", "Blackjack", "Baccarat", 
             "Roulette", "Wheel of Fortune", "Poker", "Slot Machine", "Keno"]
    
    for i in range(10):
        print(f"\n--- Game {i+1}/10: {games[i]} ---")
        input("Press Enter to play...")
        
        # Simple 50-50 chance for side quest
        if random.random() > 0.5:
            print("✅ You won this game!")
            wins += 1
        else:
            print("❌ You lost this game!")
        
        print(f"Current score: {wins} wins out of {i+1} games")
    
    print("\n" + "="*60)
    print(f"FINAL RESULT: {wins}/10 wins")
    print("="*60)
    
    if wins >= 7:
        print("\n🎉 CONGRATULATIONS! You won the challenge!")
        print("Casino gives you $1,000 loan with 0% interest!")
        money += 1000
        loan_amount += 1000
        loan_days += 15
        print("You have 15 days to pay it back!")
    else:
        print("\n😞 You didn't win enough games...")
        print("Casino takes $1,000 loan, keeps $900, gives you $100")
        print("You owe $1,200 (with 20% interest) in 15 days!")
        money += 100
        loan_amount += 1200
        loan_days += 15

    print(f"\n💰 New balance: ${money:.2f}")
    print(f"💳 Loan amount: ${loan_amount:.2f}")
    save_memory(name, money, last_login, loan_amount, loan_days)
    return money, loan_amount, loan_days

def bank(name, money, last_login, loan_amount, loan_days):
    print("\n" + "="*60)
    print("🏦 BANK - LOAN DEPARTMENT 🏦")
    print("="*60)
    print("Banker: 'Oh, you're the casino player!'")
    print("'We can't give you more than $1,000'")
    print("'Interest rate: 20%'")
    print("\n💳 LOAN PLANS:")
    print("1. $200 (pay $240 in 3 days)")
    print("2. $400 (pay $480 in 5 days)")
    print("3. $600 (pay $720 in 7 days)")
    print("4. $800 (pay $960 in 10 days)")
    print("5. $1000 (pay $1200 in 12 days)")
    print("="*60)
    
    if loan_amount > 0:
        print(f"\n⚠️  You already have a loan of ${loan_amount:.2f}!")
        print("Pay it off before taking another one.")
        return money, loan_amount, loan_days
    
    choice = int(input("Enter plan (1-5) or 0 to cancel: "))
    
    loan_plans = {
        1: (200, 240, 3),
        2: (400, 480, 5),
        3: (600, 720, 7),
        4: (800, 960, 10),
        5: (1000, 1200, 12)
    }
    
    if choice in loan_plans:
        amount, total, days = loan_plans[choice]
        money += amount
        loan_amount = total
        loan_days = days
        print(f"\n✅ Loan approved!")
        print(f"💰 You received: ${amount}")
        print(f"💳 You must pay: ${total} in {days} days")
        print(f"📅 Due date will be checked on next login")
        save_memory(name, money, last_login, loan_amount, loan_days)
    
    return money, loan_amount, loan_days

def main():
    print("="*60)
    print("💰 CASINO MILLIONAIRE SIMULATOR 💰")
    print("="*60)
    
    player_data = read_player_data()
    
    if player_data:
        name, money, last_login, loan_amount, loan_days = player_data
        today = datetime.now().strftime("%Y-%m-%d")
        
        print(f"\nWelcome back, {name}!")
        
        # Check loan status first
        money, loan_amount, loan_days = check_loan_status(name, money, loan_amount, loan_days, last_login)
        
        # Apply daily benefits
        days_passed = calculate_days_difference(last_login, today)
        money = apply_daily_benefits(money, days_passed)
        
        # Update last login
        last_login = today
        save_memory(name, money, last_login, loan_amount, loan_days)
    else:
        name, money, last_login, loan_amount, loan_days = create_new_player()
    
    print(f"\n💭 {name} thinks: 'I'm done with my $40k/year job!'")
    print("'I'll save $10 daily and become a millionaire at the casino!'")
    
    while True:
        # Check for bankruptcy
        if money < 0:
            print("\n" + "="*60)
            print("💔 YOU ARE BANKRUPT! 💔")
            print("="*60)
            print("You have negative money and cannot continue.")
            print("Starting side quest to earn some money...")
            money, loan_amount, loan_days = side_quest(name, money, last_login, loan_amount, loan_days)
            if money <= 0:
                print("\nStill broke... Game Over!")
                if os.path.exists("player_data.txt"):
                    os.remove("player_data.txt")
                break
            continue
        
        # Check if money is exactly zero
        if money == 0:
            print("\n" + "="*60)
            print("💸 YOU'RE BROKE! 💸")
            print("="*60)
            print("Starting side quest to earn some money...")
            money, loan_amount, loan_days = side_quest(name, money, last_login, loan_amount, loan_days)
            if money <= 0:
                print("\nGame Over!")
                if os.path.exists("player_data.txt"):
                    os.remove("player_data.txt")
                break
            continue
        
        print("\n" + "="*60)
        print(f"💰 Balance: ${money:.2f}")
        if loan_amount > 0:
            print(f"💳 Loan: ${loan_amount:.2f} (due in {loan_days} days)")
        print("="*60)
        print("\n📋 MAIN MENU:")
        print("1. 🎰 Go to Casino")
        print("2. 🏦 Go to Bank")
        print("3. 😴 Sleep (Quit)")
        print("="*60)
        
        try:
            choice = int(input("Enter choice (1-3): "))
            
            if choice == 1:
                money, loan_amount, loan_days = casino(name, money, last_login, loan_amount, loan_days)
            elif choice == 2:
                money, loan_amount, loan_days = bank(name, money, last_login, loan_amount, loan_days)
            elif choice == 3:
                print("\n😴 Going to sleep... See you tomorrow!")
                print(f"Remember: You save $10 per day and earn 10% bank interest!")
                save_memory(name, money, last_login, loan_amount, loan_days)
                break
            else:
                print("Invalid choice!")
        except ValueError:
            print("❌ Please enter a valid number!")
        except KeyboardInterrupt:
            print("\n\nGame interrupted!")
            save_memory(name, money, last_login, loan_amount, loan_days)
            break

if __name__ == "__main__":
    main()