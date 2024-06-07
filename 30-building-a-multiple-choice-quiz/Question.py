class Question:
    ## ** = dictionary
    def __init__(self, **kwargs) -> None:
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer