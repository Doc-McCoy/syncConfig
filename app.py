from tkinter import *
from syncConfig import SyncConfig

class App():

    def __init__(self, tk):
        self.sync = SyncConfig()
        tk.title("INI Editor")
        root = Frame(tk)
        root.pack()

        # Textareas
        filesContent = self.sync.getFilesContent()
        self.text_areas = []
        frameTextArea = Frame(tk)
        frameTextArea.pack(fill='both', expand=True)

        # Abrir cada conteudo em um text
        for file in filesContent:
            textArea = Text(frameTextArea, width='60')
            textArea.pack(side='left', fill='both', expand=True)
            textArea.insert(INSERT, file)
            self.text_areas.append(textArea)

        # Botões
        frameBtn = Frame(tk)
        frameBtn.pack(fill='x')
        Button(frameBtn, text="Salvar", command=self.saveFile).pack(side=RIGHT)
        Button(frameBtn, text="Sincronizar", command=self.syncFiles).pack(side=RIGHT)

    def saveFile(self):
        contents = []
        for text in self.text_areas:
            content = text.get("1.0", END)
            contents.append(content)
        self.sync.saveFilesContent(contents)

    def syncFiles(self):
        self.saveFile()
        self.sync.syncFiles()

if __name__ == '__main__':
    tk = Tk()
    app = App(tk)
    tk.mainloop()
