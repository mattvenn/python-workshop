total_questions = 2
current_question = 1
score = 0

#introduction
print "welcome to Matt's quiz!"
print "there are", total_questions, "questions in the quiz"

#function to ask the questions and get the answers
def ask_question(question,answer):
    print "-" * 20
    print "question", current_question, "of", total_questions
    guess = raw_input(question + "? ")
    #make the answers lower case before comparing them
    if guess.lower() == answer.lower():
        print "well done!"
        return True
    else:
        print "better luck next time!"
        return False

if ask_question("what is 5+2","7"):
    score += 1
current_question += 1

if ask_question("what the capital of France","Paris"):
    score += 1
current_question += 1

print "that's it!"
print "you got", score, "out of", total_questions
