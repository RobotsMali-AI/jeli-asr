# Core modules for the package
import os
import sys
import time
import pathlib
import glob
import shutil
from urllib.error import URLError
import wget
import json
from pydub import AudioSegment
from . import config, utils, daba
from pympi import Elan


class JeliFS(object):
    """ """

    U = "USER"

    JELI_WD = "jeli_wd"

    ROOT = config.ROOT
    PWD = os.getcwd()

    def __init__(self, root=ROOT, pwd=PWD):
        """ """
        self.ROOT = root
        self.user = os.getenv(self.U)
        self.PWD = pwd

    RECORDING_ROOT_DIR 	= f"{ROOT}/jeli/transcriptions"
    RECORDING_DIR 	= lambda self, r_id: f"{self.RECORDING_ROOT_DIR}/{r_id}"
    META_FILE 		= f"{ROOT}/jeli/meta.json"
    EXPORT_ROOT_DIR	= f"{os.getcwd()}/{JELI_WD}"
    RECORDING_LIST = os.listdir(RECORDING_ROOT_DIR)


class JeliFileLoader(JeliFS):
    """ """

    def __init__(self, root=config.ROOT, pwd=os.getcwd()):
        """ """
        super(JeliFileLoader, self).__init__(root, pwd)
        

    def valid_recording(self):
        """ """
        recs = [
            i for i in self.RECORDING_LIST if len(
                glob.glob(f"{self.RECORDING_ROOT_DIR}/{i}/*.eaf")) > 0]
        return recs

    def meta_reader(self):
        with open(self.META_FILE) as fp:
            metadata = json.load(fp)
        return metadata

    def all_eaf_files(self):
        """ 
        	Retrieve individual eaf files from the system
        """
        recs = self.valid_recording()
        all_eafs = []
        for i in recs:
            for j in glob.glob(f"{self.RECORDING_ROOT_DIR}/{i}/*.eaf"):
                all_eafs.append(j)
        return all_eafs

    def get_recording_eaf_files(self, r_id):
        """
            Retrieve recording specific eaf files
        """

        return [
            i for i in self.all_eaf_files() if i.split("/")[-2] == r_id]


class JeliEafProcessor(object):
    """ """

    def __init__(self, **kwargs) -> None:
        """ """
        for i in kwargs:
            self.__setattr__(i, kwargs[i])
        self.jfl = JeliFileLoader()

    def __get_eaf_object__(self, path):
        """ """
        return Elan.Eaf(path)

    def __get_eaf_tiers(self, path):
        """ """
        return self.__get_eaf_object__(path=path).get_tier_names()

    def get_eaf_annotation(self, path) -> list:
        """ """

        annots = []
        for i in self.__get_eaf_tiers(path):
            eob = self.__get_eaf_object__(path)
            for j in eob.get_annotation_data_for_tier(i):
                if(j[2]):
                    annots.append(j)
        return annots

    def get_annotation_paired(self, path) -> dict:
        """
            Bam-Fr Pairing of annotation
        """

        annots = self.get_eaf_annotation(path)
        pairs = {}
        for i in annots:
            jtstamp = utils.JeliTimeStamp(i[0], i[1])
            if(jtstamp.jtstamp_lookup(pairs)):
                pairs[jtstamp.__str__()]["fr"] = i[2]
            else:
                pairs[jtstamp.__str__()] = {"bam": i[2]}
            pairs[jtstamp.__str__()]["duration"] = jtstamp.jtstamp_duration(i[0], i[1])
        
        annots = []
        for i in pairs:
            if(len(pairs[i]) == 3):
                jtstamp = utils.JeliTimeStamp()
                s, e = jtstamp.jstamp_from_str(i)
                annots.append(
                    (
                        s, e, 
                        pairs[i]["bam"],
                        pairs[i]["fr"],
                        pairs[i]["duration"]
                    )
                )
        return sorted(annots, key=lambda x: x[0])

    def recording_metadata(self, r_id):
        """ """
        return self.jfl.meta_reader()[
            r_id] if r_id in self.jfl.meta_reader() else None


class JeliStats(object):
    """ """

    def __init__(self, **kwargs):
        """ """
        self.jeaf = JeliEafProcessor()

    def eaf_utterance_count(self, path):
        """ """
        return len(self.jeaf.get_annotation_paired(path))
    
    def eaf_total_clips_duration(self, annots):
        """ """
        return sum([i[4] for i in annots])
    
    def eaf_tokens_retrival(self, annots):
        """ """
        tok = daba.DabaUtils()
        all_lines = [i[2] for i in annots]
        all_tokens = tok.tokenize_line(all_lines)
        return all_tokens

    def eaf_types_retrieval(self, annots):
        """ """
        return list(set(self.eaf_tokens_retrival(annots)))

    def recording_base(self, r_id):
        """ """

        eafs = self.jeaf.jfl.get_recording_eaf_files(r_id)
        meta = self.jeaf.recording_metadata(r_id)
        annots = []

        for i in eafs:
            iid = i.split("/")[-1].replace(".eaf", "")
            for j in self.jeaf.get_annotation_paired(i):
                j = list(j)
                j.append(iid)
                annots.append(j)

        tokens = self.eaf_tokens_retrival(annots)
        out = {
            "durations": sum([i[4] for i in annots]),
            "tokens": tokens,
            "types": list(set(tokens)),
            "utterances": annots
        }
        if(r_id.startswith("griots")):
            out["gender"] = meta["gender"]
            out["theme"] = meta["theme"]
        return  out

    def full_recording_overview(self):
        """ """
        recs = self.jeaf.jfl.valid_recording()
        outer = {}
        for i in recs:
            outer[i] = self.recording_base(i)
        return outer

    def full_dataset(self):
        output = self.full_recording_overview()

        tokens = []
        durations = []
        utterances = []

        meta = self.jeaf.jfl.meta_reader() 

        number_of_females = [
            i for i in meta if meta[i]["gender"] == "F"]
        number_of_males = [
            i for i in meta if meta[i]["gender"] == "M"]

        for i in output:
            for tok in output[i]["tokens"]:
                tokens.append(tok)
            for utt  in output[i]["utterances"]:
                utterances.append(utt)
            durations.append(output[i]["durations"])

        ave_clips_length = sum(durations) / len(utterances)

        return {
            "tokens": tokens,
            "duration": sum(durations),
            "average_clip_length": ave_clips_length,
            "female_speakers": len(number_of_females),
            "male_speakers": len(number_of_males),
            "utterances": utterances}


class JeliFileExporter(JeliFS):
    """ """

    URL_P = lambda self, x: f"https://zenodo.org/record/7094702/files/{x}.zip?download=1"

    def __init__(self, path=None):
        """ """
        if(path == None):
            self.path = self.JELI_WD
        else:
            self.path = path
        self.js = JeliStats()

    def __path_create_or_yield(self, path):
        """ """
        if(not os.path.exists(path)):
            os.makedirs(path)
        return path

    def r_output(self, annots, r_id):
        """ """ 
        output = {}
        base_rec = f"{self.path}/{r_id}"

        for i in annots["utterances"]:
            if(i[5] in output ):
                output[i[5]].append(i)
            else:
                output[i[5]] = [i]
                if(output):
                    self.__path_create_or_yield(f"{base_rec}/{i[5]}")
        return output

    def j_writer(self, out, basep):
        """ """
        for i in out:
            with open(f"{basep}/{i}/{i}.json", "w") as fp:
                json.dump(out[i], fp)
        return out

    def t_writer(self, out, basep):
        """ text writer"""

        for i in out:
            with open(f"{basep}/{i}/{i}.txt", "w") as fp:
                for j in out[i]:
                    fp.write(f"{j[0]}-{j[1]}\t\t\t{j[2]}\t\t\t{j[3]}\n")
        return out

    def c_writer(self, out, basep):
        """ CSV Writer """
        for i in out:
            with open(f"{basep}/{i}/{i}.csv", "w") as fp:
                fp.write(f"Start, End, Source, Target, FILE_ID\n")
                for j in out[i]:
                    fp.write(f"{j[0]}, {j[1]}, \"{j[2]}\", \"{j[3]}\", {j[5]}\n")
        return out

    def e_copier(self, r_id):
        """ EAF Writer """

        efiles = self.js.jeaf.jfl.get_recording_eaf_files(
            r_id)

        for i in efiles:
            i_id = i.split("/")[-1].replace(".eaf", "")
            dest = self.__path_create_or_yield(
                f"{self.path}/{r_id}/{i_id}")
            shutil.copy(i, dest)

    def text_exporter(self, r_id="griots_r1", otype="json"):
        """ """

        annots = self.js.recording_base(r_id=r_id)
        output = self.r_output(annots, r_id=r_id)

        if(not output): return None
        
        base_rec_path = self.__path_create_or_yield(f"{self.path}/{r_id}")
        if(otype=="json"):
            self.j_writer(output, base_rec_path)
        if(otype=="txt"):
            self.t_writer(output, base_rec_path)
        if(otype=="csv"):
            self.c_writer(output, base_rec_path)
        if(otype=="eaf"):
            self.e_copier(r_id)

    def __file_downloader(self, file_path, file_url, r_id=None):
        """ """
        wget.download(file_url, out=file_path)
        return file_path

    def __file_mover(self, file_src, file_dest):
        """ """
        shutil.move(file_src, file_dest)

    def __zip_extractor(self, file, path, r_id=None):
        shutil.unpack_archive(file, path)

        buffer_path = f"{path}/{r_id}"
        cleaner = None
        if(os.path.exists(buffer_path)):
            files = [i for i in os.listdir(buffer_path) if i.endswith(".wav") or i.endswith(".WAV") ]
            if(f"{r_id}.wav" in files or f"{r_id}.WAV" in files):
                sys.stdout.write("\nFile extracted\n")
                return [i for i in os.listdir(path) if not i.endswith(".zip")]

            for i in files:
                iid = i.replace(".WAV", "").replace(".wav", "")
                if(not iid == r_id):
                    cleaner = True
                    self.__file_mover(f"{buffer_path}/{i}", f"{path}/{iid}/{i}")
        if(cleaner): # FIXME: invalid path given
            os.system(f"rm -rfv {buffer_path}")
        return [i for i in os.listdir(path) if not i.endswith(".zip")]

    def audio_dowloader(self, r_id="intrvw_r10"):
        lpath = self.__path_create_or_yield(
            f"{self.path}/{r_id}")

        
        lpathfile = f"{lpath}/buffer.zip"
        if(os.path.exists(lpathfile)):
            sys.stdout.write("File already downloaded... proceeding to extract.\n")
            return self.__zip_extractor(lpathfile, lpath, r_id=r_id)
        try:
            fpath = self.__file_downloader(lpathfile, self.URL_P(r_id), r_id)
            return self.__zip_extractor(fpath, lpath, r_id=r_id)
        except URLError:
            sys.stdout.write("Network ERROR unable to connect\n")
            return None

    def __audio_to_clips(self, f_id, id_output, audio_path):
        """ """

        out_path = pathlib.Path(audio_path).parent
        
        timestamps = [[i[0], i[1]] for i in id_output]

        for i, j in enumerate(timestamps):
            ts, te = j
            if((te - ts) > 0):
                sys.stdout.write(f"{ts}, {te} -> {f_id}-{i+1:0>3}.wav\n")
                new_audio = AudioSegment.from_wav(audio_path)
                new_audio = new_audio[ts:te]
                new_audio.export(
                    f"{out_path}/{f_id}-{i+1:0>3}.wav", 
                    format="wav",
                    tags={'artist': 'Various artists', 'album': 'RobotsMali Griots Recording', 'comments': "Griots Recording 2022"})
        return True

    def audio_to_clips(self, r_id):
        """ """
        output = self.r_output(self.js.recording_base(r_id), r_id)

        sub_folders = list(output.keys())

        rec_path = f"{self.path}/{r_id}"
        
        if(os.path.exists(f"{rec_path}")):
            for i in sub_folders:
                fpath = f"{rec_path}/{i}"
                if(os.path.exists(fpath)):
                    f_files = os.listdir(fpath)
                    valid_audio_format = (f"{i}.wav" in f_files) or (f"{i}.WAV" in f_files)
                    if(valid_audio_format): # FIXME: Continue from last clip download
                        ffpath = f"{fpath}/{i}.wav" if f"{i}.wav" in f_files else f"{fpath}/{i}.WAV"
                        self.__audio_to_clips(i, output[i], ffpath)
                    sys.stdout.write(f"Clips generated for {i}\n")
        time.sleep(1)
        sys.stdout.flush()
        return glob.glob(f"{self.path}/{r_id}/*/*.wav")
