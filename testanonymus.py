# TEST-ANONYMO-DE-RESPUESTAS
class ANONYMOUS():
    """ collect anonymous answers to a survey question"""
    def __init__(self,Question):
        """store a question, and prepare to store responses"""
        self.question= Question
        self.respuestas= []

    def show_question(self):    
        """  SHOW THE SURVERY QUESTION """
        print(self.question)


    def store_response(self,new_response):
        """store a sinlge response to the survey"""
        self.respuestas.append(new_response)

    def show_results(self):
        print("resultados: ")
        for response in self.respuestas:
            print(response)
