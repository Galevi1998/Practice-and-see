import time
from typing import List

class Logger:
    # dictMesseges= {}
    def __init__(self):
        self.dictMesseges = {}
        pass
    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if (message in self.dictMesseges and timestamp >= self.dictMesseges.get(message)+10) or (message not in self.dictMesseges):
            self.dictMesseges[message] = timestamp
            return True

        return False

def main():
    # Example input (timestamp, message)
    inputs = [
        (1, "foo"),
        (2, "bar"),
        (3, "foo"),
        (8, "bar"),
        (10, "foo"),
        (11, "foo")
    ]

    # Expected output: [True, True, False, False, False, True]
    
    logger = Logger()
    results = []
    for timestamp, message in inputs:
        result = logger.shouldPrintMessage(timestamp, message)
        results.append(result)

    print("Results:")
    print(results)

if __name__ == "__main__":
    main()
