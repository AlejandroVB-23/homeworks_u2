"""
Problem 5: Word frequency counter

Descripción:
Cuenta la frecuencia de cada palabra en una oración usando:
- Una lista de palabras.
- Un diccionario donde:
  - clave: palabra (string)
  - valor: frecuencia (int)
El programa debe:
1) Leer una oración.
2) Convertirla a minúsculas y separarla en una lista de palabras.
3) Construir un diccionario de frecuencias.
4) Mostrar el diccionario completo y la palabra más frecuente.

Entradas:
- sentence (string).

Salidas:
- "Words list:" <words_list>
- "Frequencies:" <freq_dict>
- "Most common word:" <word> (si hay empate, cualquier una es válida)

Validaciones:
- sentence no vacía tras strip().
- Manejar signos de puntuación simples si el estudiante decide hacerlo 
(documentar su decisión, por ejemplo usando replace()).
- Verificar que la lista de palabras no esté vacía.

Operaciones clave sugeridas:
- lower(), split()
- Recorrer la lista y actualizar el diccionario:
  - if word in freq_dict: freq_dict[word] += 1
  - else: freq_dict[word] = 1
- Uso de un ciclo para encontrar la palabra con mayor frecuencia.
"""
print("Problem 5: Word frequency counter")
sentence = input("Enter your sentence: ").lower()
if not sentence == "":
  words_list = sentence.split()
  freq_dict = {}
  for word in words_list:
    if word in freq_dict:
      freq_dict[word] += 1
    else:
      freq_dict[word] = 1
  highest_freq = None
  for word in freq_dict:
    if highest_freq == None or freq_dict[word] > highest_freq:
      highest_freq = freq_dict[word]
      most_common_word = word

  print(f"Words list: {words_list}")
  print(f"Frequencies: {freq_dict}")
  print(f"Most common word: {most_common_word}")
else:
    print("No empty entries allowed")

"""
# Test Case 1 (Normal):
# Input:
# sentence = "the dog chased the cat"
# words_list -> ['the', 'dog', 'chased', 'the', 'cat']
# freq_dict -> {'the': 2, 'dog': 1, 'chased': 1, 'cat': 1}
# most_common_word -> "the"
# Expected Output:
# Words list: ['the', 'dog', 'chased', 'the', 'cat']
# Frequencies: {'the': 2, 'dog': 1, 'chased': 1, 'cat': 1}
# Most common word: the


# Test Case 2 (Borde):
# Input:
# sentence = "hello"
# words_list -> ['hello']
# freq_dict -> {'hello': 1}
# most_common_word -> "hello"
# Expected Output:
# Words list: ['hello']
# Frequencies: {'hello': 1}
# Most common word: hello


# Test Case 3 (Error):
# Input:
# sentence = ""
# Expected Output:
# No empty entries allowed
"""