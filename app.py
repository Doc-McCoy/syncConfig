from tkinter import *
from syncConfig import SyncConfig

class App():

    def __init__(self, tk):
        self.sync = SyncConfig()
        tk.title("INI Editor")
        root = Frame(tk)
        root.pack()
        # Labels
        Label(root, text="v1").grid(row=0, column=0)
        Label(root, text="v2").grid(row=0, column=1)
        # Textareas
        # Aqui vai um loop que cria os texts conforme existam no config
        self.textArea1 = Text(root)
        self.textArea2 = Text(root)
        self.textArea1.grid(row=1, column=0)
        self.textArea2.grid(row=1, column=1)
        filesContent = self.sync.getFilesContent()
        self.textArea1.insert(INSERT, filesContent[0])
        self.textArea2.insert(INSERT, filesContent[1])
        # Botões
        frameBtn = Frame(root).grid(row=2, column=0, columnspan=2)
        Button(frameBtn, text="Salvar", command=self.saveFile).pack(side=RIGHT)
        Button(frameBtn, text="Sincronizar", command=self.sync.syncFiles).pack(side=RIGHT)

    def saveFile(self): # Mudar aqui para pegar os conteudos dinamicamente em um loop
        content1 = self.textArea1.get("1.0", END)
        content2 = self.textArea2.get("1.0", END)
        self.sync.saveFilesContent(content1, content2)

if __name__ == '__main__':
    tk = Tk()
    app = App(tk)
    tk.mainloop()
