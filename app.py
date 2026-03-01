from tkinter import *
from mydb import Database
from tkinter import messagebox
from myapi import API

class NLPApp:

    def __init__(self):

        self.db_object = Database()
        self.api_object = API()


        self.root = Tk()
        self.root.title("NLPApp")
        self.root.configure(bg="#334d4d")
        self.root.geometry('400x600')
        self.root.iconbitmap('resources/favicon.ico')
        
        self.login()
        
        self.root.mainloop()
        


    def login(self):
        
        self.clear()
        
        heading = Label(self.root,text = "NLP App",bg = "#334d4d", fg = "white")
        heading.pack(pady=(20,30))
        heading.configure(font = ("Verdana", 25, "bold"))


        label1 = Label(self.root,text = "Enter Email", bg ="#334d4d", fg = "white")
        label1.pack(pady=(15,10))
        label1.configure(font=("verdana", 15))

        self.email_input = Entry(self.root, width = 50)
        self.email_input.pack(pady=(5,10),ipady = 5)


        label2 = Label(self.root,text = "Enter Password", bg ="#334d4d", fg = "white")
        label2.pack(pady=(15,10))
        label2.configure(font=("verdana", 15))

        self.pass_input = Entry(self.root, width = 50, show = "*")
        self.pass_input.pack(pady=(5,10),ipady = 5)


        login_btn = Button(self.root,text = "Login", width = 25, command = self.logging_in)
        login_btn.pack(pady = (15,20))

        label3 = Label(self.root,text = "Not a Member?", bg ="#334d4d", fg = "white")
        label3.pack(pady=(30,5))
        label3.configure(font=("verdana", 10))    

        redirect_btn = Button(self.root,text = "Register", width = 15, command = self.register)
        redirect_btn.pack(pady = (5,20))    


    def register(self):
        self.clear()

        heading = Label(self.root,text = "NLP App",bg = "#334d4d", fg = "white")
        heading.pack(pady=(20,30))
        heading.configure(font = ("Verdana", 25, "bold"))


        label0 = Label(self.root,text = "Enter Name", bg ="#334d4d", fg = "white")
        label0.pack(pady=(15,10))
        label0.configure(font=("verdana", 15))

        self.name_input = Entry(self.root, width = 50)
        self.name_input.pack(pady=(5,10),ipady = 5)


        label1 = Label(self.root,text = "Enter Email", bg ="#334d4d", fg = "white")
        label1.pack(pady=(15,10))
        label1.configure(font=("verdana", 15))

        self.email_input = Entry(self.root, width = 50)
        self.email_input.pack(pady=(5,10),ipady = 5)


        label2 = Label(self.root,text = "Enter Password", bg ="#334d4d", fg = "white")
        label2.pack(pady=(15,10))
        label2.configure(font=("verdana", 15))

        self.pass_input = Entry(self.root, width = 50, show = "*")
        self.pass_input.pack(pady=(5,10),ipady = 5)


        login_btn = Button(self.root,text = "Register", width = 25, command = self.registration)
        login_btn.pack(pady = (15,20))

        label3 = Label(self.root,text = "Already a Member?", bg ="#334d4d", fg = "white")
        label3.pack(pady=(30,5))
        label3.configure(font=("verdana", 10))    

        redirect_btn = Button(self.root,text = "Login", width = 15, command = self.login)
        redirect_btn.pack(pady = (5,20))



    def registration(self):
        name = self.name_input.get()
        email = self.email_input.get()
        password = self.pass_input.get()

        if name == "" and email == "" and password == "":
            messagebox.showinfo("Error","Please enter all details carefully")
        else:
            response = self.db_object.add_data(name,email,password)
            if response:
                messagebox.showinfo("Success","Registration Successful!")
            else:
                messagebox.showinfo("Failed","Email already Exist!")



    def logging_in(self):
        email = self.email_input.get()
        password = self.pass_input.get()

        if email == "" and password == "":
            messagebox.showinfo("Error", "email and pssword can't be empty")
        else:
            self.response = self.db_object.search_data(email,password)
            if self.response:
                self.home()
            else:
                messagebox.showinfo("Failed", "Something Wrong check your email or password")



    def home(self):
        self.user_heading()

        sentiment_btn = Button(self.root, text = "Sentiment Analysis", width = 40, command = self.sentiment_analysis_gui)
        sentiment_btn.pack(pady=(15,10), ipady = 6)   

        ner_btn = Button(self.root, text = "NER(Entity Extraction)", width = 40, command = self.ner_gui)
        ner_btn.pack(pady=(10,10), ipady = 6) 

        headline_btn = Button(self.root, text = "Headline Genration", width = 40, command = self.headline_generation_gui)
        headline_btn.pack(pady=(10,10), ipady = 6) 

        redirect_btn = Button(self.root,text = "Logout", width = 15, command = self.login)
        redirect_btn.pack(pady = (20,20))


    
    def sentiment_analysis_gui(self):
        self.user_heading()


        heading = Label(self.root,text = "Sentiment Analysis",bg = "#334d4d", fg = "white")
        heading.pack(pady=(10,20))
        heading.configure(font = ("Verdana", 18, "bold"))

        label1 = Label(self.root, text="Enter The Text", bg = "#334d4d", fg = "white")
        label1.pack(pady = (5,0))
        label1.configure(font = ("Helvetica",10))
        self.user_input = Text(self.root, height = 6, width = 40)
        self.user_input.pack(pady = (10,10))

        analyze_btn = Button(self.root,text = "Analyze", width = 25, command = self.sentiment_analysis)
        analyze_btn.pack(pady = (7,10))

        self.result = Label(self.root,text = "",bg = "#334d4d", fg = "white")
        self.result.pack(pady = (10,0))
        self.result.configure(font = ("Helvetica",10,"bold"))

        back_btn = Button(self.root,text = "Back", width = 15, command = self.home)
        back_btn.pack(pady = (20,20))

    def sentiment_analysis(self):
        text = self.user_input.get("1.0", "end-1c")
        result = self.api_object.sentiment_analysis(text) 
        result_list = []
        for i in result["labels"]:
            result_list.append(i)

        self.result["text"] = result
    
    def headline_generation_gui(self):
        self.user_heading()

        heading = Label(self.root,text = "Headline Generation",bg = "#334d4d", fg = "white")
        heading.pack(pady=(10,20))
        heading.configure(font = ("Verdana", 18, "bold"))

        label1 = Label(self.root, text="Enter The Text", bg = "#334d4d", fg = "white")
        label1.pack(pady = (5,0))
        label1.configure(font = ("Helvetica",10))
        self.user_input = Text(self.root, height = 6, width = 40)
        self.user_input.pack(pady = (10,10))

        analyze_btn = Button(self.root,text = "Generate", width = 25, command = self.headline_generation)
        analyze_btn.pack(pady = (7,10))

        self.result = Label(self.root,text = "",bg = "#334d4d", fg = "white")
        self.result.pack(pady = (10,0))
        self.result.configure(font = ("Helvetica",10,"bold"))


        back_btn = Button(self.root,text = "Back", width = 15, command = self.home)
        back_btn.pack(pady = (20,20))

    
    def headline_generation(self):
        text = self.user_input.get("1.0", "end-1c")
        result = self.api_object.headline_generation(text)
        self.result["text"] = result["summary_text"]


    def ner_gui(self):
        self.user_heading()

        heading = Label(self.root,text = "NER(Entity Extraction)",bg = "#334d4d", fg = "white")
        heading.pack(pady=(10,20))
        heading.configure(font = ("Verdana", 18, "bold"))


        label0 = Label(self.root, text="Enter Entity to Search", bg = "#334d4d", fg = "white")
        label0.pack(pady = (5,0))
        label0.configure(font = ("Helvetica",10))
        self.search_entity = Entry(self.root,width = 40)
        self.search_entity.pack(pady = (10,10))

        label1 = Label(self.root, text="Enter The Text", bg = "#334d4d", fg = "white")
        label1.pack(pady = (5,0))
        label1.configure(font = ("Helvetica",10))
        self.user_input = Text(self.root, height = 6, width = 40)
        self.user_input.pack(pady = (10,10))

        analyze_btn = Button(self.root,text = "Extract", width = 25,command = self.ner)
        analyze_btn.pack(pady = (7,10))

        self.result = Label(self.root,text = "",bg = "#334d4d", fg = "white")
        self.result.pack(pady = (10,0))
        self.result.configure(font = ("Helvetica",10,"bold"))

        back_btn = Button(self.root,text = "Back", width = 15, command = self.home)
        back_btn.pack(pady = (20,20))



    def ner(self):
        search_entity = self.search_entity.get()
        text = self.user_input.get("1.0", "end-1c")
        result = self.api_object.ner(text,search_entity)
        res_list = []
        for i in result["entities"]:
            res_list.append(i['text'])
        
        self.result["text"] = ", ".join(res_list)
        




    def user_heading(self):
        self.clear()

        heading = Label(self.root,text = "NLP App",bg = "#334d4d", fg = "white")
        heading.pack(pady=(20,20))
        heading.configure(font = ("Verdana", 25, "bold"))

        label0 = Label(self.root,text=f"Welcome, {self.response[1]}", bg = "#334d4d", fg = "white")
        label0.pack(pady=(20,4))
        label0.configure(font = ("Verdana", 12))

        label1 = Label(self.root,text=f"{self.response[0]}", bg = "#334d4d", fg = "white")
        label1.pack(pady=(2,20))
        label1.configure(font = ("Verdana", 12))



    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()




nlp = NLPApp()