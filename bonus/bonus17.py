import json

with open('question.jason', 'r') as file:
    content = file.read()

data = json.loads(content)
score = 0
for question in data:
    print(question['Question text'])
    for index, alternative in enumerate(question['Alternatives']):
        print(index+1, '_', alternative)
    user_answer = input('Please enter your answer: ')
    question["user_answer"] = user_answer


for index, question in enumerate(data):
    if question["user_answer"] == question["Correct answer"]:
        score = score+1
        result = 'Correct answer'
    else:
        result = 'Wrong answer'
    print(f"{index+1}- {result}")

print(score,"/",len(data))



