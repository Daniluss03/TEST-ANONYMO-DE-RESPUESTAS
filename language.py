from testAnonymous import ANONYMOUS
question="what language did you speak first"
my_survey=ANONYMOUS(question)

my_survey.show_question()
print("enter q at any time to quit\n")
while True:
    response=input("language:")
    if response=='q':
        break
    my_survey.store_response(response)


my_survey.show_results()
