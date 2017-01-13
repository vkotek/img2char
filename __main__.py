#! /Usr/local/bin/python3
# coding: utf-8

from PIL import Image, ImageDraw, ImageFont
import random
import argparse

font_family = 'unifont-9.0.06.ttf'

# Character sets you can use, just change value in defaults in main()
charsets = {
    'symbols': [
        '±<>!@#$%^&*/-. ', 0.5
    ],
    'kanji': [
        '置蜀輸雄明京手子汁りしン', 1
    ],
    'kanji2': [
        'フォントサイズをにして、表示位置を少し調整すると、文字は表示できた。', 1
    ],
    'kanji3': [
        '几仄仇什叩卍吃牝吠妓屁巫彷扮肛呟呵呻姐姑妾怯拗沽泄狗狐姜屍獰懃鰻鱈攣躙鰹', 1
    ],
    'kanji4': [
        '一右雨円花貝学空月犬見五口三山子四糸字人水正生青夕石赤千川先早草足村大', 1
    ],
    'hangul': [
        'ㄱㄳㄴㄵㄶㄷㄹㄺㄻㄼㄽㄾㄿㅀㅁㅂㅄㅅㅇㅈㅊㅋㅌㅍㅎㄲㅆᇸ', 1
    ],
    'hangul2': [
        'ㅏㅐㅑㅒㅓㅔㅕㅖㅗㅘㅙㅚㅛㅜㅝㅞㅟㅠㅡㅢㅣ ', 1
    ],
}


class Characterize(object):
    """Converts an image to ASCII, you can set the size and input your \
    own characters for it to use.

    USAGE:

    python3 ./ <image> [options]

    options:
    [-s][-size]     width in characters (integer)
    [-c][-charset]  Characters to be used (string) leave blank for defaults
    [-r][-ratio]    width to height ratio"""

    def __init__(self):
        pass

    # Main function that calls all others
    def img2chars(self, img, size, ratio, charset):
        charlist = self.chars2dict(charset)
        im = Image.open(img, 'r').convert('L')
        resize = (size, int(size/(im.width/(im.height*ratio))))
        im = im.resize(resize)
        for h in range(im.height):
            for w in range(im.width):
                x = im.getpixel(xy=(w, h))
                print(self.getSymbol(x, charlist), end='')
            print('')

    # Goes through charset and creates a sorted dictionary of chars: brightness
    def chars2dict(self, charset):
        charvals = []
        chardict = {}
        for char in charset:
            z = self.char2val(char)
            charvals.append(z)
            chardict[char] = z
        multiplier = 255/(max(charvals)-min(charvals))
        final = []
        for key in chardict:
            final.append((key, int((chardict[key]-min(charvals))*multiplier)))
        return sorted(final, key=lambda x: x[1])

    # Prints the character and analyzes & returns average brightness.
    def char2val(self, char):
        fnt = ImageFont.truetype(font_family, 30)
        txt = Image.new('L', (40, 40), (255))
        d = ImageDraw.Draw(txt)
        d.text((1, 1), char, font=fnt, fill=(0), spacing=0)
        value = list(txt.getdata())
        val = int(sum(value)/len(value))
        return val

    # Gets the best matching character for given pixel brightness value
    def getSymbol(self, value, chardict):
        for char in chardict:
            if value <= char[1]+1:
                return char[0]
        raise CharacterError


def main():

    # Get radom charset and its ratio
    def randomCharset():
        rnd = random.randrange(len(charsets))
        r = [charsets[i] for i in charsets][rnd]
        return r

    rc = randomCharset()

    # Pass arguments to vars
    parser = argparse.ArgumentParser(description='Image to characters.')
    parser.add_argument('image', metavar='img', type=str, nargs='?',
                        help='Path to image.')
    parser.add_argument('-c', dest='charset', type=str, default=rc[0],
                        help='String of characters to use')
    parser.add_argument('-s', dest='size', type=int, default=50,
                        help='Size in characters.')
    parser.add_argument('-r', dest='ratio', type=float, default=rc[1],
                        help='Ratio of characters. ')
    args = parser.parse_args()

    img = args.image
    charset = args.charset
    size = args.size
    ratio = args.ratio

    Characterize().img2chars(img, size, ratio, charset)


if __name__ == '__main__':
    main()
