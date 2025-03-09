# Compiler-Construction-Phases
### Repository Name:
**Python-Compiler-Phases**

---

### Repository Description:
This repository focuses on the implementation of the three core phases of a compiler using **Python**. Each phase is implemented as a separate module, providing a clear and practical approach to understanding compiler design. The repository is designed for educational purposes, offering detailed documentation, code examples, and test cases.

#### Phases:
1. **Phase 1 - Lexical Analyzer**  
   - **Description:** Implementation of a lexical analyzer (lexer) that tokenizes input source code into meaningful tokens. The lexer identifies keywords, identifiers, literals, operators, and other language-specific symbols. This phase serves as the foundation for the subsequent phases.

2. **Phase 2 - Syntax Analyzer**  
   - **Description:** Implementation of a syntax analyzer (parser) that checks the structure of the token stream against the grammar rules of the language. The parser generates a parse tree or abstract syntax tree (AST) for valid input, ensuring the code adheres to the language's syntax.

3. **Phase 3 - Intermediate Code Generation**  
   - **Description:** Implementation of an intermediate code generator that translates the parse tree or AST into an intermediate representation (IR), such as three-address code or abstract machine code. This phase bridges the gap between high-level source code and low-level machine code.

---

#### Repository Structure:
- **Phase1_LexicalAnalyzer/**: Contains the Python implementation.
- **Phase2_SyntaxAnalyzer/**: Contains the Python implementation, documentation.
- **Phase3_IntermediateCodeGeneration/**: Contains the Python implementation, documentation.

---

#### How to Use:
1. Clone the repository.
2. Navigate to the respective phase folder (e.g., `Phase1_LexicalAnalyzer/`).
3. Follow the instructions in the `README.md` file to set up and run the code.

---

#### Dependencies:
- **Programming Language:** Python
- **Libraries:** Standard Python libraries for file I/O, string manipulation, and data structures.
- **Tools:** No external tools are required; the implementation is purely in Python.

---

#### Contribution:
Contributions are welcome! If you have suggestions for improvements, additional test cases, or better implementations, feel free to open an issue or submit a pull request.

---

This repository is designed to help students and developers understand and implement the core phases of a compiler using Python, providing a hands-on and accessible approach to learning compiler construction.
