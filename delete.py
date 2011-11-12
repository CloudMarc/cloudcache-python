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
sig = generate_signature("CloudCache","DELETE",ts,'secret')
print "My signature = " + sig
url = "http://cloudcache.ws/4081"

h = httplib.HTTPConnection("cloudcache.ws",80)
h.putrequest('DELETE','/4081')
h.putheader('User-Agent', 'CloudCache Tester version 0.01')
h.putheader('signature',sig)
h.putheader('timestamp',ts)
h.putheader('akey','nu001')
h.putheader('Transfer-Encoding', 'chunked')
h.putheader('Accept', '*/*')

h.endheaders()
h.send('0\r\n\r\n')

resp = h.getresponse()
print repr(resp.read())


