# -*- coding: utf-8 -*-
"""Untitled40.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/19rmUhSNV7Gnz1mL1y-pb-SNWMPMskinR
"""

import random
import pandas as pd

from datetime import datetime
def main():
    studentId = 'Student_' + str(random.randint(0, 10000))
    print (studentId)
    num_rounds = 8
    conditions = ["TPT"] * 4 + ["QD"] * 4

    responses = []
    #

    earnings_a = 0
    earnings_b = 0
    price_a = 0
    price_b = 0
    quantity = 0
    fixed_fee = 0
    x = 0
    y = 0
    print("********************       Welcome to the Pricing Game Study!     ***************************")
    print("     Player A: Automated | Player B: Student\n\n")

    for round_num in range(1, num_rounds + 1):
        condition = conditions[round_num - 1]
        print(f"--- Round {round_num}: Condition = {condition} ---")

        if condition == "TPT":
            price_a = random.randint(0, 10)
            fixed_fee = random.randint(0, 10)
            print(f"      Player A has set PRICE A = {price_a} and FIXED FEE = {fixed_fee}.")
            accept = input("      Player B, do you accept the offer? (yes/no): ").strip().lower()
            while accept not in ["yes", "no"]:
                print("     Invalid input. Please enter 'yes' or 'no'.")
                accept = input("    Player B, do you accept the offer? (yes/no): ").strip().lower()

            if accept == "no":
                print("     Player B rejected the offer. No earnings for this round.\n\n")
                #responses.append({"Round": round_num, "Condition": condition, "Accepted": False, "Earnings A": 0, "Earnings B": 0})
                earnings_a = 0
                earnings_b = 0
                responses.append({"Round": round_num, "Condition": condition,  "Price_A":0, "x":x, "y":fixed_fee, "Accept": False,"Price_B":'',"Quatity":10, "Earnings A": 0, "Earnings B": 0,"studentId":studentId})


            else:
              price_b = input("     Player B, set your selling price (PRICE B, must be 1-10): ")
              while not(price_b.isdigit()) or int(price_b) < 1 or int(price_b) > 10:
                 print("     Invalid input ")
                 price_b = input("     Player B, set your selling price (PRICE B, must be 1-10): ")
              price_b = int(price_b)
              quantity = 10 - price_b
              earnings_a = (price_a - 2) * quantity + fixed_fee
              earnings_b = (price_b - price_a) * quantity - fixed_fee
              y = fixed_fee
        elif condition == "QD":

            x = random.randint(1, 10)
            y = random.randint(1, 10)
            fixed_fee = ''
            print(f"      Player A has proposed the pricing scheme: PRICE A = {x} + ({y} / QUANTITY).")

            accept = input("      Player B, do you accept the offer? (yes/no): ").strip().lower()
            while accept not in ["yes", "no"]:
                print("     Invalid input. Please enter 'yes' or 'no'.")
                accept = input("      Player B, do you accept the offer? (yes/no): ").strip().lower()
            if accept == "no":
                print("     Player B rejected the offer. No earnings for this round.\n\n")
                #responses.append({"Round": round_num, "Condition": condition, "Accepted": False, "Earnings A": 0, "Earnings B": 0})
                earnings_a = 0
                earnings_b = 0
                responses.append({"Round": round_num, "Condition": condition,  "Price_A":price_a, "x":x, "y":y, "Accept": False,"Price_B":'',"Quantity":10, "Earnings A": 0, "Earnings B": 0,"studentId":studentId})
            elif accept == "yes":
                price_b = int(input("     Player B, set your selling price (PRICE B, must be 1-10): "))
                quantity = 10 - price_b
                if quantity > 0:
                  price_a = x + (y / quantity)
                  print(f"      Calculated PRICE A = {price_a:.2f}, QUANTITY = {quantity}.")
                else:
                  print ("      your price is causing a null demand\n\n")
                  responses.append({"Round": round_num, "Condition": condition,  "Price_A":price_a, "x":x, "y":y, "Accept": False,"Price_B":0,"Quantity":quantity, "Earnings A": 0, "Earnings B": 0,"studentId":studentId})
            else:
                print ('      Invalid value, please try again')
          #  accept = input("Player B, do you accept the offer? (yes/no): ").strip().lower()


            earnings_a = (price_a - 2) * quantity


            earnings_b = (price_b - price_a) * quantity

        responses.append({ "Round": round_num, "Condition": condition,  "Price_A":price_a, "x":x, "y":y, "Accept": True,"Price_B":price_b,"Quantity":quantity, "Earnings A":earnings_a,"Earnings B":earnings_b,"studentId":studentId})
        responses

        print(f"      Player A earned {earnings_a:.2f} points. Player B earned {earnings_b:.2f} points.\n")


    df= pd.DataFrame (responses,columns=['Round',"Condition",'Price_A', 'x', 'y', 'Accept', 'Price_B', 'Quantity', 'Earnings A', 'Earnings B', 'studentID'])
    file_name = "responses" + studentId +".csv"
   #print (file_name)
    df.to_csv("https://github.com/miroslava-msm/ReplicationStudy_Group/blob/main/ReplicationStudy.py/"+file_name, index=False)
    print("     Game Over! Responses have been saved for analysis.")


if __name__ == "__main__":


    main()
