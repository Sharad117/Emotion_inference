import model_l, s2t
text= s2t.s2t('help.mp3')
vect= model_l.predict([text])
print(vect)
