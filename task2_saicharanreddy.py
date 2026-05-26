# Smart Bill Splitter
total_bill = float(input("Enter total bill amount: "))
people = int(input("Enter number of people: "))
tip_percentage = float(input("Enter tip percentage: "))

if people > 0:

    tip_amount = (total_bill * tip_percentage) / 100

    total_with_tip = total_bill + tip_amount

    amount_per_person = total_with_tip / people

    remaining_value = total_with_tip % people

    print("\n===== BILL SUMMARY =====")
    print(f"Original Bill      : ₹{round(total_bill, 2)}")
    print(f"Tip Amount         : ₹{round(tip_amount, 2)}")
    print(f"Total With Tip     : ₹{round(total_with_tip, 2)}")
    print(f"Amount Per Person  : ₹{round(amount_per_person, 2)}")
    print(f"Remaining Value    : {round(remaining_value, 2)}")
    print("========================")

else:
    print("Number of people must be greater than 0.")
