from bytestream import *
from copy import deepcopy



class HuffmanTree:
  def __init__(self, freq: int, char: str = None, left = None, right = None):
    self.char = char
    self.freq = freq
    self.left = left
    self.right = right

  def __repr__(self):
    # N'hésitez pas à modifier cette fonction
    return f"({self.char}:{self.freq})"



def build_freqs(text: str) -> dict[str, int]:

  freqs = {char: 0 for char in text}

  for char in text:
    freqs[char] += 1

  return freqs



def build_huffman_tree(freqs: dict[str, int]) -> HuffmanTree:
  trees = [HuffmanTree(freq, char) for char, freq in freqs.items()]

  while len(trees) > 1:
    trees.sort(key=lambda tree: tree.freq)

    left = trees.pop(0)
    right = trees.pop(0)

    parent = HuffmanTree(left.freq + right.freq, left=left, right=right)
    trees.append(parent)

  return trees[0]



def build_encodings(tree: HuffmanTree, code="") -> dict[str, str]:
    encodings = {}

    if tree.char is not None:
        encodings[tree.char] = code

    else:
        if tree.left:
            left_encodings = build_encodings(tree.left, code + "0")

            for key, value in left_encodings.items():
                encodings[key] = value

        if tree.right:
            right_encodings = build_encodings(tree.right, code + "1")

            for key, value in right_encodings.items():
                encodings[key] = value

    return encodings



def huffman_encode(plain: str, tree: HuffmanTree) -> bytes:
  encodings = build_encodings(tree)

  compressed = ""  # TODO

  for char in plain:
     compressed += encodings[char]

  return bin2bytes(compressed)



def huffman_decode(bytestream: bytes, tree: HuffmanTree) -> str:
  compressed = bytes2bin(bytestream)

  plain = ""  # TODO

  root = deepcopy(tree)

  i = 0

  while i < len(compressed):
     
      byte = int(compressed[i])

      if byte == 0:
        tree = tree.left

      if byte == 1:
        tree = tree.right

      if tree.char is not None:
        plain += tree.char
        tree = root
     
      i += 1

  return plain

# TESTS MANUELS
freqs = build_freqs('hello-world')
# print(freqs)

tree = build_huffman_tree(freqs)


encoding = build_encodings(tree)
print(encoding)

binaire = huffman_encode("hello-world", tree)
print(binaire)

decode = huffman_decode(binaire, tree)
print(decode)