#script1
print("Hello, world!")
#script2
print(bytes([72, 101, 108, 108, 111, 44, 32, 119, 111, 114, 108, 100, 33]).decode())
#script3
data = [72, 101, 108, 108, 111, 44, 32, 119, 111, 114, 108, 100, 33]
for b in data:
  __import__("sys").stdout.buffer.write(bytes([b]))
#script4
data = [72, 45, 9, 0, 3, 67, 12, 87, 24, 29, 30, 8, 69]
this = 0
for b in data:
  this ^= b
  __import__("sys").stdout.buffer.write(bytes([this]))
#script5
data = lambda x: \
-0.00021255879093909038 * x ** 12 +\
   0.015290779965911695 * x ** 11 +\
    -0.4850084554986253 * x ** 10 +\
      8.926861581877363 * x ** 9  +\
    -105.55962788638773 * x ** 8  +\
      838.5262887094129 * x ** 7  +\
     -4543.087798793585 * x ** 6  +\
       16686.0833464189 * x ** 5  +\
    -40408.677939747104 * x ** 4  +\
      60862.03545401174 * x ** 3  +\
     -50650.19040979945 * x ** 2  +\
      17285.41375948078 * x ** 1  +\
      71.99999571139465
this = 0
for x in range(13):
  this ^= round(data(x))
  __import__("sys").stdout.buffer.write(bytes([this]))
#script6
class Polynomial:
  coefficient = []
  def __init__(self, coefficient):
    self.coefficient = coefficient
  def __call__(self, x):
    """
    Evaluate the polynomial using Horner's method.
    """
    carry = self.coefficient[0]
    for i in range(1, len(self.coefficient)):
      carry *= x
      carry += self.coefficient[i]
    return carry
data = Polynomial([-0.00021255879093909038, 0.015290779965911695, -0.4850084554986253, 8.926861581877363, -105.55962788638773, 838.5262887094129, -4543.087798793585, 16686.0833464189, -40408.677939747104, 60862.03545401174, -50650.19040979945, 17285.41375948078, 71.99999571139465])
this = 0
for x in range(13):
  this ^= round(data(x))
  __import__("sys").stdout.buffer.write(bytes([this]))
#script7
class Polynomial:
  coefficient = []
  def __init__(self, coefficient):
    self.coefficient = coefficient
  def __call__(self, x):
    """
    Evaluate the polynomial using Horner's method.
    """
    carry = self.coefficient[0]
    for i in range(1, len(self.coefficient)):
      carry *= x
      carry += self.coefficient[i]
    return carry
data = Polynomial(__import__("struct").unpack("ddddddddddddd", b'\x8asr\x1cJ\xdc+\xbf\x14F\x12\xbf\xc5P\x8f?\xb3\x9a\xa9\xe7`\n\xdf\xbf\t*\xec\x99\x8d\xda!@\xc1}{\xf1\xd0cZ\xc0v\xd9\xda\xd654\x8a@\x13S\xfby\x16\xbf\xb1\xc0\xdb7\x8cU\x85K\xd0@O\xb2\xae\xb1\x15\xbb\xe3\xc0\x9esp"\xc1\xb7\xed@\xafJ\xd6\x17F\xbb\xe8\xc0\x97\x0b\t{Z\xe1\xd0@#%\x03\xee\xff\xffQ@'))
this = 0
for x in range(13):
  this ^= round(data(x))
  __import__("sys").stdout.buffer.write(bytes([this]))
#script8
class Polynomial:
  coefficient = []
  def __init__(self, coefficient):
    self.coefficient = coefficient
  def __call__(self, x):
    """
    Evaluate the polynomial using Horner's method.
    """
    carry = self.coefficient[0]
    for i in range(1, len(self.coefficient)):
      carry *= x
      carry += self.coefficient[i]
    return carry
data = Polynomial(__import__("struct").unpack("ddddddddddddd", __import__("gzip").decompress(b'\x1f\x8b\x08\x00\xe2 \xeac\x02\xff\x01h\x00\x97\xff\x8asr\x1cJ\xdc+\xbf\x14F\x12\xbf\xc5P\x8f?\xb3\x9a\xa9\xe7`\n\xdf\xbf\t*\xec\x99\x8d\xda!@\xc1}{\xf1\xd0cZ\xc0v\xd9\xda\xd654\x8a@\x13S\xfby\x16\xbf\xb1\xc0\xdb7\x8cU\x85K\xd0@O\xb2\xae\xb1\x15\xbb\xe3\xc0\x9esp"\xc1\xb7\xed@\xafJ\xd6\x17F\xbb\xe8\xc0\x97\x0b\t{Z\xe1\xd0@#%\x03\xee\xff\xffQ@\xe0\x968\xceh\x00\x00\x00')))
this = 0
for x in range(13):
  this ^= round(data(x))
  __import__("sys").stdout.buffer.write(bytes([this]))
#script9
class Polynomial:
  coefficient = []
  def __init__(self, coefficient):
    self.coefficient = coefficient
  def __call__(self, x):
    """
    Evaluate the polynomial using Horner's method.
    """
    carry = self.coefficient[0]
    for i in range(1, len(self.coefficient)):
      carry *= x
      carry += self.coefficient[i]
    return carry
data = Polynomial(__import__("struct").unpack("ddddddddddddd", __import__("gzip").decompress(__import__("base64").b64decode(b'H4sIAOIg6mMC/wFoAJf/inNyHErcK78URhK/xVCPP7OaqedgCt+/CSrsmY3aIUDBfXvx0GNawHbZ2tY1NIpAE1P7eRa/scDbN4xVhUvQQE+yrrEVu+PAnnNwIsG37UCvStYXRrvowJcLCXta4dBAIyUD7v//UUDgljjOaAAAAA=='))))
this = 0
for x in range(13):
  this ^= round(data(x))
  __import__("sys").stdout.buffer.write(bytes([this]))
#script10
class PackedPolynomialFactory:
  _data = b""
  def load(self, data):
    if self._data != b"":  # bEcauSE SafETy!!!11!!!
      raise ValueError("data already loaded")
    self._data = data
  def build(self):
    data = __import__("base64").b64decode(self._data)
    data = __import__("gzip").decompress(data)
    coefficient = __import__("struct").unpack("d"*int(len(data) // 8), data)
    return Polynomial(coefficient)
class Polynomial:
  coefficient = []
  def __init__(self, coefficient):
    self.coefficient = coefficient
  def __call__(self, x):
    """
    Evaluate the polynomial using Horner's method.
    """
    carry = self.coefficient[0]
    for i in range(1, len(self.coefficient)):
      carry *= x
      carry += self.coefficient[i]
    return carry
factory = PackedPolynomialFactory()
factory.load(b'H4sIAOIg6mMC/wFoAJf/inNyHErcK78URhK/xVCPP7OaqedgCt+/CSrsmY3aIUDBfXvx0GNawHbZ2tY1NIpAE1P7eRa/scDbN4xVhUvQQE+yrrEVu+PAnnNwIsG37UCvStYXRrvowJcLCXta4dBAIyUD7v//UUDgljjOaAAAAA==')
data = factory.build()
this = 0
for x in range(13):
  this ^= round(data(x))
  __import__("sys").stdout.buffer.write(bytes([this]))
#script11
class PackedPolynomialFactory:
  _data = b""
  def load(self, data):
    if self._data != b"":  # bEcauSE SafETy!!!11!!!
      raise ValueError("data already loaded")
    self._data = data
  def build(self):
    data = __import__("base64").b64decode(self._data)
    data = __import__("gzip").decompress(data)
    coefficient = __import__("struct").unpack("d"*int(len(data) // 8), data)
    return Polynomial(coefficient)
class Polynomial:
  coefficient = []
  def __init__(self, coefficient):
    self.coefficient = coefficient
  def __call__(self, x):
    """
    Evaluate the polynomial using Horner's method.
    """
    carry = self.coefficient[0]
    for i in range(1, len(self.coefficient)):
      carry *= x
      carry += self.coefficient[i]
    return carry
factory = PackedPolynomialFactory()
factory.load(b'H4sIAOIg6mMC/wFoAJf/inNyHErcK78URhK/xVCPP7OaqedgCt+/CSrsmY3aIUDBfXvx0GNawHbZ2tY1NIpAE1P7eRa/scDbN4xVhUvQQE+yrrEVu+PAnnNwIsG37UCvStYXRrvowJcLCXta4dBAIyUD7v//UUDgljjOaAAAAA==')
data = factory.build()
__import__("functools").reduce(
  lambda x, y: (
    x[0] ^ round(data(y)), 
    __import__("sys").stdout.buffer.write(
      bytes([x[0] ^ round(data(y))])
    )
  ), 
  range(13),
  (0,)
)
#script12
class PackedPolynomialFactory:
  _data = b""
  def load(self, data):
    if self._data != b"":  # bEcauSE SafETy!!!11!!!
      raise ValueError("data already loaded")
    self._data = data
  def build(self):
    data = __import__("base64").b64decode(self._data)
    data = __import__("gzip").decompress(data)
    coefficient = __import__("struct").unpack("d"*int(len(data) // (([]==[])<<(([]==[])<<([]!=[])|([]==[])<<([]==[])))), data)
    return Polynomial(coefficient)
class Polynomial:
  coefficient = []
  def __init__(self, coefficient):
    self.coefficient = coefficient
  def __call__(self, x):
    """
    Evaluate the polynomial using Horner's method.
    """
    carry = self.coefficient[([]!=[])]
    for i in range(([]==[]), len(self.coefficient)):
      carry *= x
      carry += self.coefficient[i]
    return carry
factory = PackedPolynomialFactory()
factory.load(b'H4sIAOIg6mMC/wFoAJf/inNyHErcK78URhK/xVCPP7OaqedgCt+/CSrsmY3aIUDBfXvx0GNawHbZ2tY1NIpAE1P7eRa/scDbN4xVhUvQQE+yrrEVu+PAnnNwIsG37UCvStYXRrvowJcLCXta4dBAIyUD7v//UUDgljjOaAAAAA==')
data = factory.build()
__import__("functools").reduce(
  lambda x, y: (
    x[([]!=[])] ^ round(data(y)), 
    __import__("sys").stdout.buffer.write(
      bytes(
        [x[([]!=[])] ^ round(data(y))]
      )
    )
  ), 
  range(([]==[])<<([]!=[])|([]==[])<<(([]==[])<<([]==[]))|([]==[])<<(([]==[])<<([]!=[])|([]==[])<<([]==[]))),
  (([]!=[]),)
)
#script13
import gzip
exec(gzip.decompress(b'\x1f\x8b\x08\x00S2\xeac\x02\xff\x95SQo\xda0\x10~\xe7W\\\xf3R\xa7 \xb2\xae\xa8L\xb4y\xa0@\x0b\xedFi+P;\xc4\x90\x13;\xe0.\xb1\x99\xed@2\xf5\xc7\xcfI\x80B\xc5&-O\x8e\xef\xfb\xbe;\x7fw\xe7\x87X)\x18`\xff\'%\x03\x11\xa6\\D\x0c\x87\xd7\xd8\xd7B\xa6\x8d\x12L\t\xd6\x18\\\xf0,\xab\x04\x84\x06\x10\nL\x90\xa2aP\x81,d\x1b\x0c\xb0\x00\xb2\x9bj\x01>\xca\xd1\r\x89\x99\xa20\xc2aL;R\n\x89\xac<\x8aCI1Is\x1dJ,\xdb\xd0w\xb8n.Zd\xf2b\x16\x16\xa9\xf2$\xeb\xf8t\xca\xa2\x85\x90z:E\x96\x87\x15=\xafYv\xd5;\xaf\x11\xea\x0bB\xd1\xbb\x96}q\x801\xfb\xcd\x16\x06\x9f\x81\xa3\x85\xa4J\xa1\x02\xea\x0b\x1a\x04\xccg\x94\xeb\x0f\x0c\xa5e\xeck\xc3\x89\xf9\xc2\xb8d^a\x9d0\xaeQHy\xc1\x05\xc7\x01\x84\xc6\x13\xd7\x1dO\xec\xcb\xcb\xdd\xe3xr\x94\x9d\xde\xf6\xae\xf2\x93\xf9\xd6\xfe]H\xaac\xc9\xe1\xdd|\xb4S\x8c]\xf2\x8b\x06m\xa3\xc6\x8a\xfdb\xc7\x93\xc2.S4gY\xc9EsvE\x1a\x1b\x93\xf7\x99;\x7f\x1b\t\x1f\x87\xe1V"\xc9\x89V\xd6y\xe8,M#\xb1\xa6\xa0\xe7\x14\x16\xdbj V\x8c\xcf\xa0+$\xa7\xf2XAD\xf5\\\x90\xea\x96\xe6c)S\x93\xeac\xf6\xf1\xc6\x1bS<\x04B\x02\x03\xc6Ab>\xa3[\x03+\x90y\xfc\x91i\xe7E\xad\x85O\\H.\x8ac\xf9@\x12\x96\xa9\xaf\xfd\xcdQ\xa5\xa0\x18lS\xd1_F\x1e\xd9\x1bL5\x9ft\xef\xb8[S\xbd\xe6}ov\x1e}k9\xabk\xd1\xbc\r\x1c\xc6\xfbi\xb7#\xfd\xbb\xfa\x97\xe1\xe3\xfc\xceIF\xad\xc1\xa0~\x8f\x7fQ2k\xe9\xb2\xd3z\x92*z9\xc3\xbda\xfb*x^&\x9fn\xfax\xd5\xf5\xbe\x7f\xd6/\xa7\xfd\xde\xa2\xd99\x1d\xd4\xe9#v\x94\xdf\xf6\xfa\xb5d4\x1f.\x1f\x1e:\xe5T\xca\xce(.\x0f\x9a\x9c\xf7W=usV\x1f\xb6\x96O\xfa\xe5\xf9Q.\xc5\xea\xd6\xff\xdaz\xd6\xb8F\xae\x9a\xbdt\xd8\xae/\x1dg8l\xcf\xc2\xd7\xd7{\xdc\xcc>\xd7=\xb6K\xeb\xa1\xdf<\xa2X"\xbb\xb4;\xd2A\xccMP\x84\xcaL\xb5\xa4$\xf6)\nq\xe4\x11\x0cI\x05\xd2\x06\xa0\xe4\xbd=\xf0\x03\xa4\x889\xc9g\x1d\xa5fl\xf7\x96#\xcd4\x94&"\xd6&U\x10PY]I\xa6)\xf2RM\x15\x1a\xffKi\x92/\xc1~\xcf\x0f/\xcd\x81\xfdy\xfb\xff\x8d\xab\xa0M\xb8b\xdb\x7f\x007\x06\xadT\xf8\x04\x00\x00'))
#script14
import gzip, base64
exec(gzip.decompress(base64.b85decode(b'ABzY8Q!?sf0{@j$QE%EX5Ps)ZT=P<=AhNEgOtg'
b'8RKnv|gX)91W#E=s^;4ZP5?Lad1$InTCLd7O6Pmb^VzB_++=Z9D+7-0V=B?A$rTtp0q*VxxWri~I'
b'z3Dy`~@GPqYga!}_Opu~sP=PFD8w{`jvYToFKFZMziJ77>!eLB1QVNNzJc>g}F-dbBN-W#ZcerjY'
b'T4eHK78a@UB<uKe%A$pkdOAgxhZQ}qS$5SsuMz4CLeaaHeQ|&>`^^>xpMj%=q)MRz>I)hK%x9GA4'
b'-BPc>}$h``NFtlUSXXuu2D#N!3D<wgvJxs9Z&4b%iZI6a+ICk_O9}i`PTkjNUCGW;oW?+Q;c2miw'
b'13@#)|!7$CJV?Q#5B;$whN^MH(BE_nA9?8wnqW;Z`EaiB{Hm=qybmv8JHs6c*cRAXbdeperP&@>o'
b'Gc^<0qZmgZwAQ<Lgr_VLCWQ#=Gh0t3cDVm_l=11peu{E=zrMXiNTTu3g8WBEW5mZ`7(%~7SG7;IC'
b'~Uq&9;8%#Bybnm!ZQ@!SWZ+0GiYdNcH(Yy^D#`|fvBmKMjm*M05&PhhC!JvMRe^D}P>9W&$k}7&R'
b'!@XhqDtKNdpKkhi)%CuA)-R|1-lEw#9n|R~c9h@t`n6;<A1)srI^|T#&L}Pqnw<AnJ#}+dAGVfH`'
b'sMjiF2(BB|Jr)ixJIs;y>!^FFCAw%Y|p~i*L&Q|KG!|AOY5QEJfc`4yR<vfLCj51gvv~{q$Kt!3U'
b'TBS3`qsj2B74<J@5mhh&jn;9i?V$_m(5gG?XSH)+SXDP+46`rYZ7LO%)pdOKFlX!G6yVFU^7ddHe'
b's3tDsG|V%vWJHwLX#_yhm|')))
