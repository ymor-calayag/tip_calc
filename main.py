def main():
    print("\nTip Calculator")
    print("---------------")
    
    total_bill = float(input("What is your total bill? "))
    tip_percentage = float(input("How much tip would you like to give? "))
    people_splitting = int(input("How many people will split the bill? "))

    tip_conversion = tip_percentage / 100
    tip_amount = total_bill * tip_conversion
    bill_per_person = (total_bill + tip_amount) / people_splitting

    print("---------------")
    print(f"Each person should pay: {bill_per_person:.2f}\n")

if __name__ == "__main__":
    main()
