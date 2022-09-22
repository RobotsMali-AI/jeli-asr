"""
"""

import time
from InquirerPy import inquirer
from InquirerPy.validator import PathValidator
from jeli.core import core, utils

class JeliASR(object):
    """ """

    def __init__(self):
        """ """
        self.jfl = core.JeliFileLoader()
        self.jeaf = core.JeliEafProcessor()
        self.js = core.JeliStats()

    def recording_selector(self):
        """ """

        choices = []

        for i in self.jfl.valid_recording():
            r_id = i.split("_r")
            number = f"{int(r_id[1]):0>2}"
            choices.append((f"{r_id[0]}_r{number}", i))

        selection = inquirer.select(
            message="Select recording ID:",
            choices=sorted([i[0] for i in choices]),
            default=None,
            qmark="jeli>",
            amark="jeli>"
        ).execute()

        def choice_selector(select):
            """ """
            for j in choices:
                if(j[0] == select):
                    return j[1]
            return None
        return choice_selector(selection)

    def recording_detail(self, r_id, nd=None):
        """ """
        rec = self.js.recording_base(r_id)
        disp = utils.DisplayUtils()
        disp.display_detailed_recording(rec, self.js)
        if(nd):
            self.downloand_check(r_id)

    def recording_overview(self, r_id, nd=None):
        """ """
        rec = self.js.recording_base(r_id)
        disp = utils.DisplayUtils()
        disp.display_recording_overview(rec, head=True, r_id=r_id)
        if(nd):
            self.downloand_check(r_id)

    def downloand_check(self, r_id):
        """ """
        download = inquirer.confirm(
            message=f"Download {r_id}?", 
            default=False, qmark="jeli>", 
            amark="jeli>").execute()
        if(download):
            d_choices = [
            "text",
            "text/audio"]
    
            d_select = inquirer.select(
                message="Choose download option",
                choices=d_choices,
                default=None,
                qmark="jeli>",
                amark="jeli>"
            ).execute()

            d_index = d_choices.index(d_select)
            self.download_recording(r_id, d_index)
        else:
            pass

    def __file_type_inq(self):
        ftype = inquirer.select(
            message="Choose text file type:",
            choices=["eaf", "json", "txt", "csv"],
            default="eaf",
            qmark="jeli>",
            amark="jeli>"
        ).execute()
        return ftype

    def download_recording(self, r_id, t=0):
        """ """
        jexp = core.JeliFileExporter()
        disp = utils.DisplayUtils()
        ft = self.__file_type_inq()
        dest_path = inquirer.filepath(
                message="Enter path to download ('.' default):",
                validate=PathValidator(is_dir=True, message="Input is not a directory"),
                only_directories=True,
                default=".",
                qmark="jeli>",
                amark="jeli>"
        ).execute()

        if(dest_path != '.'):
                jexp.path = dest_path

        if(t==0):
            jexp.text_exporter(r_id, ft)
            self.recording_overview(r_id)
            disp.out(f"Exported {r_id} in {jexp.path}\n")
        else:
            jexp.text_exporter(r_id, ft)
            batch_or_clips = [
                "batch", "clips"]

            batch = inquirer.select(
                message="Download audio batch or clips",
                choices=batch_or_clips,
                default="batch",
                qmark="jeli>",
                amark="jeli>"
            ).execute()
            disp.out(f"Downloading {r_id}\n")
            out = jexp.audio_dowloader(r_id)
            
            if(out):
                disp.out(f"\n{r_id} Download completed!\n")
                if(batch == "clips"):
                    time.sleep(3)
                    jexp.audio_to_clips(r_id)
                self.recording_overview(r_id)
