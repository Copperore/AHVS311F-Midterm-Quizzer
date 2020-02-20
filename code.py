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
            print(Fore.WHITE + Back.RED + 'WRONG' + Style.RESET_ALL + " - " + self.choices[self.answer-1])
            #print(self.choices)
            #print(self.answer)

with open('questions.txt', 'r') as f:
    data = f.read().split('\n')

qlist = []
ccount = 0
q = ''
a = ''
cs = []

numas = 0
numbs = 0
numcs = 0
numds = 0
numes = 0
numalls = 0
totalalls = 0
numnones = 0
totalnones = 0

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

                # get counts to find most common answer
                if "All of " in line:
                    totalalls += 1
                    if line[0].islower():
                        numalls += 1

                if "None of " in line:
                    numnones += 1
                    if line[0].islower():
                        totalnones += 1

                if(line[0] == 'a'):
                    numas += 1
                elif(line[0] == 'b'):
                    numbs += 1
                elif(line[0] == 'c'):
                    numcs += 1
                elif(line[0] == 'd'):
                    numds += 1
                elif(line[0] == 'e'):
                    numes += 1


        else:
            qlist.append(question(q, cs, a))
            cs = []

total = numas + numbs + numcs + numds + numes
print("Percent of the time the answer is: ")
print("A: " + str(numas/total*100))
print("B: " + str(numbs/total*100))
print("C: " + str(numcs/total*100))
print("D: " + str(numds/total*100))
print("E: " + str(numes/total*100))
print("*NOTE* The stats for E dont yet reflect only answers that have 5 options")
#print("All of the above: " + str(numalls/totalalls*100))
#print("None of the above: " + str(numnones/totalnones*100))


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
