import ply.yacc as yacc
from Lex import MyLexer

class MyParser(object):
    tokens = MyLexer.tokens

    def p_program(self, p):
        '''program : PROGRAM_KW identifier SEMICOLON block'''
        # Handle the program structure
        print("Program parsed successfully!")

    def p_identifier(self, p):
        '''identifier : IDENTIFIER'''
        # Handle identifier
        print(f"Identifier: {p[1]}")

    def p_block(self, p):
        '''block : BEGIN_KW statement_list END_KW'''
        # Handle the block structure
        print("Block parsed successfully!")

    def p_statement_list(self, p):
        '''statement_list : statement SEMICOLON statement_list
                          | empty'''
        # Handle the list of statements
        if len(p) == 4:
            print("Statement List parsed successfully!")
        else:
            print("Empty Statement List")

    def p_statement(self, p):
        '''statement : assignment_statement
                     | if_statement
                     | while_statement
                     | for_statement
                     | other_statements'''
        # Handle different types of statements
        print("Statement parsed successfully!")

    def p_assignment_statement(self, p):
        '''assignment_statement : identifier ASSIGN_OP expression'''
        # Handle assignment statements
        print("Assignment Statement parsed successfully!")

    def p_if_statement(self, p):
        '''if_statement : IF_KW condition THEN_KW statement_list else_part'''
        # Handle if statements
        print("If Statement parsed successfully!")

    def p_else_part(self, p):
        '''else_part : ELSE_KW statement_list
                     | empty'''
        # Handle optional else part
        if len(p) == 3:
            print("Else Part parsed successfully!")
        else:
            print("No Else Part")

    def p_condition(self, p):
        '''condition : expression LT_OP expression
                     | expression LE_OP expression
                     | expression EQ_OP expression
                     | expression NE_OP expression
                     | expression GE_OP expression
                     | expression GT_OP expression'''
        # Handle conditions
        print("Condition parsed successfully!")

    def p_expression(self, p):
        '''expression : term
                      | expression ADD_OP term
                      | expression SUB_OP term'''
        # Handle expressions
        print("Expression parsed successfully!")

    def p_term(self, p):
        '''term : factor
                | term MUL_OP factor
                | term DIV_OP factor'''
        # Handle terms
        print("Term parsed successfully!")

    def p_factor(self, p):
        '''factor : NUMBER
                  | identifier
                  | LEFT_PA expression RIGHT_PA'''
        # Handle factors
        print("Factor parsed successfully!")

    def p_while_statement(self, p):
        '''while_statement : WHILE_KW condition DO_KW statement_list'''
        # Handle while statements
        print("While Statement parsed successfully!")

    def p_for_statement(self, p):
        '''for_statement : FOR_KW identifier ASSIGN_OP expression TO_KW expression DO_KW statement_list'''
        # Handle for statements
        print("For Statement parsed successfully!")

    def p_other_statements(self, p):
        '''other_statements : RETURN_KW expression
                           | function_call'''
        # Handle other statements
        print("Other Statement parsed successfully!")

    def p_function_call(self, p):
        '''function_call : FUNCTION_KW identifier LEFT_PA argument_list RIGHT_PA'''
        # Handle function calls
        print("Function Call parsed successfully!")

    def p_argument_list(self, p):
        '''argument_list : expression COMMA argument_list
                        | expression
                        | empty'''
        # Handle argument lists
        if len(p) == 4:
            print("Argument List parsed successfully!")
        elif len(p) == 2:
            print("Single Argument parsed successfully!")
        else:
            print("Empty Argument List")

    def p_empty(self, p):
        '''empty :'''
        # Empty production rule
        pass

    def p_error(self, p):
        print(f"Syntax error at line {p.lineno}, position {p.lexpos}")

    def build(self, **kwargs):
        self.parser = yacc.yacc(module=self, **kwargs)

    def parse(self, data):
        return self.parser.parse(data)


# Example usage
if __name__ == '__main__':
    lexer = MyLexer()
    lexer.build()
    parser = MyParser()
    parser.build()
    path = r"pr.txt"
    data = open(path, 'r').read()
    result = parser.parse(data)
