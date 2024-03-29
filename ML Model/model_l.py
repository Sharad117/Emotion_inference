import pandas as pd

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression


sentences = [
    "Help!",
    "Stop!",
    "Someone, please!",
    "Emergency!",
    "Please, help me!",
    "Get away!",
    "I'm in danger!",
    "No!",
    "Someone, call for help!",
    "I need assistance!",
    "Help now!",
    "Danger!",
    "Please, anyone!",
    "Help me, please!",
    "Stop harassing me!",
    "Somebody, help!",
    "I can't breathe!",
    "Please, make them stop!",
    "This is an emergency!",
    "Why are you doing this?",
    "Help me, I'm scared!",
    "Someone, please intervene!",
    "I'm in distress!",
    "Emergency situation! Help!",
    "Stop harassing me, now!",
    "Quick, assistance needed!",
    "I'm in trouble! Help!",
    "Immediate danger!",
    "Please, someone help!",
    "I can't handle this alone!",
    "Urgent help required!",
    "This is a crisis, help me out!",
    "Stop, I need help!",
    "Someone, call for assistance!",
    "I'm being threatened!",
    "Emergency, act now!",
    "Please, get help for me!",
    "I'm at risk, help!",
    "Intervene, I'm in danger!",
    "Don't ignore, I need help!",
    "Help! Urgent! Now!",
    "Immediate danger! Act!",
    "Emergency! Assistance now!",
    "Stop! Urgent help needed!",
    "I'm at risk! Help me, now!",
    "Critical situation! Help!",
    "This is an emergency! Act immediately!",
    "Stop them! I need urgent help!",
    "Life-threatening! Immediate assistance required!",
    "Assistance needed urgently! Now!",
    "Urgent intervention! Help me, please!",
    "I'm in peril! Emergency assistance!",
    "Stop this danger! Help now!",
    "SOS! Urgent assistance necessary!",
    "Immediate crisis! Help, please!",
    "I'm in imminent danger! Help!",
    "Swift help needed now! Urgent!",
    "Emergency distress! Act now, please!",
    "Urgent danger! Help me, now!",
    "Life-or-death situation! Immediate help!",
    "This is an emergency! Act now, please!",
    "Urgent danger! Help me, now!",
    "Life-or-death situation! Immediate help!",
    "Immediate help required! Now!",
    "Emergency! Urgent assistance, please!",
    "In danger! Quick, help needed!",
    "This is a crisis! Urgent help now!",
    "Help me escape! Urgent situation!",
    "I'm under threat! Immediate assistance!",
    "Emergency distress! Help, now!",
    "Stop! Urgent help necessary!",
    "Danger! Immediate assistance required!",
    "Critical emergency! Help me, please!",
    "Urgent danger! Act now, please!",
    "Life in jeopardy! Quick, help!",
    "Emergency situation! Help me now!",
    "Urgent crisis! Someone, help!",
    "SOS! Immediate assistance, now!",
    "In peril! Urgent help needed!",
    "This is urgent! Help me, now!"
]

label1= 1
label2=0
random_sentences = [
    "The sunsets here are breathtaking.",
    "She danced like nobody was watching.",
    "Pizza is my favorite comfort food.",
    "The mountain air was crisp and refreshing.",
    "Learning a new language can be challenging but rewarding.",
    "Laughter is the best medicine.",
    "The city skyline sparkled with lights at night.",
    "The old bookstore had a charming atmosphere.",
    "Music has the power to evoke strong emotions.",
    "The smell of freshly baked bread is irresistible.",
    "Raindrops tapped gently on the windowpane.",
    "Painting allows me to express my creativity.",
    "The butterfly fluttered gracefully from flower to flower.",
    "Exploring new cultures broadens your perspective.",
    "Reading a good book is like taking a journey.",
    "A cup of hot tea is soothing on a cold day.",
    "The waves crashed against the shore.",
    "The smell of a barbecue fills the air during summer.",
    "The sound of rain on the roof is a calming lullaby.",
    "Hiking through the forest is a great way to connect with nature.",
    "Ice cream is a delicious treat, especially on a hot day.",
    "Traveling opens your mind to new possibilities.",
    "A warm blanket and a good movie make for a cozy night in.",
    "The smell of coffee in the morning is invigorating.",
    "Gazing at the stars on a clear night is awe-inspiring.",
    "Creating art is a form of self-expression.",
    "Kindness has a ripple effect that can change the world.",
    "The first snowfall transforms the landscape into a winter wonderland.",
    "Singing in the shower is a great stress reliever.",
    "A handwritten letter has a personal touch that emails lack.",
    "The laughter of children is infectious and heartwarming.",
    "Morning walks are a peaceful way to start the day.",
    "A good friend is like a rare gem, precious and valuable.",
    "The smell of a campfire brings back fond memories.",
    "Dancing in the rain is liberating and fun.",
    "A smile can brighten someone's day.",
    "Sunflowers always turn their faces towards the sun.",
    "Freshly squeezed orange juice is a breakfast delight.",
    "A hammock in the backyard is the perfect spot for relaxation.",
    "Chasing fireflies on a summer evening is a nostalgic activity.",
    "The aroma of a barbecue can bring neighbors together.",
    "Solving a puzzle is a satisfying mental challenge.",
    "The beauty of a sunset is a reminder of life's fleeting moments.",
    "A handwritten note can make someone's day.",
    "Meditation brings inner peace and clarity.",
    "A well-balanced diet contributes to overall well-being.",
    "Sitting by the fireplace with a good book is a cozy pastime.",
    "The thrill of a roller coaster ride is exhilarating.",
    "A heartfelt apology can mend relationships.",
    "I don't need help.",
    "I can handle it on my own.",
    "No assistance required.",
    "I've got this under control.",
    "Thanks, but I don't need help.",
    "I appreciate it, but I'm fine.",
    "No need for help, thank you.",
    "I can manage without assistance.",
    "I'm okay, no help necessary.",
    "Don't worry, I don't need help.",
    "I'm capable of handling it alone.",
    "Help is not necessary for me.",
    "I'll manage without any assistance.",
    "No, I don't need any help.",
    "I'm not in need of assistance.",
    "I've got it covered, no help needed.",
    "I'm self-sufficient, thanks.",
    "I'm good, no need for help.",
    "I can take care of it by myself.",
    "No assistance required, I'm fine.",
    "I prefer to handle things independently.",
    "I'm independent, I don't need help.",
    "I'm self-reliant, thank you.",
    "I can handle this situation solo.",
    "No thanks, I don't need any help.",
    "I'll manage without any support.",
    "I'm self-supportive, no assistance needed.",
    "I'm capable of resolving this on my own.",
    "No assistance necessary, I've got it.",
    "I'm self-sustaining, no need for help.",
    "I'm self-dependent, thank you.",
    "I can manage without any help.",
    "I don't require assistance at the moment.",
    "I'm self-contained, no need for help.",
    "I'm self-standing, no assistance needed.",
    "I'm handling it independently, thank you.",
    "I can handle it without any assistance.",
    "I'm self-maintaining, no help needed.",
    "I'm self-subsistent, thank you.",
    "I don't need anyone's help right now.",
    "I'm self-sufficient, no assistance required.",
    "I'm capable of resolving this myself.",
    "I'm self-sustained, no need for help.",
    "I'm self-standing, no assistance needed.",
    "I'm self-sufficient, thank you.",
    "I'm managing on my own, no help needed.",
    "I'm self-sustainable, no assistance required.",
    "I don't need help at the moment.",
    "I'm self-sufficient, no assistance required.",
    "I'm handling it on my own, thanks.",
    "I'm self-supporting, no need for help.",
    "I'm self-sufficient, no assistance required.",
    "I can manage independently, thank you.",
    "I don't need any help right now.",
    "I'm self-sustainable, no assistance needed.",
    "I'm handling it on my own, no need for help.",
    "I'm self-sufficient, thank you.",
    "I can manage without assistance.",
    "I'm self-reliant, no need for help.",
    "I'm self-contained, thank you.",
    "I'm good, no assistance necessary.",
    "I can handle this situation without help.",
    "I'm self-sufficient, no assistance needed.",
    "I'm managing independently, no need for help.",
    "I'm self-supporting, thank you.",
    "I'm self-sustained, no assistance required.",
    "I'm self-reliant, no need for help.",
    "I don't need help right now, thanks.",
    "I'm handling it independently, no assistance needed."
    "Don't help!",
    "Don't stop!",
    "Don't someone, please!",
    "Don't emergency!",
    "Don't please, help me!",
    "Don't get away!",
    "I'm not in danger!",
    "Don't no!",
    "Don't someone, don't call for help!",
    "I don't need assistance!",
    "Don't help now!",
    "Don't danger!",
    "Don't please, anyone!",
    "Don't help me, please!",
    "Don't stop harassing me!",
    "Don't somebody, help!",
    "I can breathe!",
    "Don't please, make them stop!",
    "This isn't an emergency!",
    "Why aren't you doing this?",
    "Don't help me, I'm not scared!",
    "Don't someone, don't intervene!",
    "I'm not in distress!",
    "Not an emergency situation! Don't help!",
    "Don't stop harassing me, now!",
    "Not quick, assistance not needed!",
    "I'm not in trouble! Don't help!",
    "No immediate danger!",
    "Don't please, someone don't help!",
    "I can handle this alone!",
    "No urgent help required!",
    "This isn't a crisis, don't help me out!",
    "Don't stop, I don't need help!",
    "Don't someone, don't call for assistance!",
    "I'm not being threatened!",
    "No emergency, don't act now!",
    "Don't please, don't get help for me!",
    "I'm not at risk, don't help!",
    "Don't intervene, I'm not in danger!",
    "Ignore, I don't need help!",
    "Don't help! Not urgent! Not now!",
    "No immediate danger! Don't act!",
    "No emergency! No assistance now!",
    "Don't stop! Not urgent help needed!",
    "I'm not at risk! Don't help me, now!",
    "Not critical situation! Don't help!",
    "This isn't an emergency! Don't act immediately!",
    "Don't stop them! I don't need urgent help!",
    "Not life-threatening! No immediate assistance required!",
    "No assistance needed urgently! Not now!",
    "Not urgent intervention! Don't help me, please!",
    "I'm not in peril! No emergency assistance!",
    "Don't stop this danger! Don't help now!",
    "Not SOS! Not urgent assistance necessary!",
    "No immediate crisis! Don't help, please!",
    "I'm not in imminent danger! Don't help!",
    "Not swift help needed now! Not urgent!",
    "Not emergency distress! Don't act now, please!",
    "Not urgent danger! Don't help me, now!",
    "Not life-or-death situation! No immediate help!",
    "This isn't an emergency! Don't act now, please!",
    "Not urgent danger! Don't help me, now!",
    "Not life-or-death situation! No immediate help!",
    "No immediate help required! Not now!",
    "No emergency! Not urgent assistance, please!",
    "Not in danger! Not quick, help needed!",
    "This isn't a crisis! Not urgent help now!",
    "Don't help me escape! Not urgent situation!",
    "I'm not under threat! No immediate assistance!",
    "Not emergency distress! Don't help, now!",
    "Don't stop! Not urgent help necessary!",
    "Not danger! No immediate assistance required!",
    "Not critical emergency! Don't help me, please!",
    "Not urgent danger! Don't act now, please!",
    "Life not in jeopardy! Not quick, help!",
    "This isn't an emergency situation! Don't help me now!",
    "Not urgent crisis! No someone, help!",
    "Not SOS! Not immediate assistance, now!",
    "Not in peril! No urgent help needed!",
    "This isn't urgent! Don't help me, now!"
]



s= {'text':sentences,'labels':1}
s2={'text':random_sentences,'labels':0}
df1=pd.DataFrame(s2)
df2=pd.DataFrame(s)
df=pd.concat((df1,df2))
df= df.sample(frac=1)



vect= CountVectorizer(ngram_range=(1,3)).fit(df['text'])
feature= vect.transform(df['text'])
model= LogisticRegression(penalty='l2',solver="newton-cholesky")
model.fit(feature, df['labels'])

def predict (l:list)->str:
   feat= vect.transform(l)
   return  model.predict(feat)
