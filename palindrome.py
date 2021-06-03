from collections import deque

empty_string=""

def is_palindrome(data):


    try:
        if data==str(data):
            data=data.lower()
            deque_holder= deque(data)
            deque_reverse=deque()
            deque_forward=deque()
            string_true="True"
            string_false="False"

            for character in deque_holder:
                deque_reverse.appendleft(character)
                deque_forward.append(character)
            #        if character.isdigit():
            #            return False
            #            print("only words are palindrome")
            #            break
        #

            if deque_reverse==deque_forward:
                return True
            else:
                return False
            if data==empty_string:
                return False
        else:
            return ValueError

    except:
        return ValueError
#
