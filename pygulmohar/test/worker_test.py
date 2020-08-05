import time
from pygulmohar.mdwrkapi import MajorDomoWorker
from pygulmohar.mdcliapi import MajorDomoClient

class TestWorker():
    def test_create_worker(self):
        main() # start broker at localhost:555
        worker = MajorDomoWorker("tcp://localhost:5555", b"sq", verbose=True)
        client = MajorDomoClient("tcp://localhost:5555", False)
        request = b"10"
        time.sleep(1)
        client_reply = client.send(b"sq", request)
        worker_reply = None

        request = worker.recv(worker_reply)
        print(request)
        assert False

