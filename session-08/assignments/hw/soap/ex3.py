# http://spyne.io/docs/2.10/

#  Application is the glue between one or more service definitions, interface and protocol choices
from spyne.application import Application#webserver apacheIIS..WSGI asgi
# The @srpc decorator exposes methods as remote procedure calls and declares the data types it accepts and returns.
from spyne.decorator import srpc, rpc
# spyne.service.ServiceBase is the base class for all service definitions.
from spyne.service import ServiceBase

from spyne.model.complex import Iterable
from spyne.model.primitive import UnsignedInteger
from spyne.model.primitive import String

# Our server is going to use HTTP as transport,
# so we import the WsgiApplication from the :mod:`spyne.server.wsgi module.
# It’s going to wrap the Application instance.
from spyne.server.wsgi import WsgiApplication

from wsgiref.simple_server import make_server
from spyne.protocol.soap import Soap11



class HelloWorldService(ServiceBase):
    # @rpc(Unicode, Integer, _returns=Iterable(Unicode))
    @srpc(String, UnsignedInteger, _returns=Iterable(String))#wsdl
    def say_hello(ctx, name, times):
        for i in range(times):
            yield 'Hello, %s' % name
application = Application([HelloWorldService],
    tns='spyne.examples.hello',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11()
)
if __name__ == '__main__':
    # You can use any Wsgi server. Here, we chose
    # Python's built-in wsgi server but you're not
    # supposed to use it in production.
    from wsgiref.simple_server import make_server
    wsgi_app = WsgiApplication(application)
    server = make_server('0.0.0.0', 8000, wsgi_app)
    server.serve_forever()
