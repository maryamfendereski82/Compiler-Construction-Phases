import ply.lex as lex


class MyLexer(object):
    symbol_table = {}
    tokens = ["IDENTIFIER",
              "COMMENT",
              'LEFT_PA',
              'RIGHT_PA',
              'DIV_OP',
              'SUB_OP',
              'ADD_OP',
              'LE_OP',
              'LT_OP',
              'NE_OP',
              'EQ_OP',
              'GT_OP',
              'GE_OP',
              'SEMICOLON',
              'COLON',
              'COMMA',
              'MUL_OP',
              'ASSIGN_OP',
              'NUMBER'
              ]

    reserved = {"if": "IF_KW",
                "then": "THEN_KW",
                "else": "ELSE_KW",
                "while": "WHILE_KW",
                "do": "DO_KW",
                "begin": "BEGIN_KW",
                "end": "END_KW",
                "for": "FOR_KW",
                "or": "OR_KW",
                "and": "AND_KW",
                "return": "RETURN_KW",
                "program": "PROGRAM_KW",
                "integer": "INTEGER_KW",
                "real": "REAL_KW",
                "boolean": "BOOLEAN_KW",
                "function": "FUNCTION_KW",
                "to": "TO_KW",
                "true": "TRUE_KW",
                "false": "FALSE_KW"}

    tokens += reserved.values()

    t_ignore_COMMENT = r'\#.*'  # Ignores the comments
    t_ignore = ' \t'  # Ignores the tabs and spaces
    t_SUB_OP = r'-'
    t_ADD_OP = r'\+'
    t_DIV_OP = r'/'
    t_ASSIGN_OP = r':='
    t_SEMICOLON = r';'
    t_COLON = r':'
    t_COMMA = r','
    t_MUL_OP = r'\*'
    t_LT_OP = r'\<'
    t_LE_OP = r'\<\='
    t_NE_OP = r'\<\>'
    t_EQ_OP = r'\='
    t_GE_OP = r'\>\='
    t_GT_OP = r'\>'

    def t_LEFT_PA(self, t):
        r'\('
        t.value = '-'
        return t

    def t_RIGHT_PA(self, t):
        r'\)'
        t.value = '-'
        return t

    def t_IDENTIFIER(self, t):
        r'[a-zA-Z_][a-zA-Z_0-9]*'
        t.type = self.reserved.get(t.value, 'IDENTIFIER')  # Check for reserved words
        if t.type == 'IDENTIFIER':
            if t.value not in self.symbol_table:
                if self.symbol_table:
                    self.symbol_table[t.value] = len(self.symbol_table) + 1
                else:
                    self.symbol_table[t.value] = 1
        return t

    def t_NUMBER(self, t):
        r'(.)[0-9]+|([0-9])+(\.[0-9]+)?'
        t.value = str(t.value)
        if str(t.value) not in self.symbol_table:
            if self.symbol_table:
                self.symbol_table[t.value] = len(self.symbol_table) + 1
            else:
                self.symbol_table[t.value] = 1
        return t

    def t_error(self, t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)

    def t_Newline(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    def build(self, **kwargs):  # Build the lexer
        self.lexer = lex.lex(module=self, **kwargs)

    # Test its output
    def test(self, data):
        self.lexer.input(data)
        token_list = []
        for tok in self.lexer:
            if tok.type != 'NUMBER' and tok.type != 'IDENTIFIER':
                tok.value = '-'
            else:
                tok.value = self.symbol_table[tok.value]
            token_list.append([tok.type, tok.value])

        for tok in token_list:
            print(tok)


# Build the lexer and try it out
m = MyLexer()
m.build()  # Build the lexer
m.test('program identifier 40007893 40008823')
