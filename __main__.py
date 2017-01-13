#! /Usr/local/bin/python3
# coding: utf-8

from PIL import Image, ImageDraw, ImageFont
import sys

# Some testing images
one = '/Users/ares/Pictures/Yosemite-us.jpg'

# Character sets you can use, just change value in defaults in main()
symbs = '±<>!@#$%^&*/-. '
kanji1 = "蜀輸雄明京手子汁り"
kanji2 = '置蜀輸雄明京手子汁りしン'
kanji3 = 'フォントサイズをにして、表示位置を少し調整すると、文字は表示できた。'
kanji4 = '几仄仇什叩伜卍吃牝佇吠囮妓屁巫彷扮肛呟呵呻姐姑妾怯拗沽泄狗狐爬姜屍獰懃鰻鱈攣讐躙鰹'
kanji_grade1 = '一右雨円王音下火花貝学気九休玉金空月犬見五口校左三山子四糸字耳七車手十出女小上森人水正生青夕石赤千川先早草足村大男竹中虫町天田土二日入年白八百文木本名目立力林六'
korean = 'ㄱㄳㄴㄵㄶㄷㄹㄺㄻㄼㄽㄾㄿㅀㅁㅂㅄㅅㅇㅈㅊㅋㅌㅍㅎㄲㅆᇸ'
korean2 = 'ㅏ ㅐ ㅑ ㅒ ㅓ ㅔ ㅕ ㅖ ㅗ ㅘ ㅙ ㅚ ㅛ ㅜ ㅝ ㅞ ㅟ ㅠ ㅡ ㅢ ㅣ'

class Characterize(object):
    """Converts an image to ASCII, you can set the size and input your own characters for it to use.

    USAGE:

    [-i][-image]    image filename
    [-s][-size]     width in characters (integer)
    [-c][-charset]  Characters to be used (string) leave blank for default presets
    [-r][-ratio]    width to height ratio"""

    def __init__(self):
        pass

    def img2symbols(self, img, size, ratio, charset):
        charlist = self.chars2dict(charset)
        im = Image.open(img,'r').convert('L')
        resize = (size, int(size/(im.width/(im.height*ratio))))
        im = im.resize(resize)
        for h in range(im.height):
            for w in range(im.width):
                x = im.getpixel(xy=(w,h))
                print(self.getSymbol(x, charlist),end='')
            print('')

    def char2val(self, char):
        fnt = ImageFont.truetype('/Library/Fonts/Arial Unicode.ttf', 30)
        txt = Image.new('L', (40,40),(255))
        d = ImageDraw.Draw(txt)
        d.text((1,1), char, font=fnt, fill=(0), spacing=0)
        value = list(txt.getdata())
        val = int(sum(value)/len(value))
        return val

    def chars2dict(self,charset):
        charvals = []
        chardict = {}
        for char in charset:
            z = self.char2val(char)
            charvals.append(z)
            chardict[char] = z
        multiplier = 255/(max(charvals)-min(charvals))
        final = []
        for key in chardict:
            final.append((key,int((chardict[key]-min(charvals))*multiplier)))
        return sorted(final, key=lambda x: x[1])

    def getSymbol(self, symbol, chardict):
        for char in chardict:
            if symbol <= char[1]+1:
                return char[0]
        raise SymbolError

def main():

    # Defaults
    size = 50
    ratio = 1
    charset = symbs    

    args = sys.argv[1:]

    for n in range( len(args) ):
        if args[n] == '-i' or args[n] == '-image':
            img = args[n+1]
        elif args[n] == '-c' or args[n] == '-charset':
            charset = args[n+1]
        elif args[n] == '-s' or args[n] == '-size':
            size = int( args[n+1] )
        elif args[n] == '-r' or args[n] == '-ratio':
            ratio = float( args[n+1] )

    Characterize().img2symbols(img, size, ratio, charset)

if __name__ == '__main__':
    main()
