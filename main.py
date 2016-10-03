# MetadataMP3 - Johnathon Kwisses (Kwistech)
# NOTE: For Python 2.7

import eyed3
from Tkinter import *
import tkFileDialog


class App:
    def __init__(self, root):
        self.var = StringVar()
        self.top_txt = "MetadataMP3 - Change the Metadata of MP3 Files"
        self.var.set("C:/")
        self.file_path = ""
        self.interface(root)

    def interface(self, root):
        main_label = Label(root, text=self.top_txt)
        main_label.grid(row=0, column=0, columnspan=3)

        file_path = Label(root, textvariable=self.var, wraplength=300)
        file_path.grid(row=1, column=1, sticky=W)

        title_label = Label(root, text="Title: ")
        title_label.grid(row=3, column=0, pady=2)

        artist_label = Label(root, text="Artist: ")
        artist_label.grid(row=4, column=0, pady=2)

        album_label = Label(root, text="Album: ")
        album_label.grid(row=5, column=0, pady=2)

        track_entry = Entry(root, width=35)
        track_entry.grid(row=3, column=1, padx=10)

        artist_entry = Entry(root, width=35)
        artist_entry.grid(row=4, column=1)

        album_entry = Entry(root, width=35)
        album_entry.grid(row=5, column=1)

        info = [track_entry, artist_entry, album_entry]

        file_path_button = Button(root, text="File Path:",
                                  command=lambda: self.open_file_handler())
        file_path_button.grid(row=1, column=0, padx=5, pady=15, sticky=N)

        save_button = Button(root, text="Save", width=8,
                             command=lambda: self.save(info, root))
        save_button.grid(row=6, column=1, pady=5)

    def open_file_handler(self):
        file_path = tkFileDialog.askopenfilename()
        self.file_path = file_path
        self.var.set(value=file_path)

    def save(self, info, root):
        info_new = [x.get() for x in info]
        title, artist, album = info_new
        a_file = self.file_path

        audiofile = eyed3.load(a_file)
        audiofile.tag.title = u"{}".format(title)
        audiofile.tag.artist = u"{}".format(artist)
        audiofile.tag.album = u"{}".format(album)
        audiofile.tag.save()

        save_label = Label(root, text="Metadata Saved!")
        save_label.grid(row=0, column=1)

        [x.delete(0, 140) for x in info]


def main():
    root = Tk()
    root.title("MetadataMP3")

    App(root)

    root.mainloop()

if __name__ == "__main__":
    main()
