import time
import pytest
import zmq
from pygulmohar.mdwrkapi import MajorDomoWorker
# from pygulmohar.mdcliapi import MajorDomoClient

class TestWorkerAPI():
    def test_reconnect_to_borker(self):

        test_service = MajorDomoWorker("tcp://localhost:5555", b"test_service", False)


        test_service.__reconnect_to_broker__();

        print(type(test_service.worker))

        assert isinstance(test_service.worker, zmq.Socket)
        assert test_service.worker.type == zmq.DEALER
        assert test_service.worker.linger == 0
        assert test_service.broker == "tcp://localhost:5555"




