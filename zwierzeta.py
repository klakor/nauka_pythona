#! /usr/bin/python

print("W lesie mieszkaja zwierzeta, takie jak: ")
zwierzeta = ["lew", "niedzwiedz", "lis", "jez"]
print(zwierzeta[0:3])


print("\nDo wodopoju o poranku przybiegly w kolejnosci:")
for s in zwierzeta:
    print(s)

print("\nTomek zanotowal kolejnosc, w ktorej zaobserwowal pojawienie sie zwierzat:")
for idx in range(len(zwierzeta)):
    print("jako " + str(idx+1) + " przybiegl " + zwierzeta[idx])
