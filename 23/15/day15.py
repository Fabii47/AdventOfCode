def calcHash(str):
    num = 0
    for char in str:
        num = ((num + ord(char)) * 17 ) % 256
    return num

with open('input_15.txt', 'r') as file:
    print(sum(map(calcHash, file.readlines()[0].split(","))))