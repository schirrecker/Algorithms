class State(object):
    def __init__(self):
        pass
        print ('Processing current state:', self._name)
    
    def on_event(self, event):
        pass

class CLOSED_State(State):
    def __init__(self):
        self._name = "CLOSED"
    def on_event(self, event):
        if event == 'APP_PASSIVE_OPEN':
            return LISTEN_State()
        if event == 'APP_ACTIVE_OPEN':
            return SYN_SENT_State()
        return self

class LISTEN_State(State):
    def __init__(self):
        self._name = "LISTEN"
    def on_event(self, event):
        if event == 'RCV_SYN':
            return SYN_RCVD_State()
        if event == 'APP_SEND':
            return SYN_SENT_State()
        if event == 'APP_CLOSE':
            return CLOSED_State()
        return self

class SYN_RCVD_State(State):
    def __init__(self):
        self._name = "SYN_RCVD"    
    def on_event(self, event):
        if event == 'APP_CLOSE':
            return FIN_WAIT_1_State()
        if event == 'RCV_ACK':
            return ESTABLISHED_State()
        return self

class SYN_SENT_State(State):
    def __init__(self):
        self._name = "SYN_SENT"
    def on_event(self, event):
        if event == 'RCV_SYN':
            return SYN_RCVD_State()
        if event == 'RCV_SYN_ACK':
            return ESTABLISHED_State()
        if event == 'APP_CLOSE':
            return CLOSED_State()
        return self

class ESTABLISHED_State:
    def __init__(self):
        self._name = "ESTABLISHED"
    def on_event(self, event):
        if event == 'APP_CLOSE':
            return FIN_WAIT_1_State()
        if event == 'RCV_FIN':
            return CLOSE_WAIT_State()
        return self

class FIN_WAIT_1_State(State):
    def __init__(self):
        self._name = "FIN_WAIT_1"
    def on_event(self, event):
        if event == 'RCV_FIN':
            return CLOSING_State()
        if event == 'RCV_FIN_ACK':
            return TIME_WAIT_State()
        if event == 'RCV_ACK':
            return FIN_WAIT_2_State()
        return self

class CLOSING_State:
    def __init__(self):
        self._name = "CLOSING"
    def on_event(self, event):
        if event == 'RCV_ACK':
            return TIME_WAIT_State()
        return self

class FIN_WAIT_2_State:
    def __init__(self):
        self._name = "FIN_WAIT_2"
    def on_event(self, event):
        if event == 'RCV_FIN':
            return TIME_WAIT_State()
        return self    

class TIME_WAIT_State:
    def __init__(self):
        self._name = "TIME_WAIT"
    def on_event(self, event):
        if event == 'APP_TIMEOUT':
            return CLOSED_State()
        return self    

class CLOSE_WAIT_State:
    def __init__(self):
        self._name = "CLOSE_WAIT"
    def on_event(self, event):
        if event == 'APP_CLOSE':
            return LAST_ACK_State()
        return self  

class LAST_ACK_State:
    def __init__(self):
        self._name = "LAST_ACK"
    def on_event(self, event):
        if event == 'RCV_ACK':
            return CLOSED_State()
        return self  
  
def traverse_TCP_states(events):
    state = CLOSED_State()  # initial state, always
    trail = []
    trail.append(state)

    for event in events:
        new_state = trail[-1].on_event(event)
        trail.append(new_state)
    return trail[-1]._name

# print(traverse_TCP_states(["APP_ACTIVE_OPEN"]))
# outcome = traverse_TCP_states(["APP_ACTIVE_OPEN","RCV_SYN_ACK","RCV_FIN"])
# outcome = traverse_TCP_states(["APP_PASSIVE_OPEN",  "RCV_SYN","RCV_ACK"])
outcome = traverse_TCP_states(["APP_ACTIVE_OPEN","RCV_SYN_ACK","RCV_FIN","APP_CLOSE"])

print(outcome)
