import sys
from mdcliapi import MajorDomoClient

def main():
    verbose = '-v' in sys.argv
    client = MajorDomoClient("tcp://localhost:5555", verbose)
    request = b"sq"
    reply = client.send(b"mmi.service", request)

    if reply:
        replycode = reply[0].decode()
        print("Lookup echo services:", replycode)
    else:
        print("E: no response from broker, make sure it's running")

if __name__ == '__main__':
    main()
