import operator
INTEGER, PLUS, MINUS, EOF, WHITESPACE = 'INTEGER', 'PLUS', 'MINUS', 'EOF', 'WHITESPACE'

class Token(object):
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __str__(self):
        return 'Token({type}, {value})'.format(type=self.type, value=repr(self.value))

    def __repr__(self):
        return self.__str__()

class Interpreter(object):
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_token = None

    def error(self):
        raise Exception('error parsing input')

    def get_next_token(self):
        text = self.text
        if self.pos > len(text) - 1:
            return Token(EOF, None)

        current_char = text[self.pos]

        if current_char.isdigit():
            # start out with a empty value
            value = ''
            # for as long as the current character is a digit we add it.
            while(current_char.isdigit()):
                value += current_char 
                self.pos += 1
                # check if we are not going of the end. if so break
                if self.pos == len(self.text):
                    break
                # current_char is the next position.
                current_char = text[self.pos]
            # return a token representing the integer.
            return Token(INTEGER, int(value))

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
        if self.current_token.type == token_type:
            self.current_token = self.get_next_token()
        else:
            self.error()

    def expr(self):
        self.current_token = self.get_next_token()

        while(self.current_token.type == WHITESPACE):
            self.eat(WHITESPACE)
        left = self.current_token
        self.eat(INTEGER)

        while(self.current_token.type == WHITESPACE):
            self.eat(WHITESPACE)
        op = self.current_token
        opf = None
        if op.type == PLUS:
            self.eat(PLUS)
            opf = operator.add
        if op.type == MINUS:
            self.eat(MINUS)
            opf = operator.sub

        while(self.current_token.type == WHITESPACE):
            self.current_token = self.get_next_token()
        right = self.current_token
        self.eat(INTEGER)

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
        interpreter = Interpreter(text)
        result = interpreter.expr()
        print(result)

if __name__ == "__main__":
    main()
