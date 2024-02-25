import decimal

def binary_split(a, b):
    if b == a + 1:
        Pab = -(6*a - 5)*(2*a - 1) * (6*a - 1)
        Qab = 10939058860032000 * a**3
        Rab = Pab * (545140134*a + 13591409)
    else:
        m = (a + b) // 2
        Pam, Qam, Ram = binary_split(a, m)
        Pmb, Qmb, Rmb = binary_split(m, b)
        Pab = Pam * Pmb
        Qab = Qam * Qmb
        Rab = Qmb * Ram + Pam * Rmb
    return Pab, Qab, Rab

def chudnovsky(n):
    P1n, Q1n, R1n = binary_split(1, n)
    return (426880 * decimal.Decimal(10005).sqrt() * Q1n) / (13591409*Q1n + R1n)


# Set the precision you want. Just uncomment number of Pi that you want :)

# decimal.getcontext().prec = 10         # Ten digits  
# decimal.getcontext().prec = 100        # One hundred digits
# decimal.getcontext().prec = 1000       # One thousand digits
# decimal.getcontext().prec = 10000      # Ten thousand digits
# decimal.getcontext().prec = 100000     # One hundred thousand digits.
# decimal.getcontext().prec = 1000000    # One million digits. Takes like 12 seconds.
# decimal.getcontext().prec = 2000000    # Two million digits. Takes like 28 seconds.
# decimal.getcontext().prec = 2500000    # Two million five hundred thousand digits. Takes like 40 seconds.
# decimal.getcontext().prec = 2600000    # Two million six hundred thousand digits. Takes like 42 seconds.
# decimal.getcontext().prec = 2700000    # Two million seven hundred thousand digits. Takes like 42 seconds.
# decimal.getcontext().prec = 2800000    # Two million eight hundred thousand digits. Takes like 43 seconds.
# decimal.getcontext().prec = 2900000    # Two million nine hundred thousand digits. Takes like 43 seconds.
# decimal.getcontext().prec = 2950000    # Two million five hundred fifty thousand digits. Takes like 44 seconds.
# decimal.getcontext().prec = 2990000    # Two million five hundred ninety thousand digits. Takes like 44 seconds.
# decimal.getcontext().prec = 2999000    # Two million nine hundred ninety-nine thousand. Takes like 44 seconds.
# decimal.getcontext().prec = 2999470    # Two million nine hundred ninety-nine thousand four hundred seventy. Takes like 44 seconds.

# decimal.getcontext().prec = 2999471    # Max: Two million nine hundred ninety-nine thousand four hundred seventy-one. Takes like 44 seconds.

# decimal.getcontext().prec = 2999473    # Two million nine hundred ninety-nine thousand. It takes like 44 seconds.
# decimal.getcontext().prec = 2999475    # Almost three million digits. Crashed at 45 seconds.
# decimal.getcontext().prec = 2999480    # Almost three million digits. Crashed at 45 seconds.
# decimal.getcontext().prec = 2999490    # Almost three million digits. Crashed at 45 seconds.
# decimal.getcontext().prec = 2999500    # Almost three million digits. Crashed at 45 seconds.
# decimal.getcontext().prec = 2999900    # Almost three million digits. Crashed at 45 seconds.
# decimal.getcontext().prec = 2999990    # Almost three million digits. Crashed at 45 seconds.
# decimal.getcontext().prec = 2999999    # Almost three million digits. Crashed at 45 seconds.
# decimal.getcontext().prec = 3000000    # Three million digits. Crashed in 45 seconds. 
# decimal.getcontext().prec = 5000000    # Five million digits. Crashed in 2:30 minutes. IOPub data rate exceeded.
decimal.getcontext().prec = 100000000   # Ten million digits. Crashed in 3 minutes. IOPub data rate exceeded.

pi = chudnovsky(2)

output_filename = "pi_digits.txt"
with open(output_filename, "w") as file:
    file.write(str(pi))

print("Output saved to:", output_filename)