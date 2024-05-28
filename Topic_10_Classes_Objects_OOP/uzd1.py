class Song:
    def __init__(self, title="", author="", lyrics=()):
        self.title = title
        self.author = author
        self.lyrics = lyrics
        print("Jauna dziesma izveidota")
        if self.title:
            print(f"Title: {self.title}")
        if self.author:
            print(f"Author: {self.author}")
 
    def sing(self, max_lines=-1):
        if self.title and self.author:
            print(f"\n{self.title} - {self.author}")
        lines_to_print = self.lyrics if max_lines == -1 else self.lyrics[:max_lines]
        for line in lines_to_print:
            print(line)
 
        return self
 
    def yell(self, max_lines=-1):
        if self.title and self.author:
            print(f"\n{self.title} - {self.author}")
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
    def break_it(self, max_lines=-1, drop='yeah'):
        if self.title and self.author:
            print(f"{self.title} - {self.author}")
        if max_lines == -1:
            for line in self.lyrics:
                words = line.split()
                # modified_line = ' '.join([word + ' ' + drop for word in words])
                # alternative we could add drop in join
                modified_line = f' {drop} '.join(words) + ' ' + drop
                print(modified_line)
        else:
            for line in self.lyrics[:max_lines]:
                words = line.split()
                modified_line = ' '.join([word + ' ' + drop for word in words])
                print(modified_line)
        return self

zrap = Rap("Ziemeļmeita", "Jumprava", ["Gāju meklēt ziemeļmeitu",
                                        "Garu, tālu ceļu veicu"])
zrap.break_it(5, 'yo').yell(1)