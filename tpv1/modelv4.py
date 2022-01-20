from tensorflow import keras
from tensorflow.keras import layers
import tensorflow_hub as hub
import numpy as np


#selber definierte Funktionen

# Sätze, die in x-Array stehen zu einzelnen String-Arrays machen.
def toStrArray(Satz):
  for character in '!?#+()[]{}/""-_*$%=:;,.><~':
    Satz = Satz.replace(character, '')
  return (Satz.split())

# Übergabe eines String-Arrays
def fill(stringArray):
  EmbedIn = [""]*40
  if(len(stringArray) > 41):
   print("Satz zu lang")
  # Error bearbeiten und entsprechende Ausgabe durchführen
  else:
    for i in range (len(stringArray)):
      EmbedIn[i] = stringArray[i]
  return EmbedIn


# Satz zu Satzmatrix
def word2vec(EmbedIn):
    embed = hub.load("https://tfhub.dev/google/nnlm-de-dim50-with-normalization/2")
    return embed(EmbedIn)


def handler(eingabe):

    num_classes = 2
    input_shape = (40, 50, 1)

    model = keras.Sequential(
        [
            keras.Input(shape=input_shape),
            layers.Conv2D(32, kernel_size=(3, 3), activation="relu"),
            layers.MaxPooling2D(pool_size=(2, 2)),
            layers.Conv2D(64, kernel_size=(3, 3), activation="relu"),
            layers.MaxPooling2D(pool_size=(2, 2)),
            layers.Flatten(),
            layers.Dropout(0.5),
            layers.Dense(64, activation="relu"),
            layers.Dense(num_classes, activation="softmax"),
        ]
    )
    model.load_weights('trainiertfinal')


    strArray = toStrArray(eingabe)
    filled = fill(strArray)
    print(filled)
    vectorized = word2vec(filled)
    print(vectorized)

    array = ['']*len(vectorized)
    for i in range(len(vectorized)):
      array[i] = vectorized[i]

    # Make sure images have shape (40, 50, 1) -> dritte Dimension hinzufügen
    array = np.expand_dims(array, -1)
    array = np.expand_dims(array, axis=0)
    print("vectorized shape", array.shape)


    predicted = model.predict(array)
    print (predicted)
    ausgabewert = predicted[0][1]
    return ausgabewert

