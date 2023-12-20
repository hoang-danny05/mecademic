class Logger:
    def log(self, message: str):
        print(" "*100, end="\r")
        print(message, end="\r")
    
    def finished(self):
        print("DONE")