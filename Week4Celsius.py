from breezypythongui  import EasyFrame

class temperature(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self,title="temp")
        self.addLabel(text="Celsuis",row=0,column=0)
        self.celsuisfield=self.addFloatField(value=0.0,row=1,column=0,precision =2)
        self.addLabel(text="Farenheit",row=0, column=1)
        self.farenheitfield=self.addFloatField(value=32.0,row=1,column=1,precision=2)

        self.addButton(text=">>>>",row=2,column=0,command=self.calcfahr)

    
        self.addButton(text="<<<<<<",row=2,column=1,command=self.calccels)

    def calcfahr(self):
     degrees=self.celsuisfield.getNumber()
     degrees=degrees*9/5+32
     self.farenheitfield.setNumber(degrees)

    def calccels(self):
     degrees=self.farenheitfield.getNumber()
     degrees=(degrees-32)*5/9
     self.celsuisfield.setNumber(degrees)

def main():
    temperature().mainloop()
if __name__ == "__main__":
                main()
        
    

    
        
    
    
        
