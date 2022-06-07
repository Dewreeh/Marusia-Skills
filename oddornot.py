import random
registred_states = {}

def Get_State(state_id):
    return registred_states[state_id]

class State():

    def __init__(self, state_id, transitions, text, default_transition):
        self.state_id = state_id
        self.transitions = transitions
        self.text = text
        self.default_transition = default_transition
    
    def next_state(self, input):
        for transitions in self.transitions:
            if Transition.must_go(input):
                return Transition.to_id
        return Get_State(self.default_transition)

    def state_register(self):
        global registred_states
        registred_states[self.state_id] = self
class Transition():
    def __init__(self, to_id, synonims):
        self.to_id = to_id
        self.synonims = synonims
    def must_go(self, user_text):
        return user_text in self.synonims
    def get_next_id(self):
        return Get_State(self.to_id)

def init():
    global root_state_id
    State("100", [], "Привет, я загадаю число, а ты попробуешь угадать: чётное оно, или нет!", None).state_register
    root_state_id = "100"  
    
init()
    
        
