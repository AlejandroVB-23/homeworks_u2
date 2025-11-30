"""
Problem 4. Sentence word stats

Descripción:
Dada una oración, el programa debe:
1) Normalizar espacios (quitar espacios al principio y al final).
2) Separar las palabras por espacios.
3) Mostrar:
   - Número total de palabras.
   - Primera palabra.
   - Última palabra.
   - Palabra más corta y más larga (por longitud).

Entradas:
- sentence (string).

Salidas:
- "Word count: <n>"
- "First word: <...>"
- "Last word: <...>"
- "Shortest word: <...>"
- "Longest word: <...>"

Validaciones:
- Oración no vacía tras strip().
- Debe contener al menos una palabra válida después de split().
"""
shortest_word = None
longest_word = None

print("Sentence word stats")
sentence = input("Enter your sentence: ").strip()
if not sentence == "":
   splited_sentence = sentence.split()
   word_count = len(splited_sentence)
   for word in splited_sentence:
      word_length = len(word)
      if shortest_word is None or word_length < len(shortest_word):
         shortest_word = word
      if longest_word is None or word_length > len(longest_word) :
         longest_word = word
   print(f"Word count: {word_count}")
   print(f"First Word: {splited_sentence[0]}")
   print(f"Last Word: {splited_sentence[-1]}")
   print(f"Shortest Word: {shortest_word}")
   print(f"Longest Word: {longest_word}")
else:
   print("No empty entries allowed")

"""
# Test Case 1 (Normal):
# Input: "Python makes coding fun"
# Expected Output:
# Word count: 4
# First Word: Python
# Last Word: fun
# Shortest Word: fun
# Longest Word: Python

# Test Case 2 (Borde):
# Input: "Hola"
# Expected Output:
# Word count: 1
# First Word: Hola
# Last Word: Hola
# Shortest Word: Hola
# Longest Word: Hola

# Test Case 3 (Error):
# Input: ""
# Expected Output:
# No empty entries allowed

"""