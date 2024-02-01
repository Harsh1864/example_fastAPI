
questions = [["which language is use to create facebook?",
            "python","java","php","js","None",4],
["1 which language is use to create facebook?",
            "python","java","php","js","None",4],
["2 which language is use to create facebook?",
            "python","java","php","js","None",4],
["3 which language is use to create facebook?",
            "python","java","php","js","None",4],
["4 which language is use to create facebook?",
            "python","java","php","js","None",4],
["5 which language is use to create facebook?",
            "python","java","php","js","None",4],
["6 which language is use to create facebook?",
            "python","java","php","js","None",4],
["7 which language is use to create facebook?",
            "python","java","php","js","None",4],
["8 which language is use to create facebook?",
            "python","java","php","js","None",4],
["9 which language is use to create facebook?",
            "python","java","php","js","None",4],
["10 which language is use to create facebook?",
            "python","java","php","js","None",4],
["11 which language is use to create facebook?",
            "python","java","php","js","None",4],
["12 Which language is use to create facebook?",
            "python","java","php","js","None",4]
]


levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000,740000,1500000,100000000]
money = 0

for i in range(0,len(questions)):
    question = questions[i]
    # print(f"your question of {levels[i]}")
    print(f"{question[0]}")
    print(f"A.{question[1]}                    B.{question[2]}")
                
    print(f"C.{question[3]}                    D.{question[4]}")

    reply = int(input("Enter your answer (1-4) :"))
    if(reply == question[-1]):
        print(f"Correct answer congratulations you have won Rs. {levels[i]}")
        if(i == 4):
            money=10000
        elif(i == 9):
            money = 320000
        elif(i == 124):
            money = 10000000

    else:
        print("Wrong answer")
        break

print(f"You take a money {money}")




