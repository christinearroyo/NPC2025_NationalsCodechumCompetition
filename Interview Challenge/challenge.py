print("Oiy tara laro!")
user = input("Pano ba kita tatawagin?: \n")
print(f"Ahh!, {user}\n")
print("Tara laro tayo!")

while True:
    hula = input(f"Pumili ka ng alas mo {user} 1 - 6: ")

    if hula == "3":
        print(f"Panalo ka {user}! Isa kang manghuhula!") 
        break
    else:
        print(f"Mali ka {user}! Ulitin mo wag kang susuko!")

"""
Arroyo, Christine R.
BSCS 2A

a filipino game where u guess numbers until u succeed!
i used input syntax, with while loop to create an if else and guess the 
right number for the user with interpolation in print.

Language: Python <3
"""





