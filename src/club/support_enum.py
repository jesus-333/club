"""

Authors
-------
Alberto Zancanaro <alberto.zancanaro@uni.lu>

"""
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Imports

from enum import Enum
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

class mode(str, Enum) :
    compress = "compress"
    decompress = "decompress"

class language(str, Enum) :
    en = "en"
    es = "es"
    de = "de"
    fr = "fr"
    it = "it"
    pt = "pt"
    nl = "nl"
    el = "el"
    nb = "nb"
    lt = "lt"
    ja = "ja"
    zh = "zh"
    pl = "pl"
    ro = "ro"
    ru = "ru"

