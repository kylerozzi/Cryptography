"""
cryptography.py
Author: Kyle Rozzi
Credit: Help from Tristan Meyer

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"

def loop():
    input1=input("Enter e to encrypt, d to decrypt, or q to quit: ")
    for i in input1:
        m=[]
        k=[]
        if input1=='d':
            message1=list(input('Message: '))
            message2=len(message1)
            key1=list(input('Key: '))
            while len(key1) <= message2:
                key1=key1+key1
            for o in message1:
                message3=associations.find(o)
                m.append(message3)
            for p in key1:
                key3=associations.find(p)
                k.append(key3)
            list1=[(m-k) for m,k in zip(m,k)]
            for a in list1:
                e=''.join([associations[s%len(associations)] for s in list1])
            print(e)
            loop()
        elif input1=='e':
            message1=list(input('Message: '))
            message2=len(message1)
            key1=list(input('Key: '))
            while len(key1) <= message2:
                key1=key1+key1
            for o in message1:
                message3=associations.find(o)
                m.append(message3)
            for p in key1:
                key3=associations.find(p)
                k.append(key3)
            list1=[(m+k) for m,k in zip(m,k)]
            for a in list1:
                e=''.join([associations[s%len(associations)] for s in list1])
            print(e)
            loop()    
        elif input1=='q':
            print('Goodbye!')
        else:
            print('Did not understand command, try again.')
            loop()
loop()