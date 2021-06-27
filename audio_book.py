import pyttsx3        # pip install pyttsx3
import PyPDF2         # pip install PyPDF2

# creating speak engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# getting voice rate
vr=input("enter voice rate or enter 'd' for default: ")
if vr!='d':
    newVoiceRate = int(vr)
if vr=='d':
    newVoiceRate = 146
engine.setProperty('rate',newVoiceRate)

# creating speak function to speak the text
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# getting pdf path and pg no
pdf=input("enter your pdf path : ")
pg_no=input("for read full page enter 'f' and for start from your selected page enter 's' : ")
if pg_no=='s':
    pg_no=int(input("enter your pdf page number to read : "))
if pg_no=='f':
    pg_no=1

# opening the pdf as read mode
book = open(f'{pdf}.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book) 
# getting total number of page
pages = pdfReader.numPages

# for loop to read the text and speak page by page 
i=0
for num in range(pg_no-1, pages):
    i+=1
    speak(f"page number {i}")
    page = pdfReader.getPage(num)
    text = page.extractText() # extrating the text in this page
    print(text)
    speak(text) # speaking the getting text