from zeep import Client, Settings

settings = Settings(strict=False, xml_huge_tree=True)
client = Client('http://www.soapclient.com/xml/soapresponder.wsdl', settings=settings)

with client.settings(raw_response=True):
    response = client.service.Method1('Hello', 'lima-BEAN')
