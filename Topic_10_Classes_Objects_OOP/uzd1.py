class Song:
    def __init__(self, title="", author="", lyrics=()):
        self.title = title
        self.author = author
        self.lyrics = lyrics
        print("Jauna dziesma izveidota")
        self._print_title_author

    # let's make a semi private method to print the title and author
    def _print_title_author(self):
        if self.title and self.author:
            print(f"{self.title} - {self.author}")
            return self # not required
        # print(f"{self.title}{self.author}") # okay but will print empty row if no title or author
        if self.title:
            print(f"Title: {self.title}")
        if self.author:
            print(f"Author: {self.author}")
 
    def sing(self, max_lines=-1):
        self._print_title_author()
        lines_to_print = self.lyrics if max_lines == -1 else self.lyrics[:max_lines]
        for line in lines_to_print:
            print(line)
 
        return self
 
    def yell(self, max_lines=-1):
        self._print_title_author()
        # lines_to_print = self.lyrics if max_lines == -1 else self.lyrics[:max_lines]
        # rewrite above using normal if-else
        if max_lines == -1:
            lines_to_print = self.lyrics
        else:
            lines_to_print = self.lyrics[:max_lines]
        # alternative would be to assume max_lines is always -1
        # lines_to_print = self.lyrics[:max_lines]
        # if max_lines == -1:
        #     lines_to_print = self.lyrics

        for line in lines_to_print:
            print(line.upper())
 
        return self
 
 
ziemelmeita = Song("Ziemeļmeita", "Jumprava", ["Gāju meklēt ziemeļmeitu",
                                                 "Garu, tālu ceļu veicu"])
 
ziemelmeita.sing(1).yell().yell(55)

# let's make another song
talu_aizgaja = Song("Tālu aizgāja", "Jumprava", ["Tālu aizgāja brālis",
                                                 "Mana nama durvis viņam ciet"])

talu_aizgaja.sing().yell(1)


class Rap(Song):

    # let's make a helper method to print passed in lyrics with a drop
    def _print_lyrics_with_drop(self, lyrics, drop):
        # this method could be actually public
        # as it will work with any lyrics iterable and any drop string
        # it does not depend on inner state of the object
        for line in lyrics:
            words = line.split()
            modified_line = ' '.join([word + ' ' + drop for word in words])
            print(modified_line)

    def break_it(self, max_lines=-1, drop='yeah'):
        self._print_title_author()
        if max_lines == -1:
            self._print_lyrics_with_drop(self.lyrics, drop)
        else: # we have some lines to print
            self._print_lyrics_with_drop(self.lyrics[:max_lines], drop)
        return self

zrap = Rap("Ziemeļmeita", "Jumprava", ["Gāju meklēt ziemeļmeitu",
                                        "Garu, tālu ceļu veicu"])
zrap.break_it(5, 'yo').yell(1)

# let's make a Rap with no know title but with author Andre3000
no_title_song = Rap(author="Andre3000", lyrics=["Hey ya", "Hey ya", "Hey ya",
                                            ])

no_title_song.break_it(1, 'ahh').yell(1).sing()

# now let's use our _print_lyrics_with_drop method with outside data
lyrics = ["I'm sorry, Ms. Jackson", "I am for real"]
drop = "baby"
# example how we can use the method without actually using the object
no_title_song._print_lyrics_with_drop(lyrics, drop)
# so this type of method could be actually a static method TODO later
# static method is a method that does not depend on the state of the object
# it can be used before the object is created or without the object
