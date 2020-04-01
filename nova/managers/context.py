"""Context manager module """


class ContextManager(object):
    """Basic context manager"""
    def __init__(self):
        """Initialize the context to None"""
        self.actual_context = None

    def has_context(self):
        """check if there exist a context """
        return self.actual_context != None

    def set_context(self, ctx):
        """change the context for something else """
        self.actual_context = ctx

    def get_context(self):
        """returns the actual context """
        return self.actual_context

    def reset_context(self):
        """reset the context to None """
        self.actual_context = None
    
