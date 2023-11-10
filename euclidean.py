adhar=int(input("enter adhar number: "))
prn=int(input("enter last four digit of PRN No. : "))
rem = 1
ads=[]
qus=[]
ns=[]
while(rem !=0):
    qut=adhar//prn
    rem=int(adhar%prn)

    ads.append(adhar)
    qus.append(qut)
    ns.append(prn)

    print(f'{adhar} = {prn} ({qut}) + {rem}')

    t=prn
    prn=rem
    adhar=t

gcd=ns[-1]
ads.reverse()
qus.reverse()
ns.reverse()
ads=ads[1:]
qus=qus[1:]
ns=ns[1:]

print()

x=1
y=-qus[0]

for i in range(len(ads)):
    print(f'{gcd} = {ads[i]}({x}) + {ns[i]}({y})')

    if i==len(ads)-1:break
    t=x
    x=y
    y=t-y*qus[i+1]
print(f" m = {x} & n = {y}")
input()
