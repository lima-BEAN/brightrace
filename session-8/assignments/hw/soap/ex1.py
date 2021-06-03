import zeep

wsdl = 'http://www.soapclient.com/xml/soapresponder.wsdl' #SOAP WS #implementaion details
client = zeep.Client(wsdl=wsdl)
print(client.service.Method1('Hello', 'lima-BEAN')) # RPC
