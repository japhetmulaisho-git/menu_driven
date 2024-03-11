#This application shows a menu for mobile money.
import os

def clear_screen():
    os.system('cls')

def display_menu():
    clear_screen()
    print("Welcome to Mobile Money Menu:")
    print("1. Send Money")
    print("2. Withdraw Cash")
    print("3. Pay Bill")
    print("4. Airtime & Bundles")
    print("5. MoMoPay")
    print("6. Kongola & Savings")
    print("7. Banking Services")
    print("8. PIN Reset")
    print("9. My Account")
    print("00. Next")

def get_user_choice():
    while True:
        try:
            choice = input("Please enter your choice: ")
            if choice in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "00"]:
                return choice
            else:
                print("Invalid choice. Please enter a valid option.")
        except KeyboardInterrupt:
            print("\nProgram terminated by user.")
            exit()
        except:
            print("An error occurred. Please try again.")

# Main program
if __name__ == "__main__":
    while True:
        display_menu()
        user_choice = get_user_choice()
        
        # Handling user choice
        if user_choice == "1":
            print("You selected: Send Money")
            input("Press Enter to go back to the main menu...")
        elif user_choice == "2":
            print("You selected: Withdraw Cash")
            input("Press Enter to go back to the main menu...")
        elif user_choice == "3":
            print("You selected: Pay Bill")
            input("Press Enter to go back to the main menu...")
        elif user_choice == "4":
            print("You selected: Airtime & Bundles")
            input("Press Enter to go back to the main menu...")
        elif user_choice == "5":
            print("You selected: MoMoPay")
            input("Press Enter to go back to the main menu...")
        elif user_choice == "6":
            print("You selected: Kongola & Savings")
            input("Press Enter to go back to the main menu...")
        elif user_choice == "7":
            print("You selected: Banking Services")
            input("Press Enter to go back to the main menu...")
        elif user_choice == "8":
            print("You selected: PIN Reset")
            input("Press Enter to go back to the main menu...")
        elif user_choice == "9":
            print("You selected: My Account")
            input("Press Enter to go back to the main menu...")
        elif user_choice == "00":
            print("You selected: Next")
            input("Press Enter to go back to the main menu...")
        else:
            print("Invalid choice. Please try again.")
