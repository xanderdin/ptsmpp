PTSMPP - Python Twisted SMPP 3.4 client library
===============================================

This is a mixdown version of smpp.pdu and smpp.twisted packages found at
github. It also includes enum package. The enum package was put to ptsmpp
package in order to eliminate a dependency conflict: the smpp.twisted
package requires pyOpenSSL package, which requires cryptography package,
which requires enum34 package, which conflicts with the enum package,
which is required by both smpp.pdu and smpp.twisted packages.


SMPP 3.4 Protocol Specification
-------------------------------

http://www.nowsms.com/discus/messages/1/24856.html


Debian packages
---------------

https://github.com/xanderdin/ptsmpp-dist-debian


Usage example
-------------

    import logging
    from twisted.internet import reactor, defer
    from ptsmpp.twisted.client import SMPPClientTransceiver, SMPPClientService
    from ptsmpp.twisted.config import SMPPClientConfig

    class SMPP(object):

        def __init__(self, config=None):
            if config is None:
                config = SMPPClientConfig(host='localhost', port=999,
                                          username='uname', password='pwd')
            self.config = config
        
        @defer.inlineCallbacks
        def run(self):
            try:
                #Bind
                smpp = yield SMPPClientTransceiver(
                    self.config, self.handleMsg).connectAndBind()
                #Wait for disconnect
                yield smpp.getDisconnectedDeferred()
            except Exception, e:
                print "ERROR: %s" % str(e)
            finally:
                reactor.stop()
    
        def handleMsg(self, smpp, pdu):
            """
            NOTE: you can return a Deferred here
            """
            print "Received pdu %s" % pdu
    
    if __name__ == '__main__':
        logging.basicConfig(level=logging.DEBUG)
        SMPP().run()
        reactor.run()
