#! C:\Users\thepe\AppData\Local\Programs\Python\Python312\python.exe

import PySimpleGUI as xpg

running_total = 0
calories = 0
fat = 0
carb_total = 0
carbs = 0
fiber = 0
fiber_total = 0
protein = 0
protein_total = 0
CarbsPerServing = 0
FiberPerServing = 0
ProteinPerServing = 0


# 1. Set Theme
xpg.theme("Black")

# 2. Create Layout
layout = [  
    [
        xpg.Text("Food: ", size=(7,1)),#size makes the boxes allign
        xpg.Combo(["9-Grain Cereal", "Almonds", "Almond Flour", "Apple Sauce", "Avocado","Bacon", "Bananas", "Barley, dry", "Beans, black canned", "Beans, garbanzo canned", "Beans, garbanzo dry", "Beans, kidney canned", "Beans, pinto canned", "Beans, dry", "Beef", "Beef, lean ground", "Bell Pepper", "Bourbon", "Bulgur Wheat", "Broccoli", "Butter", "Butternut Squash", "Cabbage", "Canadian Bacon", "Carrots", "Celery", "Cheese", "Chia Seeds", "Chicken", "Chicken Sausage", "Chicken Wings", "Chocolate", "Coconut Flakes, unsweetened", "Corn", "Cornmeal", "Cream", "Dried Fruit", "# Eggs", "# Falafel", "Feta", "Flax Seeds", "Flour", "Flour, Sprouted", "Flour, Whole Wheat", "Goat Cheese", "# Greek Meatballs", "Honey", "Hummus", "Italian Sausage", "Ketchup", "Lentils, dry", "Malt", "Mayo", "Milk", "Molasses", "Mozzarella", "Mushrooms", "Oatmeal", "Oat Milk", "# Olives", "Oil", "Onions", "Panko", "Pasta, dry", "Pasta, lo mein", "Peanuts", "Peanut Butter", "Peppers, bell", "Pepperoni", "# Pita, whole wheat", "# Pizza Dough", "# Whole-Wheat Pizza Dough", "Pork", "Potatoes", "Protein Powder", "Raisins", "Rice, dry", "Rice, brown, dry", "Rice, red, dry", "# Rice Paper", "Rye", "Semolina", "Sour Cream", "Sourdough, slice weight", "Sourdough, whole-wheat, slice weight", "Sugar", "Sunflower Seeds", "Sweet Potato", "Tahini", "Tofu", "# Tortillas, Corn", "# Tortillas, Whole Wheat Flour", "Turkey, Ground", "Walnuts", "Wheat Bran", "Yogurt", "Variable Item @ 1 calorie/gram" ])
    ], # Don't forget the comma here and if NEW foods are added remember to update values[0]!
    [
        xpg.Text("Grams/#: ", size=(7,1)),
        xpg.InputText(do_not_clear=False)
    ],
    [
        xpg.Text("Servings: ", size=(7,1)),
        xpg.InputText()     
    ],
     [
        xpg.Button("OK"),
        xpg.Button("Cancel")  
    ],
     
        [
        xpg.Text("Index: ", size=(7,1)),#size makes the boxes allign
        xpg.Combo(["Slice 9-Grain Sourdough = 60g", "1 can beans = 250g drained", "1 oz = 28.3g", "1# = 453g", "1 c Water = 236g", "1 T Sugar = 12.5g", "1 T Oil = 14g", "1 c oats = 80g", "1 T Almond Flour = 7g", "1 T Butter = 14g", "1 Egg = 45g", "1 c Rice, dry = 180g", "1/2 c Beans, cooked = 130g", "1 c raisins = 180", "1/4 c Beans, dry = 35g", "1 Corn Tortilla = 25g", "1 Flour Tortilla = 71g", "1 Chicken Thigh, boneless = 100 g", "1 c Cheddar = 113 g", "1 c Flour = 120g", "1 Sourdough, slice = 50g", "1 T Sour Cream = 15g", "1 Avacado = 100g", "1 c Barley = 200g","1 Potato, large = 360g", "1 T Mayo = 14g", "1 T Honey = 21g", "1 Yam Roll = 218 calories", "1 Slice Bacon = 35 g", "Pizza Dough = 285g","1 Italian Sausage Link = 80g", "1 can beans = 250g", "Variable Item @ 1 calorie/gram"])
        ] ,# Don't forget the comma here and if NEW foods are added remember to update values[0]! ""  
     
    [
        xpg.Output(size=(70,35))
    ]   
]

# 3. Create Window
window = xpg.Window("Path to Weight Loss", layout)

# 4. Event Loop
while True:
    event, values = window.read()
    if event == xpg.WIN_CLOSED or event == "Cancel" or values[0] == "" or values[1] == "" or values[2] == "":
        break
    elif event == "OK":
        print(f"Food: {values[0]}")
        print(f"Grams: {values[1]}")
        
        values[1] = int(values[1])
        values[2] = int(values[2])
        
        if values[0] == '9-Grain Cereal':
            fat = 3.42
            carbs = .684
            fiber = .132
            protein = .16
        if values[0] == 'Almonds':
            fat = 6.07
            carbs = .1786
            fiber = .107
            protein = .214
        if values[0] == 'Almond Flour':
            fat = 5.8
            carbs =.162
            fiber = .093
            protein = .262
        if values[0] == 'Apple Sauce':
            fat = .396
            carbs = .111
            fiber = .008
            protein = 0
        if values[0] == 'Avocado':
            fat = 1.67
            carbs = .09
            fiber = .07
            protein = .02
        if values[0] == 'Bananas':
            fat = .89
            carbs = .23
            fiber = .02
            protein = .01            
        if values[0] == 'Bacon':
            fat = 3.9
            carbs = 0
            fiber = 0
            protein = .14
        if values[0] == 'Beans, black canned':
            fat = .85
            carbs = .16
            fiber = .077
            protein = .054 
        if values[0] == 'Beans, garbanzo canned':
            fat = .92
            carbs = .14
            fiber = .03
            protein = .046 
        if values[0] == 'Beans, garbanzo dry':
            fat =1.8
            carbs = .28
            fiber = .08
            protein = .08
        if values[0] == 'Beans, kidney canned':
            fat = .92
            carbs = .17
            fiber = .038
            protein = .054
        if values[0] == 'Beans, pinto canned':
            fat = .85
            carbs = .054
            fiber = .069
            protein = .054           
        if values[0] == 'Beans, dry':
            fat = 2.29
            carbs = .6
            fiber = .343
            protein = .2
        if values[0] == 'Beef':
            fat = 2.2
            carbs = 0
            fiber = 0
            protein = .257
        if values[0] == 'Beef, lean ground':
            fat = 1.
            carbs = 0
            fiber = 0
            protein = .208
        if values[0] == 'Bell Pepper':
            fat = .31
            carbs = .0665
            fiber = .012
            protein = .009
        if values[0] == 'Broccoli':
            fat = .39
            carbs = .062
            fiber = .024
            protein = .025
        if values[0] == 'Bulgur Wheat':
            fat = 3.5
            carbs =.72
            fiber = .12
            protein = .16
        if values[0] == 'Butter':
            fat = 7.43
            carbs = 0
            fiber = 0
            protein = .0085
        if values[0] == 'Butternut Squash':
            fat = .48
            carbs = .105
            fiber = .02
            protein = .015
        if values[0] == "Cabbage":
            fat = .25
            carbs = .06
            fiber = .03
            protein = .0128
        if values[0] == 'Canadian Bacon':
            fat = 1.17
            carbs = 0
            fiber = 0
            protein = .2
        if values[0] == 'Carrots':
            fat = .48
            carbs = .1
            fiber = .03
            protein = .009
        if values[0] == 'Celery':
            fat = .17
            carbs = .03
            fiber = .016
            protein = .0069
        if values[0] == 'Cheese':
            fat = 4.1
            carbs = .0244
            fiber = 0
            protein = .233
        if values[0] == 'Chia Seeds':
            fat = 4.9
            carbs = .42
            fiber = .344
            protein = .165
        if values[0] == 'Chicken':
            fat = 1.8
            carbs = 0
            fiber = 0
            protein = .246
        if values[0] == 'Chicken Sausage':
            fat = 1.88
            carbs = .0235
            fiber = .01
            protein = .165
        if values[0] == 'Chicken Wings':
            fat = 2.5
            carbs = 0
            fiber = 0
            protein = .236
        if values[0] == 'Chocolate':
            fat = 4.8
            carbs = .64
            fiber = .06
            protein = .042
        if values[0] == 'Coconut Flakes, unsweetened':
            fat = 4.56
            carbs = .518
            fiber = .099
            protein = .0313
        if values[0] == 'Corn':
            fat = 1.05
            carbs = .224
            fiber = .0235
            protein = .0352
        if values[0] == 'Cornmeal':
            fat = 3.7
            carbs = .79
            fiber = .039
            protein = .0711            
        if values[0] == 'Cream':
            fat = 3.4
            carbs = .0284
            fiber = 0
            protein = .0284
        if values[0] == 'Dried Fruit':
            fat = 2.75
            carbs = .675
            fiber = .075
            protein = .025
        if values[0] == '# Eggs':
            fat = 72
            carbs = .36
            fiber = 0
            protein = 6.3
        if values[0] == '# Falafel':
            fat = 22
            carbs = 4
            fiber = 1
            protein = 1
        if values[0] == 'Feta':
            fat = 2.7
            carbs = .0388
            fiber = 0
            protein = .142
        if values[0] == 'Flax Seeds':
            fat = 5.3
            carbs = .29
            fiber = .27
            protein = .183
        if values[0] == 'Flour':
            fat = 3.6
            carbs = .75
            fiber = 0
            protein = .143
        if values[0] == 'Flour, Sprouted':
            fat = 3.17
            carbs = .68
            fiber = .12
            protein = .146
        if values[0] == 'Flour, Whole Wheat':
            fat = 3.66
            carbs = .733
            fiber = .1
            protein = .13          
        if values[0] == 'Goat Cheese':
            fat = 2.64
            carbs = 0           
            fiber = 0
            protein = .185
        if values[0] == '# Greek Meatballs':
            fat = 42
            carbs = 2
            fiber = 0
            protein = 6
        if values[0] == 'Honey':
            fat = 3
            carbs = .82
            fiber = 0
            protein = .003
        if values[0] == 'Hummus':
            fat = 1.5
            carbs = .1
            fiber = .025
            protein = .05
        if values[0] == "Italian Sausage":
            fat = 3.2
            carbs = 0
            fiber = 0
            protein = .182
        if values[0] == 'Ketchup':
            fat = 1
            carbs = .27
            fiber = 0
            protein = .0018
        if values[0] == 'Lentils, dry':
            fat = 3.52
            carbs = .634
            fiber = .107
            protein = .246
        if values[0] == 'Malt':
            fat = 3.6
            carbs = .78
            fiber = .071
            protein = .103
        if values[0] == 'Mayo':
            fat = 6.8
            carbs = 0
            fiber = 0
            protein = .0096
        if values[0] == 'Milk':
            fat = .6
            carbs = .05
            fiber = 0
            protein = .0327
        if values[0] == 'Molasses':
            fat = 4
            carbs = 1
            fiber = .066
            protein = 0 
        if values[0] == 'Mozzarella':
            fat = 3
            carbs = .02
            fiber = 0
            protein = .222
        if values[0] == 'Mushrooms':
            fat = .31
            carbs = .048
            fiber = .017
            protein = .0289
        if values[0] == 'Oatmeal':
            fat = .64
            carbs = .11
            fiber = .02
            protein = .0221  
        if values[0] == 'Oat Milk':
            fat = .1666666
            carbs = .0375
            fiber = .004
            protein = .004          
        if values[0] == '# Olives':
            fat = 5.1
            carbs = 0
            fiber = 0
            protein = .037
        if values[0] == 'Oil':
            fat = 8.8
            carbs = 0
            fiber = 0
            protein = 0
        if values[0] == 'Onions':
            fat =.44
            carbs = .093
            fiber = .022
            protein = .0094
        if values[0] == 'Pasta, dry':
            fat = 3.21
            carbs = .7
            fiber = .125
            protein = .143  
        if values[0] == 'Pasta, lo mein':
            fat = 3.4
            carbs = .691
            fiber = .032
            protein = .138          
        if values[0] == 'Peanuts':
            fat = 6
            carbs = .153
            fiber = .094
            protein = .028
        if values[0] == 'Peanut Butter':
            fat = 5.93
            carbs = .188
            fiber = .0625
            protein = .21875
        if values[0] == 'Pepperoni':
            fat = 3.21
            carbs = 0
            fiber = 0
            protein = .192 
        if values[0] == 'Peppers, bell':
            fat =.31
            carbs = .065
            fiber = .012
            protein = .009  
        if values[0] == '# Pita, whole wheat': 
            fat = 143
            carbs = 29
            fiber = 3
            protein = 4.25   
        if values[0] == '# Pizza Dough':
            fat = 581
            carbs = 113
            fiber = 0
            protein = 21
        if values[0] == '# Whole-Wheat Pizza Dough':
            fat = 572
            carbs = 116
            fiber = 12
            protein = 17
        if values[0] == 'Pork':
            fat = 1.34
            carbs = 0
            fiber = 0
            protein = .246
        if values[0] == 'Potatoes':
            fat = 1.26
            carbs = .204
            fiber = .014
            protein = .0187
        if values[0] == 'Protein Powder':
            fat = 3.658
            carbs = .098
            fiber = .0243
            protein = .732
        if values[0] == 'Raisins':
            fat = 3
            carbs = .79
            fiber = .045
            protein = .033
        if values[0] == 'Rice, dry':
            fat = 3.55
            carbs = .35
            fiber = .004
            protein = .08888
        if values[0] == 'Rice, brown, dry':
            fat = 3.77
            carbs = .75
            fiber = .0444
            protein = .0666
        if values[0] == 'Rice, red, dry':
            fat = 3.6
            carbs = .76
            fiber = .067
        if values[0] == '# Rice Paper':
            fat = 27 
            carbs = 6.33
            fiber = .1666
            protein = .333333
        if values[0] == 'Rye':
            fat = 3.25
            carbs = .686
            fiber = .238
            protein = .159
        if values[0] == "Semolina":
            fat = 3.33
            carbs = .66
            fiber = .0333
            protein = .0133
        if values[0] == 'Sugar':
            fat = 3.87
            carbs = 1
            fiber = 0
            protein = 0
        if values[0] == 'Sourdough, slice weight':
            fat = 2.4
            carbs = .48
            fiber = .02
            protein = .088
        if values[0] == 'Sourdough, whole-wheat, slice weight':
            fat = 2.2
            carbs = .455
            fiber = .0447
            protein = .0746
        if values[0] == 'Sunflower Seeds':
            fat = 5.75
            carbs = .238
            fiber = .11
            protein = .191
        if values[0] == 'Sweet Potato':
            fat = .79
            carbs = .173
            fiber = .044
            protein = .0158
        if values[0] == 'Tahini':
            fat = 7.14
            carbs = .1
            fiber = 0
            protein = .214
        if values[0] == 'Tofu':
            fat = .8233
            carbs = .0235
            fiber = 0
            protein = .082
        if values[0] == 'Turkey, Ground':
            fat = 2.11
            carbs = 0
            fiber = 0
            protein = .269            
        if values[0] == '# Tortillas, Corn':
            fat = 50
            carbs = 10.5
            fiber = 1
            protein = 1
        if values[0] == '# Tortillas, Whole Wheat Flour':
            fat = 220
            carbs = 32
            fiber = 4.87
            protein = 4.375
        if values[0] == 'Walnuts':
            fat = 6.5
            carbs = .18
            fiber = .07
            protein = .143
        if values[0] == 'Sour Cream':
            fat = 2
            carbs = .0463
            fiber = 0
            protein = .0244
        if values[0] == 'Bourbon':
            fat = 2.3
            carbs = 0
            fiber = 0
        if values[0] == 'Barley, dry':
            fat = 3.5
            carbs = .78
            fiber = .16
            protein = .991
        if values[0] == 'Panko':
            fat = 3.7
            carbs = .77
            fiber = .03
            protein = .1333
        if values[0] == 'Wheat Bran':
            fat = 2.16
            carbs = .645
            fiber = .428
            protein = .156
        if values[0] == 'Variable Item @ 1 calorie/gram':
            fat = 1
            carbs = 0
            fiber = 0
            protein = 0
        if values[0] == 'Yogurt':
            fat = .97
            carbs = .0398
            fiber = 0
            protein = .09
                    
        calories = values[1] * fat
        #calories = int(calories)
        
        carbs = values[1] * carbs
        #carbs = int(carbs)
        
        fiber = values[1] * fiber
        
        protein = values[1] * protein
        #protein = int(protein)
        
        running_total = running_total + calories
        #running_total = int(running_total)
        
        carb_total = carb_total + carbs
        
        #carb_total = int(carb_total)
        
        fiber_total = fiber_total + fiber
        
        protein_total = protein_total + protein
        
        servings = running_total / values[2]
        #servings = int(servings)
        
        CarbsPerServing = carb_total / values[2]
        round(CarbsPerServing,2)
        #CarbsPerServing = int(CarbsPerServing)
        
        FiberPerServing = fiber_total / values[2]
        #FiberPerServing = int(FiberPerServing)
        
        ProteinPerServing = protein_total / values[2]
        #ProteinPerServing - int(ProteinPerServing)
        
        print(f"Calories in ", values[0], "are: ", round(calories,1), "\n")
       # print(f"Running Total Calories: ", running_total,"\n")
        print(f"Calories per Serving: ", round(servings,1))
        print(f"Carbs per Serving:", round(CarbsPerServing,1))
        print(f"Fiber per Serving: ", round(FiberPerServing,1))
        print(f"Protein per Serving:", round(ProteinPerServing,1))
        print(f"______________________________________________________________________", "\n")
        
# 5. Close Window
window.close() 
# To Make Desktop Icon
# c:>users>thepe>onedrive>desktop>python
# pip install pyinstaller
# pyinstaller CaloriesMenu_x.x.py --onefile