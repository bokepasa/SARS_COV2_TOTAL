# Import math Library
import math
from num2words import num2words
import os

#Console clear
clear = lambda: os.system('cls')
clear()

virus_size = 100 #80 nanómetro a 120 nanómetro
size_cm = virus_size/10000000
print("Size SARS-COV2:",size_cm, "cm")
print("{0:.6f}".format(size_cm),"cm")

virus_cm3 = 4/3 * math.pi * pow(size_cm/2,3)
virus_nano3 = 4/3 * math.pi * pow(virus_size/2,3)
print ("Centimeters\u00b3:" , virus_cm3)
#print("{0:.16f}".format(virus_cm3))
print ("Nanometres\u00b3:" , int(virus_nano3))

total_virus = 200000000000000000 # virus particles in the world at any one time.
print("Virus particles in the world: ",total_virus)
tot = total_virus*virus_cm3

print("Centimeters\u00b3 total virus:" ,int(tot))
#Close sphere packing 26%
print("Centimeters\u00b3 total virus space +26%:" ,int(tot+(tot*26)/100))

lata = 33 # centilitro 1 --10 cm3
lata_cm3 = lata*10
print("###########################################################################")
print("Coke: ", lata_cm3,"cm\u00b3 -----> Virus ",int(tot+(tot*26)/100), "cm\u00b3")
print("###########################################################################")

total_virus_lata = lata_cm3/virus_cm3
#Close sphere packing 26%
total_virus_lata = total_virus_lata+(total_virus_lata * 26) / 100
print("Total virus in Coke: ", int(total_virus_lata))

valor = lata_cm3/int(tot)
#print(valor)

print("Linear: ",num2words(int((total_virus*size_cm)/100000), lang='en'), "kilometers.")

superfice_cm2 = math.pi* pow((size_cm/2),2)

print("Extension:", int((total_virus*superfice_cm2)/10000), "m\u00b2---football field: 7140 m\u00b2")