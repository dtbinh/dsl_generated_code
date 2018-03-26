#from statte_machine import StateMachine 
from state import State

def my_print():
	 print "hola"
def main():
    state=State("ciao","hola",my_print,"current")
    state.execute()
    

if __name__ == "__main__":
    main()
