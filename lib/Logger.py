class Logger:
    def log(message: str):
        print(message, end="\r")
    
    def finished():
        print("DONE")