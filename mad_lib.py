#Mad Lib is a game which allows users input different verbs, adjectives, punctuation marks into a particular story while completing the story.
#I made a few upgrades to the game such that you can know what your score is at the end of the game and see the correct answer.
#I picked my story from the Holy Bible
# The story comprises of 5 Bible verses from the book of Matthew 5 
adj1 = "...."
verb1 = "...."
adj2 = "...."
noun1 = '....'
verb2 = '....'
noun2 = '....'
adj3 = "...."
story = f"Blessed are the {adj1} in spirit: for theirs is the {noun1} in heaven.  Blessed are they that {verb1}: for they shall be comforted. Blessed are the {adj2}: for they shall inherit the earth. Blessed are they which do {verb2} and thirst after {noun2}: for they shall be filled. Blessed are the {adj3}: for they shall obtain mercy. Blessed are the pure in heart: for they shall see God. Blessed are the peacemakers : for they shall be called the children of God. "
# Blessed are they which are persecutted for righteousness' sake: for theirs is the kingdom of heaven. 
# Blessed are ye, when men shall revile you, and persecute you, and shall say all manner of evil against you falsely, for my sake."
print(story)
adj1 = input('Pls input noun1: '); adj1 = adj1.lower()
noun1 = input('Pls input noun2: '); noun1 = noun1.lower()
verb1 = input('Pls input verb1: '); verb1 = verb1.lower()
adj2 = input("Pls input adj2: "); adj2 = adj2.lower()
verb2 = input("Pls input verb2: "); verb2 = verb2.lower()
noun2 = input("Pls input noun2: "); noun2 = noun2.lower()

Answer_List1= [adj1, noun1, verb1, adj2,verb2, noun2]
Answer_List =["poor", "kingdom", "mourn", "meek","hunger","righteousness"]
if Answer_List1 == Answer_List:
    score = len(Answer_List1)
else:
    list = [Answer_List1 == Answer_List]
    score = len(list)

story = f"Blessed are the {adj1} in spirit: for theirs is the {noun1} in heaven.  Blessed are they that {verb1}: for they shall be comforted. Blessed are the {adj2}: for they shall inherit the earth. Blessed are they which do hunger and thirst after righteousness: for they shall be filled. Blessed are the merciful: for they shall obtain mercy. Blessed are the pure in heart: for they shall see God. Blessed are the peacemakers : for they shall be called the children of God. Blessed are they which are persecutted for righteousness' sake: for theirs is the kingdom of heaven. Blessed are ye, when men shall revile you, and persecute you, and shall say all manner of evil against you falsely, for my sake."
print(story)
print(f"Your score is {score}")
