# MetadataMP3 - Johnathon Kwisses (Kwistech)
# NOTE: For Python 2.7

import eyed3
from tkFileDialog import askopenfilename
from Tkinter import *
from tkMessageBox import showinfo


class App:
    """Create MetadataMP3 main program loop."""
    def __init__(self, root):
        """Initialize class variables and call interface method.

        Args:
            root (instance): Tk() instance.
        """
        self.var = StringVar()
        self.top_txt = "MetadataMP3 - Change the Metadata of MP3 Files"
        self.var.set("C:/")
        self.file_path = ""
        self.interface(root)

    def interface(self, root):
        """Create GUI interface for class.

        Args:
            root (instance): Tk() instance.
        """
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

        info = [track_entry, artist_entry, album_entry]  # Collects entry data

        file_path_button = Button(root, text="File Path:",
                                  command=lambda: self.open_file_handler())
        file_path_button.grid(row=1, column=0, padx=5, pady=15, sticky=N)

        save_button = Button(root, text="Save", width=8,
                             command=lambda: self.save(info))
        save_button.grid(row=6, column=1, pady=5)

    def open_file_handler(self):
        """Open explorer window for user to choose .mp3 file."""
        file_path = askopenfilename()
        self.file_path = file_path
        self.var.set(value=file_path)

    def save(self, info):
        """Save user data for .mp3 to .mp3 metadata.

        Args:
            info (list): Contains Tkinter Entry widgets.
        """
        info_new = [x.get() for x in info]
        title, artist, album = info_new
        a_file = self.file_path

        # Saves user data to .mp3 file metadata.
        audiofile = eyed3.load(a_file)
        audiofile.tag.title = u"{}".format(title)
        audiofile.tag.artist = u"{}".format(artist)
        audiofile.tag.album = u"{}".format(album)
        audiofile.tag.save()

        showinfo("MetadataMP3 Message", "Metadata Saved to MP3 File!")

        [x.delete(0, 140) for x in info]


def main():
    """Create Tk() instance and main program loop."""
    root = Tk()
    root.title("MetadataMP3")

    App(root)

    root.mainloop()

if __name__ == "__main__":
    main()
