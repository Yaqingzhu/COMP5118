import gzip
from msilib.schema import Error
import simplejson

def parse(filename):
  f = gzip.open(filename, 'r')
  entry = {}
  for l in f:
    l = l.strip()
    colonPos = l.find(b':')
    if colonPos == -1:
      yield entry
      entry = {}
      continue
    eName = l[:colonPos]
    rest = l[colonPos+2:]
    entry[eName] = rest
  yield entry

f = open("book.txt", "a")

for e in parse("Books.txt.gz"):
  try:
    dump = simplejson.dumps(e)
    userId = e[b'review/userId']
    itemId = e[b'product/productId']
    score = e[b'review/score']
    timestamp = e[b'review/time']
    f.write(userId.decode("utf-8") + ", " + itemId.decode("utf-8") + ", " +  ("0" if int(float(score.decode("utf-8"))) <= 2 else "1") + ", " + timestamp.decode("utf-8") + "\n")
  except:
    print("error")
f.close()