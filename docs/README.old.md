Jeli ASR & Corpus

## What is Jeli-ASR
Jeli-ASR is a multidimentional package that was developed with the aim to empower the usage of the Bambara Language. Starting in an initiative to the develop the Bambara Language, and its cultural values. The package is consisted of an ASR model under ongoing development, and a mini corpus of griots narration in [audio](https://zenodo.org/record/6997806), its transcription in ***eaf*** which is [ELAN format](https://archive.mpi.nl/tla/elan/download), and a tool to download and exctract the dataset.

## ASR - Model
[TODO]

## Corpus
The Griots corpus is a speech corpus containing both audio and its accompanying transcribed text. You can find the intent, the approaches, a detailed look, and a thorough explanation of the dataset on the [Data-Card (coming)](). Refer to the following list of recordings and the general meta information about the recordings:

### Griots Narrations

| Recording ID | Theme | Dialect | Utterance Count | Spkr. Gender |
|:------------:|:-----:|:-------:|:---------------:|:------------:|
| griots_r1 | L'histoire d'une fille | Bamako | 980 | M |
| griots_r2 | L'histoire d'un grand marabo | Ségou | 1030 | M |
| griots_r3 | Les forgérons | Bamako | 805 | M |
| griots_r4 | Les Noms Authentiques | Bamako | 764 | M |
| griots_r5 | Les Coulibaly | Bamako | 981 | M |
| griots_r6 | Les Diarra | Ségou | 1122 | M |
| griots_r7 | L'histoire du roi Razaly | Bamako | 1407 | M |
| griots_r8 | L'histoire des fils d'Abraham | Bamako | 1126 | F |
| griots_r9 | Les ''Niamala'' hommes de caste |  Bamako | 821 | M |
| griots_r10 | L'éducaion d'hier et d'aujourd'hui | Bamako | 1078 | F |
| griots_r11 | Garba Mama | Bamako | 970 | M |
| griots_r12 | La Bataille de Kaana | Bamako | 997 | M |
| griots_r13 | Diokala | Bamako | 964 | M |
| griots_r14 | Nos ancetres | Malinké Siby | 1136 | M |
| griots_r15 | L'histoire d'El Hadj Oumar Tall | Bamako | 844 | M |
| griots_r16 | Les Massassi du Karta 'Bɔ' | Bamako | 941 | M |
| griots_r17 | Histoire de Samory |  Malinké kangaba | 773 | M |
| griots_r18 | Le griot | Malinké de kangaba | 809 | M |
| griots_r19 | La vie d'avant en milieu Bamanan | Bamako | 611 | F |
| griots_r20 | Les Maabo | Ségou | 1102 | M |
| griots_r21 | L'histoire de Djonkoloni | Bamako | 859 | M |
| griots_r22 | Various | Malinké de Siby | 926 | F |
| griots_r23 | L'histoire de Bɔ | Ségou | 1319 | M |
| griots_r24 | L'éducaion d'hier et d'aujourd'hui | Bamako | 942 | F |
| griots_r25 | L'hisoire de la jeune fille Niamakolo | Bamako | 828 | F |
| griots_r26 | Hier et aujourd'hui | Bamako | 1128 | M |
| griots_r27 | Les Mianka | Bamako | 1166 | M |
| griots_r28 | Le mariage d'hier et d'aujourd'hui | Bamako | 810 | F |
| griots_r29 | L' histoire de Dabo | Bamako | 774 | M |
| griots_r30 | Les valeurs du Mali | Bamako | 968 | M |
|**TOTAL**||| ***28971*** ||
||

### Street Interviews
Along side the griots' narrations, a smaller sample of individuals were interviewd about the importance of bambara in the technology. 

**N.B**: Not all of these audios have been transcribed.

| Recording ID | Utt. Count | Spkr. Gender | Status |
|:------------:|:-------:|:------------:|:------:|
| intrvw_r1 | 55 | F | V |
| intrvw_r2 | X | X | X |
| intrvw_r3 | 24 | M | V |
| intrvw_r4 | 25 | M | V |
| intrvw_r5 | 31 | M | V |
| intrvw_r6 | 20 | M | V |
| intrvw_r7 | X | X | X |
| intrvw_r8 | X | X | X |
| intrvw_r9 | X | X | X |
| intrvw_r10 | X | F | V |
| intrvw_r11 | X | M | V |
| intrvw_r12 | X | M | V |
| intrvw_r13 | 25 | M | V |
| intrvw_r14 | X | X | X |
| intrvw_r15 | X | X | X |
| intrvw_r16 | X | X | X |
| intrvw_r17 | X | X | X |
| intrvw_r18 | X | X | X |
| intrvw_r19 | X | X | X |
| intrvw_r20 | 17 | M | V |
| intrvw_r21 | 137 | M | V |
| intrvw_r22 | 142 | F | V |
| **TOTAL** | ***476*** | - | - |
||

### jelipkg toolkit
<code>jelipkg</code> is sub-package that serves as an entry point to the corpus. It is a python package that allows you to browse, and download the corpus for your own convenience, you can download the textual data either in raw text format or json format.

#### Installation

```bash
$ pip install -U https://github.com/s7d11/daba/releases/download/v0.0.1-alpha/daba-0.9.2.tar.gz
```

#### Quickstart
#### Documentation

**IMPORTANT**: It is recommended to download one recording/interview at a time, if you have an unreliable network due to the size of the dataset.

## Contact & People
**Principal Investigator**: Michael Leventhal, `mleventhal <at> robotsmali.org`  
**Manager**: Sebastien Diarra, `sdiarra <at> robotsmali.org`  
**inquiries & Collaboration**: `research <at> robotsmali.org`

## Reference

## Errors & Bugs

## License
This work is licensed under the Creative Commons Attribution 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/ or send a letter to Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.
