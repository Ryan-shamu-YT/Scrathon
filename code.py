new = [
  None,
  None,
  None,
  None,
  None,
  None,
  None,
  None,
  None,
  None,
  "1",
  "2",
  "3",
  "4",
  "5",
  "6",
  "7",
  "8",
  "9",
  "0",
  " ",
  "a",
  "A",
  "b",
  "B",
  "c",
  "C",
  "d",
  "D",
  "e",
  "E",
  "f",
  "F",
  "g",
  "G",
  "h",
  "H",
  "i",
  "I",
  "j",
  "J",
  "k",
  "K",
  "l",
  "L",
  "m",
  "M",
  "n",
  "N",
  "o",
  "O",
  "p",
  "P",
  "q",
  "Q",
  "r",
  "R",
  "s",
  "S",
  "t",
  "T",
  "u",
  "U",
  "v",
  "V",
  "w",
  "W",
  "x",
  "X",
  "y",
  "Y",
  "z",
  "Z",
  "*",
  "/",
  ".",
  ",",
  "!",
  '"',
  "§",
  "$",
  "%",
  "_",
  "-",
  "(",
  "´",
  ")",
  "`",
  "?",
  "new line",
  "@",
  "#",
  "~",
  ";",
  ":",
  "+",
  "&",
  "|",
  "^",
  "'"
]

def encode(password, key):
  e = ''
  for i in range(0, len(str(key))):
    e = str(e) + str(new.index(str(str(key)[int(i)])))
    if len(str(e)) <= 1:
      e = '0' + str(e)
  p = ''
  for i in range(0, len(str(password))):
    p = str(p) + str(new.index(str(str(password)[int(i)])))
    if len(str(p)) <= 1:
      p = '0' + str(p)
  return round(int(e) + int(p))

def decode(password, key):
  p = ''
  for i in range(0, len(str(password))):
    p = str(p) + str(new.index(str(str(password)[int(i)])))
    if len(str(p)) <= 1:
      p = '0' + p

  key = round(int(key) - int(p))
  
  d = ''
  for i in range(0, int(int(len(str(key))) / int(2))):
    d = str(d) + str(new[int(str(str(key)[int(i * 2)]) + str(str(key)[int(i * 2 + 1)]))])

  return d