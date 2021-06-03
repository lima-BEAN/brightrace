import zeep

wsdl = 'http://localhost:3333/?wsdl'#URIs
client = zeep.Client(wsdl=wsdl) #SOAP
print(client.service.say_hello("There!!!", 2)) # SOAP11
