class Logger:
    def log(self, message: str):
        print(message, end="\r")
    
    def finished(self):
        print("DONE")