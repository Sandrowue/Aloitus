# MODULE FOR ASKING QUESTIONS FROM CONSOLE AND CONVERTING ANSWERS TO VARIOUS DATA TYPES

# Libraries and Mudules

# Class definitions

class Question():
    """A class containing methods to ask questions on console 
    and converting answers to various datatypes."""
    def __init__(self, kysymys):
        self.kysymys = kysymys

    @staticmethod
    def kysy_tiedo_integer(question, loop):
        """Asks a question and converts the answer to a integer point number

        Args:
            loop (bool): If True asks the question until able to convert it

        Returns:
            tupple: answer as integer, error message, error code, detailed error
        """

            # If loop arguments is True use whil loop until inputs correct value
        if loop == True:

            while True:
                answer_txt = input(question)
                try:
                    answer = int(answer_txt)
                    result = (answer, 'OK', 0, 'Conversion successful')
                    break
                except Exception as e:
                    print('Virhe syötetyssä arvossa, älä käytä yksiköitä', e)
                    result = (0, 'Error', 1, str(e))
            return result
        
        # Else ask once and return zero value an error information
        else:
            answer_txt = input(question)
            try:
                answer = int(answer_txt)
                result = (answer, 'OK', 0, 'Conversion successful')
            except Exception as e:
                print('Virhe syötetyssä arvossa, älä käytä yksiköitä', e)
                result = (0, 'Error', 1, str(e))
            return result    


    # Ask a question and covert the answer to float
    def kysy_tiedo_float(self, loop):
        """Asks a question and converts the answer to a floating point number

        Args:
            loop (bool): If True asks the question until able to convert it

        Returns:
            tupple: answer as float, error message, error code, detailed error
        """

        # If loop arguments is True use whil loop until inputs correct value
        if loop == True:

            while True:
                answer_txt = input(self.kysymys)
                # TODO: Add a routine to change , to . if user types the wrong symbol
                try:
                    answer = float(answer_txt)
                    result = (answer, 'OK', 0, 'Conversion successful')
                    break
                except Exception as e:
                    print('Virhe syötetyssä arvossa, älä käytä yksiköitä', e)
                    result = (0, 'Error', 1, str(e))
            return result
        
        # Else ask once and return zero value an error information
        else:
            answer_txt = input(self.kysymys)
            try:
                answer = float(answer_txt)
                result = (answer, 'OK', 0, 'Conversion successful')
            except Exception as e:
                print('Virhe syötetyssä arvossa, älä käytä yksiköitä', e)
                result = (0, 'Error', 1, str(e))
            return result
        
    '''def kysy_tiedo_integer(self, loop):
            """Asks a question and converts the answer to a integer point number

            Args:
                loop (bool): If True asks the question until able to convert it

            Returns:
                tupple: answer as integer, error message, error code, detailed error
            """

            # If loop arguments is True use whil loop until inputs correct value
            if loop == True:

                while True:
                    answer_txt = input(self.kysymys)
                    try:
                        answer = int(answer_txt)
                        result = (answer, 'OK', 0, 'Conversion successful')
                        break
                    except Exception as e:
                        print('Virhe syötetyssä arvossa, älä käytä yksiköitä', e)
                        result = (0, 'Error', 1, str(e))
                return result
            
            # Else ask once and return zero value an error information
            else:
                answer_txt = input(self.kysymys)
                try:
                    answer = int(answer_txt)
                    result = (answer, 'OK', 0, 'Conversion successful')
                except Exception as e:
                    print('Virhe syötetyssä arvossa, älä käytä yksiköitä', e)
                    result = (0, 'Error', 1, str(e))
                return result'''    

    def kysy_tiedo_boolean(self, true_value, false_value, loop):
        """Asks a question and converts the answer to a boolean value

        Args:
            true_value (str): value to use as True
            false_value (str): value to use as False
            loop (bool): If True asks the question unitl able to convet it

        Returns:
            tupple: answer as boolean, error message, error code, detailed error
        """
# If loop arguments is True use whil loop until inputs correct value
        prompt = f'{self.kysymys}, vastaa {true_value}/{false_value}: '
        if loop == True:

            while True:
                answer_txt = input(prompt).lower()

                if answer_txt == true_value.lower():
                    answer = True
                    result = (answer, 'OK', 0, 'Conversion successful')
                    break 
                elif answer_txt == false_value.lower():
                    answer = False
                    result = (answer, 'OK', 0, 'Conversion successful')
                    break
                else:
                     print('Virhe syötetyssä arvossa, sallitut arvot:',true_value, false_value)
                     result = ('N/A', 'Error', 1, 'unable to convert to boolean')

                

# Else ask once and return zero value an error information
        else:
            answer_txt = input(prompt)
            answer_txt = answer_txt.lower()

            if answer_txt == true_value.lower():
                answer = True
                result = (answer, 'OK', 0, 'Conversion successful')
            
            elif answer_txt == false_value.lower():
                answer = False
                result = (answer, 'OK', 0, 'Conversion successful')

            else:
                print('Virhe syötetyssä arvossa, sallitut arvot', true_value, false_value)
                result = ('N/A', 'Error', 1, 'unable to convert boolean')    
         
        return result    
                
if __name__ == "__main__":

    question = Question('Kuinka paljo painat (kg)? ')
    answer_and_error = question.kysy_tiedo_float(False)
    print(answer_and_error)

    question2 = Question('Kuinka vanha olet? ')
    answer_and_error = question2.kysy_tiedo_integer(True)
    print(answer_and_error)

    question3 = Question('Haluatko lähteä viikonlopun viettoon?')
    answer_and_error = question3.kysy_tiedo_boolean('Y', 'N', False)
    print(answer_and_error)
        
    




    

    










