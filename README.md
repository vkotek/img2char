# img2char
Convert image to ASCIIesque art using any given character set.

Example usage:

python3 ./ <image> [options]

options:
-s  -size     Width of output in characters.
-r  -ratio    The ratio of sides, because this varies for character sets.
-c  -charset  The a string of characters to use. Leave blank for default.

```bash
$ python3 ./ test/paris.jpg -s 50 -r 1 -c '!@#$%^&*()/'
```
