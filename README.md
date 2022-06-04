# Cipher Encryption 

This little python desktop app is inspired from a problem on [Edabit.com](https://edabit.com/challenge/9fbbjaLt22Zfvjjau) related to *Cipher Encryption*. We aim here to play around by chatting only encrypted words just for fun. The principle for a message goes as:

:key: All alpha characters will be treated as uppercase letters.

:key: The first alpha character will not change (except for switching to upper case)

:key: All subsequent alpha characters will be shifted toward "*Z*" by the alphabetical position of the previous alpha character (wrap back to "*A*" if "*Z*" is passed)


:o: **IMPORTANT: A sentence is not encrypted word by word.** :o:  



***


**Example**: The famous sentence *Hello world* is encrypted **HMQXA LLGDP** in this way

P(x) is x position in the alphabet

| Origin | Translation |     Explanation    |
| :----: |    :----:   |        :----:      |
| H      |           H |     First letter   |
| e      |           M |    M = e + P(H)    |
| l      |           Q |    Q = l + P(e)    |
| l      |           X |    X = l + P(l)    |
| o      |           A |    A = o + P(l)    |
| w      |           L |    L = w + P(o)    |
| o      |           L |    L = o + P(w)    |
| r      |           G |    G = r + P(o)    |
| l      |           D |    D = l + P(r)    |
| d      |           P |    P = d + P(l)    |




## Running the app


:key: Clone the files and basically put them in the same folder;

:key: Check all requirements on the packages used;

:key: Run [cipher_main.py](https://github.com/JeanLucYAO/Accessible-cryptography-with-Cipher-Encryption/blob/main/cipher_main.py) with [python 3.9](https://www.python.org/downloads/) or version around.

You should obtain something like this

<img align="center"
src="https://drive.google.com/uc?export=view&id=1LfR5CmQn0odgIe2SW6hU0YBetICgzSX-" 
title="Cipher App"></img>


## Requirements

:key: [Qt version](https://pypi.org/project/PyQt5/) 5.15.2

:key: [PyQt version](https://pypi.org/project/PyQt5/) 5.15.2


## Editing files

:key: You can make changes to [main.ui](https://github.com/JeanLucYAO/Accessible-cryptography-with-Cipher-Encryption/blob/main/main.ui) by using [Qt Designer](https://build-system.fman.io/qt-designer-download)

:key: Just pick your favourite text editor for [cipher_main.py](https://github.com/JeanLucYAO/Accessible-cryptography-with-Cipher-Encryption/blob/main/cipher_main.py). Only make sure you are using python 3.


