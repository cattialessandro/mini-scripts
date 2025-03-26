# funzione
def somma(nums, s=0):
    for num in nums:
        s += num
    return s

# esempio di utilizzo
nums = list()
inserimento = True
while inserimento:
    try:
        num = int(input("Inserisci un numero [0 o VUOTO per terminare]: "))
    except:
        num = 0
    if num == 0:
        inserimento = False
    nums.append(num)

s = somma(nums)

print("SOMMA NUMERI:", s)

