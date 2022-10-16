import pandas as pd
import random

df = pd.read_excel("/Users/manojkl/Documents/Language/english_german.xlsx")

df_length = len(df)

num_old = 0
flag = False

while True:
    print("==============================================================================================")
    num = random.sample(range(df_length), 1)
    print(num, num_old)
    while num[0] == num_old:
        num = random.sample(range(df_length), 1)
        # print(num, num_old)

    num_old = num[0]

    a = df.iloc[num[0]]["english_sentences"]
    b = df.iloc[num[0]]["german_sentences"]

    while flag == False:
        translated = input("Enter the translated sentence for "+a+": ")
        if translated == b:
            print("Correctly translated! ")
            print("The translated input for: "+ a + " is " +translated)
            flag = True
        elif translated == "pass":
            print("The correct translation is: "+b)
            flag = True
        else:
            print("Try once again :)")
            print("--------------------------------------------------------------------------------------")
    flag = False