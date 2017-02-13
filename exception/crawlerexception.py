class FetchFailedException(Exception):

    def __init__(self, message):
        super(FetchFailedException, self).__init__(message)
