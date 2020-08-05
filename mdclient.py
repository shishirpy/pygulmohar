import sys
import time
import random
from pygulmohar import MajorDomoClient

def main():
    verbose = '-v' in sys.argv
    client = MajorDomoClient("tcp://localhost:5555", verbose)
    count = 0
    print(123, count)
    while count < 1:
        request = str(random.randint(20, 99)).encode()
        try:
            reply = client.send(b"square", request)
            try:
                print(request.decode(), reply[0].decode())
                time.sleep(0.1)
            except TypeError as e:
                print("type error", e, type(reply))
                break
        except KeyboardInterrupt:
            break
        else:
            # also break on failure to reply:
            if reply is None:
                break
        count += 1
    print ("%i requests/replies processed" % count)

if __name__ == '__main__':
    main()
