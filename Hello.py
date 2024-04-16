import streamlit as st

def cesar_cipher_encode(text, shift):
  """
  Fonction pour encoder un texte avec le chiffrement César.

  Args:
    text (str): Le texte à encoder.
    shift (int): Le décalage du chiffrement.

  Returns:
    str: Le texte chiffré.
  """
  alphabet = "abcdefghijklmnopqrstuvwxyz"
  encoded_text = ""

  for char in text:
    if char in alphabet:
      index = alphabet.index(char)
      new_index = (index + shift) % len(alphabet)
      encoded_text += alphabet[new_index]
    else:
      encoded_text += char

  return encoded_text

def cesar_cipher_decode(text, shift):
  """
  Fonction pour décoder un texte avec le chiffrement César.

  Args:
    text (str): Le texte chiffré à décoder.
    shift (int): Le décalage du chiffrement.

  Returns:
    str: Le texte déchiffré.
  """
  return cesar_cipher_encode(text, -shift)

st.title("Chiffrement et déchiffrement César")

st.markdown("Entrez un mot de passe à crypter ou à décrypter :")
password = st.text_input("Mot de passe", "")

st.markdown("Entrez le décalage du chiffrement :")
shift = st.number_input("Décalage", min_value=-25, max_value=25, value=0)

st.markdown("**Chiffrement :**")
encrypted_password = cesar_cipher_encode(password, shift)
st.write(encrypted_password)

st.markdown("**Déchiffrement :**")
decrypted_password = cesar_cipher_decode(encrypted_password, shift)
st.write(decrypted_password)
