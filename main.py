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
            #print(id)

            ingredients = row['ingredients_text']
            #print(ingredients)

            #use regular expression to replace comma with ; when it exists within the ()
            new_ingredient=re.sub(r'\([^()]+\)', lambda x: x.group().replace(',', ';'), ingredients)
        
            ingredientssplit = new_ingredient.split(',')

            for eachingredient in ingredientssplit:
                # replaces the semi colons with the original commas
                new_eachingredient=re.sub(r'\([^()]+\)', lambda x: x.group().replace(';', ','),  eachingredient)
                data = [id, new_eachingredient]
                writerforfile.writerow(data)

#closes the ingredients.csv and the OpenFoodFactsDatabase.csv
originalcsv.close()
ingredientscsv.close()

#new header for new file
header2 = ['id', 'peanutbutter']           

# create a new file called peanutbutter.csv
with open('peanutbutter.csv', 'w', encoding = 'UTF8') as peanutbuttercsv:
  writerforfile = csv.writer(peanutbuttercsv)
  writerforfile.writerow(header2)

  #reopens the ingredients.csv file
  with open('ingredients.csv', 'r', newline = '') as ingredientscsv:
    reader2 = csv.DictReader(ingredientscsv)

    for row in reader2:
      id = row['id']
      peanutbutter = row['ingredients']

      # if the ingredient in the ingredients.csv file contains peanut butter
      if "peanut butter" in row['ingredients']:
        data2 = [id, peanutbutter]
        writerforfile.writerow(data2)

#--------------------------------------------------------------------------------




       







  




  






            



