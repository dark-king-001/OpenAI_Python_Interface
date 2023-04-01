import os
import json
import openai
import tkinter as tk
dataset = r'settings.json'
f = open(dataset,'r')
data = json.load(f)
f.close()

openai.api_key = data["api_key"]
root=tk.Tk(className='Custom UI for OpenAI')

root.geometry("900x650")
root.configure(background="#444444")

def response(text):
    response =  openai.Completion.create(
        engine="text-davinci-003",
        prompt= text,
        temperature = float(data["settings"]["temperature"]),
        max_tokens = int(data["settings"]['maximum_tokens']),
        top_p = float(data["settings"]['top_p']),
        frequency_penalty = float(data["settings"]['frequency_penalty']),
        presence_penalty = float(data["settings"]['presence_penalty'])
    )
    # print(response.choices[0].text)
    return response.choices[0].text
def complete():
    text = T_field.get("1.0",'end')
    result = response(text)
    T_field.insert(tk.END," "+ result)
def export():
    result = T_field.get("1.0",'end')
    file1 = open(data["save_path"], "a")
    file1.write("\n" + result)
    file1.close()
def clear():
    T_field.delete("1.0", "end")
def saved():
    os.system(data["save_path"])

def settings():
    new = tk.Toplevel(root)
    new.geometry("350x350")
    def updateSettings():
        ndata = {
            "api_key" : token.get("1.0",'end-1c'),
            "save_path" : file_path.get("1.0",'end-1c'),
            "settings" : {
                "temperature" : temp.get("1.0",'end-1c'),
                "maximum_tokens" : max_tokens.get("1.0",'end-1c'),
                "top_p" : top_p.get("1.0",'end-1c'),
                "frequency_penalty" : frequency_penalty.get("1.0",'end-1c'),
                "presence_penalty" : presence_penalty.get("1.0",'end-1c')
            }
        }
        json_object = json.dumps(ndata,indent=4)
        with open(dataset, "w") as outfile:
            outfile.write(json_object)
        global data
        f = open(dataset,'r')
        data = json.load(f)
        f.close()
    
    tk.Label(new, text= "Api Token").grid(row = 0, column=0)
    token = tk.Text(new, height=3, width=20)    
    token.insert(tk.END, data["api_key"])

    tk.Label(new, text= "data file path").grid(row = 1, column=0)
    file_path = tk.Text(new, height=5, width=20)
    file_path.insert(tk.END, data["save_path"])

    tk.Label(new, text= "Temperature ").grid(row = 2, column=0)
    temp = tk.Text(new, height=1, width=10)
    temp.insert(tk.END, data["settings"]["temperature"])

    tk.Label(new, text= "Maximum Tokens ").grid(row = 3, column=0)
    max_tokens = tk.Text(new, height=1, width=10)
    max_tokens.insert(tk.END, data["settings"]['maximum_tokens'])

    tk.Label(new, text= "top p ").grid(row =4, column=0)
    top_p = tk.Text(new, height=1, width=10)
    top_p.insert(tk.END, data["settings"]['top_p'])

    tk.Label(new, text= "frequency penalty ").grid(row = 5, column=0)
    frequency_penalty = tk.Text(new, height=1, width=10)
    frequency_penalty.insert(tk.END, data["settings"]['frequency_penalty'])

    tk.Label(new, text= "presence penalty ").grid(row = 6, column=0)
    presence_penalty = tk.Text(new, height=1, width=10)
    presence_penalty.insert(tk.END, data["settings"]['presence_penalty'])

    tk.Button(new,text = 'Update', command = updateSettings).grid(row=7,column=0)

    token            .grid(row = 0, column=1)
    file_path        .grid(row = 1, column=1)
    temp             .grid(row = 2, column=1)
    max_tokens       .grid(row = 3, column=1)
    top_p            .grid(row = 4, column=1)
    frequency_penalty.grid(row = 5, column=1)
    presence_penalty .grid(row = 6, column=1)

    
complete_btn=tk.Button(root,text = 'Complete', command = complete)
export_btn  =tk.Button(root,text = 'Export', command = export)    
clear_btn   =tk.Button(root,text = 'Clear', command = clear)      
saved_btn   =tk.Button(root,text = 'Open Saved', command = saved) 
settings_btn=tk.Button(root,text = 'Settings', command = settings)
T_field     = tk.Text(root, height=40, width=100)       

complete_btn.grid(column=0)
export_btn  .grid(column=0)
clear_btn   .grid(column=0)
saved_btn   .grid(column=0)
settings_btn.grid(column=0)
T_field     .grid(column=1,row=0,rowspan=40)

root.mainloop()