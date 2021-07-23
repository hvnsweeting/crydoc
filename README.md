# crydoc
CLI doc for [Crystal lang](https://crystal-lang.org/api/1.1.0/index.html) standard libraries.

## Install
Requires python3.6+

```
sudo curl -Lo /usr/local/bin/crydoc https://raw.githubusercontent.com/hvnsweeting/crydoc/main/crydoc.py
sudo chmod a+x /usr/local/bin/crydoc
```

## Usage

Add `--html` to open doc site on default browser.

### List modules
```
crydoc
```
### Display module doc

```
crydoc --module json
crydoc -m string
```

### Open HTML doc page of HTTP::Client::Response class


```
$ crydoc --html -t HTTP::Client::Response
HTTP::Client::Response of HTTP::Client
HTTP::Client::Response https://crystal-lang.org/api/1.1.0/HTTP/Client/Response.html
Opening https://crystal-lang.org/api/1.1.0/HTTP/Client/Response.html
```

### Find methods split
```
$ crydoc -f String::split  | grep Signature
Signature: split(limit:Int32?=nil):Array(String)-instance-method
Signature: split(limit:Int32?=nil,&block:String->_)-instance-method
Signature: split(separator:Char,limit=nil,*,remove_empty=false)-instance-method
Signature: split(separator:Char,limit=nil,*,remove_empty=false,&block:String->_)-instance-method
Signature: split(separator:String,limit=nil,*,remove_empty=false)-instance-method
Signature: split(separator:String,limit=nil,*,remove_empty=false,&block:String->_)-instance-method
Signature: split(separator:Regex,limit=nil,*,remove_empty=false)-instance-method
Signature: split(separator:Regex,limit=nil,*,remove_empty=false,&block:String->_)-instance-method
```

### All options

```
$ crydoc -h
usage: crydoc [-h] [--module MODULE] [--type TYPE] [--method METHOD] [--html]

optional arguments:
  -h, --help            show this help message and exit
  --module MODULE, -m MODULE
                        search a module name
  --type TYPE, -t TYPE  search a type (class)
  --method METHOD, -f METHOD
                        search a method
  --html                Open the URL in default browser
```

### TODO
- Distribute on pypi
- Better align
- Rewrite in Crystal
