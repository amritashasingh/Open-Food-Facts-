import csv
import re

#gives the header of the new ingredients file
header = ['id', 'ingredients']

#creates a new csv file
with open('ingredients.csv', 'w', encoding='UTF8') as ingredientscsv:
    writerforfile = csv.writer(ingredientscsv)
    writerforfile.writerow(header)

    #opens the original database
    with open('OpenFoodFactsDatabase.csv', newline='') as originalcsv:
        reader = csv.DictReader(originalcsv)

        for row in reader:

            id = row['code']
            ingredients = row['ingredients_text']
           
            #use regular expressions to replace comma with ; when it exists within the ()
            new_ingredient = re.sub(r'\([^()]+\)',lambda x: x.group().replace(',', ';'),ingredients)

            ingredientssplit = new_ingredient.split(',')

            for eachingredient in ingredientssplit:
                # replaces the semi colons with the original commas
                new_eachingredient = re.sub(
                    r'\([^()]+\)', lambda x: x.group().replace(';', ','),
                    eachingredient)
                data = [id, new_eachingredient]
                writerforfile.writerow(data)

#closes the ingredients.csv and the OpenFoodFactsDatabase.csv
originalcsv.close()
ingredientscsv.close()

#new header for new file
header2 = ['id', 'ironferroussulfate']

# create a new file called ironferroussulfate.csv
with open('ironferroussulfate.csv', 'w', encoding='UTF8') as ironferroussulfatecsv:
    writerforfile = csv.writer(ironferroussulfatecsv)
    writerforfile.writerow(header2)

    #reopens the ingredients.csv file
    with open('ingredients.csv', 'r', newline='') as ingredientscsv:
        reader2 = csv.DictReader(ingredientscsv)

        for row in reader2:
            id = row['id']
            ironferroussulfate = row['ingredients']

            # if the ingredient in the ingredients.csv file contains the term iron or ferrous sulfate (different capitalizations)
            if row['ingredients'].find("IRON") != -1 or row['ingredients'].find("Iron") != -1 or row['ingredients'].find("iron") != -1 or row['ingredients'].find("Ferrous Sulfate") !=-1 or row['ingredients'].find("FERROUS SULFATE") != -1 or row['ingredients'].find("ferrous sulfate") != -1:
                data2 = [id, ironferroussulfate]
                writerforfile.writerow(data2)

ingredientscsv.close()
ironferroussulfatecsv.close()


#declaring count variables
countofIron=0
countofIRON=0
countofiron=0
countofreducediron=0
countofReducedIron=0
countofironferroussulfate=0
countofironferroussulfate2=0
countofIRONFERROUSSULFATE=0
countofelectrolyticiron=0
countofferroussulfate=0
countofFERROUSSULFATE=0
countofferroussulfateiron=0
countofferroussulfateiron2=0
countofferroussulfateiron3=0
countofferroussulfateiron4=0

with open ('ironferroussulfate.csv', 'r', newline ='') as ironferroussulfatecsv:
  reader3 = csv.DictReader(ironferroussulfatecsv)

  for row in reader3:
    
     if "Iron" in  row['ironferroussulfate']:
       countofIron+=1
    
     if "IRON" in row['ironferroussulfate']:
       countofIRON+=1

     if "iron" in row['ironferroussulfate']:
       countofiron+=1

     if "reduced iron" in row['ironferroussulfate']:
       countofreducediron+=1

     if "Reduced Iron" in row['ironferroussulfate']:
        countofReducedIron+=1

     if "electrolytic iron" in row['ironferroussulfate']:
       countofelectrolyticiron+=1

     if "iron (ferrous sulfate)" in row['ironferroussulfate']:
       countofironferroussulfate+=1

     if "IRON (FERROUS SULFATE" in row['ironferroussulfate']:
       countofIRONFERROUSSULFATE+=1
      
     if "Iron [Ferrous Sulfate]" in row['ironferroussulfate']:
       countofironferroussulfate2+=1
      
     if "ferrous sulfate" in row['ironferroussulfate']:
       countofferroussulfate+=1

     if "FERROUS SULFATE" in row['ironferroussulfate']:
      countofFERROUSSULFATE+=1
 
     if "ferrous sulfate {iron}" in row['ironferroussulfate']:
      countofferroussulfateiron+=1

     if "ferrous sulfate (iron)" in row['ironferroussulfate']:
       countofferroussulfateiron2+=1

     if "ferrous sulfate [iron]" in row['ironferroussulfate']:
       countofferroussulfateiron3+=1

     if "FERROUS SULFATE [IRON]" in row['ironferroussulfate']:
       countofferroussulfateiron4+=1

      
#printing out the counts    

#subtrating countofironferroussulfate2 and countofReducedIron because althought the term "Iron" is in it, the instances of Iron are when the ingredient is listed as "Iron"             
print("The count of Iron is: " +  str(countofIron-countofironferroussulfate2-countofReducedIron))

#subtracting countofIRONFERROUSSULFATE and countofferroussulfateiron4 because although the term "IRON" is in it, the instances of IRON are when the ingredient is listed as "IRON"
print("The count of IRON is: " + str(countofIRON-countofIRONFERROUSSULFATE-countofferroussulfateiron4))

#subtracting countofreducediron,countofironferroussulfate,countofelectrolyticiron, and countofferroussulfateiron because althought the term "Iron" is in it, the instances of "iron" are when the ingredient is listed as "iron" 
print("The count of iron is: " + str(countofiron-countofreducediron-countofironferroussulfate-countofelectrolyticiron- countofferroussulfateiron))


print("The count of reduced iron is: "+ str(countofreducediron))

print("The count of Reduced Iron is: " + str(countofReducedIron))

print("The count of electrolytic iron is: " + str(countofelectrolyticiron))

print("The count of iron (ferrous sulfate) is: " + str(countofironferroussulfate))

print("The count of IRON (FERROUS SULFATE) is: " + str(countofIRONFERROUSSULFATE))

print("The count of Iron [Ferrous Sulfate] is: " + str(countofironferroussulfate2))

#subracting countofironferroussulfate, countofferroussulfateiron, countofferroussulfateiron2, and countofferroussulfateiron3 because although the term "ferrous sulfate" is in it, instances of iron are when the ingredient is listed as "ferrous sulfate"
print("The count of ferrous sulfate is: " + str(countofferroussulfate-countofironferroussulfate-countofferroussulfateiron-countofferroussulfateiron2-countofferroussulfateiron3))

#subtracting countofIRONFERROUSSULFATE and countofferroussulfateiron4 because althought the term "FERROUS SULFATE" is in it, instances of FERROUS SULFATE are when the ingredient is listed as "FERROUS SULFATE" 
print("The count of FERROUS SULFATE is: " + str(countofFERROUSSULFATE-countofIRONFERROUSSULFATE-countofferroussulfateiron4))

print("The count of ferrous sulfate {iron} is: " + str(countofferroussulfateiron))

print("The count of ferrous sulfate(iron) is: " + str(countofferroussulfateiron2))

print("The count of ferrous sulfate [iron] is: " + str(countofferroussulfateiron3))

print("The count of FERROUS SULFATE [IRON] is: " + str(countofferroussulfateiron4))
