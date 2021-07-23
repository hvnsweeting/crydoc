# crydoc
CLI doc for [Crystal lang](https://crystal-lang.org/api/1.1.0/index.html)

## Usage

### List modules
```
python3 crydoc.py
```
### Display module methods

```
python3 crydoc.py --module json
python3 crydoc.py -m string
```

### Examples

```
$ python3 crydoc.py -m string | head -n20
Signature: from_utf16(pointer:Pointer(UInt16)):Tuple(String,Pointer(UInt16))-class-method
   Decodes the given *slice* UTF-16 sequence into a String and returns the
pointer after reading. The string ends when a zero value is found.

```
slice = Slice[104_u16, 105_u16, 0_u16, 55296_u16, 56485_u16, 0_u16]
String.from_utf16(slice) # => "hi\0000𐂥"
pointer = slice.to_unsafe
string, pointer = String.from_utf16(pointer) # => "hi"
string, pointer = String.from_utf16(pointer) # => "𐂥"
```

Invalid values are encoded using the unicode replacement char with
codepoint `0xfffd`.
==============================

Signature: %(other):String-instance-method
   Interpolates *other* into the string using top-level `::sprintf`.

```


### TODO
- Show doc for a given method
- Better align
- Rewrite in Crystal
