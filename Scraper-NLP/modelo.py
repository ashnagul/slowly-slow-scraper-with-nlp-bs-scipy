                                                                                                                                                                                                                                                                                                                                                                                                                            import nltk
import spacy

def parser_spacy_texto(texto, idioma='es'):
    nlp=spacy.load(idioma)
    texto=nlp(texto)
    textoparseado=[]
    for palabra in texto:
        textoparseado.append(palabra.text)
    return textoparseado

def parsers_spacy_textos_mismalista(textos, idioma='es'):
    textosparseados=[]
    nlp=spacy.load(idioma)
    for texto in textos:
        texto=nlp(texto)
        for palabra in texto:
            textosparseados.append(palabra.text)
    return textosparseados

def parsers_spacy_textos_distintalista(textos, nlp=spacy.load('es')):
    textosparseados=[]
    for texto in textos:
        texto=nlp(texto)
        listatexto=[]
        for palabra in texto:
            listatexto.append(palabra.text)
        textosparseados.append(listatexto)
    return textosparseados

def word_embedding(textos, nlp=spacy.load('es_core_news_md')):
    word_embedding=[]
    for texto in textos:
        texto=nlp(texto)
        listatexto=[]
        for palabra in texto:
            listatexto.append(palabra.vector)
        word_embedding.append(listatexto)
    return word_embedding

a=word_embedding(['Hola','Chao'])
print(a)
