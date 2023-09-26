# mortgage_1.11.py

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0

extra_payment = 1000.0
extra_payment_start_month = 61
extra_payment_end_month = 108

previous_payment = 0.0  # Overpayment from previous month

while principal > 0:
    month = month + 1
    principal = principal * (1 + rate / 12) - payment
    total_paid = total_paid + payment + previous_payment

    if month >= extra_payment_start_month and month <= extra_payment_end_month:
        principal = principal - extra_payment
        total_paid = total_paid + extra_payment

    if principal < 0:  # Correction of overpayment from previous month
        previous_payment = principal
        principal = 0

    print(month, round(total_paid, 2), round(principal, 2))

print("Total paid", round(total_paid, 2))
print("Months", month)