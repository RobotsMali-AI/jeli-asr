"""
Daba Interface for custom BAM parsing
"""

import os
import shutil
from html.parser import HTMLParser
import subprocess
from rmai import config

class DabaHTMLParser(HTMLParser):
    def __init__(self, *, convert_charrefs: bool = ...) -> None:
        super().__init__(convert_charrefs=convert_charrefs)
        self.counter = 0
        self.words = {}
        self.selected_data = ""
        self.ptag = None

    def handle_starttag(self, tag: str, attrs):
        for i in attrs:
            if(i[1] == "lemma"):
                self.words[self.counter] = ""
        return super().handle_starttag(tag, attrs)
    
    def handle_endtag(self, tag: str) -> None:
        if(self.ptag == True):
            self.ptag = False
            print("Closing parent")
        return super().handle_endtag(tag)

    def handle_data(self, data: str) -> None:
        ndata = data.replace("\n", "")
        if(self.counter in self.words and ndata):
            self.words[self.counter] = ndata
            self.counter += 1
        return super().handle_data(data)
    
    def outer(self):
        return [i.lower() for i in self.words.values()]

class DabaUtils(object):
    """
    
    """
    # RUN_DIR = f"{config.ROOT}/jeli/run"

    BUF_DIR = f"{config.ROOT}/res/tmp"
    BAMAROOT = f"{config.ROOT}/res/bamadaba"
    BAMADABA = f"{BAMAROOT}/all_dict.txt"
    BAMAGRAM = f"{BAMAROOT}/bamana.gram.tonal.txt"

    def __init__(self, lines: list = []):
        """ """
        self.lines = lines

    def __get_tmp_dir(self):
        if(not os.path.exists(self.BUF_DIR)):
            os.makedirs(self.BUF_DIR)
        return self.BUF_DIR

    @staticmethod
    def __reader(path):
        with open(path) as fp:
            p = fp.read()
        return p

    def __get_fname(self):
        """ """
        return len(os.listdir(self.BUF_DIR))

    def __write_line(self, line):
        """ """
        buf = self.__get_tmp_dir()
        lpath = f"{buf}/{self.__get_fname()+1}.txt"
        with open(lpath, "w") as fp:
            fp.write(line+"\n")
        return lpath

    def __write_lines(self, lines):
        buf = self.__get_tmp_dir()
        lpath = f"{buf}/{self.__get_fname()+1}.txt"
        with open(lpath, "w") as fp:
            for line in lines:
                if(not line.endswith(".")):
                    fp.write(line + ".\n")
                else:
                    fp.write(line + "\n")
        return lpath

    def __mparse_text(self, lpath):
        lout = lpath.replace(".txt", ".html")
        cmd = f"mparser -i {lpath} -c -d {self.BAMADABA} -g {self.BAMAGRAM} -o {lout} --tokenizer bamana --nolemmas --detone"
        subprocess.run([cmd], shell=True, capture_output=True)
        return lout

    def tokenize_line(self, lines):
        """ 
            mparser > repl > output > parsed
        """

        lpath = self.__write_lines(lines)
        parsed = self.__mparse_text(lpath)
        rawp = self.__reader(parsed)
        
        hparser = DabaHTMLParser()
        hparser.feed(rawp)
        shutil.rmtree(self.BUF_DIR)
        return hparser.outer()
