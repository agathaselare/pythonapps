import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class MyGrid(GridLayout):
    global i 
    i=0
    global cifrado
    global final
    cifrado= ""
    final = ""

    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 1

        self.inside = GridLayout()
        self.inside.cols = 2

        self.inside.add_widget(Label(text="Keyword"))
        self.name = TextInput(multiline=False)
      
        self.inside.add_widget(self.name)

        self.inside.add_widget(Label(text="Input"))
        self.lastName = TextInput(multiline=False)
        self.inside.add_widget(self.lastName)

        self.inside.add_widget(Label(text="Output"))
        self.email = TextInput(multiline=False)
        self.inside.add_widget(self.email)

        self.add_widget(self.inside)

        self.submit = Button(text="Encode", font_size=40)
        self.submit.bind(on_press=self.pressed)
        self.add_widget(self.submit)
        self.submitt = Button(text="Decode", font_size=40)
        self.submitt.bind(on_press=self.pressedd)
        self.add_widget(self.submitt)

    def pressed(self, instance):
        global cifrado
        global i
        global lista
        lista = self.name.text
        lista = list(lista)
        texto = self.lastName.text
        email = self.email.text
        
        for x in texto:
            
            if(x==" "):
                cifrado = cifrado + " "
                continue
            else:
                if i <= len(lista):
                    num = ord(lista[i])
                cifrado = cifrado + chr(((ord(x)-97 + num-96)%26)+97)
            
            i += 1
            if bool(i==len(lista)):
                i=0
        self.email.text = cifrado
        cifrado = ""
        lista = ""
        final = ""
        i=0
        
#DECODE DOESN'T WORK LOL NO WONDER
    def pressedd(self, instance):
        global final
        global i
        global cifrado
        global lista
        lista = self.name.text
        lista = list(lista)
        texto = self.lastName.text
        email = self.email.text
        for x in texto:
            
            if(x==" "):
                final = final + " "
                continue
            else:
                if i <= len(lista):
                    num = ord(lista[i])
                final= final + chr(((ord(x) - num-1)%26)+97)
            i+= 1
            if bool(i==len(lista)):
                i=0
        self.email.text = final
        final = ""
        cifrado = ""
        lista = ""
        i=0
class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    MyApp().run()