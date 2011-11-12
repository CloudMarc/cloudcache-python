# Apache License, Version 2.0 - http://www.apache.org/licenses/LICENSE-2.0.html
# See also LICENSE in root directory
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
sig = generate_signature("CloudCache","POST",ts,'secret')
print "My signature = " + sig
url = "http://cloudcache.ws/counter001/incr"

print url
user_agent = "CloudCache Tester version 0.01"
headers = {'User-Agent' : user_agent , 'signature' : sig , 'timestamp' : ts , 'akey' : 'ccpy'}
#data = {'val' : '2'}
data = {}
data = urllib.urlencode(data)
try:
  req = urllib2.Request(url, data, headers)
  #print "past creating request..."
except urllib2.HTTPError, e:
  print e.code, str(e)

try:
  ret = urllib2.urlopen(req)
  #print "past urlopen..."
except urllib2.HTTPError, e:
  print e.code, str(e)

print str(ret.read())
