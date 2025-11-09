questions = {
        "What is the capital of France?": "Paris",
         "2 + 2 = ? ":"4",
        "python is a ______?": "programing language"  
}

score = 0
for q, a in questions.items():
    answer = input(q+" ")
    if answer.strip().lower() == a.lower():
        print('Correct')
        score += 1
    else:
        print("Wrong")
        
        
print('Your score:', score , '/' ,len(questions))