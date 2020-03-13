def computepay(hours, rate) :

    if hours > 40:
        reg = rate * hours
        otp = (hours - 40) * (rate * 0.5)
        pay = reg + otp
    else:
        pay = hours * rate

    return pay
hours = float(input("Enter hours:"))
rate = float(input("Enter Rate:"))

pay = computepay(hours, rate)

print("Pay:", pay)
