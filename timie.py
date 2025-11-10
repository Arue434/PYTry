import time
import random

numerous_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
calculation_list = ['+', '-', '*', '/']

while True:

    start_time = time.time()
    heart = 10
        
    while True:
        lanjut = input("Ketik 'p' untuk lanjut atau 'n' untuk keluar: ").strip().lower()
        if lanjut == 'n':
            print("Terima kasih telah menggunakan program ini!!!")
            exit()
        elif lanjut == 'p':
            print("===============================================================")
            print("Game Start!")
            print("You have 10 hearts. Each wrong answer costs 1 heart.")
            print("===============================================================")
            break 
        else:
            print("Input tidak valid!")
            print("===============================================================")

    while heart > 0:

        num1 = random.choice(numerous_list)
        num2 = random.choice(numerous_list)
        operation = random.choice(calculation_list)

        if operation == '/' and num2 == 0:
            num2 = 1

        expression = f"{num1} {operation} {num2}"
        question = (f"what is {expression}?")
        elapsed_time = int(time.time() - start_time)
        print("================================================================")
        print(f"Elapsed Time: {elapsed_time} seconds | Hearts: {heart}")
        print(question)
        print("================================================================")   

        try:
            correct_answer = round(eval(expression), 1)

            answer = float(input("Your answer: "))

            if answer == correct_answer:
                print("Correct!")
            
            else:
                heart -= 1
                print(f"Wrong answer! The correct answer is {correct_answer}. Remaining hearts: {heart}")
            
        except ValueError:
            print("Invalid input! Please enter a number.")
        
        except ZeroDivisionError:
            print("Division by zero is not allowed.")

        time.sleep(1)

        if elapsed_time // 30 == 0 and elapsed_time:
            last_penalty_time = elapsed_time // 30
            heart -= 1
            print("30 seconds passed! You lost 1 heart due to time penalty.")

        if heart <= 0:
            print("Game Over! You have no hearts left.")
            break

        print ("thank you for playing the game!")

        