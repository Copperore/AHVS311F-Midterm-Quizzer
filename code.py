import random
from colorama import Fore, Back, Style

class question:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    def print_question(self):
        print('\n' + self.question)
        for x in range(1, len(self.choices)+1):
            ans = self.choices[x-1]
            print('\t' + str(x) + ")" + ans[2:])

    def check_answer(self, input):
        if input == self.answer:
            print(Fore.WHITE + Back.GREEN + 'CORRECT' + Style.RESET_ALL)
        else:
            print(Fore.WHITE + Back.RED + 'WRONG' + Style.RESET_ALL)
            #print(self.choices)
            #print(self.answer)

with open('questions.txt', 'r') as f:
    data = f.read().split('\n')

qlist = []
ccount = 0
q = ''
a = ''
cs = []

for line in data:
    if line.startswith("X.)"):
        ccount = 0
        q = line
        continue

    else:
        if line:
            ccount += 1
            cs.append(line)
            if (line[0].islower()):
                a = ccount

        else:
            qlist.append(question(q, cs, a))
            cs = []

acceptedInput = [1, 2, 3, 4, 5, 'r', 's']

while(True):
    userAns = None
    current = random.choice(qlist)
    current.print_question()

    while userAns is None:
        userAns = input("Enter your answer: ")
        try:
            if userAns in str(acceptedInput[:5]):
                a = int(userAns)
                current.check_answer(a)

            #TODO: add results and skip option

            else:
                userAns = None
                raise ValueError("Dummy")

        except ValueError as ve:
            continue
