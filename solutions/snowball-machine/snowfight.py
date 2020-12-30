#!/usr/bin/env python3
#
# mt19937.py - a quick and dirty implementation of the MT19937 PRNG in Python
#
#    Copyright (C) 2020  Tom Liston - email: tom.liston@bad-wolf-sec.com
#                                   - twitter: @tliston
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see [http://www.gnu.org/licenses/].

import random

# this is simply a python implementation of a standard Mersenne Twister PRNG.
# the parameters used, implement the MT19937 variant of the PRNG, based on the
# Mersenne prime 2^19937−1
# see https://en.wikipedia.org/wiki/Mersenne_Twister for a very good explanation
# of the math behind this...

class mt19937():
    u, d = 11, 0xFFFFFFFF
    s, b = 7, 0x9D2C5680
    t, c = 15, 0xEFC60000
    l = 18
    n = 624

    def my_int32(self, x):
        return(x & 0xFFFFFFFF)

    def __init__(self, seed):
        w = 32
        r = 31
        f = 1812433253
        self.m = 397
        self.a = 0x9908B0DF
        self.MT = [0] * self.n
        self.index = self.n + 1
        self.lower_mask = (1 << r) - 1
        self.upper_mask = self.my_int32(~self.lower_mask)
        self.MT[0] = self.my_int32(seed)
        for i in range(1, self.n):
            self.MT[i] = self.my_int32((f * (self.MT[i - 1] ^ (self.MT[i - 1] >> (w - 2))) + i))

    def extract_number(self):
        if self.index >= self.n:
            self.twist()
            self.index = 0
        y = self.MT[self.index]
        # this implements the so-called "tempering matrix"
        # this, functionally, should alter the output to
        # provide a better, higher-dimensional distribution
        # of the most significant bits in the numbers extracted
        y = y ^ ((y >> self.u) & self.d)
        y = y ^ ((y << self.s) & self.b)
        y = y ^ ((y << self.t) & self.c)
        y = y ^ (y >> self.l)
        self.index += 1
        return self.my_int32(y)

    def twist(self):
        for i in range(0, self.n):
            x = (self.MT[i] & self.upper_mask) + (self.MT[(i + 1) % self.n] & self.lower_mask)
            xA = x >> 1
            if(x % 2) != 0:
                xA = xA ^ self.a
            self.MT[i] = self.MT[(i + self.m) % self.n] ^ xA


# so... guess what! while it isn't necessarily obvious, the
# functioning of the tempering matrix are mathematically
# reversible. this function impliments that...
#
# by using this, we can take the output of the MT PRNG, and turn
# it back into the actual values held within the MT[] array itself
# and therefore, we can "clone" the state of the PRNG from "n"
# generated random numbers...
#
# initially, figuring out the math to do this made my brain hurt.
# simplifying it caused even more pain.
# please don't ask me to explain it...
def untemper(y):
    y ^= y >> mt19937.l
    y ^= y << mt19937.t & mt19937.c
    for i in range(7):
        y ^= y << mt19937.s & mt19937.b
    for i in range(3):
        y ^= y >> mt19937.u & mt19937.d
    return y
# Paste your seeds here.
comments = """
    1142661414 - Not random enough
    3795138894 - Not random enough
    4078105108 - Not random enough
    3268740873 - Not random enough
    2507128209 - Not random enough
    305236020 - Not random enough
    2138375967 - Not random enough
    1749882708 - Not random enough
    864097036 - Not random enough
    4083016893 - Not random enough
    1947337387 - Not random enough
    3793923071 - Not random enough
    2592258125 - Not random enough
    3330033011 - Not random enough
    3496118714 - Not random enough
    3671864601 - Not random enough
    3100621415 - Not random enough
    2559971200 - Not random enough
    309000505 - Not random enough
    2716976984 - Not random enough
    4074471329 - Not random enough
    3929087489 - Not random enough
    1146613288 - Not random enough
    3540117482 - Not random enough
    1884758960 - Not random enough
    1320121063 - Not random enough
    649933500 - Not random enough
    3710159941 - Not random enough
    1457524059 - Not random enough
    3447985545 - Not random enough
    2230822134 - Not random enough
    2233887387 - Not random enough
    1309096595 - Not random enough
    270581704 - Not random enough
    808236946 - Not random enough
    3444370127 - Not random enough
    3501582956 - Not random enough
    2129698347 - Not random enough
    2620127685 - Not random enough
    3246819191 - Not random enough
    881892762 - Not random enough
    3586260512 - Not random enough
    68836934 - Not random enough
    276589638 - Not random enough
    1654572927 - Not random enough
    1842357532 - Not random enough
    3681272785 - Not random enough
    364797824 - Not random enough
    2982477841 - Not random enough
    2072301313 - Not random enough
    692185259 - Not random enough
    2663333380 - Not random enough
    357272504 - Not random enough
    3595256709 - Not random enough
    494245313 - Not random enough
    4079695910 - Not random enough
    3460386529 - Not random enough
    2799168467 - Not random enough
    2576321168 - Not random enough
    2592624170 - Not random enough
    335229706 - Not random enough
    437182739 - Not random enough
    648092877 - Not random enough
    3942330482 - Not random enough
    1043206160 - Not random enough
    1215606484 - Not random enough
    3287462922 - Not random enough
    3523855832 - Not random enough
    4179392146 - Not random enough
    3417534910 - Not random enough
    1914237894 - Not random enough
    840672830 - Not random enough
    1639957669 - Not random enough
    242477483 - Not random enough
    1729828933 - Not random enough
    953276503 - Not random enough
    2078220819 - Not random enough
    625041064 - Not random enough
    1748029530 - Not random enough
    2494362698 - Not random enough
    3599027386 - Not random enough
    786454540 - Not random enough
    4213474425 - Not random enough
    1744800863 - Not random enough
    2089829208 - Not random enough
    848119442 - Not random enough
    3022986560 - Not random enough
    2679445797 - Not random enough
    3774353031 - Not random enough
    885216035 - Not random enough
    25947726 - Not random enough
    874454040 - Not random enough
    2521027090 - Not random enough
    766824330 - Not random enough
    1469041863 - Not random enough
    2227651083 - Not random enough
    3821759061 - Not random enough
    2391535986 - Not random enough
    1335654767 - Not random enough
    2751397790 - Not random enough
    1081445937 - Not random enough
    1708454774 - Not random enough
    975041410 - Not random enough
    490232289 - Not random enough
    2205275304 - Not random enough
    1378278201 - Not random enough
    2046591912 - Not random enough
    2765539619 - Not random enough
    3316492486 - Not random enough
    2958276372 - Not random enough
    2005516296 - Not random enough
    3395887856 - Not random enough
    1382461065 - Not random enough
    1967574723 - Not random enough
    1305011210 - Not random enough
    1819755401 - Not random enough
    2984903070 - Not random enough
    709838047 - Not random enough
    2964713867 - Not random enough
    3569737657 - Not random enough
    3203826179 - Not random enough
    1973413881 - Not random enough
    869664440 - Not random enough
    2321180657 - Not random enough
    1655883397 - Not random enough
    2271843142 - Not random enough
    2768048750 - Not random enough
    553500296 - Not random enough
    430035547 - Not random enough
    1005779464 - Not random enough
    3116722671 - Not random enough
    2601758365 - Not random enough
    2637676406 - Not random enough
    79312040 - Not random enough
    331601011 - Not random enough
    608586801 - Not random enough
    2097549560 - Not random enough
    352245145 - Not random enough
    585910849 - Not random enough
    2673270953 - Not random enough
    3679017417 - Not random enough
    3027628407 - Not random enough
    545210176 - Not random enough
    1135878919 - Not random enough
    2043256954 - Not random enough
    2940322143 - Not random enough
    3636068042 - Not random enough
    3925717014 - Not random enough
    3081301987 - Not random enough
    3216655131 - Not random enough
    2613852096 - Not random enough
    1916544293 - Not random enough
    1703723103 - Not random enough
    3763960097 - Not random enough
    608537710 - Not random enough
    1884519100 - Not random enough
    2379258376 - Not random enough
    2824513970 - Not random enough
    2898267400 - Not random enough
    3233722431 - Not random enough
    1798495985 - Not random enough
    4088806631 - Not random enough
    2180539723 - Not random enough
    2650074944 - Not random enough
    3711391355 - Not random enough
    33523827 - Not random enough
    892844481 - Not random enough
    3223461721 - Not random enough
    2534342002 - Not random enough
    751461900 - Not random enough
    1327284376 - Not random enough
    4229390651 - Not random enough
    1250799459 - Not random enough
    1790062107 - Not random enough
    3837205056 - Not random enough
    3216931322 - Not random enough
    1864741985 - Not random enough
    428998071 - Not random enough
    2557588811 - Not random enough
    95124611 - Not random enough
    2002753051 - Not random enough
    3861180290 - Not random enough
    4142418334 - Not random enough
    1376305400 - Not random enough
    444194306 - Not random enough
    3434754360 - Not random enough
    2060150550 - Not random enough
    3556103376 - Not random enough
    3359287081 - Not random enough
    3436269779 - Not random enough
    2098532257 - Not random enough
    2678477656 - Not random enough
    2425244218 - Not random enough
    607685757 - Not random enough
    3471439536 - Not random enough
    3120636564 - Not random enough
    579615708 - Not random enough
    630583124 - Not random enough
    1653970850 - Not random enough
    2704987860 - Not random enough
    786215619 - Not random enough
    4088948338 - Not random enough
    2388289434 - Not random enough
    533051950 - Not random enough
    3981274465 - Not random enough
    243416546 - Not random enough
    638398023 - Not random enough
    678818886 - Not random enough
    3822542291 - Not random enough
    3923232815 - Not random enough
    3177603143 - Not random enough
    1562147373 - Not random enough
    21081260 - Not random enough
    3410134679 - Not random enough
    504126420 - Not random enough
    2435195654 - Not random enough
    4217313366 - Not random enough
    1525158149 - Not random enough
    3685004458 - Not random enough
    693098883 - Not random enough
    1376076551 - Not random enough
    2825461298 - Not random enough
    2896014724 - Not random enough
    11325766 - Not random enough
    1768825213 - Not random enough
    3689551981 - Not random enough
    2267920466 - Not random enough
    1517018004 - Not random enough
    1097581698 - Not random enough
    610451040 - Not random enough
    2963070311 - Not random enough
    1213802111 - Not random enough
    159099169 - Not random enough
    1636098257 - Not random enough
    1582464482 - Not random enough
    106514853 - Not random enough
    2204815954 - Not random enough
    241572743 - Not random enough
    106122901 - Not random enough
    1430924905 - Not random enough
    3036925948 - Not random enough
    859337777 - Not random enough
    1950452902 - Not random enough
    5621563 - Not random enough
    2357555052 - Not random enough
    230794900 - Not random enough
    957037584 - Not random enough
    2066775320 - Not random enough
    1839287893 - Not random enough
    3046807860 - Not random enough
    449493427 - Not random enough
    2758552486 - Not random enough
    2519940048 - Not random enough
    1298282839 - Not random enough
    273515972 - Not random enough
    2643805527 - Not random enough
    1862352878 - Not random enough
    704406462 - Not random enough
    4068476207 - Not random enough
    406933218 - Not random enough
    3788126713 - Not random enough
    1848434825 - Not random enough
    1053208644 - Not random enough
    177696300 - Not random enough
    484690784 - Not random enough
    1219707829 - Not random enough
    2409422233 - Not random enough
    3863942866 - Not random enough
    4102089595 - Not random enough
    3814676757 - Not random enough
    1459904070 - Not random enough
    1881544428 - Not random enough
    1681705103 - Not random enough
    3255337200 - Not random enough
    1510738720 - Not random enough
    751618204 - Not random enough
    3429235408 - Not random enough
    1378725837 - Not random enough
    2275999267 - Not random enough
    2746833328 - Not random enough
    1788476761 - Not random enough
    952116046 - Not random enough
    3975855541 - Not random enough
    1645069159 - Not random enough
    1130237020 - Not random enough
    1080955017 - Not random enough
    2949662022 - Not random enough
    56659582 - Not random enough
    2304019632 - Not random enough
    2729850409 - Not random enough
    3963827466 - Not random enough
    1495996292 - Not random enough
    2444803951 - Not random enough
    496943786 - Not random enough
    2317417445 - Not random enough
    2581664888 - Not random enough
    2683845516 - Not random enough
    3139358807 - Not random enough
    551830950 - Not random enough
    2163890042 - Not random enough
    376425204 - Not random enough
    111454259 - Not random enough
    2327328304 - Not random enough
    3163865930 - Not random enough
    2555563184 - Not random enough
    631500764 - Not random enough
    2275827983 - Not random enough
    3057639655 - Not random enough
    4214938270 - Not random enough
    3976917326 - Not random enough
    2819206888 - Not random enough
    3798784472 - Not random enough
    3415196660 - Not random enough
    1091512979 - Not random enough
    867895988 - Not random enough
    746506644 - Not random enough
    1133560006 - Not random enough
    995382127 - Not random enough
    3784020149 - Not random enough
    714560360 - Not random enough
    736825320 - Not random enough
    3474707728 - Not random enough
    2745161514 - Not random enough
    2038407960 - Not random enough
    2531947400 - Not random enough
    579179478 - Not random enough
    1435129077 - Not random enough
    898764995 - Not random enough
    1777233118 - Not random enough
    3262982562 - Not random enough
    1930607810 - Not random enough
    3148821216 - Not random enough
    3894956602 - Not random enough
    985787202 - Not random enough
    3312204415 - Not random enough
    9148367 - Not random enough
    2119898275 - Not random enough
    607202532 - Not random enough
    512779319 - Not random enough
    2756901673 - Not random enough
    3521570465 - Not random enough
    3276103538 - Not random enough
    3625623192 - Not random enough
    4061070571 - Not random enough
    1803163493 - Not random enough
    1395518177 - Not random enough
    4089145448 - Not random enough
    148255961 - Not random enough
    355584920 - Not random enough
    186655431 - Not random enough
    1191021410 - Not random enough
    2291626438 - Not random enough
    885084412 - Not random enough
    1310988143 - Not random enough
    3603057951 - Not random enough
    1954033386 - Not random enough
    580247262 - Not random enough
    1581399561 - Not random enough
    467098987 - Not random enough
    2879434637 - Not random enough
    2378042783 - Not random enough
    1753512142 - Not random enough
    2854613880 - Not random enough
    1847128844 - Not random enough
    2094934434 - Not random enough
    261636904 - Not random enough
    4078090378 - Not random enough
    3059787657 - Not random enough
    3922821245 - Not random enough
    3451012079 - Not random enough
    3611087687 - Not random enough
    3816478041 - Not random enough
    1746608820 - Not random enough
    1057263257 - Not random enough
    1509025518 - Not random enough
    1084332170 - Not random enough
    3579880252 - Not random enough
    381974958 - Not random enough
    101561123 - Not random enough
    524052411 - Not random enough
    3827701313 - Not random enough
    4259169778 - Not random enough
    3568079088 - Not random enough
    1777156089 - Not random enough
    1875702963 - Not random enough
    2228667237 - Not random enough
    3511561638 - Not random enough
    3058723000 - Not random enough
    1704475681 - Not random enough
    3423685649 - Not random enough
    741751050 - Not random enough
    1395857777 - Not random enough
    482822434 - Not random enough
    2128963339 - Not random enough
    1726424438 - Not random enough
    558843009 - Not random enough
    2525315176 - Not random enough
    2631225120 - Not random enough
    2438670224 - Not random enough
    1058992032 - Not random enough
    400727925 - Not random enough
    349648187 - Not random enough
    1038486420 - Not random enough
    1794223312 - Not random enough
    1955359599 - Not random enough
    1658797031 - Not random enough
    2285367171 - Not random enough
    1001801520 - Not random enough
    796803236 - Not random enough
    3219405708 - Not random enough
    6618925 - Not random enough
    1395559694 - Not random enough
    248856703 - Not random enough
    532454645 - Not random enough
    3313506403 - Not random enough
    1922354077 - Not random enough
    363386654 - Not random enough
    1782873834 - Not random enough
    934532940 - Not random enough
    2319696142 - Not random enough
    833288462 - Not random enough
    3159699558 - Not random enough
    741847558 - Not random enough
    2640416332 - Not random enough
    4116914797 - Not random enough
    2764652187 - Not random enough
    893932700 - Not random enough
    1524433686 - Not random enough
    2747935470 - Not random enough
    2737895382 - Not random enough
    399362299 - Not random enough
    1315504485 - Not random enough
    396651233 - Not random enough
    1076089603 - Not random enough
    1364208694 - Not random enough
    2548285204 - Not random enough
    1592567708 - Not random enough
    2444835764 - Not random enough
    1338649882 - Not random enough
    3399615231 - Not random enough
    1479159200 - Not random enough
    3126836508 - Not random enough
    1289472456 - Not random enough
    3466330048 - Not random enough
    2170586464 - Not random enough
    481812847 - Not random enough
    2520116977 - Not random enough
    454885316 - Not random enough
    2513617667 - Not random enough
    3904306344 - Not random enough
    4215331756 - Not random enough
    1275373032 - Not random enough
    1112870747 - Not random enough
    1441747490 - Not random enough
    2900832636 - Not random enough
    1463567806 - Not random enough
    546377480 - Not random enough
    1921218802 - Not random enough
    183616514 - Not random enough
    1514020659 - Not random enough
    4153857735 - Not random enough
    2939069159 - Not random enough
    3182265817 - Not random enough
    1561095002 - Not random enough
    199352335 - Not random enough
    1803436875 - Not random enough
    1101722786 - Not random enough
    98443511 - Not random enough
    843308119 - Not random enough
    4064491886 - Not random enough
    1276991475 - Not random enough
    2802967118 - Not random enough
    703511923 - Not random enough
    3083418973 - Not random enough
    3756319109 - Not random enough
    4164186446 - Not random enough
    1500674043 - Not random enough
    2710242229 - Not random enough
    2253647336 - Not random enough
    1092529864 - Not random enough
    689803221 - Not random enough
    3039319458 - Not random enough
    3952083068 - Not random enough
    1655428081 - Not random enough
    2300747645 - Not random enough
    1672175396 - Not random enough
    1564545724 - Not random enough
    4060627254 - Not random enough
    2117432240 - Not random enough
    420703351 - Not random enough
    983013567 - Not random enough
    2144359480 - Not random enough
    1759287793 - Not random enough
    1813553135 - Not random enough
    3916983599 - Not random enough
    2256132019 - Not random enough
    3156017603 - Not random enough
    1552847968 - Not random enough
    4203378278 - Not random enough
    2301811711 - Not random enough
    2880882489 - Not random enough
    2936299693 - Not random enough
    778224566 - Not random enough
    3151156000 - Not random enough
    1922812552 - Not random enough
    1722030153 - Not random enough
    2530003744 - Not random enough
    3134145103 - Not random enough
    2970974626 - Not random enough
    1491091952 - Not random enough
    2123078984 - Not random enough
    2770500002 - Not random enough
    2995506271 - Not random enough
    3822487065 - Not random enough
    1979590326 - Not random enough
    1911653314 - Not random enough
    3072264583 - Not random enough
    3791762433 - Not random enough
    954270108 - Not random enough
    3435498032 - Not random enough
    3871673917 - Not random enough
    2529775929 - Not random enough
    1086290140 - Not random enough
    394515691 - Not random enough
    735994975 - Not random enough
    4099644616 - Not random enough
    370120429 - Not random enough
    1571998550 - Not random enough
    2771897111 - Not random enough
    2287997650 - Not random enough
    2753324088 - Not random enough
    3604633360 - Not random enough
    1282649584 - Not random enough
    1462302681 - Not random enough
    1728182478 - Not random enough
    350608369 - Not random enough
    2203870935 - Not random enough
    3487593533 - Not random enough
    3925329917 - Not random enough
    511575321 - Not random enough
    1984812748 - Not random enough
    3725104602 - Not random enough
    3443397300 - Not random enough
    1377657643 - Not random enough
    3080947470 - Not random enough
    3227131697 - Not random enough
    4018121349 - Not random enough
    583162639 - Not random enough
    3579072756 - Not random enough
    951539558 - Not random enough
    713150128 - Not random enough
    3090714866 - Not random enough
    1106912507 - Not random enough
    431642902 - Not random enough
    2131320396 - Not random enough
    3684460949 - Not random enough
    3055494905 - Not random enough
    91220100 - Not random enough
    748620183 - Not random enough
    693709026 - Not random enough
    1001554778 - Not random enough
    230351155 - Not random enough
    2945001254 - Not random enough
    4257333321 - Not random enough
    3277940953 - Not random enough
    2123891432 - Not random enough
    429194280 - Not random enough
    1295517912 - Not random enough
    3034415835 - Not random enough
    1360063642 - Not random enough
    985312271 - Not random enough
    3788483922 - Not random enough
    3466022509 - Not random enough
    2299560612 - Not random enough
    1042534148 - Not random enough
    3240843447 - Not random enough
    2739207233 - Not random enough
    2398541999 - Not random enough
    545611268 - Not random enough
    3841854534 - Not random enough
    2599671798 - Not random enough
    1348273863 - Not random enough
    2821862074 - Not random enough
    2660593236 - Not random enough
    1205136910 - Not random enough
    775362322 - Not random enough
    4244893300 - Not random enough
    3462031762 - Not random enough
    1091648751 - Not random enough
    3295600105 - Not random enough
    1864746947 - Not random enough
    2876335704 - Not random enough
    2414619395 - Not random enough
    3386926461 - Not random enough
    2712275744 - Not random enough
    3633015862 - Not random enough
    1001954496 - Not random enough
    396028204 - Not random enough
    1961357736 - Not random enough
    3550707149 - Not random enough
    3910274089 - Not random enough
    3625804254 - Not random enough
    3063641557 - Not random enough
    3632285727 - Not random enough
    4184499601 - Not random enough
    1906084735 - Not random enough
    1339279869 - Not random enough
    1366835667 - Not random enough
    3661786130 - Not random enough
    3157503985 - Not random enough
    4201815352 - Not random enough
    801427195 - Not random enough
    2875792971 - Not random enough
    1455488862 - Not random enough
    81984665 - Not random enough
    4178904322 - Not random enough
    1430847436 - Not random enough
    2421175024 - Not random enough
    3219761530 - Not random enough
    528636379 - Not random enough
    3143245672 - Not random enough
    3957321334 - Not random enough
    3265172653 - Not random enough
    1042856531 - Not random enough
"""
def parse_comments():
    data = comments.split('\n')[1:-1]
    numbers = []
    for comment in data:
        numbers.append(int(comment.strip().split('-')[0].strip()))
    return numbers

if __name__ == "__main__":
    numbers = parse_comments()

    # create our own version of an MT19937 PRNG.
    myprng = mt19937(0)

    print("Feeding %i numbers from comments var.\nWe'll use those values to create a clone of the current state of Python's built-in PRNG..." % (mt19937.n))
    for i in range(mt19937.n):
        myprng.MT[i] = untemper(numbers[i])
    print("Now, we'll test the clone...")
    print("\nOur clone (pick the first number)")
    for i in range(5):
        r2 = myprng.extract_number()
        print("%10.10i" % (r2))
