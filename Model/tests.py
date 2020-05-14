from __future__ import unicode_literals
import sys
try:
    from functools import lru_cache
except ImportError:
    from backports.functools_lru_cache import lru_cache
DEVANAGARI = 'devanagari'
ITRANS = 'itrans'
SCHEMES = {}
class Scheme(dict):
  def __init__(self, data=None, synonym_map=None, is_roman=True, name=None):
    super(Scheme, self).__init__(data or {})
    if synonym_map is None:
      synonym_map = {}
    self.synonym_map = synonym_map
    self.is_roman = is_roman
    self.name = name
class SchemeMap(object):
  def __init__(self, from_scheme, to_scheme):
    self.marks = {}
    self.virama = {}
    self.vowels = {}
    self.consonants = {}
    self.non_marks_viraama = {}
    self.from_scheme = from_scheme
    self.to_scheme = to_scheme
    self.max_key_length_from_scheme = max(len(x) for g in from_scheme
                                          for x in from_scheme[g])
    for group in from_scheme.keys():
      if group not in to_scheme.keys():
        continue
      conjunct_map = {}
      for (k, v) in zip(from_scheme[group], to_scheme[group]):
        conjunct_map[k] = v
        if k in from_scheme.synonym_map:
          for k_syn in from_scheme.synonym_map[k]:
            conjunct_map[k_syn] = v
      if group.endswith('marks'):
        self.marks.update(conjunct_map)
      elif group == 'virama':
        self.virama = conjunct_map
      else:
        self.non_marks_viraama.update(conjunct_map)
        if group.endswith('consonants'):
          self.consonants.update(conjunct_map)
        elif group.endswith('vowels'):
          self.vowels.update(conjunct_map)

   

  def __str__(self):
    import pprint
    return pprint.pformat({"vowels": self.vowels,
                           "marks":  self.marks,
                           "virama":  self.virama,
                           "consonants": self.consonants})

def _roman(data, scheme_map, **kw):
  vowels = scheme_map.vowels
  marks = scheme_map.marks
  virama = scheme_map.virama
  consonants = scheme_map.consonants
  non_marks_viraama = scheme_map.non_marks_viraama
  max_key_length_from_scheme = scheme_map.max_key_length_from_scheme
  to_roman = scheme_map.to_scheme.is_roman
  togglers = kw.pop('togglers', set())
  suspend_on = kw.pop('suspend_on', set())
  suspend_off = kw.pop('suspend_off', set())
  if kw:
    raise TypeError('Unexpected keyword argument %s' % list(kw.keys())[0])
  buf = []
  i = 0
  had_consonant = found = False
  len_data = len(data)
  append = buf.append
  toggled = False
  suspended = False
  while i <= len_data:
    token = data[i:i + max_key_length_from_scheme]

    while token:
      if token in togglers:
        toggled = not toggled
        i += 2  
        found = True  
        break
      if token in suspend_on:
        suspended = True
      elif token in suspend_off:
        suspended = False
      if toggled or suspended:
        token = token[:-1]
        continue
      if had_consonant and token in vowels:
        mark = marks.get(token, '')
        if mark:
          append(mark)
        elif to_roman:
          append(vowels[token])
        found = True

      elif token in non_marks_viraama:
        if had_consonant:
          append(virama[''])
        append(non_marks_viraama[token])
        found = True

      if found:
        had_consonant = token in consonants
        i += len(token)
        break
      else:
        token = token[:-1]

    if not found:
      if had_consonant:
        append(virama[''])
      if i < len_data:
        append(data[i])
        had_consonant = False
      i += 1
    found = False
  return ''.join(buf)
def _brahmic(data, scheme_map, **kw):
  marks = scheme_map.marks
  virama = scheme_map.virama
  consonants = scheme_map.consonants
  non_marks_viraama = scheme_map.non_marks_viraama
  to_roman = scheme_map.to_scheme.is_roman
  max_key_length_from_scheme = scheme_map.max_key_length_from_scheme
  buf = []
  i = 0
  to_roman_had_consonant = found = False
  append = buf.append
  while i <= len(data):
    token = data[i:i + max_key_length_from_scheme]
    while token:
      if len(token) == 1:
        if token in marks:
          append(marks[token])
          found = True
        elif token in virama:
          append(virama[token])
          found = True
        else:
          if to_roman_had_consonant:
            append('a')
          append(non_marks_viraama.get(token, token))
          found = True
      else:
        if token in non_marks_viraama:
          if to_roman_had_consonant:
            append('a')
          append(non_marks_viraama.get(token))
          found = True
      if found:
        to_roman_had_consonant = to_roman and token in consonants
        i += len(token)
        break        
      else:
        token = token[:-1]
    if not found:
      if to_roman_had_consonant:
        append(next(iter(virama.values())))
      if i < len(data):
        append(data[i])
        to_roman_had_consonant = False
      i += 1
    found = False
  if to_roman_had_consonant:
    append('a')
  return ''.join(buf)
@lru_cache(maxsize=8)
def _get_scheme_map(input_encoding, output_encoding):
    return SchemeMap(SCHEMES[input_encoding], SCHEMES[output_encoding])
def transliterate(data, _from=None, _to=None, scheme_map=None, **kw):
 
  if scheme_map is None:
    scheme_map = _get_scheme_map(_from, _to)
  options = {
    'togglers': {'##'},
    'suspend_on': set('<'),
    'suspend_off': set('>')
  }
  options.update(kw)
  func = _roman if scheme_map.from_scheme.is_roman else _brahmic
  return func(data, scheme_map, **options)
def _setup():
    s = str.split
    if sys.version_info < (3, 0):
        s = unicode.split
    SCHEMES.update({
    DEVANAGARI: Scheme({
      'vowels': s("""अ आ इ ई उ ऊ ऋ ॠ ऌ ॡ ए ऐ ओ औ"""),
      'marks': s("""ा ि ी ु ू ृ ॄ ॢ ॣ े ै ो ौ"""),
      'virama': s('्'),
      'yogavaahas': s('ं ः ँ'),
      'consonants': s("""
                            क ख ग घ ङ
                            च छ ज झ ञ
                            ट ठ ड ढ ण
                            त थ द ध न
                            प फ ब भ म
                            य र ल व
                            श ष स ह
                            ळ क्ष ज्ञ
                            """),
      'symbols': s("""
                       ॐ ऽ । ॥
                       ० १ २ ३ ४ ५ ६ ७ ८ ९
                       """)
    }, is_roman=False, name=DEVANAGARI),
    ITRANS: Scheme({
      'vowels': s("""a A i I u U RRi RRI LLi LLI e ai o au"""),
      'marks': s("""A i I u U RRi RRI LLi LLI e ai o au"""),
      'virama': [''],
      'yogavaahas': s('M H .N'),
      'consonants': s("""
                            k kh g gh ~N
                            ch Ch j jh ~n
                            T Th D Dh N
                            t th d dh n
                            p ph b bh m
                            y r l v
                            sh Sh s h
                            L kSh j~n
                            """),
      'symbols': s("""
                       OM .a | ||
                       0 1 2 3 4 5 6 7 8 9
                       """)
    }, synonym_map={
      "A": ["aa"], "I": ["ii"], "U": ["uu"], "e": ["E"], "o": ["O"], "RRi": ["R^i"], "RRI": ["R^I"], "LLi": ["L^i"], "LLI": ["L^I"],
      "M": [".m", ".n"], "v": ["w"], "kSh": ["x", "kS"], "j~n": ["GY", "jJN"],
      "||": [".."], "|": ["."],
    }, name=ITRANS)
  })
_setup()
