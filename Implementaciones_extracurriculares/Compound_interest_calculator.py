def getArgs () -> list[float]:
    dataArray: list[float] = []   # [C0, r%, t]
    capital0: float = float(input("Enter initial capital: $"))
    interestR: float = float(input("Enter interest rate (%): "))
    dataArray.append(capital0)
    dataArray.append(interestR)
    nperiods: int = int(input("Enter number of periods: "))
    dataArray.append(nperiods)
    return dataArray

def simpleCompoundInterest (dataArray: list[float]):
    newCapital: float = dataArray[0]
    for i in range(0, (int(dataArray[2]) + 1)):
        print(f"Month #{i}: ${newCapital:.2f}")
        newCapital = dataArray[0] * (1 + (dataArray[1]/100)) ** (i + 1)

def incrementedCompoundInterest (dataArray: list[float]):
    newCapital: float = 0
    print(f"Month #{0}: ${dataArray[0]:.2f}")
    for i in range(int(dataArray[2])):
        newCapital =  (newCapital + dataArray[0]) * (1 + (dataArray[1]/100))
        newCapital = newCapital
        print(f"Month #{i+1}: ${newCapital:.2f}")

def main():
    try:
        selector = int(input("For SCI write 0, for ICI write 1: "))
        dataArray: list[float] = getArgs()
        if selector == 0:
            simpleCompoundInterest(dataArray)
        elif selector == 1:
            incrementedCompoundInterest(dataArray)
    except ValueError:
        print("Error: Invalid Value")
    except TypeError:
        print("Error: Invalid Type")

if __name__ == "__main__":
    main()