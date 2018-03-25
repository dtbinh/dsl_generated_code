from state_machine import StateMachine 
from state import State

def my_print(st):
	print st
def main():
    state=State("one","two","three")
    statemachine=StateMachine(state)
    statemachine.build()
    

if __name__ == "__main__":
    main()
