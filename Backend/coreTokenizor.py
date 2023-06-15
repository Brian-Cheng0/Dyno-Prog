import re
import keywordTokenizor

class CoreScanner:

    def __init__(self, file_name, keywords):
        self.keywords = keywords
        with open(file_name, 'r') as file:
            self.lines = file.readlines()
        self.line_num = 0
        self.tokens = []
        self.current_tokens = []
        self.cursor_index = 0
        self.tokenize_line()

    def tokenize_line(self):
        while True:
            if self.line_num >= len(self.lines):
                self.current_tokens = []
                return
            self.curr_line = self.lines[self.line_num].strip()
            if self.curr_line:
                break
            self.line_num += 1
        
        # Split tokens, considering special characters as separate tokens
        tokens = re.findall(r'[A-Za-z0-9]+|[^A-Za-z0-9\s]+', self.curr_line)
        for token in tokens:
            self.process_token(token)
        
        self.current_tokens = self.tokens[:]
        self.tokens.clear()
        self.cursor_index = 0
        self.line_num += 1

    def process_token(self, token):
        token_type = self.get_token_type(token)
        if token_type not in [34, -1]:
            self.tokens.append(token)

    def get_token(self):
        if not self.current_tokens:
            return 33
        token_string = self.current_tokens[self.cursor_index]
        return self.get_token_type(token_string)

    def skip_token(self):
        if not self.current_tokens or self.get_token() in [33, 34]:
            return
        self.cursor_index += 1
        if self.cursor_index >= len(self.current_tokens):
            self.tokenize_line()

    def get_token_type(self, token_string):
        if re.match(r'\d+[A-Z].*', token_string):
            return -1
        elif re.match(r'\d+', token_string):
            return 31
        elif re.match(r'[A-Z][A-Za-z0-9]*', token_string):
            return 32
        elif token_string in self.keywords:
            return self.keywords.index(token_string) + 1
        else:
            return 34


# Example usage:
bnf_parser = keywordTokenizor.BNFParser("sampleBNF.txt")
keywords = bnf_parser.get_keywords()
keywords += [";", ",", "=", "[", "]", "&&", "||", "(", ")", "+", "*", "!=", "==", "<", ">", "<=", ">=", "+"]
keywords = [*set(keywords)]
print(keywords)
# keywords = ["program", "begin", "end", "int", "if", "then", "else", "while", "loop", "read", "write", ";", ",", "=", "!", "[", "]", "&&", "||", "(", ")", "+", "-", "*", "!=", "==", "<", ">", "<=", ">="]

scanner = CoreScanner('input.txt', keywords)

while True:
    token_type = scanner.get_token()
    if token_type == 33:
        break
    print(token_type, scanner.current_tokens[scanner.cursor_index])
    scanner.skip_token()





# TODO: 31 & 32 is harcoded, try fix this