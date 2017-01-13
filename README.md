# img2char
Convert image to ASCIIesque art using any given character set.

####Syntax:
```
python3 ./ <image> [options]

options:
-s  -size     Width of output in characters.
-r  -ratio    The ratio of sides, because this varies for character sets.
-c  -charset  The a string of characters to use. Leave blank for default.
```
####Example:
```bash
$ python3 ./ test/paris.jpg -s 50 -r 1 -c '!@#$%^&*()/'
```

![alt-text](https://github.com/vkotek/img2char/raw/master/test/example.jpg)
