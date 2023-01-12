# Jeli ASR & Dataset

## CRITICAL INFORMATION
**The dataset is going through major revision work and therefore is not static. We suggest to contact the authors prior to using the dataset for any research related activities.** Review [Adjustments](./adjustments.md) to track the status of the revision work.

## What is Jeli-ASR
This is a multidimentional open-source package consisting of a dataset and an ASR model. The dataset consists of the transcriptions of 30 hours of griots stories and narrations, and their translations. The corresponding [audio](https://zenodo.org/record/7296317) is hosted on zenodo. The ASR model development is actively ongoing, please take a look [asr](./asr/).

## Dataset
The Griots corpus is a speech corpus containing both audio and its accompanying transcribed text. You can find the intent, the approaches, a detailed look, and a thorough explanation of the dataset on the [Data-Card](https://docs.google.com/document/d/17cBQo7yisZuRpLP9gFul4pvQiARgrDwPLDNE980zxx4/edit?usp=sharing). It is about 28k utterances & clips (couting). There are two sub-speech dataset. Griots Narrations and Street Interviews.

### Griots Narrations
These are recording of 30 griots (23 Males / 7 Females) talking about various subjects. In a controlled environment. *The subjects are culture oriented*.

### Street Interviews
Along side the griots' narrations, a smaller sample of individuals were interviewd about the importance of bambara in the technology. These interviews were conducted on the street with background noises. 

**N.B**: Not all of these audios have been transcribed.

### Snapshot
|      |     |
|:----:|:----|
|Size | 16 GB (text + audio) |
| Length | 31 hours+ | 
| Utterances (Clips) | 29800 |
|Ave. Clips Length | 3.02 s
| Tokens | 300923 |
| Types | 62753 |
| M/F Speaker Ratio | 23/7 |

## ASR - Model
### [Wav2Vec](./asr/wav2vec/)
### [Kaldi](./asr/kaldi) (Soon)
### [Espnet](./asr/espnet) (Soon)
<!-- ### [KumaSTT](./asr/kuma/) -->

## jelipkg toolkit (Jeli => Griot in Bambara)

`jelipkg` is sub-package that serves as an entry point to the dataset. It is a python package that allows you to browse, and download the items from the dataset for your own convenience, you can download the textual data either in raw text format or json format, csv. The package can be used to download the audio in batch format or as clips (utterance) format.

### Installation

- Install a revised version of [DABA](https://github.com/maslinych/daba)

```bash
pip install -U https://github.com/s7d11/daba/releases/download/v0.0.1-alpha/daba-0.9.2.tar.gz
```

- Install `jelipkg`

```sh
	
pip install -U https://github.com/RobotsMali-AI/jeli-asr/releases/download/v0.0.1-alpa/jelipkg.tar.gz

```

### Quickstart

- Launching the interactive shell

```bash
$ jelipkg
```

- Choose option

```
Welcome to jelipkg v0.0.1

Type browse, download, help, exit
jeli> browse
```

- Select a recording

```
jeli> Select a recording ID:
    >   griots_r01
        griots_r02
        griots_r03
        griots_r04
        griots_r05
        ...
```

- Choose `browsing` option

```
jeli> Choose browsing option:
    >   Recording overview
        Detailed view of recording
```

- Output

```
Recording                               griots_r1
Theme:                     L'histoire d'une fille
Speaker:                                        M
Utterances:                                   982
Duration:                                  3277.0
Tokens:                                     12289
Types:                                       1080
jeli> Download griots_r1? (y/N)
```

### Documentation
Type one of the followings to:  
- **browse** -> Interactively browse the list of recordings  
- **download** -> Directly download a recording from the dataset  
- **help** -> Display the help message  
- **exit** -> Exit the `jelipkg` console  

### Bugs
- [Bugs](https://github.com/robotsmali-ai/jeli-asr/issues)

### License
- [MIT License](./jeli/LICENSE)

### Future Functionalities & Work
- Standardize EAFs
- Disambiguate Bambara lines 
- Ajust Translations
- Direct CLI (one command) capability
- Multi-recording download

**IMPORTANT**: It is recommended to download one recording/interview at a time, if you have an unreliable network due to the size of the dataset.

## Contact & People
**Principal Investigator**: Michael Leventhal, `mleventhal <at> robotsmali.org`    
**Manager**: Sebastien Diarra, `sdiarra <at> robotsmali.org`  
**ASR**: Allahsera Auguste Tapo, `aat3261 <at> rit.edu`  
**Inquiries & Collaboration**: `research <at> robotsmali.org`  

## Reference

```
@misc{griotsdataset2022,
  author                = {Sebastien Diarra and Michael Leventhal and Allahsera Auguste Tapo},
  title                 = {RobotsMali Griots Speech Dataset, and ASR},
  howpublished          = {\url{https://github.com/robotsmali-ai/jeli-asr/}},
  year                  = 2022
}
```

## Known Issues
- refers to [ISSUES](./ISSUES.md)

## Contribute

### Linguistics / Language
Contribution is highly sought after from language experts and language professionals. Principally those with dual bambara-french knowledge. It is our goal to get a good quality dataset. There are three ways you can contribute to this project:

- [Utterance Validation/Revision](./docs/utterances.md)
- [Bambara Adjustment](./docs/bambara_text.md)
- [French Adjustment](./docs/french_text.md)

### ASR
Point person: **Allahsera Auguste Tapo**: `aat3261 <at> rit.edu`

Reach out to the point person. If interested in collaborating or contributing to this work.

### Package
Contributions are welcomed. There are no defined guidelines. In order to keep the philosophy of the package please refers to [jeli](./jeli/TODO.md).

## Contributors & Acknowlegments
- **[INALCO LLACAN](http://www.inalco.fr/en/research/research-units/llacan)**'s Valentin Vydrine and Jean-Jacques Meric for their active help in all stages of this project.
- `Coleman Donaldson` of ***[An ka taa](https://www.ankataa.com/)*** for critically reviewing the work, and pointing out some very important facts about the data.
- **[Google](https://about.google/)** specially the Creative Lab, and Google Cloud for supporting this work in its initial stages.

## License
This work is licensed under the Creative Commons Attribution 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/ or send a letter to Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.
