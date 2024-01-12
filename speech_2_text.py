import librosa
import torch
from faster_whisper import WhisperModel
from transformers import DistilBertTokenizer, DistilBertForSequenceClassification
class Conversion:
    model = None
    tokenizer = DistilBertTokenizer.from_pretrained('model/bert_model')
    inf_model = DistilBertForSequenceClassification.from_pretrained('model/bert_model')
    def __init__(self):
        self.model = WhisperModel('small', device='cpu', compute_type='int8')
    def convert(self, filename):
        # model = WhisperForConditionalGeneration.from_pretrained("openai/whisper-tiny.en")
        # processor = WhisperProcessor.from_pretrained("openai/whisper-tiny.en")
        # audio,_= librosa.load(filename,sr=16000)

        # metadata= torchaudio.info(filename)

        # input_features=processor(audio, return_tensors='pt',sr=16000).input_features
        # generated_ids = model.generate(input_features)
        # transcription = processor.batch_decode(generated_ids, skip_special_tokens=True)
        segments, _ = self.model.transcribe(filename, vad_filter=True)
        transcription = ""
        for segment in segments:
            transcription = segment.text

        return transcription
    
    def speech(self, audio):
        audio, _ = librosa.load(audio)
        text = self.convert(audio)
        
        label,conf=self.infer_danger(text)
        return label,conf
    def infer_danger(self,text):
        ids= Conversion.tokenizer(text,return_tensors='pt')
        outputs = Conversion.inf_model(**ids)
        probabilities = torch.softmax(outputs.logits, dim=1).detach().numpy()

        # Check if the predicted label corresponds to a request for help
        label = torch.argmax(outputs.logits, dim=1).item()
        labels = ["not_help", "help"]

        return labels[label], probabilities[0, label]


