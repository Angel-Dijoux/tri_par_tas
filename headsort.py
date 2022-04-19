"""
-(°-°)-                         ---------------------------------------------------------
                                PROJECT NSI | ALEXANDRE CORREIA - ANGEL DIJOUX | TRI TAS
                                ---------------------------------------------------------

   import: tkinter

   try_tas :  --------------------------------------------------------------------------------------------------------
              |  try_tas ->  __init__  [ retrieve the list of the user ]                                              |
              |                                                                                                       |
              |               gauche   [ return a left child has index i ]                                            |
              |                                                                                                       |
              |               droite   [ return a right child has index i ]                                           |
              |                                                                                                       |
              |               pere     [ return a parent has index i ]                                                |
              |                                                                                                       |
              |               est_tas  [ check if it's a heap ]                                                       |
              |                                                                                                       |
              |               maximum  [ returns the maximum index between an index i and a limit                     |
              |                                    lim, if the value is equal then the smallest value is returned ]   |  
              |                                                                                                       |
              |               entasser [ recursive function to lower small values and raise large ones ]              |
              |                                                                                                       |
              |               contruireTas [ build heap from list for all elements ]                                  |
              |                                                                                                       |
              |               Trier_par_tas [ #build the heap and sort the heap ]                                     |
              |                                                                                                       |
              --------------------------------------------------------------------------------------------------------

    App :     --------------------------------------------------------------------------------------------------------
              |  App ->  __init__  [ set tkinter window ]                                                             |
              |                                                                                                       |
              |               github   [ return my github page for help ]                                             |
              |                                                                                                       |
              |               instagram   [ return my instagram page for help ]                                       |
              |                                                                                                       |
              |               tri_par_tas     [ transform str list (= '12,58,95') to [12,58,95] and send result of    |
              |                                   sort in tkinter window ]                                            |
              |                                                                                                       |
              |               est_tas  [ transform list and return True or False if list is a heap or no ]            |
              |                                                                                                       |
              |               widgets  [ create all elements of tkinter ]                                             |
              |                                                                                                       |
              --------------------------------------------------------------------------------------------------------

"""

""" import """

import tkinter
import webbrowser

""" import """

""" -------- tri_tas -------- """
class tri_tas:

    def __init__(self,liste):
        self.liste = liste
    
    def gauche(self, i):
        return i*2+1

    def droite(self, i):
        return i*2+2

    def pere(self, i):
        return (i-1)//2

    def est_tas(self): #return boolean if it's a heap
        for i in range(1, len(self.liste)):
            if self.liste[self.pere(i)] < self.liste[i]:
                return False
            return True

    def maximum(self, i, lim): #return maximum between i and lim (= size list)
        maxi = i
        g = self.gauche(i)
        d = self.droite(i)
        if g < lim and self.liste[g] > self.liste[maxi]:
            maxi = g
        if d < lim and self.liste[d] > self.liste[maxi]:
            maxi = d
        return maxi


    def entasser(self, i, lim): #lowers the small values and raises the large ones
        maxi = self.maximum(i, lim)
        if maxi != i:
            self.liste[i], self.liste[maxi] = self.liste[maxi], self.liste[i] #swap
            self.entasser(maxi, lim)

    def construireTas(self):
        for i in range(len(self.liste)-1,-1,-1):
            self.entasser(i, len(self.liste))
    
    def Trier_par_tas(self): #build the heap and sort the heap
        self.construireTas()
        for i in range(len(self.liste)-1,0,-1):
            self.liste[0], self.liste[i] = self.liste[i], self.liste[0] #swap
            self.entasser(0, i)
        return self.liste

""" -------- tri_tas -------- """

""" -------- tkinter display -------- """

class App(tkinter.Tk):
    
    def __init__(self):
        tkinter.Tk.__init__(self)
        self.widgets()

    """ help """

    def github(self):
        lien_github='https://github.com/Angel-Dijoux/Code-Cesar/tree/main'
        return webbrowser.open(lien_github)

    def instagram(self):
        lien_instagram='https://www.instagram.com/elki_8/'
        return webbrowser.open(lien_instagram)

    """ help """

    def tri_par_tas(self):
        entry = self.entry.get()
        if entry != '':
            result = list(map(int,entry.split(",")))
            Tri = tri_tas(result)
            display = Tri.Trier_par_tas()
            return self.label_result.configure(text=str(display))

    def est_tas(self):
        entry = self.entry.get()
        if entry != '':
            result = list(map(int,entry.split(",")))
            Tri = tri_tas(result)
            display = Tri.est_tas()
            return self.label_result.configure(text=str(display))

    def widgets(self):

        """ config app """

        self.geometry("800x400")
        self.minsize(480, 360)
        self.title("Tri par tas")
        self.config(background='#2E3138')
        font = ("Roboto", 15)

        """ config app """

        """ features """

        #frames
        self.frame = tkinter.Frame(self, bg='#2E3138')
        self.frame_print = tkinter.Frame(self)
        self.frame_result = tkinter.Frame(self, bg='#2E3138')

        #title
        self.label_title = tkinter.Label(self, text="Tri par tas")
        self.label_title.pack()
        self.label_title.configure(font=font, bg='#2E3138', fg='white')

        #input
        self.label_entry = tkinter.Label(self.frame, text="Liste : ")
        self.label_entry.pack()
        self.label_entry.configure(font=font, bg='#2E3138', fg='white')

        self.entry = tkinter.Entry(self.frame, font=font, bg='#EBEBEB', fg='#2E3138')
        self.entry.pack()

        #display result
        self.label_result = tkinter.Label(self.frame_print)
        self.label_result.pack()
        self.label_result.configure(font=font ,bg='#2E3138', fg='white')

        #calls tri_tas class
        self.button_tri = tkinter.Button(self.frame_result, text="Trie", bg='#EBEBEB', fg='#2E3138', activebackground='#F76C5E', activeforeground='#2E3138', command=self.tri_par_tas)
        self.button_tri.grid(row=1, column=1)

        self.button_tri = tkinter.Button(self.frame_result, text="Un tas ?", bg='#EBEBEB', fg='#2E3138', activebackground='#F76C5E', activeforeground='#2E3138', command=self.est_tas)
        self.button_tri.grid(row=1, column=2)

        #menu
        self.menu_bar = tkinter.Menu(self,bg='#EBEBEB', fg='#2E3138', activebackground='#F76C5E', activeforeground='#2E3138')
        self.file_menu = tkinter.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_command(label="Quit", command=self.quit)
        self.config(menu=self.menu_bar)

        self.help = tkinter.Menu(self.menu_bar, tearoff=0,bg='#EBEBEB', fg='#2E3138', activebackground='#F76C5E', activeforeground='#2E3138')  
        self.help.add_command(label="GitHub", command= self.github) 
        self.help.add_command(label="Instagram", command= self.instagram ) 
        self.menu_bar.add_cascade(label="Help", menu=self.help) 

        #set frames
        self.frame.pack(expand=tkinter.YES)
        self.frame_print.pack(expand=tkinter.YES)
        self.frame_result.pack(expand=tkinter.YES)

        """ features """

""" -------- tkinter display -------- """


if __name__ == "__main__":
    app = App()
    app.mainloop()
