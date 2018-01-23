def fizz_buzz(max_count: int):

    """
   A program that prints numbers But for multiples of three print “Fizz”
   instead of the number and for the multiples of five print “Buzz”.
   For numbers which are multiples of both three and five print “FizzBuzz”.
 
    Parameters:
 
        :param int max_count  : The max number that the fizz_buzz function will count to
 
    Returns:
 
        :return : None


    The Program first counts from 1 to the max_count provided in the parameters. An empty
    string is used to store the message to be printed. We check if the counted number is
    divisible by 3 and if so, append Fizz to the message. If the number is divisible by 5
    we append Buzz. If the message is empty after these checks, it is therefore not divisible
    by 5 or 3 and the number counted is appended to the message. The results are then printed
    to the user.

   
    """
    
    # Count from 1 to the maximum value given in the parameters
    for number in range(1, max_count):
    
            # Stores the message to display to user and is cleared after printed
            message = ''
            
            # Check if number is divisible by 3
            if number % 3 == 0:

                # Concatenate Fizz to message string
                message += "Fizz"

            # Check if number is divisible by 5
            if number % 5 == 0:

                # Concatenate Fizz to message string
                message += "Buzz"

            # If not divisible by 3 or 5, print number the number
            if message == '':

                # Concatenate counted number to message as a string
                message += str(number)

            print(message)

    return None


if __name__ == "__main__":

    fizz_buzz(max_count=100)








