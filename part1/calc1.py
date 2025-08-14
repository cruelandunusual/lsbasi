# Token types
#
# EOF (end-of-file) token is used to indicate that
# there is no more input left for lexical analysis
INTEGER, PLUS, MINUS, WHITESPACE, EOF = 'INTEGER', 'PLUS', 'MINUS', 'WHITESPACE', 'EOF'

class Token(object):
    def __init__(self, type, value):
        # token type: INTEGER, PLUS, or EOF
        self.type = type
        # token value: 0, 1, 2. 3, 4, 5, 6, 7, 8, 9, '+', or None
        self.value = value

    def __str__(self):
        """String representation of the class instance.

        Examples:
            Token(INTEGER, 3)
            Token(PLUS '+')
        """
        return 'Token({type}, {value})'.format(
            type=self.type,
            value=repr(self.value)
        )

    def __repr__(self):
        return self.__str__()

class Operator():
    def __init__(self):

    def error(operation):
        raise Exception('Not a valid arithmetic operation')

    def operation(lvalue, rvalue):
        return lvalue - rvalue

    def 

class Interpreter(object):
    def __init__(self, text):
        # client string input, e.g. "3+5"
        self.text = text
        # self.pos is an index into self.text
        self.pos = 0
        # current token instance
        self.current_token = None
        self.opf = Operator()

    def error(self):
        raise Exception('Error parsing input')

    def get_next_token(self):
        """Lexical analyzer (also known as scanner or tokenizer)

        This method is responsible for breaking a sentence
        apart into tokens. One token at a time.
        """
        text = self.text
        # is self.pos index past the end of the self.text ?
        # if so, then return EOF token because there is no more
        # input left to convert into tokens
        if self.pos > len(text) - 1:
            return Token(EOF, None)
        # get a character at the position self.pos 
        current_char = text[self.pos]
        if current_char.isdigit():
            value = '' # value will store the multidigit number
            # check if a multidigit integer has been entered by checking if
            # the next char is also a digit
            while (current_char.isdigit()):
                value += current_char
                # increment the position to point to the next char in input string
                self.pos += 1
                # if we've reached the end of the input string then get out of the loop 
                if self.pos == len(self.text):
                    break
                # set current_char to the next character in the string for the next loop iteration
                current_char = text[self.pos]
            # create a token instance of type INTEGER pass it the
            # value of current_char as an int 
            token = Token(INTEGER, int(value))
            # return the instantiated token to the caller
            return token

        if current_char == '+':
            token = Token(PLUS, current_char)
            self.pos += 1
            return token
        
        if current_char == '-':
            token = Token(MINUS, current_char)
            self.pos += 1
            return token

        if current_char == ' ':
            token = Token(WHITESPACE, current_char)
            self.pos += 1
            return token

        self.error()

    def eat(self, token_type):
        # compare the current token type with the passed token
        # type and if they match then "eat" the current token
        # and assign the next token to the self.current_token,
        # otherwise raise an exception.
        if self.current_token.type == token_type:
            self.current_token = self.get_next_token()
        else:
            self.error()

    def expr(self):
        """expr -> INTEGER MINUS INTEGER"""
        # set current token to the first token taken from the input
        self.current_token = self.get_next_token()

        # ignore whitespace
        while (self.current_token.type == WHITESPACE):
            self.eat(WHITESPACE)

        # we expect the current token to be an integer
        left = self.current_token
        self.eat(INTEGER)

        # ignore whitespace
        while (self.current_token.type == WHITESPACE):
            self.eat(WHITESPACE)

        # get the operator used 
        op = self.current_token
        #opf = None
        if op.type == PLUS:
            self.eat(PLUS)
            opf = operator.add
        if op.type == MINUS:
            self.eat(MINUS)
            opf = operator.sub


        # ignore whitespace
        while (self.current_token.type == WHITESPACE):
            self.eat(WHITESPACE)

        # we expect the current token to be an integer
        right = self.current_token
        self.eat(INTEGER)

        # ignore whitespace
        while (self.current_token.type == WHITESPACE):
            self.eat(WHITESPACE)

        # after the above call the self.current_token is set to
        # EOF token

        # at this point INTEGER MINUS INTEGER sequence of tokens
        # has been successfully found and the method can just
        # return the result of subtracting the second integer from the first,
        # effectively interpreting client input
        #result = left.value - right.value
        result = opf(left.value, right.value)
        return result


def main():
    while True:
        try:
            text = input('calc> ')
        except EOFError:
            break
        if not text:
            continue
        if quit(text):
            break
        # make a new interpreter object for each loop iteration
        interpreter = Interpreter(text)
        # call the expr() method on the interpreter object;
        # this takes care of scanning the text
        result = interpreter.expr()
        print(result)


def quit(text):
    if text == 'q' or text == 'quit' or text == 'exit':
        return True
    else:
        return False


if __name__ == '__main__':
    main()
