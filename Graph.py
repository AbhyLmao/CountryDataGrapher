
import numpy as np
import matplotlib.pyplot as plt
import csv

print("\nEndg 233 FINAL PROJECT")

class Graph:
    """
    A class used to create a Graph object.

        Attributes:
            data_x = (list) x data to graph
            data_Y = (list) y data to graph
            country_name = (str) name of the country
    """

    def __init__(self,data_x,data_y,country_name):
        self.x_data = data_x
        self.y_data = data_y
        self.country = country_name


    def line_Graph(self):
        plt.figure(1, figsize = (12,6))
        plt.plot(self.x_data,self.y_data,"--", color = "blue")
        plt.xlabel("Countries")
        plt.ylabel("Population in 10^8")
        plt.xticks(self.x_data, rotation = 'vertical')
        plt.title("Population data 2000 - 2020 of {0}".format(self.country.upper()))
        plt.show()


    def bar_Graph(self):
        plt.figure()
        plt.xlabel("Species")
        plt.ylabel("Number of threatend species")
        plt.bar(self.x_data, self.y_data)
        plt.title("Threatend species data of {0}".format(self.country.upper()))
        plt.show()

def check_species(input_data, dataset):
    '''
    Function to check if the input giving by the user is present in the given dataset

    parameters:

    input_data = data given by the user to be checked
    dataset = array of data in which input_data is to be checked

    returns:
    True: if input is present in the array
    False: if input is not present in the array 
    '''

    for i in range(1, len(dataset[0])):
        if (input_data.lower() == dataset[0][i].lower()):
            return True
    else:
        return False

def max_threat_in_row(input_data, dataset):
    '''
    Function which is used to find the maximum value in a column for threatened species

    input_data = data given by the user
    dataset = array of data in which input_data is used to get the maximum value of a coulum input_data is present

    returns:
    none
    '''
    
    for i in range(1,len(dataset[0])):
        if input_data.lower() == dataset[0][i].lower():
            empty_list = []
            for j in range(1,len(dataset)):
                empty_list.append(int(dataset[j][i]))
            
            max_value = max(empty_list)

            for h in range(1,len(dataset)):
                if (max_value == int(dataset[h][i])):
                    print("\n",dataset[h][0], "had", max_value, "threatened species which are the most threatend", dataset[0][i], "out of all countries")


def min_threat_in_row(input_data, dataset):
    '''
    Function which is used to find the minimum value in a column for threatened species

    input_data = data given by the user
    dataset = array of data in which input_data is used to get the minimum value of a coulum input_data is present

    returns:
    none
    '''
    for i in range(1,len(dataset[0])):
        if input_data.lower() == dataset[0][i].lower():
            empty_list = []
            for j in range(1,len(dataset)):
                empty_list.append(int(dataset[j][i]))
            
            min_value = min(empty_list)


            for h in range(1,len(dataset)):
                if (min_value == int(dataset[h][i])):
                    print("\n",dataset[h][0], "had", min_value, "threatened species which are the least threatend", dataset[0][i], "out of all countries")


def max_in_columb(input_data,dataset):
    '''
    Function which is used to find the maximum value in a column

    input_data = data given by the user
    dataset = array of data in which input_data is used to get the maximum value of a coulum input_data is present

    returns:
    none
    '''
    index1 = input_data-1999
    empty_list = []
    for i in range(1,len(dataset)):
        empty_list.append(int(dataset[i][index1]))

    max_value = max(empty_list)
    
    for i in range(1,len(dataset)):
        if (max_value == int(dataset[i][index1])):
            print("\n",dataset[i][0],"had",max_value,"in",input_data,"and was the most populous country that year")
        

def min_in_columb(input_data,dataset):
    '''
    Function which is used to find the minimum value in a column

    input_data = data given by the user
    dataset = array of data in which input_data is used to get the minimum value of a coulum input_data is present

    returns:
    none
    '''
    index1 = input_data-1999
    empty_list = []
    for i in range(1,len(dataset)):
        empty_list.append(int(dataset[i][index1]))

    min_value = min(empty_list)
    
    for i in range(1,len(dataset)):
        if (min_value == int(dataset[i][index1])):
            print("\n",dataset[i][0],"had",min_value,"in",input_data,"and was the least populous country that year")


def avgfun(input_data,dataset):
    '''
    Function used to find the average of a specified index of array

    input_data = data given by the user
    dataset = array of data in which input_data is used to get the average value of the array index where input_data is present

    returns:
    none
    '''
    for i in range(len(dataset)):
        if (input_data.lower() == dataset[i][0].lower()):
            empty_list = []
            for j in range(1,len(dataset[i])):
                empty_list.append(int(dataset[i][j]))

            avg_value = np.mean(empty_list)
            print ("\nThe average population of", dataset[i][0],"is", avg_value)

def avgthreatfun(input_data,dataset):
    '''
    Function used to find the average of a specified index of array for the threatend species

    input_data = data given by the user
    dataset = array of data in which input_data is used to get the average value of the array index where input_data is present

    returns:
    none
    '''
    for i in range(len(dataset)):
        if (input_data.lower() == dataset[i][0].lower()):
            empty_list = []
            for j in range(1,len(dataset[i])):
                empty_list.append(int(dataset[i][j]))
            
            avg_value = np.mean(empty_list)
            print ("\nThe avg endanged number of species of", dataset[i][0],"is", avg_value, "which are")

def maxthreatfun(input_data,dataset):
    '''
    Function used to find the maximum of a specified index of array for the threatend species

    input_data = data given by the user
    dataset = array of data in which input_data is used to get the maximum value of the array index where input_data is present

    returns:
    none
    '''
    for i in range(len(dataset)):
        if (input_data.lower() == dataset[i][0].lower()):
            empty_list = []
            for j in range(1,len(dataset[i])):
                empty_list.append(int(dataset[i][j]))
            
            max_value = max(empty_list)
            max_index = empty_list.index(max_value)
            type_of_species = dataset[0][max_index+1]
            print ("\nThe most endanged number of species of", dataset[i][0],"is", max_value, "which are", type_of_species)

def minthreatfun(input_data,dataset):
    '''
    Function used to find the minimum of a specified index of array for the threatend species

    input_data = data given by the user
    dataset = array of data in which input_data is used to get the minimum value of the array index where input_data is present

    returns:
    none
    '''
    for i in range(len(dataset)):
        if (input_data.lower() == dataset[i][0].lower()):
            empty_list = []
            for j in range(1,len(dataset[i])):
                empty_list.append(int(dataset[i][j]))
            
            min_value = min(empty_list)
            min_index = empty_list.index(min_value)
            type_of_species = dataset[0][min_index+1]
            print ("\nThe most endanged number of species of", dataset[i][0],"is", min_value, "which are", type_of_species)


def maxfun(input_data,dataset):
    '''
    Function used to find the maximum of a specified index of array

    input_data = data given by the user
    dataset = array of data in which input_data is used to get the maximum value of the array index where input_data is present

    returns:
    none
    '''
    for i in range(len(dataset)):
        if (input_data.lower() == dataset[i][0].lower()):
            empty_list = []
            for j in range(1,len(dataset[i])):
                empty_list.append(int(dataset[i][j]))
            
            max_value = max(empty_list)
            print ("\nThe maximum population of", dataset[i][0],"between 2000-2020 was =", max_value)

def minfun(input_data,dataset):
    '''
    Function used to find the minimum of a specified index of array

    input_data = data given by the user
    dataset = array of data in which input_data is used to get the minimum value of the array index where input_data is present

    returns:
    none
    '''
    for i in range(len(dataset)):
        if (input_data.lower() == dataset[i][0].lower()):
            empty_list = []
            for j in range(1,len(dataset[i])):
                empty_list.append(int(dataset[i][j]))
            
            min_value = min(empty_list)
            print ("\nThe minimum population of", dataset[i][0],"between 2000-2020 was =", min_value)

def get_data(input_data, dataset):
    '''
    Function which gets the Y axis data to graph

    input_data = data given by the user
    dataset = array of data in which input_data is used to get the values for y axis data
    
    returns:
    data_list = list of y axis data
    '''
    data_list = []
    for i in range(len(dataset)):
        if (input_data.lower() == dataset[i][0].lower()):
            for j in range(1, len(dataset[i])):
                data_list.append(dataset[i][j])
    return data_list

def get_x_data(dataset):
    '''
    Function which gets the X axis data to graph

    
    dataset = array of data which is used to get the values for x axis data
    
    returns:
    data_list = list of x axis data
    '''
    data_list = []
    for i in range(1, len(dataset[0])):
        data_list.append(str(dataset[0][i]))
    return data_list


def print_Countries(dataset):
    '''
    Function to print all the countries

    parameters:

    dataset = array of data from which the countries need to be printed

    returns:
    none
    '''
    for i in range(len(dataset)):
        print ("\n",dataset[i][0])

def check_input(input_data,dataset):
    '''
    Function to check if the input giving by the user is present in the given dataset

    parameters:

    input_data = data given by the user to be checked
    dataset = array of data in which input_data is to be checked

    returns:
    True: if input is present in the array
    False: if input is not present in the array 
    '''
    for i in range(len(dataset)):
        if (input_data.lower() == dataset[i][0].lower()):
            return True
    else:
        return False

def print_General_data(input_data, dataset):
    '''
    Function to print general data of a country inputted by the user

    parameters:

    input_data = data given by the user
    dataset = array of data in which input_data is used to access other data

    returns:
    none
    '''
    for i in range(len(dataset)):
        if (input_data.lower() == dataset[i][0].lower()):
            print("\nShowing Data for =", dataset[i][0])
            print("The UN region for", dataset[i][0], "is", dataset[i][1])
            print("The UN sub-region for", dataset[i][0], "is", dataset[i][2])
            print("The area of", dataset[i][0], "is", dataset[i][3],"sqKm")

def print_species_data(input_data, dataset):
    '''
    Function to print species data of a country inputted by the user

    parameters:

    input_data = data given by the user
    dataset = array of data in which input_data is used to access other data

    returns:
    none
    '''
    for i in range(len(dataset)):
        if (input_data.lower() == dataset[i][0].lower()):
            print("\nShowing Data for =", dataset[i][0])
            print("The number of plants for", dataset[i][0], "is", dataset[i][1])
            print("The number of fish for", dataset[i][0], "is", dataset[i][2])
            print("The number of birds for", dataset[i][0], "is", dataset[i][3])
            print("The number of mammals for", dataset[i][0], "is", dataset[i][4])

def print_Population_data(input_data, input_year, dataset):
    '''
    Function to print population data of a country inputted by the user based on year inputted by the user

    parameters:

    input_data = data given by the user
    input_year = data given by the user
    dataset = array of data in which input_data and input_year is used to access other data

    returns:
    none
    '''
    for i in range(len(dataset)):
        if (input_data.lower() == dataset[i][0].lower()):
            print ("\nthe population of",dataset[i][0], "in the year", input_year, "is", dataset[i][input_year-1999])

def compare_population(dataset, input_year, country_1, country_2):

    for i in range(len(dataset)):
        if (country_1.lower() == dataset[i][0].lower()):

            for l in range(len(dataset)):
                if (country_2.lower() == dataset[l][0].lower()):

                    if (dataset[i][input_year-1999] > dataset[l][input_year-1999]):
                        difference = int(dataset[i][input_year-1999]) - int(dataset[l][input_year-1999])
                        print("\nThe diffrence in population of", dataset[i][0],"and", dataset[l][0], "in the year", input_year,'is',abs(difference))

                    elif (dataset[l][input_year-1999] > dataset[i][input_year-1999]):
                        difference = int(dataset[l][input_year-1999]) - int(dataset[i][input_year-1999])
                        print("\nThe diffrence in population of", dataset[l][0],"and", dataset[i][0], "in the year", input_year,'is',abs(difference))

def compare_area (dataset, country_1, country_2):
    for i in range(len(dataset)):
        if (country_1.lower() == dataset[i][0].lower()): 

            for l in range(len(dataset)):
                if (country_2.lower() == dataset[l][0].lower()): 

                    if (dataset[i][3] > dataset[l][3]):
                        difference = int(dataset[i][3]) - int(dataset[l][3])
                        print('\nDiffrence in Area of', dataset[i][0],"and",dataset[l][0], 'is', abs(difference),"sqKm") 

                    elif (dataset[l][3] > dataset[i][3]):
                        difference = int(dataset[l][3]) - int(dataset[i][3])
                        print('\nDiffrence in Area of', dataset[l][0],"and", dataset[i][0], 'is', abs(difference),"sqKm")     

def compare_species (dataset, animal, animal_num, country_1, country_2):
    for i in range(len(dataset)):
        if (country_1.lower() == dataset[i][0].lower()): 

            for l in range(len(dataset)):
                if (country_2.lower() == dataset[l][0].lower()): 

                    if (dataset[i][animal_num] > dataset[l][animal_num]):
                        difference = int(dataset[i][animal_num]) - int(dataset[l][animal_num])
                        print('\nThe diffrence in  number of', animal, 'between', dataset[i][0], 'and', dataset[l][0], 'is', abs(difference)) 

                    elif (dataset[l][animal_num] > dataset[i][animal_num]):
                        difference = int(dataset[l][animal_num]) - int(dataset[i][animal_num])
                        print('\nThe diffrence in  number of', animal, 'between', dataset[l][0], 'and', dataset[i][0], 'is', abs(difference)) 


def calculate_proportion(country, animal, animal_num, dataset):
    for i in range(len(dataset)):
        if(country.lower() == dataset[i][0].lower()):

            total = int(dataset[i][1]) + int(dataset[i][2]) + int(dataset[i][3]) + int(dataset[i][4])
            percentage = (total/100) * int(dataset[i][animal_num])

            print("\nTotal number of species:", total)
            print('Percentage of', animal, "is:", percentage)

def check_year(year):
    if year>=2000 and year<=2020:
        return True
    else:
        return False

#Start of main function
def main():

    #Importing csv data
    results_1 = []
    with open("Country_Data.csv") as csvfile:
        reader = csv.reader(csvfile) # change contents to floats
        for row in reader: # each row is a list
            results_1.append(row)

    results_1 = np.array(results_1)
    
    results_2 = []
    with open("Population_Data.csv") as csvfile:
        reader = csv.reader(csvfile) # change contents to floats
        for row in reader: # each row is a list
            results_2.append(row)

    results_2 = np.array(results_2)
    
    results_3 = []
    with open("Threatened_Species.csv") as csvfile:
        reader = csv.reader(csvfile) # change contents to floats
        for row in reader: # each row is a list
            results_3.append(row)

    results_3 = np.array(results_3)
    

    country_data = results_1
    pop_data = results_2
    threat_data = results_3

    #Menu print for the user
    while True:
        print("\nWhat would you like to do?")
        print("(1) View list of countries to choose from")
        print("(2) View General data for a country")
        print("(3) View Population data for a country for a specific year")
        print("(4) View species data for a country")
        print("(5) Graph data")
        print("(6) Compare data")
        print("(7) See species percentage")
        print("(8) See max, min, avg data")
        print("(0) To quit the program")

        #Ask user for their choice
        ans = (input("\nPlease choose which one you would like to do = "))
        
        #If statement for the first menu option
        if (ans == "1"):
            print_Countries(country_data) 

         #If statement for the second menu option
        elif (ans == "2"):
            while True:
                user_input = input("\nPlease enter the country whose data you would like to view = ")

                valid_check = check_input(user_input, country_data) #function to check if input is valid

                #if statement to print general data
                if valid_check == True:
                    print_General_data(user_input, country_data)
                    break
                elif valid_check == False:
                    print("\nPlease enter a valid country\n HINT: Choose option 1 to see a list of countries")

        #If statement for the third menu option
        elif(ans == "3"):
            while True:
                #input country and year
                user_input = input("\nPlease enter the country whose data you would like to view = ")
                year_input = int(input("\nEnter the year for which you would like to see data (2000 - 2019) = "))
                #checks if inputs are valid
                valid_check = check_input(user_input, country_data)
                y_check = check_year(year_input)
                #start using function to print population data if everything is valid
                if (y_check == True) and (valid_check == True):
                    print_Population_data(user_input,year_input,pop_data)
                    break
                elif (y_check == False):
                    print("\nInput not valid\nPlease enter an integer (2000-2019)\n")

                elif (valid_check == False):
                    print("\nPlease enter a valid country\n HINT: Choose option 1 to see a list of countries")

                elif (y_check == False) and (valid_check == False):
                    print("\nPlease check your inputs, both are not valid")

        #If statement for the fourth menu option
        elif(ans == "4"):
            while True:
                #input country
                user_input = input("\nPlease enter the country whose data you would like to view = ")
                #check if input is valid
                valid_check = check_input(user_input, threat_data)
                #start using function to print species data if everything is valid
                if valid_check == True:
                    print_species_data(user_input, threat_data)
                    break
                #keeps asking for input until it is valid
                elif valid_check == False:
                    print("\nPlease enter a valid country\n HINT: Choose option 1 to see a list of countries")
        #If statement for the fifth menu option
        elif(ans == "5"):
            while True:
                print("\n(1) Graph population data")
                print("(2) Graph species data")
                print("(0) Go back <-")
                input_choice = input("\nPlease choose which graph you would like to plot = ")

                #if statement for first menu option
                if (input_choice == "1"):
                    while True:
                        #input country and check if it is valid
                        user_input = input("\nPlease enter the country whose data you would like to view = ")
                        valid_check = check_input(user_input, country_data)
                        #gets y data
                        graph_pop_data = get_data(user_input,pop_data)
                        #gets x data

                        int_graph_data = []
                        for i in graph_pop_data:
                            int_graph_data.append(int(i))
                        country_x_data = get_x_data(pop_data)

                        int_graph_data.reverse()
                        #if statement for graphing if input is valid
                        if(valid_check == True):     
                            graph_data = Graph(country_x_data, int_graph_data, user_input)
                            graph_data.line_Graph()
                            break
                        #keeps asking for input until it is valid
                        elif (valid_check == False):
                            print("\nPlease enter a valid country\n HINT: Choose option 1 to see a list of countries")
                    break
                #if statement for second menu option
                elif (input_choice == "2"):
                    while True:
                        #input country and check if it is valid
                        user_input = input("\nPlease enter the country whose data you would like to view = ")
                        valid_check = check_input(user_input, country_data)
                        #gets y data
                        graph_threat_data = get_data(user_input, threat_data)
                        #gets x data
                        threat_x_data = get_x_data(threat_data)
                        
                        #convert to intager
                        int_graph_threat_data = []
                        for i in graph_threat_data:
                            int_graph_threat_data.append(int(i))
                        
                        #if statement to graph if input is valid
                        if(valid_check == True):
                            graph_data = Graph(threat_x_data, int_graph_threat_data, user_input)
                            graph_data.bar_Graph()
                            break
                        #keeps asking for input until it is valid
                        elif (valid_check == False):
                            print("\nPlease enter a valid country\n HINT: Choose option 1 to see a list of countries")
                        elif (valid_check == False):
                            print("\nPlease enter a valid country\n HINT: Choose option 1 to see a list of countries")
                    break
                #if statement for third menu option
                elif (input_choice == "0"):
                    break

                else:
                    print("\nPlease choose a valid option!")

        elif(ans == "6"):
            while True:
                valid_inputs = {'Population', 'Area', 'Species'}
                user_input = input("\nPlease enter which data you want to compare(Population, Area, Species) or 'quit' to stop the program :")
                if user_input == 'quit':
                    break

                #if user's choice is in valid inputs start next step of the program
                if user_input in valid_inputs:
                    #input two countries to compare and check if they are valid
                    country_1 = input('Please choose first country you want to compare:')
                    country_2 = input('Please choose second country you want to compare:')
                    valid_check_1 = check_input(country_1, pop_data)
                    valid_check_2 = check_input(country_2, pop_data)

                    if (valid_check_1 == True) and (valid_check_2 == True):
                        #ask the year if choice is 'Population' and use function to compare population
                        if user_input == 'Population':      
                            year = int(input('\nPlease choose the year:'))
                            y_check = check_year(year)
                            if (y_check == True):
                                compare_population(pop_data, year, country_1, country_2)
                                break

                        #use compare function if choice is 'Area'
                        elif user_input == 'Area':
                            compare_area(country_data, country_1, country_2)
                            break
                        #ask to choose from a list of species and use function for comparing 
                        elif user_input == 'Species':
                            while True:
                                animal = input('\nChoose who you want to compare (plants, fish, birds, mammals) or "quit" to stop the program:')
                                #if statement for quiting the program
                                if animal == 'quit':
                                    break
                                check_animal = check_species(animal, threat_data)
                                #creates numeration for chosen specie to use that in a function
                                if check_animal ==True:
                                    if animal == 'plants':
                                        animal_num = 1
                                    elif animal == 'fish':
                                        animal_num = 2  
                                    elif animal == 'birds':
                                        animal_num = 3  
                                    elif animal == 'mammals':
                                        animal_num = 4        
                                    compare_species(threat_data, animal, animal_num, country_1, country_2)
                                    break
                                elif check_animal == False:
                                    print('Sorry, enter valid specie')
                    #keeps asking for input until it is valid
                    elif (valid_check_1 == False) or (valid_check_2 == False):
                            print("\nPlease enter a valid country\n HINT: Choose option 1 to see a list of countries")
                else:
                    print('\nPlease choose valid data.')

        #If statement for the seventh menu option
        elif(ans == '7'):
            while True:
                #input country and choose one of the species
                country = input('Please choose country:')
                animal = input('Please choose which percentage you want to see:')
                valid_check = check_input(country, threat_data)

                if valid_check == True:
                    #creates numeration for chosen specie to use that in a function
                    if animal == 'plants':
                        animal_num = 1
                    elif animal == 'fish':
                        animal_num = 2  
                    elif animal == 'birds':  
                        animal_num = 3  
                    elif animal == 'mammals':
                        animal_num = 4     

                    calculate_proportion(country, animal, animal_num, threat_data)
                    break   
                #keeps asking for input until it is valid
                elif valid_check == False:
                    print("\nPlease enter a valid country\n HINT: Choose option 1 to see a list of countries")
        
        #If statement for eighths menu option
        elif(ans == '8'):
            while True:
                #prints main menu
                print("\n(1) Max")
                print("(2) Min")
                print("(3) Average/Mean")
                print("(0) Go back <-")
                #asks for input
                user_choice = input("\nWhich one would you like to do = ")

                #if statemnet for first main menu option
                if (user_choice == "1"):
                    while True:
                        #prints sub-menu and asks for input
                        print("\n(1) Max population of a certain country between 2000 and 2021")
                        print("(2) Most threatend species of a certain country")
                        print("(3) Find the country with max population for certain year")
                        print("(4) Find ccountry with max threatend species for a certain type of species")
                        print("(0) Go back <-")
                        user_choice = input("\nWhich one would you like to do = ")

                        #if statement for first sub-menu option to find max population
                        if (user_choice == "1"):
                            while True:
                                #asks to input country
                                user_input = input("\nPlease enter the country whose data you would like to view = ")
                                valid_check = check_input(user_input, country_data)
                            
                                #uses function if everything is valid
                                if(valid_check == True):
                                    maxfun(user_input, pop_data)
                                    break
                                elif (valid_check == False):
                                    print("\nPlease enter a valid country\n HINT: Choose option 1 to see a list of countries")

                        #if statement for second sub-menu option to find most endagered specie
                        elif (user_choice == "2"):
                            
                            while True:
                                #asks to input country
                                user_input = input("\nPlease enter the country whose most threatend number of species you would like to view = ")
                                valid_check = check_input(user_input, country_data)
                                
                                #uses function if everything is valid
                                if(valid_check == True):
                                    maxthreatfun(user_input, threat_data)
                                    break
                                elif (valid_check == False):
                                    print("\nPlease enter a valid country\n HINT: Choose option 1 to see a list of countries")

                        #if statement for third sub-menu option to find country with country with max population in certain year 
                        elif (user_choice == "3"):
                            while True:
                                #asks to input year
                                year_input = int(input("\nEnter the year for which you would like to see data (2000 - 2019) = "))
                                y_check = check_year(year_input)

                                #uses function if everything is valid
                                if (y_check == True):
                                    max_in_columb(year_input,pop_data)
                                    break
                                else:
                                   print("\nInput not valid\nPlease enter an integer (2000-2019)\n")

                        #if statement for third sub-menu option to find the country with max threatend species for a certain type of species
                        elif (user_choice == "4"):
                            while True:
                                 #asks to input specie type and checks if it is valid
                                user_input = input("\nPlease enter the species type of which you would like to see max= ")
                                valid_check_species = check_species(user_input,threat_data)

                                #uses function if everything is valid
                                if(valid_check_species == True):
                                    max_threat_in_row(user_input, threat_data)
                                    break
                                elif (valid_check_species == False):
                                    print("\nPlease enter a valid species type\n")
                        
                        #if statement for fourth sub-menu option
                        elif (user_choice == "0"):
                            break
                        #if statement for wrong sub-menu option
                        else:
                            print("\nPlease choose a valid option!")

                #if statement for second main menu option
                elif (user_choice == "2"):
                    while True:
                        #prints sub-menu and asks for user's choice
                        print("\n(1) Minimum population of a certain country between 2000 and 2021")
                        print("(2) Least threatend species of a certain country")
                        print("(3) Find the country with min population for certain year")
                        print("(4) Find the country with min threatend species for a certain type of species")
                        print("(0) Go back <-")
                        user_choice = input("\nWhich one would you like to do = ")

                        #if statement for first sub-menu option to find min population
                        if (user_choice == "1"):
                            while True:
                                #asks for input and checks if it is valid
                                user_input = input("\nPlease enter the country whose data you would like to view = ")
                                valid_check = check_input(user_input, country_data)

                                #uses function if everything is valid
                                if(valid_check == True):
                                    minfun(user_input, pop_data)
                                    break
                                elif (valid_check == False):
                                    print("\nPlease enter a valid country\n HINT: Choose option 1 to see a list of countries")

                        #if statement for second sub-menu option to find least endagered specie
                        elif (user_choice == "2"):
                            while True:
                                #asks for input and checks if it is valid
                                user_input = input("\nPlease enter the country whose most threatend number of species you would like to view = ")
                                valid_check = check_input(user_input, country_data)

                                #uses function if everything is valid
                                if(valid_check == True):
                                    minthreatfun(user_input, threat_data)
                                    break
                                elif (valid_check == False):
                                    print("\nPlease enter a valid country\n HINT: Choose option 1 to see a list of countries")
                        
                        #if statement for third sub-menu option to find country with country with min population in certain year
                        elif (user_choice == "3"):
                            while True:
                                #asks for input and checks if it is valid
                                year_input = int(input("\nEnter the year for which you would like to see data (2000 - 2019) = "))
                                y_check = check_year(year_input)

                                #uses function if everything is valid
                                if (y_check == True):
                                    min_in_columb(year_input,pop_data)
                                    break
                                else:
                                   print("\nInput not valid\nPlease enter an integer (2000-2019)\n")

                         #if statement for third sub-menu option to find the country with min threatend species for a certain type of species
                        elif (user_choice == "4"):
                            while True:
                                #asks for input and checks if it is valid
                                user_input = input("\nPlease enter the species type of which you would like to see min= ")
                                valid_check_species = check_species(user_input,threat_data)

                                #uses function if everything is valid
                                if(valid_check_species == True):
                                    min_threat_in_row(user_input, threat_data)
                                    break
                                elif (valid_check_species == False):
                                    print("\nPlease enter a valid species type\n")

                        #if statement for fourth sub-menu option
                        elif (user_choice == "0"):
                            break

                        else:
                            print("\nPlease choose a valid option!")

                #if statement for third main menu option
                elif(user_choice == "3"):
                    #prints menu and aks for a sub-menu choice
                    print("\n(1) Average population of a country between 2000 and 2020")
                    print("(2) Average number of endangered species of a country")
                    print("(0) Go back <-")
                    user_choice = (input("\nWhich one would you like to do = "))
                    
                    #if statement for first sub-menu option to find average population
                    if(user_choice == "1"):
                        
                        while True:
                            #asks to input country
                            user_input = input("\nPlease enter the country whose average population you would like to view = ")
                            valid_check = check_input(user_input, country_data)
                            
                            #uses function if everything is valid
                            if(valid_check == True):
                                avgfun(user_input, pop_data)
                                break
                            elif (valid_check == False):
                                print("\nPlease enter a valid country\nHINT: Choose option 1 to see a list of countries")
                    
                    #if statement for second sub-menu option to find average number of species
                    elif (user_choice == "2"):

                        while True:
                            #asks to input country
                            user_input = input("\nPlease enter the country whose avg threatend number of species you would like to view = ")
                            valid_check = check_input(user_input, country_data)
                            
                            #uses function if everything is valid
                            if(valid_check == True):
                                avgthreatfun(user_input, threat_data)
                                break
                            elif (valid_check == False):
                                print("\nPlease enter a valid country\n HINT: Choose option 1 to see a list of countries")

                    #if statement for third sub-menu option to quit
                    elif (user_choice == "0"):
                        break
                    
                #if statement for fourth sub-menu option to quit
                elif(user_choice == "0"):
                    break

                else:
                    print("\nPlease choose a valid option!")

        #If statement for the eights menu option
        elif(ans == '0'):
            #quits the program
            print('Thank you for using our program!')
            break


        else:
            print("\nplease enter a valid option\n")        

if __name__ == '__main__':
    main()
