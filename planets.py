def weight_on_planets():
   # write your code here
  print("What do you weigh on earth? ", end = '')
  earthWeightInput = input()
  earthWeightFloat = float(earthWeightInput)
  print ("\nOn Mars you would weigh " + str(earthWeightFloat*0.38) + " pounds.\n" + "On Jupiter you would weigh " + str(earthWeightFloat*2.34) + " pounds.") 

   
if __name__ == '__main__':
   weight_on_planets()