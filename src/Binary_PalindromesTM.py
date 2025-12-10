#Binary_Palindromes
from TwoTapeTM import TwoTapeTM

class Binary_PalindromesTM(TwoTapeTM):
    def __init__(self):
        initial_state= "q0"
        final_states=("q4", )
        blank_symbol="B"
        #Diccionario de la funcion delta key("Estado en el que esta", "Que lee en la cinta 1", "Que lee en la cinta 2")
        #Value("Estado a donde va", "Que escribe en la cinta 1", "Movimiento de la cinta 1 R L S", "Que escribe en la cinta 2", "Movimiento de la cinta 2 R L S")
        delta={("q0", "0", blank_symbol):("q0", "0", "R", blank_symbol, "S"), ("q0", "1", blank_symbol):("q0", "1", "R", blank_symbol, "S"),\
                ("q0",blank_symbol, blank_symbol ): ("q1", blank_symbol, "L", blank_symbol, "S"), ("q1", "1", blank_symbol):("q1", "1", "L", "1","R" ),\
                ("q1", "0", blank_symbol):("q1", "0", "L", "0", "R"), ("q1", blank_symbol, blank_symbol):("q2", blank_symbol, "R",blank_symbol, "L"),\
                ("q2", "1", "0"):("q2", "1", "S", "0", "L"), ("q2", "0", "1"):("q2", "0", "S", "1", "L"), ("q2", "1", "1"):("q2", "1", "S", "1", "L"),\
                ("q2", "0", "0"):("q2", "0", "S","0", "L"), ("q2", "1", blank_symbol):("q3", "1", "S", blank_symbol, "R"), ("q2", "0", blank_symbol): ("q3", "0", "S", blank_symbol, "R"),\
                ("q3", "1", "1"): ("q3", "1", "R", "1", "R"), ("q3", "0", "0"):("q3", "0", "R", "0", "R"), ("q3", blank_symbol, blank_symbol):("q4", blank_symbol, "R", blank_symbol, "R")}

        super().__init__(delta, initial_state, final_states, blank_symbol)

    def check(self, input_string, run_type=False):
        self.load(input_string, run_type)
        return self.run()