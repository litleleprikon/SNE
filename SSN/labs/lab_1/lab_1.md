# Security of Systems and Networks: Lab 1

**Author**: Emil A. Sharifullin 
**Date**:   19 October, 2016  

Assignment about encoding/decoding.

## Installing the VirtualBox

To install virtualbox I used command
```bash
sudo yum install VirtualBox-5.1.x86_64 -y
```

## Crypto
###What is:
#####Affine cipher
Affine cipher is a simple substitution cipher based on addition and multiplication mathematical operations. Affine cipher firstly convert letters to their numbers ant then operates with this numbers. To encrypt and decrypt message in affine cipher you need to know two numbers: on which every letter in text was multiplied and with which it was added. The following formula is used to encrypt message.
$$
E(x) = (ax+b) mod\;m
$$
Where **x** is original symbol, **m** is alphabet size, **a** is multiplicator, **b** is adder.
To decrypt message is used following formula.
$$
D(x) = a^{-1}(x-b)mod\;m
$$

As a simple substitution cipher affine can be cracked with letters frequency counting.

##### 	Playfair

Playfer is the first digramsubstitution cipher was developed by Charles Wheatstone.

To generate the key table, one would first fill in the spaces in the table with the letters of the keyword (dropping any duplicate letters), then fill the remaining spaces with the rest of the letters of the alphabet in order (usually omitting "Q" to reduce the alphabet to fit; other versions put both "I" and "J" in the same space). The key can be written in the top rows of the table, from left to right, or in some other pattern, such as a spiral beginning in the upper-left-hand corner and ending in the center. The keyword together with the conventions for filling in the 5 by 5 table constitute the cipher key.

To encrypt a message, one would break the message into digrams (groups of 2 letters) such that, for example, "HelloWorld" becomes "HE LL OW OR LD", and map them out on the key table. If needed, append an uncommon monogram to complete the final digram. The two letters of the digram are considered as the opposite corners of a rectangle in the key table. Note the relative position of the corners of this rectangle. Then apply the following 4 rules, in order, to each pair of letters in the plaintext:

1. If both letters are the same (or only one letter is left), add an "X" after the first letter. Encrypt the new pair and continue. Some variants of Playfair use "Q" instead of "X", but any letter, itself uncommon as a repeated pair, will do.
2. If the letters appear on the same row of your table, replace them with the letters to their immediate right respectively (wrapping around to the left side of the row if a letter in the original pair was on the right side of the row).
3. If the letters appear on the same column of your table, replace them with the letters immediately below respectively (wrapping around to the top side of the column if a letter in the original pair was on the bottom side of the column).
4. If the letters are not on the same row or column, replace them with the letters on the same row respectively but at the other pair of corners of the rectangle defined by the original pair. The order is important – the first letter of the encrypted pair is the one that lies on the same row as the first letter of the plaintext pair.

To decrypt, use the INVERSE (opposite) of the last 3 rules, and the 1st as-is (dropping any extra "X"s, or "Q"s that do not make sense in the final message when finished).

There are several minor variations of the original Playfair cipher.

**[UPDATE]**

Referencing to this question http://crypto.stackexchange.com/questions/36/what-are-the-main-weaknesses-of-a-playfair-cipher-if-any in playfair reversed bigramms have reversed ciphertexts so with this knowledge we still can perform frequency analisys attack.

##### 	ADFGVX

Is a cipher that was used by German army at WWI. ADFGVX uses six(or five in earlier versions) letters to encrypt messages. This cipher combine substitution and transposition algorithms to make cryptoanalisys more complex. There two steps of encryption:

###### Substitution

At this step we need to use radom filled Polybus square for certain alphabet. For english alphabet it looks like following:

|      | A    | D    | F    | G    | V    | X    |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| A    | 1    | G    | R    | 4    | H    | D    |
| D    | E    | 2    | A    | V    | 9    | M    |
| F    | 8    | P    | I    | N    | K    | Z    |
| G    | B    | Y    | U    | F    | 6    | T    |
| V    | 5    | G    | X    | S    | 3    | O    |
| X    | W    | L    | Q    | 7    | C    | 0    |

Using this table every number and letter can be represented as two lettered code.

###### Transposition

After substitution all pairs of letters is written in table with key word in the header and then columns are sorted alphabetically based on the keyword.

| S    | E    | C    | R    | E    | T    |
| ---- | ---- | ---- | ---- | ---- | ---- |
| D    | F    | G    | X    | G    | X    |
| D    | F    | X    | V    | F    | V    |
| X    | A    | F    | F    | X    | D    |
| X    | D    | G    | A    | D    | A    |
| V    | D    | F    | F    | F    | G    |
| F    | F    | F    | G    | A    | A    |
| A    | A    | D    | F    | D    | X    |

And this table stands to following.

| C    | E    | E    | R    | S    | T    |
| ---- | ---- | ---- | ---- | ---- | ---- |
| G    | F    | G    | X    | D    | X    |
| X    | F    | F    | V    | D    | V    |
| F    | A    | X    | F    | X    | D    |
| G    | D    | D    | A    | X    | A    |
| F    | D    | F    | F    | V    | G    |
| F    | F    | A    | G    | F    | A    |
| D    | A    | D    | F    | A    | X    |

And then all columns are red sequentially and cyphertext looks like G X F G F F D F F A D D F A G F X D F A D X V F A F G F D D X X V F A X V D A G A X

**[UPDATE]**

In my opinion ADFGVX is stronger than playfair because after substitution we need to transpose columns using keyword. This enforce to attacker to make two bruteforce attacks rather than one and makes frequency analisys attack not trivial.

### Encrypt an English text of at least 80 words using the Vigenere cipher and exchange it with one of your fellow students.

As a plaintext I used first two paragraphs form Vigeneres ciphers page at wikipedia.

```
The first well documented description of a polyalphabetic cipher was formulated by Leon Battista Alberti around 1467 and used a metal cipher disc to switch between cipher alphabets. Alberti's system only switched alphabets after several words, and switches were indicated by writing the letter of the corresponding alphabet in the ciphertext. Later, in 1508, Johannes Trithemius, in his work Poligraphia, invented the tabula recta, a critical component of the Vigenère cipher. The Trithemius cipher, however, only provided a progressive, rigid, and predictable system for switching between cipher alphabets.

What is now known as the Vigenère cipher was originally described by Giovan Battista Bellaso in his 1553 book La cifra del. Sig. Giovan Battista Bellaso. He built upon the tabula recta of Trithemius, but added a repeating "countersign" (a key) to switch cipher alphabets every letter. Whereas Alberti and Trithemius used a fixed pattern of substitutions, Bellaso's scheme meant the pattern of substitutions could be easily changed simply by selecting a new key. Keys were typically single words or short phrases, known to both parties in advance, or transmitted "out of band" along with the message. Bellaso's method thus required strong security for only the key. As it is relatively easy to secure a short key phrase, say by a previous private conversation, Bellaso's system was considerably more secure.
```

After encrytion with key "Emils" resulting ciphertext is 

```
XTMQAVEBHWPXLZUYYMYLIPLPKGDQALMAVZXEBWWQEXXSSFQBTUGUXSWVIIDXSDUFDEFMOTCXMZFFMBEAWFILDFQZEAEDWFFHMVOMWQLLEIFIWUMBPPJHUANLSEETLGTJPLAQMYUMBPPJEXXSSFQBDSPNMCLMEAJKXQUZFPKAHAXOPPVEXXSSFQBDSJFMCKIHMCSPIWCVWMVOKAUBNZIEEPJIUVOAGMBPVFKECAXUVRLLQTPLXQZZXXTMNGVDMDHSZLTFKMTAZENMEARFPPUMBPPJXQFEDEFMCARVWSSRZMDLVUBSWQUCDARTQDOSDSAGPUOCSTTQLARHMYLIPBSWXMJFDEDMNLEMKCAXUKLDGAUAGRQVEGJFPPNMSMYWVQKTHLQZEZIFZTLLQUTMWOQAZIDPZOIHMCGRXGAJSHQOWHMXCGKDMDKMHMCAKULLFHBZPVMOBLTPQAJKXQUQGVEETLGTQYYFQBHWIZKTHLQZLDTTIMWXEESSXUAYGAWVZORMAEZIHQRWRQZPUMBPPJAMAZJMSQYSPXGOWWOZTTIPJJYMADLFFMBEAWFIMWPXIDGMZPTKFAWVDEOQQJEPMWKMSOTGZMVMSXFQDLENMWDEEWSWFGQWLYBWYLLQBLTYXICWGFIZXXDQEZIYQFKFGBLVHQLLJIBMLLMZONGYZBPJWUOYSOQGEGWIQEULOQAZIDIWHLMJPLWQDPJCXMELIDESWVQIDSPNMCLMMVOLVUBSWQUCDMWQLLXMJMOHEFBPJRANDMFEBTLYFQZFWNMWDEEWDKGTMXWQQIYLXTMASXFMCFSRAFTWFQEMXUWYKGACWVFQMLKMXGNZEZOPVWUUADCNGDWPQKEARSIYWAWMJCIKAHWVQBJHMOIWDCEQYYPQEZJHEWCKLAZEHLDIDWWWVZORFWMGXTXLJXUMDARMLGSROMZJXDIYKQUBEWHACEGJNIYVEXWYYAUBSLLQUPKWMOPTIXTLKSEUPLLALEZYEZPIYUZPVWFZZFKEMNMVUBJXSDWYDCFPPCIKIDAXUACWPMBTNIXGPSWKBZKIOCCWEEPZJXWMJHLDIDWWMGMQEBZPNMACDHVUDLLIOWYNIDALLMAVMWPXIDGWEGDLIYELKGAVDAHQZLTPKUZJIEMNMVQ
```

### Crack the crypted text of your fellow student using the Vigenere cipher tool.

My fellow student gave me following ciphertext 

```
SGRUIIPLFITPWWRLJAGRNEQBDDOHCQXLFACOWQPAWXGPAAUHYEGRAVEYQPGIKZGHUHYHPBGYLYCHZQPHDAZSEVFPUAGHZIFPXFRUAVVSWTGHNIEJGRQLJOVVSPFHQLQYSNQRIAWIKTVWQBKVFBNVALWWGNGKAEKYANTRBBJLEAPKEVGAZEYHPBGYANQLYIVLVBLWDMNHEPJRQTFIWRRFKZFLVAFWDMGUUICKAZGKKUOVPQVBLIBQPPGHUTVRJWHWJEFVEVIHCELDHAQTGVRGPPGYGTBUOWVOSTGKAVGELKRBLZGZKUFHZIFPXFRUAVVLDEPWNQEHDPNWDECFSNQWDCUHVISIAZGULSHEOBKAMTVRJEQBDDBFYCTMGRRDYPMLQPEHOAVOWRRZWATVLAGLKVQMSTYHWAVAZEELCPVOSNQUKBQYYIILJOCKAFSHNMPAKUOVPQVBLIBQWTROSBRWPPKZUOAWEVWLVFBUAIEODEGWAZKULHRPAAUHYEHQPQNAZEZHOACNWWNVYWOWDEGHZIPKSSRUEMUVXSHEOBKAMTVRJAGHUHQLBNGYWNGINWOAZEBWDMTZZAQRYKWYJEQWKKTLSTRDYGROWRGHTBHYGMGKAXNHANGHTBVOWCLSDMTAWXGZKCNKLHRQXMVYSNFPEBVLVAFQKZOHDTBDJWRLJAGRNWHHFOGKAZGUAGZDIIEOANRWDQUVHEEDPWTDGUYGGMAPFTUHYGROWRGHTBCUVAFOKVIHKAYOPPGZWTGLJOUVXTUHZMEPHHRUEVITSCULJMYLJEVGAVVPUAYWKBJVKEBIPPGLFCVSDMTPFGZDYPKUWFBUADGYQKRBLZGZKTUHNMXLJSRVQJUAATHWEWPDGUYGKKEBJAAGPPGWDAVQPMZAEEFVWOGDGUYGAUGYYE
```

To crack it I used free [online ciphers cracking tool](https://f00l.de/hacking/vigenere.php).  After bruteforcing different key sizes I realized that key length is 8, key is "sandwich" and plain text is 

```
AGERMANENIGMAOPERATORWOULDBEGIVENAPLAINTEXTMESSAGETOENCRYPTFOREACHLETTERTYPEDINALAMPINDICATEDADIFFERENTLETTERACCORDINGTOAPSEUDORANDOMSUBSTITUTIONBASEDUPONTHEWIRINGOFTHEMACHINETHELETTERINDICATEDBYTHELAMPWOULDBERECORDEDASTHEENCIPHEREDSUBSTITUTIONTHEACTIONOFPRESSINGAKEYALSOMOVEDTHEROTORSOTHATTHENEXTKEYPRESSUSEDADIFFERENTELECTRICALPATHWAYANDTHUSADIFFERENTSUBSTITUTIONWOULDOCCURFOREACHKEYPRESSTHEREWASROTATIONOFATLEASTTHERIGHTHANDROTORGIVINGADIFFERENTSUBSTITUTIONALPHABETTHISCONTINUEDFOREACHLETTERINTHEM
```

**[UPDATE]**

This site allows to bruteforce keys based on decrypted text frequency analysis and comparing with dictionary to find words and sentences. 

### Go through the previous two steps again, this time using a cipher of your own choosing. Do not tellyour fellow student what cipher you used!

##### My cipher

For my teammate I chase kamasutra cipher and after encryption plain text 

```
AT THE END OF LAST WEEK, WE (THE MOBILE LAB) ALL TURNED TO LOOK AT EACH OTHER. DCAN YOU BELIEVE ITDS ONLY BEEN 18 DAYS SINCE WE RAN OUR FIRST PUBLIC EXPERIMENT?D ONE OF US ASKED. WE COULD NOT IN FACT BELIEVE IT. AFTER MONTHS OF RAMPING UP THE LAB, WE WERE SUDDENLY OPERATING AT FULL SPEED.
THE LAST SEVERAL WEEKS HAVE BEEN HUGE FOR US: WE WELCOMED ANOTHER DEVELOPER, CONNOR JENNINGS; WE RAN TWO PUBLIC VERSIONS OF OUR JOBS REPORT NOTIFICATION EXPERIMENT; WE COVERED TWO PRIMARY NIGHTS THROUGH NOTIFICATIONS; AND WE RAN A NOTIFICATIONS EXPERIMENT COVERING THE EU REFERENDUM.
AND WEDVE LEARNED A LOT.
WEDVE KNOWN SINCE ESTABLISHING OUR FIVE AREAS OF FOCUS THAT WE WANTED TO EXPERIMENT WITH NOTIFICATIONS. THE JOBS REPORT, PRIMARIES, AND NOW THE EU REFERENDUM, HAVE BEEN INTERESTING FOR A FEW REASONS: THEY ARE EVENTS THAT UNFOLD OVER THE COURSE OF A NUMBER OF HOURS WHERE THERE ARE SMALLER DEVELOPMENTS THROUGHOUT.
MOST ORGANIZATIONS ARE USING NEWS ALERTS TO PUSH OUT TOP NEWS, AND INCLUDE ONLY STRAIGHT HEADLINES. THIS IS WITH GOOD REASON: ALERTS REQUIRE AN APP DOWNLOAD, AND A USERDS OPTIONS ARE USUALLY EITHER TO GET EVERY ALERT (ALTHOUGH SOME ORGANIZATIONS HAVE BROKEN DOWN THE OPTIONS TO SET OF TOPICAL PREFERENCES: SPORTS, BUSINESS, ETC) OR NONE, MAKING THE RISK OF ALIENATING A USER WITH ONE TOO MANY ALERTS A CONSTANT.
```

was 

```
VG GOK KUM HC SVLG XKKE, XK (GOK DHZJSK SVZ) VSS GNYUKM GH SHHE VG KVFO HGOKY. MFVU RHN ZKSJKAK JGML HUSR ZKKU 18 MVRL LJUFK XK YVU HNY CJYLG QNZSJF KWQKYJDKUG?M HUK HC NL VLEKM. XK FHNSM UHG JU CVFG ZKSJKAK JG. VCGKY DHUGOL HC YVDQJUT NQ GOK SVZ, XK XKYK LNMMKUSR HQKYVGJUT VG CNSS LQKKM.
GOK SVLG LKAKYVS XKKEL OVAK ZKKU ONTK CHY NL: XK XKSFHDKM VUHGOKY MKAKSHQKY, FHUUHY IKUUJUTL; XK YVU GXH QNZSJF AKYLJHUL HC HNY IHZL YKQHYG UHGJCJFVGJHU KWQKYJDKUG; XK FHAKYKM GXH QYJDVYR UJTOGL GOYHNTO UHGJCJFVGJHUL; VUM XK YVU V UHGJCJFVGJHUL KWQKYJDKUG FHAKYJUT GOK KN YKCKYKUMND.
VUM XKMAK SKVYUKM V SHG.
XKMAK EUHXU LJUFK KLGVZSJLOJUT HNY CJAK VYKVL HC CHFNL GOVG XK XVUGKM GH KWQKYJDKUG XJGO UHGJCJFVGJHUL. GOK IHZL YKQHYG, QYJDVYJKL, VUM UHX GOK KN YKCKYKUMND, OVAK ZKKU JUGKYKLGJUT CHY V CKX YKVLHUL: GOKR VYK KAKUGL GOVG NUCHSM HAKY GOK FHNYLK HC V UNDZKY HC OHNYL XOKYK GOKYK VYK LDVSSKY MKAKSHQDKUGL GOYHNTOHNG.
DHLG HYTVUJBVGJHUL VYK NLJUT UKXL VSKYGL GH QNLO HNG GHQ UKXL, VUM JUFSNMK HUSR LGYVJTOG OKVMSJUKL. GOJL JL XJGO THHM YKVLHU: VSKYGL YKPNJYK VU VQQ MHXUSHVM, VUM V NLKYML HQGJHUL VYK NLNVSSR KJGOKY GH TKG KAKYR VSKYG (VSGOHNTO LHDK HYTVUJBVGJHUL OVAK ZYHEKU MHXU GOK HQGJHUL GH LKG HC GHQJFVS QYKCKYKUFKL: LQHYGL, ZNLJUKLL, KGF) HY UHUK, DVEJUT GOK YJLE HC VSJKUVGJUT V NLKY XJGO HUK GHH DVUR VSKYGL V FHULGVUG.
```

##### My teammate's cipher

My teammate gave me following ciphertext

```
TVMLDVPZMNAWTVMLDVPZMTMLZWNULTZPIZBNPPDXVTIPVMGMLPZWSINSCDMSIZXDXZASPIZJVLSZCDMFDSIDBSDPGZNRFDDWZAFULPIADBLXDGZALAFDVSULRZSIZUNMFZPSSZUZPTDGZSINSZYZMBNPFDDWQHCZZSDIXHGDDMULSSUZCZZSLBDAWZMBIDBLUUGVSDAHDVMPIDZPNAWPSDTRLAFPCDMHDVADBWZNMPLPINUUQZNFMZNSWZNUSDDCNMDCCSDSMDVQUZXHPZUCNQDVSHDVOVPSNSSILPXDXZASIZMIZNWPSMVTRNFNLAPSSIZMDDCDCSIZINUULACNTSPIZBNPADBMNSIZMXDMZSINAALAZCZZSILFINAWPIZNSDATZSDDRVGSIZULSSUZFDUWZARZHNAWIVMMLZWDCCSDSIZFNMWZAWDDMGDDMNULTZLSBNPNPXVTINPPIZTDVUWWDUHLAFWDBADADAZPLWZSDUDDRSIMDVFILASDSIZFNMWZABLSIDAZZHZQVSSDFZSSIMDVFIBNPXDMZIDGZUZPPSINAZYZMPIZPNSWDBANAWQZFNASDTMHNFNLAPIZBZASDAPIZWWLAFFNUUDAPDCSZNMPVASLUSIZMZBNPNUNMFZGDDUNUUMDVAWIZMNAWMZNTILAFINUCWDBASIZINUU
```

I tried to crack it with frequency analyser, but because of small message length this idea was failed. After that I tried different transposition ciphers and they was wrong choices. After that I tried to bruteforce affine cipher at http://www.dcode.fr/affine-cipher and the possible solution was A=3 and B=13 and plain text is

```
CURIOUSERANDCURIOUSERCRIEDALICESHEWASSOMUCHSURPRISEDTHATFORTHEMOMENTSHEQUITEFORGOTHOWTOSPEAKGOODENGLISHNOWIMOPENINGOUTLIKETHELARGESTTELESCOPETHATEVERWASGOODBYFEETOHMYPOORLITTLEFEETIWONDERWHOWILLPUTONYOURSHOESANDSTOCKINGSFORYOUNOWDEARSISHALLBEAGREATDEALTOOFAROFFTOTROUBLEMYSELFABOUTYOUJUSTATTHISMOMENTHERHEADSTRUCKAGAINSTTHEROOFOFTHEHALLINFACTSHEWASNOWRATHERMORETHANNINEFEETHIGHANDSHEATONCETOOKUPTHELITTLEGOLDENKEYANDHURRIEDOFFTOTHEGARDENDOORPOORALICEITWASASMUCHASSHECOULDDOLYINGDOWNONONESIDETOLOOKTHROUGHINTOTHEGARDENWITHONEEYEBUTTOGETTHROUGHWASMOREHOPELESSTHANEVERSHESATDOWNANDBEGANTOCRYAGAINSHEWENTONSHEDDINGGALLONSOFTEARSUNTILTHEREWASALARGEPOOLALLROUNDHERANDREACHINGHALFDOWNTHEHALL
```

