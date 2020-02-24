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

with open('questions.txt', 'r', encoding='utf8') as f:
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
totales = 0

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

            # finds percent of answer being All of the Above
            if line[3:9] == "All of":
                totalalls += 1
                if line[0].islower():
                    numalls += 1

            # finds percent of answer being None of the Above
            if line[3:10] == "None of":
                numnones += 1
                if line[0].islower():
                    totalnones += 1

            # finds percent of answer being each option
            if (line[0].islower()):
                a = ccount

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
                    totales += 1

            # counts questions that have 5 choices instead of 4
            if(line[0] == "E"):
                totales += 1

        else:
            qlist.append(question(q, cs, a))
            cs = []

total = numas + numbs + numcs + numds + numes
print("\n******************************************************************")
print('\t' + "STATISTICS OF ANSWER DISTRIBUTIONS\n")
print("\tPercent of the time the answer is: ")
print("\tA: " + str(round(numas/total*100)))
print("\tB: " + str(round(numbs/total*100)))
print("\tC: " + str(round(numcs/total*100)))
print("\tD: " + str(round(numds/total*100)))
print("\n\tE: " + str(round(numes/totales*100)) + "\t\t\t(Only when E is an option)")
print("\tAll of the above:  " + (str(round(numalls/totalalls*100)) if totalalls != 0 else "0") + "\t(Only when All is an option)")
print("\tNone of the above: " + (str(round(numnones/totalnones*100)) if totalnones != 0 else "0") + "\t(Only when None is an option)")
print("******************************************************************")


acceptedInput = [1, 2, 3, 4, 5]

while(True):
    userAns = None
    current = random.choice(qlist)
    current.print_question()

    while userAns is None:
        userAns = input("Enter your answer: ")
        try:
            if userAns in str(acceptedInput):
                a = int(userAns)
                current.check_answer(a)

            #TODO: add results and skip option

            else:
                userAns = None
                raise ValueError("Dummy")

        except ValueError as ve:
            continue
