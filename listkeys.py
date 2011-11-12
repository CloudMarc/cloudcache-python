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
sig = generate_signature("CloudCache","listkeys",ts,'secret')
print "My signature = " + sig
url = "http://cloudcache.ws/listkeys.xml"

print url
user_agent = "CloudCache Tester version 0.01"
headers = {'User-Agent' : user_agent , 'signature' : sig , 'timestamp' : ts , 'akey' : 'ccpy'}
req = urllib2.Request(url, None, headers)
try:
  ret = urllib2.urlopen(req)
  print ret.read()
except urllib2.HTTPError, e:
  print e.code
  print e.read()



