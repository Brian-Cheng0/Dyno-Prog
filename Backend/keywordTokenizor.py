class BNFParser:
    def __init__(self, file_path):
        self.file_path = file_path
        self.grammar_lines = []
        self.keywords = []
        self._read_file()

    def _read_file(self):
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                self.grammar_lines = file.readlines()
        except Exception as e:
            print(f"Error reading file: {e}")

    def get_keywords(self):
        if not self.keywords:
            skip_definitions = ["<数字>", "<字符串>", "<标识符>"]
            for line in self.grammar_lines:
                # Skip lines starting with <数字>, <字符串>, or <标识符>
                if any(line.strip().startswith(skip) for skip in skip_definitions):
                    continue
                
                is_inside_angle_brackets = False
                keyword = ""
                for char in line:
                    if char == '<':
                        is_inside_angle_brackets = True
                    elif char == '>':
                        is_inside_angle_brackets = False
                    elif not is_inside_angle_brackets:
                        if char in ['=', '|', ' ', '\n', ':', '(', ')', '[', ']', '*', '+', ';']:
                            if keyword:
                                self.keywords.append(keyword)
                                keyword = ""
                        else:
                            keyword += char

                if keyword:
                    self.keywords.append(keyword)

            # Remove duplicates
            self.keywords = list(set(self.keywords))

        return self.keywords


# Example usage:
bnf_parser = BNFParser("sampleBNF.txt")
keywords = bnf_parser.get_keywords()
keywords += [";", ",", "=", "[", "]", "&&", "||", "(", ")", "+", "*", "!=", "==", "<", ">", "<=", ">=", "+"]
keywords = [*set(keywords)]
# print(keywords)
