import httplib
import simplejson as json
import time
import hmac
import sha
import base64
def generate_timestamp(gmtime):
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", gmtime)

def generate_signature(service, operation, timestamp, secret_access_key):
    my_sha_hmac = hmac.new(secret_access_key, service + operation + timestamp, sha)
    my_b64_hmac_digest = base64.encodestring(my_sha_hmac.digest()).strip()
    return my_b64_hmac_digest

import urllib2
import urllib
import time

ts = generate_timestamp(time.gmtime())
sig = generate_signature("CloudCache","PUT",ts,'secret')
print "My signature = " + sig
url = "http://cloudcache.ws/s1"

h = httplib.HTTPConnection("cloudcache.ws",80)
h.putrequest('PUT','/s1')
h.putheader('User-Agent', 'CloudCache Tester version 0.01')
h.putheader('signature',sig)
h.putheader('timestamp',ts)
h.putheader('akey','ccpy')
h.putheader('ttl','300')
h.putheader('Transfer-Encoding', 'chunked')
h.putheader('Accept', '*/*')

h.endheaders()

#bytes = {'val' : '32321'}
#bytes = json.dumps(bytes)
bytes = "1111121111"
length = len(bytes)
h.send('%X\r\n' % length)
h.send(bytes + '\r\n')
h.send('0\r\n\r\n')

resp = h.getresponse()
print repr(resp.read())


