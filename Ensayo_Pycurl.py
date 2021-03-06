import pycurl
from io import BytesIO
buffer = BytesIO()
c = pycurl.Curl()
c.setopt(c.URL, 'http://localhost:9200/cars/sold_cars/')
c.setopt(c.POSTFIELDS, '{ "model" : "colt", "body_type" : "other"}')
c.setopt(c.WRITEDATA, buffer)
c.perform()
c.close()

body = buffer.getvalue()
# Body is a byte string.
# We have to know the encoding in order to print it to a text file
# such as standard output.
print(body.decode('iso-8859-1'))