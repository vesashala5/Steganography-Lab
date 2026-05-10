# Image Steganography
## Përshkrimi

Ky projekt është realizuar në kuadër të lëndës **Data Security** dhe demonstron implementimin praktik të **steganografisë së imazheve** duke përdorur teknikën **Least Significant Bit (LSB)**.

Sistemi mundëson fshehjen e një mesazhi sekret brenda një imazhi bitmap (`.bmp`) dhe rikthimin e tij duke përdorur të njëjtët parametra të konfigurimit.

---

## Qëllimi i Projektit

Qëllimi është ndërtimi i një sistemi që:

* Fsheh një mesazh sekret brenda një imazhi `.bmp`
* Rikthen mesazhin nga imazhi stego
* Përdor parametra konfigurimi për kontroll dhe siguri (`key`, `colour_plane`, `bit_position`)

---

## Struktura e Projektit

```
steg_lab/
│
├── embed.py
├── extract.py
├── secret.txt
├── stego-image.bmp
│
└── img/
    ├── flowers.bmp
    ├── dice.bmp
    └── tiger.bmp
```

---

## Teknologjitë e Përdorura

* Python
* Pillow (PIL)
* Google Colab
* Visual Studio Code
* GitHub

---

## Implementimi

### `embed.py`

Programi përdoret për fshehjen e mesazhit sekret në imazh.

Hapat që ndjek:

1. Lexon mesazhin nga `secret.txt`
2. E konverton në **7-bit ASCII**
3. E shpërndan në pikselët e imazhit duke përdorur rend **pseudo-random**

**Parametrat e përdorur:**

```python
key = 2026
colour_plane = 1
bit_position = 7
```

---

### `extract.py`

Programi përdoret për nxjerrjen e mesazhit nga `stego-image.bmp`.

Përdor të njëjtët parametra (`key`, `colour_plane`, `bit_position`) për të rindërtuar rendin e pikselëve dhe për të rikuperuar mesazhin origjinal.

---

## Eksperimentet e Realizuara

### Testimi me `flowers.bmp`

Sistemi u ekzekutua me:

* `colour_plane = 1`
* `bit_position = 7`

Mesazhi u rikuperua me sukses dhe ndryshimet vizuale në imazh ishin minimale.

---

### Ndryshimi i `colour_plane`

U testuan të tre planet e ngjyrave:

* Red (`0`)
* Green (`1`)
* Blue (`2`)

Në të gjitha rastet, mesazhi u rikuperua me sukses me ndryshime shumë të vogla vizuale.

---

### Ndryshimi i `bit_position`

U testuan vlerat:

* `7`

* `5`

* `0`

* Me `bit_position = 7`, ndryshimet vizuale ishin pothuajse të padukshme

* Me `bit_position = 0`, pritet deformim më i madh vizual sepse modifikohet biti më i rëndësishëm i pikselit. Në eksperiment, deformimi nuk ishte shumë i theksuar për shkak të gjatësisë së mesazhit dhe shpërndarjes së pikselëve.

---

### Testimi me `tiger.bmp`

Sistemi u testua edhe me këtë imazh duke përdorur `bit_position = 7`. Mesazhi u rikuperua me sukses dhe cilësia vizuale mbeti e mirë.

---

## Rezultatet e Kapacitetit të Imazheve

Kapaciteti për ruajtjen e të dhënave varet direkt nga numri i pikselëve (`width × height`).

| Image       | Width | Height | Pixels | Capacity (bits) | Capacity (bytes) |
| ----------- | ----: | -----: | -----: | --------------: | ---------------: |
| flowers.bmp |   500 |    300 | 150000 |          150000 |            18750 |
| dice.bmp    |   400 |    454 | 181600 |          181600 |            22700 |
| tiger.bmp   |   520 |    330 | 171600 |          171600 |            21450 |

Imazhi **dice.bmp** ka kapacitetin më të madh për ruajtjen e të dhënave sepse ka numrin më të madh të pikselëve.

---

## Testimi me `key` të gabuar

`extract.py` u ekzekutua me një `key` të pasaktë (p.sh. `1234` në vend të `2026`).

Rezultati ishte një mesazh i korruptuar dhe i pakuptueshëm.

**Shpjegimi:**
Kur përdoret `key` i gabuar, rendi pseudo-random i pikselëve nuk përputhet me atë të përdorur gjatë embedding-ut. Si rezultat, bitat lexohen në rend të gabuar dhe mesazhi nuk mund të rikuperohet saktë.

Kjo tregon rëndësinë e `key` si komponent sigurie në sistemin e steganografisë.

---

## Përmbledhje

Ky projekt demonstron implementimin praktik të steganografisë së imazheve me teknikën LSB duke përdorur Python. Sistemi arrin të fshehë dhe rikuperojë mesazhin sekret me sukses, duke ruajtur cilësinë vizuale të imazhit dhe duke ofruar kontroll përmes parametrave të konfigurimit.
