"""
"""

import shutil
import os
import pathlib
from jeli.core import core

class JeliTestConfig(object):

    def __init__(self) -> None:
        self.jfs = core.JeliFS()
        self.jfl = core.JeliFileLoader(pwd=pathlib.Path(__file__).parent)
        self.jeaf = core.JeliEafProcessor(pwd=pathlib.Path(__file__).parent)
        self.js = core.JeliStats()
        self.je = core.JeliFileExporter()

    def jeli_fs_test(self):
        """ Verify Attributes """
        try:
            attrs = [
                "RECORDING_ROOT_DIR",
                "META_FILE",
                "RECORDING_DIR"
            ]
            for i in attrs:
                self.jfs.__getattribute__(i)
            return True
        except AttributeError:
            return False

    def jeli_file_loader(self):
        """ """
        pass

    def jeli_eaf_processor(self):
        """ """
        if(hasattr(self.jeaf, "pwd")):
            self.jeaf.jfl.PWD = self.jeaf.pwd
        pass

    def jeli_stats(self):
        pass

    def jeli_exporter(self):
        """ """
        self.je.PWD = pathlib.Path(__file__).parent
        self.je.path = f"{self.je.PWD}/{self.je.JELI_WD}"
        pob = pathlib.Path(self.je.path)

        # Test 1 - Only parse valid ID
        """
        annots = self.je.js.recording_base(r_id="griots_r1")
        annots2 = self.je.js.recording_base("intrvw_r1")
        annots3 = self.je.js.recording_base("intrvw_r2")

        output1 = self.je.r_output(annots, r_id="griots_r1")
        output2 = self.je.r_output(annots2, r_id="intrvw_r1")
        output3 = self.je.r_output(annots3, r_id="intrvw_r2")
        
        
        t1 = len(
            output3.keys()
            ) == 0 and (len(
                output1.keys()
                ) > 0 and len(
                    output2.keys()) > 0)

        # Test 2 - Exporting to file types

        self.je.text_exporter("griots_r1", otype="txt")
        self.je.text_exporter("griots_r1", otype="csv")
        self.je.text_exporter("griots_r1", otype="eaf")
        self.je.text_exporter("griots_r1", otype="json")
        
        
        self.je.text_exporter("intrvw_r1", otype="txt")
        self.je.text_exporter("intrvw_r1", otype="csv")
        self.je.text_exporter("intrvw_r1", otype="eaf")
        self.je.text_exporter("intrvw_r1", otype="json")

        self.je.text_exporter("intrvw_r2", otype="txt")
        self.je.text_exporter("intrvw_r2", otype="csv")
        self.je.text_exporter("intrvw_r2", otype="eaf")
        self.je.text_exporter("intrvw_r2", otype="json")

        t2 = os.path.exists(
            f"{self.je.path}/griots_r1/griots_r1_1/griots_r1_1.txt"
        )

        # Test 3 - File Download and parsing
        print("Mock downloading")

        # TODO: remove on 
        shutil.copy(
            f"{self.je.PWD}/res/buffer.zip", 
            f"{self.je.path}/griots_r1/")
        
        shutil.copyfile(
            f"{self.je.PWD}/res/buffer3.zip",
            f"{self.je.path}/intrvw_r1/buffer.zip")

        aud1 = self.je.audio_dowloader("griots_r1")
        aud2 = self.je.audio_dowloader("intrvw_r1")

        print(aud1)
        print(aud2)
        """

        # Test 4 - Clipify audio
        # clip1 = self.je.audio_to_clips("griots_r1")
        clip2 = self.je.audio_to_clips("intrvw_r1")

        print("Cleaning up working dir")
        shutil.rmtree(pob)
