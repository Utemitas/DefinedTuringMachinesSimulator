#Binary_Palindromes
from TwoTapeTM import TwoTapeTM

class Binary_PalindromesTM(TwoTapeTM):
    def __init__(self):
        #Diccionario de la funcion delta key("Estado en el que esta", "Que lee en la cinta 1", "Que lee en la cinta 2")
        #Value("Estado a donde va", "Que escribe en la cinta 1", "Movimiento de la cinta 1 R L S", "Que escribe en la cinta 2", "Movimiento de la cinta 2 R L S")
        delta={("q0", "0", "B"):("q0", "0", "R", "B", "S")}
        initial_state= "q0"
        final_states=("q4", )
        blank_symbol="B"
        super().__init__(delta, initial_state, final_states, blank_symbol)

    def check(self, input_string, run_type=False):
        self.load(input_string, run_type)
        return self.run()