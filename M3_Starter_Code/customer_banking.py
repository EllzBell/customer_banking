# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
from cd_account import create_cd_account
from savings_account import create_savings_account

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE
    # Force the user to only input digits as the input 
    savings_balance = input("What is the balance for the new savings account? ")
    while not(savings_balance.isdigit()):
        savings_balance = input("Please enter only numerical values ")
    savings_balance = float(savings_balance)
        
    savings_interest = input("What is the interest rate in percentage for the new savings account? ")
    while not(savings_interest.isdigit()):
        savings_interest = input("Please enter only numerical values ")
    savings_interest = float(savings_interest)

    savings_maturity = input("What is the length of months for the savings account? ")
    while not(savings_maturity.isdigit()):
        savings_maturity = input("Please enter only numerical values ")
    savings_maturity = int(savings_balance)

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_savings_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f"The interest earned from the savings account is: {interest_savings_earned}.\nThe updated balance is: {updated_savings_balance}.")

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE
    # Similarly force the user to only input digits
    cd_balance = input("What is the balance for the new CD account? ")
    while not(cd_balance.isdigit()):
        cd_balance = input("Please enter only numerical values ")
    cd_balance = float(cd_balance)
        
    cd_interest = input("What is the interest rate in percentage for the new CD account? ")
    while not(cd_interest.isdigit()):
        cd_interest = input("Please enter only numerical values ")
    cd_interest = float(cd_interest)

    cd_maturity = input("What is the length of months for the CD account? ")
    while not(cd_maturity.isdigit()):
        cd_maturity = input("Please enter only numerical values ")
    cd_maturity = int(cd_balance)

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_cd_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f"The interest earned from the CD account is: {interest_cd_earned}.\nThe updated balance is: {updated_cd_balance}.")
if __name__ == "__main__":
    # Call the main function.
    main()