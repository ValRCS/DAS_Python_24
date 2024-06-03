class Song:
    def __init__(self, title = "", author = "", lyrics = ()):
        self.title = title
        self.author = author
        self.lyrics = lyrics # could convert to list here if we wanted to change lyrics
        print(f"New song made")
        self._print_title_author

    # helper method to print title and author
    def _print_title_author(self): # _ is not required but it is a convention to show that this is a semi-hidden method
        print(f"{self.title} - {self.author}")
        return self
    
    def sing(self, max_lines = -1):
        self._print_title_author()
        lyrics = self.lyrics # for our internal method usage
        if max_lines != -1:
            lyrics = lyrics[:max_lines] 
        print(*lyrics, sep = "\n")# we could use for loop here as well as seen in yell method
        # above approach would not work for uppercasing
        return self
    
    def yell(self, max_lines = -1):
        """
        Yell the lyrics of the song
        max_lines - how many lines to yell, -1 means all
        """
        self._print_title_author()
        if max_lines == -1:
            max_lines = len(self.lyrics) # to ensure that we print all lines
        for line in self.lyrics[:max_lines]:
            print(line.upper())
        return self
 
ziemelmeita = Song("Ziemeļmeita", 
                   "Jumprava", 
                   ["Gāju meklēt ziemeļmeitu",
                    "Garu, tālu ceļu veicu",
                    "Lēni un par vēlu nācu",
                    "Meklējot šo ziemeļmalu",
                    ])
 
ziemelmeita.sing().yell().sing().yell()

ziemelmeita.sing(2).yell(2).sing(2).yell(3)

# let's make a Rap class that inherits from Song

class Rap(Song):
    pass
    #TODO implement break_it method that will print lyrics with drop

    def break_it(self, max_lines = -1, drop="AHA"):
        """
        Break it down with a drop
        max_lines - how many lines to break, -1 means all
        drop - what to add as a drop text
        """
        self._print_title_author()
        # TODO implement as exercise
        return self


# note Rap already works but it is just like Song
in_da_club = Rap("In Da Club", "50 Cent", ["Go, go, go, go, go, go, go, go",
                              "Go shorty, it's your birthday",
                              "We gonna party like it's your birthday",
                              "We gonna sip Bacardi like it's your birthday",
                                ])

in_da_club.sing().yell().sing().yell().break_it()
