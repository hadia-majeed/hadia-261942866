class User:
    def __init__ (self, username,password):
        self.username = username
        self.password = password
    
    def set_pass(self,password ):
        self.password = password
    
    def set_username(self, username ):
        self.username = username
    
    def get_name(self ):
        return self.username
    
    def get_pass(self ):
        return self.password
    
    
            
    
class Nutrition:
    def __init__ (self, calories, fats, protiens, carbohydrates):
        self.calories = calories
        self.fats= fats
        self.protiens = protiens
        self.carbohydrates = carbohydrates

class Ingredients:
    def __init__ (self,name):
        self.name = name
        self.ingredients = []

    def add_ingredient(self,ingrename):
        self.ingredients.append(ingrename)

    def remove_ingredient(self,ingredel):
        self.ingredients.append(ingredel)
          
class Receipe(Nutrition):
    def __init__ (self,name, ingredient, cooking_time, preparation_instructions, calories, fats, protiens, carbohydrates):
        super().__init__(calories, fats, protiens, carbohydrates)
        self.name=name
        self.ingredients= ingredient
        self.cooking_time =cooking_time
        self.preparation_instructions = preparation_instructions

    def set_nutrition(self,nutrition):
        self.nutrition = nutrition
    def get_name(self):
        return self.name
class baking(Receipe):
    def __init__ (self,name, ingredient, cooking_time, preparation_instructions, calories, fats, protiens, carbohydrates,):
        super().__init__ (name, ingredient, cooking_time, preparation_instructions, calories, fats, protiens, carbohydrates)
        self.receipe_type = "baking"
    def type(self):
        print('this receipe is baked\n')
    def gettype(self):
        return self.receipe_type
    
class cooking(Receipe):
    def __init__ (self,name, ingredient, cooking_time, preparation_instructions, calories, fats, protiens, carbohydrates,):
        super().__init__ (name, ingredient, cooking_time, preparation_instructions, calories, fats, protiens, carbohydrates)
        self.receipe_type = "cooking"
    def type(self):
        print('this receipe is cooked\n')
    def gettype(self):
        return self.receipe_type
        
class ReceipeManagementSystem():
    def __init__ (self):
        self.receipe = []
        self.userslst = []

    def display_all_recipes (self):
        for recipe in self.receipe:
            print("-------------------------")
            print("Recipe:")
            print(f"Name: {recipe.name}")
            print(f"Ingredients: {recipe.ingredients}")
            print(f"Cooking Time: {recipe.cooking_time}")
            print(f"Instructions: {recipe.preparation_instructions}")                
            print("Nutrition:")
            print(f"Calories: {recipe.calories}")
            print(f"Fat: {recipe.fats}g")
            print(f"Protein: {recipe.protiens}g")
            print(f"Carbohydrates: {recipe.carbohydrates}g")

    def register_user(self, username, password):
        user = User(username,password)
        self.userslst.append(user)

    def login_user(self, username, password):
        for user in self.userslst:
            if user.username == username and user.password == password:
                return user
        return None
    
    def manage_profile (self):
        print('Manage Profile:')
        print('1- change Username')
        print('2- change password')
        optionz = input('Select an option')
        for i in self.userslst:
            if optionz == '1':
                i.username = input('enter new username:')
                print('Username Update successfully!')
            if optionz == '2':
                i.password = input('enter new password:')
                print('Password updated successfully!')


    def delete_receipe (self, receipedel):
        for receipe in self.receipe:
            if receipe.name.lower() == receipedel.lower():
                self.receipe.remove(receipe)
                print(f"Receipe '{receipedel}' has been deleted!")
                return      
        print(f'Receipe {receipedel} not found')

    def edit_receipe(self, recedit):
        for receipe in self.receipe:
            if receipe.name.lower() == recedit.lower():
                print(f'Editing Receipe {recedit}')
                new_name = input('New name: ')
                receipe.ingredients = input('Enter new Ingredients:')
                receipe.cooking_time = input('Enter new cooking Time:')
                receipe.preparation_instructions = input('Enter new Instruction:')
                receipe.calories = input('Enter new calories:')
                receipe.fats = input('Enter new fats:')
                receipe.protiens = input('Enter new protiens:')
                receipe.carbohydrates = input('Enter new carbohydrates:')
                if new_name:
                    receipe.name = new_name
                print(f'Receipe ', {receipe.name} ,' has been updated')
                return 
        print('Receipe "{receipe.name}" not found')            

    def create_nutrients(self,calories, fats, protiens, carbohydrates):
        nutri = Nutrition(calories, fats, protiens, carbohydrates)
        self.receipe.append(nutri)

    def create_receipe(self,name, ingredients, cooking_time, preparation_instructions,calories, fats, protiens, carbohydrates):
        rec = Receipe(name, ingredients, cooking_time, preparation_instructions,calories, fats, protiens, carbohydrates)
        self.receipe.append(rec)
        return 

    def get_receipe_by_name(self,receipe_name):
        for receipe in self.receipe:
            if receipe.name.lower() == receipe_name.lower():
                return receipe
        return None
    def get_receipe_by_ingredients(self,receipe_ingredi):
        for receipe in self.receipe:
            if receipe.receipe_ingredi.lower() == receipe_ingredi.lower():
                return receipe
        return None

obj = ReceipeManagementSystem()

def main():
    

    while True:
        print("welcome to Recipe Management System")
        print('1-Register ')
        print('2-Login')
        print('3- Exit')
        a = input('Select an option:')

        if a == '1':
            username = input('Enter your Username:')
            password = input('Enter your password:')
            obj.register_user( username, password)
            print("You're Signed Up!") 
       
        elif a == '2':
            username = input('Enter your Username:')
            password = input('Enter your password:')
            user = obj.login_user(username,password)
            if user:
                print('Logged in Successfully!')
                while True:
                    print('Select any option below :')
                    print('1- Create Receipe')
                    print('2- Edit Receipe')
                    print('3- Delete Receipe')
                    print('4- Veiw Receipes')
                    print('5- Search Receipes')                     
                    b = input('Select an option:')
                    if b == '1':
                        name = input('Enter reciepe name: ')
                        ingredients = input('Enter ingredients name: ')
                        cooking_time = input('Enter cooking time: ')
                        preparation_instructions = input('Enter preparation_instructions: ')
                        print('--ENTER NUTRIENTS--')
                        calories = input ("calories: ")
                        fats = input ('fats:')
                        protiens = input('protiens:')
                        carbohydrates = input('Carbs: ')
                        obj.create_receipe(name, ingredients, cooking_time, preparation_instructions, calories, fats, protiens, carbohydrates)    
                        print('Receipe Created!')
                    elif b == '2':
                        editz = input('Enter the name of the receipe you want to edit: ')
                        obj.edit_receipe(editz)

                    elif b == '3':
                        dell= input("enter receipe you want to delete:")
                        obj.delete_receipe(dell)

                    elif b == '4':
                        obj.display_all_recipes()      

                    elif b == '5':
                        receipe_name_get = input('Search any Recipe: ')
                        print('--RECIPE DETAILS--')
                        recipe = obj.get_receipe_by_name(receipe_name_get)

                        if recipe is not None:
                            print(f'Name: {recipe.name}')
                            print(f'Ingredients: {recipe.ingredients}')
                            print(f'Cooking Time: {recipe.cooking_time}')
                            print(f'Instructions: {recipe.preparation_instructions}')
                            print(f'Nutrition: ')
                            print(f'Calories: {recipe.calories}')
                            print(f'Fat: {recipe.fats}g')
                            print(f'Protein: {recipe.protiens}g')
                            print(f'Carbohydrates: {recipe.carbohydrates}g')
                        else:
                            print('Recipe not found')                            
            else:
                print('Wrong username or password!') 

        elif a == "3":
            break

main ()
 

