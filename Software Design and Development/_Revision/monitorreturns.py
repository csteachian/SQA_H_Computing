from dataclasses import dataclass
@dataclass
class aReturn():
    name : str = ""
    address : str = ""
    modelNo : str = ""
    quantity : int = 0
    collectionDate : str = ""

returns = [aReturn() for index in range(10)]

def getReturnInfo():
    # get stuff
    localReturns = [aReturn() for index in range(10)] 
    for index in range(10):                             # 1.1. Loop 10 times
        localName = input("What is your name? ")        # 1.2.    Ask for and store localName
        localReturns[index].name = localName            # 1.3.    Set current record name to localName
                                                        # 1.4. End loop
    return localReturns()                               # 1.5. Return array of records

# main program
returns = getReturnInfo()