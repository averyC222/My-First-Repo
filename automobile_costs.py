# Avery Mitchell
# Prog Assign_5 COSC 1010 500
#
# Automobile Costs
# Asks the user for monthly automobile expenses, then displays
# the total monthly cost and the total annual cost.

MONTHS_PER_YEAR = 12


def get_expense(name):
    """Prompt for one monthly expense and return it as a float.
    Re-prompts until the user enters a valid, non-negative number."""
    while True:
        try:
            amount = float(input(f"Enter the monthly cost for {name}: $"))
            if amount < 0:
                print("Please enter a non-negative amount.")
            else:
                return amount
        except ValueError:
            print("Invalid input. Please enter a number (e.g., 125.50).")


def calculate_totals(expenses):
    """Return the total monthly and total annual cost for a list of expenses."""
    monthly_total = sum(expenses)
    annual_total = monthly_total * MONTHS_PER_YEAR
    return monthly_total, annual_total


def main():
    print("Automobile Monthly Cost Calculator")
    print("-" * 36)

    loan = get_expense("loan payment")
    insurance = get_expense("insurance")
    gas = get_expense("gas")
    oil = get_expense("oil")
    tires = get_expense("tires")
    maintenance = get_expense("maintenance")

    monthly_total, annual_total = calculate_totals(
        [loan, insurance, gas, oil, tires, maintenance]
    )

    print("-" * 36)
    print(f"Total monthly cost: ${monthly_total:,.2f}")
    print(f"Total annual cost:  ${annual_total:,.2f}")


main()
