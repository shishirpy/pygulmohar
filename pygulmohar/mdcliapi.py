import logging

import zmq

import pygulmohar.MDP as MDP
from pygulmohar.zhelpers import dump

class MajorDomoClient(object):
    """
        Majordomo Protocol Client API, Python version.

        Implements the MDP/Worker spec at http:#rfc.zeromq.org/spec:7.


        Parameters
        ---------------

        broker: str
            address of the broker

        verbose: bool


        Attributes
        --------------
        ctx: zmq.Context

        client: zmq.Socket


        poller: zmq.Poller
            polling request and replies

        retries: int
            number of retries allowed

        timeout: int
            millisecond timeout

    """
    broker = None
    ctx = None
    client = None
    poller = None
    timeout = 2500
    retries = 3
    verbose = False

    def __init__(self, broker, verbose=False):
        self.broker = broker
        self.verbose = verbose
        self.ctx = zmq.Context()
        self.poller = zmq.Poller()
        logging.basicConfig(format="%(asctime)s %(message)s", datefmt="%Y-%m-%d %H:%M:%S",
                level=logging.INFO)
        self.reconnect_to_broker()

    def __reconnect_to_broker__(self):
        """
            Connect or reconnect to broker
        """
        if self.client:
            self.poller.unregister(self.client)
            self.client.close()
        self.client = self.ctx.socket(zmq.REQ)
        self.client.linger = 0
        self.client.connect(self.broker)
        self.poller.register(self.client, zmq.POLLIN)
        if self.verbose:
            logging.info("I: connecting to broker at %s…", self.broker)

    def send(self, service, request):
        """
            Send request to broker and get reply by hook or crook.

            Takes ownership of request message and destroys it when sent.
            Returns the reply message or None if there was no reply.

            Parameters
            ------------
            service : bytes
                name of the service, eg. b"service1"
            
            request : bytes

        """
        if not isinstance(request, list):
            request = [request]
        request = [MDP.C_CLIENT, service] + request
        if self.verbose:
            logging.warn("I: send request to '%s' service: ", service)
            dump(request)
        reply = None

        retries = self.retries
        while retries > 0:
            self.client.send_multipart(request)
            try:
                items = self.poller.poll(self.timeout)
            except KeyboardInterrupt:
                break # interrupted

            if items:
                msg = self.client.recv_multipart()
                if self.verbose:
                    logging.info("I: received reply:")
                    dump(msg)

                # Don't try to handle errors, just assert noisily
                assert len(msg) >= 3

                header = msg.pop(0)
                assert MDP.C_CLIENT == header

                reply_service = msg.pop(0)
                assert service == reply_service

                reply = msg
                break
            else:
                if retries:
                    logging.warn("W: no reply, reconnecting…")
                    self.__reconnect_to_broker__()
                else:
                    logging.warn("W: permanent error, abandoning")
                    break
                retries -= 1

        return reply

    def destroy(self):
        self.context.destroy()
