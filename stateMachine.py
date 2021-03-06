class State(object):
    """
    We define a state object which provides some utility functions for the
    individual states within the state machine.
    
    """
    def __init__(self):
    	print("Current state: ", str(self))

    def on_event(self, event):
        """
        Handle events that are delegated to this State.
        
        """
        pass
    
    def __repr__(self):
        """
        Leverages the __str__ method to describe the State.

        """
        return self.__str__()

    def __str__(self):
        """
        Returns the name of the State.

        """
        return self.__class__.__name__

# Start of our states
class UninitialisedState(State):
    """
    The uninitialised state.        
    
    """
    def on_event(self, event):
        if event == 'Initialised':
            return Live()

        return self

class Live(State):
    """
    The initialised state.

    """
    def on_event(self, event):
        if event == "Initialised":
            return PreStack()

        return self

class PreStack(State):
    """
    The configured state.

    """
    def on_event(self, event):
        if event == "":
            return ExecuteStack()
        return self

class ExecuteStack(State):
    """
    The running state.

    """
    def on_event(self, event):
        if event == "Stop":
            return UninitialisedState()
        return self

class SimpleDevice(object):
    """
    A simple state machine that mimics the functionality of a device from a 
    high level.

    """
    def __init__(self):
        """ Initialise the components. """

        # Start with a default state.
        self.state = UninitialisedState()

    def on_event(self, event):
        """
        This is the bread and butter of the state machine. Incoming events are
        delegated to the given states which then handle the event. The result is
        then assigned as the new state.
        
        """

        # The next state will be the result of the on_event function.
        self.state = self.state.on_event(event)
device = SimpleDevice()