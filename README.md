# img2char
Convert image to ASCIIesque art using any given character set.

####Syntax:
```
python3 ./ <image> [options]

Image to character map.

positional arguments:
  img         Path to image.

optional arguments:
  -h, --help  show this help message and exit
  -c CHARSET  String of characters to use
  -s SIZE     Size in characters.
  -r RATIO    Ratio of characters.
```
####Example:
```bash
$ python3 ./ test/paris.jpg -s 50 -r 1 -c '!@#$%^&*()/'
```

![alt-text](https://github.com/vkotek/img2char/raw/master/test/example.jpg)
