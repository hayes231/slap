import time
def animation():
    x = 0
    while x < 20:
        x += 1
        print("  Calculating.   \\ [     ] <>", end="", flush=True)
        print("\r", end="", flush=True)
        time.sleep(.05)
        print("  Calculating..  | [  =  ] ==", end="", flush=True)
        print("\r", end="", flush=True)
        time.sleep(.05)
        print("  Calculating... / [ === ] --", end="", flush=True)
        print("\r", end="", flush=True)
        time.sleep(.05)
        print("  Calculating.   - [=====] {}", end="", flush=True)
        print("\r", end="", flush=True)
        time.sleep(.05)

    print("Results are in:                ", end="", flush=True)
    time.sleep(3)
    print("\r", end="", flush=True)
    print("Results are in: You're a bitch")
    input("")
