# Utilities for the package: logging, caching mechanisms, services management.

import os
import sys
import glob
from . import config, core

class DisplayUtils(object):

    def out(self, item):
        sys.stdout.write(item)
        return item

    def err(self, err):
        sys.stderr.write(err)
        return err

    def display_recording_overview(self, annots, head=False, r_id=None):
        """ """
        if(head):
            self.out(f"{'Recording':<20}\t{r_id if r_id else 'N/A':>25}\n")
        self.out(f"{'Theme:':<20}\t{annots['theme'] if 'theme' in annots else 'N/A':>25}\n")
        self.out(f"{'Speaker:':<20}\t{annots['gender'] if 'gender' in annots else 'N/A':>25}\n")
        self.out(f"{'Utterances:':<20}\t{int(len(annots['utterances'])):>25}\n")
        self.out(f"{'Duration:':<20}\t{round(annots['durations'], 2):>25}\n")
        self.out(f"{'Tokens:':<20}\t{len(annots['tokens']):>25}\n")
        self.out(f"{'Types:':<20}\t{len(annots['types']):>25}\n")

    def display_detailed_recording(self, annots, js=None):
        """ """
        by_file = {}

        for i in annots["utterances"]:
            if(i[5] in by_file):
                by_file[i[5]].append(i)
            else:
                by_file[i[5]] = [i]

        self.err(f"{'Files':<8}\t{'Utterances':^8}\t{'Tokens':^8}\t{'Types':^8}\t{'Avg. Clip(s)':^8}\t{'Duration':^8}\n")

        for i in by_file:
            i_tokens = js.eaf_tokens_retrival(by_file[i])
            i_types = list(set(i_tokens))
            i_utt = len(by_file[i])
            duration = round(sum([i[4] for i in by_file[i]]), 2)
            i_avg = round(duration/i_utt, 2)
            self.out(f"{i:<8}\t{i_utt:>8}\t{len(i_tokens):>8}\t{len(i_types):>8}\t{i_avg:>8}\t{duration:>8}\n")

        self.out("-"*50+"\n")

        self.display_recording_overview(annots)



class JeliTimeStamp(object):
    """ """

    def __init__(self, start=None, end=None) -> None:
        """ """
        self.start = start
        self.end = end

    def set_jtstamp(self, start, end):
        """ """
        self.start, self.end = start, end

    def jtstamp_lookup(self, element):
        """ """
        return self.__str__() in element

    def jtstamp_duration(self, start, end):
        return round(((end - start) / 1000) % 60, 2)

    def jstamp_from_str(self, time_str):
        t = time_str.split("-")
        self.start = int(t[0])
        self.end = int(t[1])
        return (self.start, self.end)

    def __str__(self) -> str:
        return f"{self.start}-{self.end}"

class DateTimeUtils(object):
    """ TODO: Do later"""
    pass
        
class JeliLogger(object):
    """ TODO: Do later"""
    pass
