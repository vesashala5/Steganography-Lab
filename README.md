# Image Steganography me Python (LSB Method)
## Përshkrimi i Projektit

Ky projekt është realizuar në kuadër të laboratorit për Data Security. Qëllimi i tij është implementimi i një sistemi të thjeshtë të steganografisë së imazheve duke përdorur teknikën Least Significant Bit (LSB) për fshehjen dhe rikthimin e mesazheve sekrete brenda imazheve bitmap (.bmp).

## Funksionaliteti

Sistemi mundëson:

Fshehjen e një mesazhi sekret brenda një imazhi (.bmp)
Rikthimin e mesazhit nga imazhi stego
Përdorimin e parametrave si key, colour_plane dhe bit_position për siguri dhe kontroll
Struktura e Projektit

## Projekti përbëhet nga këto file:

embed.py
extract.py
secret.txt
stego-image.bmp
img/flowers.bmp
img/dice.bmp
img/tiger.bmp
Teknologjitë e Përdorura
Python
Pillow (PIL)
Google Colab
Visual Studio Code
GitHub
Implementimi
embed.py

Ky program përdoret për fshehjen e mesazhit sekret brenda imazhit. Ai lexon mesazhin nga file secret.txt, e konverton në 7-bit ASCII dhe e vendos në pixelat e imazhit duke përdorur një rend pseudo-random.

## Parametrat:

key = 2026
colour_plane = 1
bit_position = 7
extract.py

Ky program përdoret për rikthimin e mesazhit nga imazhi stego (stego-image.bmp). Ai përdor të njëjtat parametra si në embed për të rindërtuar rendin e pixelave dhe për të nxjerrë mesazhin origjinal.

## Eksperimentet
### Testimi me flowers.bmp

Mesazhi u fsheh dhe u rikuperua me sukses. Ndryshimet vizuale ishin minimale.

Ndryshimi i colour_plane

U testuan:

Red (0)
Green (1)
Blue (2)

Mesazhi u rikuperua me sukses në të gjitha rastet.

Ndryshimi i bit_position

U testuan vlerat 7, 5 dhe 0.

Me bit_position = 7 ndryshimet vizuale janë pothuajse të padukshme
Me bit_position = 0 mund të ndodhin deformime më të mëdha, por në këtë projekt ato nuk ishin shumë të theksuara për shkak të mesazhit të shkurtër
Testimi me tiger.bmp

Mesazhi u rikuperua me sukses dhe cilësia vizuale e imazhit mbeti e mirë.

### Observime
bit_position = 7 është më i sigurt për ruajtje pa ndryshime vizuale
key siguron shpërndarje pseudo-random të pixelave
përdorimi i key të gabuar bën që mesazhi të mos rikuperohet saktë
BMP është format i përshtatshëm sepse nuk përdor kompresim
Rezultatet e Kapacitetit

### flowers.bmp
Width: 500
Height: 300
Pixels: 150000
Capacity: 18750 bytes

### dice.bmp
Width: 400
Height: 454
Pixels: 181600
Capacity: 22700 bytes

### tiger.bmp
Width: 520
Height: 330
Pixels: 171600
Capacity: 21450 bytes

## Përfundim

Ky projekt demonstroi me sukses implementimin bazik të steganografisë së imazheve duke përdorur teknikën LSB. Sistemi arriti të fshehë dhe rikuperojë mesazhin sekret në mënyrë efektive, duke ruajtur cilësinë vizuale të imazhit.
