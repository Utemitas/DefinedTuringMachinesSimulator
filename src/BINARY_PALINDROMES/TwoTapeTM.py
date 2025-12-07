#TwoTapeTM

class TwoTapeTM:
    def __init__(self, delta, initial_state, final_states, blank_symbol="B"):
            self.delta= delta
            self.current_state= initial_state
            self.final_states= final_states
            self.blank= blank_symbol

            #Tapes Cinta 1 y Cinta 2
            self.tape_1=[]
            self.tape_2=[]

            #Heads Cabezales de cada una de las cintas 
            self.head_1=0
            self.head_2=0

    def load(self, input_string, run_type= False):
            #Run 
            #if run_type==True La TM imprimira paso a paso como la cadena se procesa
            #else La maquina de Turing solo dira si la cadena es aceptada o no
            self.run_type= run_type

            #Tape 1: Recibe la cadena y la convierte a lista "10001" -> [1,0,0,0,1]
            #Taoe 2: Lista llena de Blancos de la longitud de tape1
            self.tape_1= list(input_string)
            self.tape_2=[self.blank] * len(self.tape1)

    def _ensure_bounds(self): #Metodo de utileria, se encarga de ver en caso de que el cabezal se sobrepase del rango de la lista
        
        #Caso 1: Desbordamiento por extremo R
        if self.head_1<0:
            self.tape_1.insert(0,self.blank)
            self.head_1=0

        if self.head_2<0:
            self.tape_2.insert(0,self.blank)
            self.head_2=0

        #Caso 2: Desbordamiento por Extremo L
        if self.head_1>=len(self.tape_1):
            self.tape_1.append(self.blank)

        if self.head_2>=len(self.tape_2):
            self.tape_2.append(self.blank)

    def step(self):
        #Ejecuta una sola DI
        self.symbol1= self.tape_1[self.head_1]
        self.symbol2= self.tape_2[self.head_2]
        
        key= (self.current_state, self.symbol1, self.symbol2)

        if key not in self.delta:
            if self.run_type:
                #Mostrar que no se encontro una transicion de la forma key/ Cadena No Aceptada
                return False
        (new_state, write_1, move_1, write_2, move_2)=self.delta[key]

        #Escritura en la cinta 1 y 2
        self.tape_1[self.head_1]=write_1
        self.tape_2[self.head_2]=write_2

        #Movimientos de las cintas
        if move_1 == "R":
            self.head_1+=1
        elif move_1 == "L":
            self.head_1-=1
        
        if move_2 == "R":
            self.head_2+=1
        elif move_2== "L":
            self.head_2-=1
        
        #Comprobar que no haya desbordamiento en los extremos
        self._ensure_bounds()

        #Pasar al nuevo estado
        self.current_state= new_state

        #Impresion por paso
        if self.run_type:
            #Si el procesamiento de la cadena es por pasos mostrar el paso que se acaba de hacer (hacer el metodo que falta)
            pass
        
        return True
    

    def run(self):
        step_counter=0
        while True:
            if self.current_state in self.final_states:
                #Se imprimen el numero de pasos que se hicieron para procesar la cadena sin importar el run_type IMPLEMENTARLO
                return True
            
            #Intentar hacer una ID
            moved=self.step()

            if not moved:
                #imprimir a ventana que la cadena no fue aceptada (IMPLEMENTAR)
                return False
            
            step_counter+=1


#La TM's de palindromos recibirá una delta en forma de diccionario de tuplas en donde Key llevara el estado en donde esta, el simbolo de la cinta 1 que se esta leyendo
#y el simbolo de la cinta 2 que se leyo. Por otro lado los valores de los keys tendran el estado a donde se moverá, el simbolo a escribir en la cinta 1 y 2 y si se desplaza a
#la izq, der o se mantiene