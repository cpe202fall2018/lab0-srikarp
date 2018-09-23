def weight_on_planets():
   # write your code here

  earthWeightInput = input("What do you weigh on earth? ")
  earthWeightFloat = float(earthWeightInput)
  print ("\nOn Mars you would weigh ", earthWeightFloat*0.38, " pounds.\n" + "On Jupiter you would weigh ", earthWeightFloat*2.34, " pounds.") 

   
if __name__ == '__main__':
   weight_on_planets()