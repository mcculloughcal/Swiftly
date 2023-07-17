from tkinter import *
import requests
import json
from flask import Flask

#webapp dev shenanigans
app = Flask(__name__)
@app.route("/")
def index():
    return "yay webapp"

#init GUI
root = Tk()
root.configure(bg="Light Gray")
root.title("Swiftly")
root.geometry('585x585')
lbl = Label(root, text='', bg="Light Gray")
lbl.place(relx=0.5, rely=0.5, anchor=CENTER)



#button function
def clicked():

    lbl.configure(text="Listening... please wait.")
    root.update()

    #record a wav file from default audio input
    with open("wavRecord.py") as f:
        exec(f.read())

    #create a POST payload
    data = {
        'api_token': '74064fc6187a8283ebfe9f85d95954cc',
        'request_api_method': 'recognize',
        'request_http_method': 'POST'
    }
    headers = {
        'content-type': 'multipart/from-data'
    }
    files = {
        'file': open('newWav.wav', 'rb')
    }

    #get a POST response
    response = requests.post('https://api.audd.io/', data=data, files=files)

    #create the is-it-taylor-swift t/f output
    resp2 = json.loads(response.text)
    resp3 = resp2["result"]
    if resp2["status"]=="success" and resp3 != [] and resp3 != "null" and resp3 is not None:
        artist = resp3["artist"] 
        def isTSwift():
            if artist == "Taylor Swift":
                return True
            else:
                return False
            
    #GUI results
        if isTSwift():
            root.configure(bg='Green')
            lbl.configure(text="This is Taylor Swift.", bg="Green")
            return
        else:
            root.configure(bg='Red')
            lbl.configure(text="This is not Taylor Swift.", bg="Red")
            return        
    else:
        root.configure(bg='Light Gray')
        lbl.configure(text="Null result, please try again.", bg='Light Gray')
        return



btn = Button(root, text="Is This Taylor Swift?", command=clicked)
btn.place(relx=0.5, rely=0.3, anchor=CENTER)

root.mainloop()

#more webapp dev shenanigans
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080, debug=True)