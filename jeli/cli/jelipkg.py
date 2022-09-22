"""
"""

from email import message
import os
from select import select
import sys
from InquirerPy import inquirer
from jeli.core import jeli, utils, config

def recording_browser(jl: jeli.JeliASR):
    select = jl.recording_selector()
    view_choices = [
        "Recording overview",
        "Detailed view of recording"]
    view_select = inquirer.select(
        message="Choose browsing option:",
        choices=view_choices,
        default=None,
        qmark="jeli>",
        amark="jeli>"
    ).execute()
    view_select = view_choices.index(view_select)
    if(view_select == 0):
        jl.recording_overview(select, True)
    if(view_select == 1):
        jl.recording_detail(select, True)

def recording_dowloader(jl: jeli.JeliASR, r_id=None):
    """ """

    if(not r_id):
        select = jl.recording_selector()
    else:
        select = r_id

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
    
    if(d_index == 0):
        jl.download_recording(select, d_index)
    if(d_index == 1):
        jl.download_recording(select, d_index)

def help_message():
    """ """
    disp = utils.DisplayUtils()
    text = """
    Type one of the followings to:
        - browse -> Interactively browse the list of recordings
        - download -> Directly download a recording from the dataset
        - help -> Display this message
        - exit -> Exit the jelipkg console
    \n"""

    disp.out(text)
    hp = inquirer.text(
        message="continue [ENTER]",
        qmark="",
        amark=""
    ).execute()

def main():

    jl = jeli.JeliASR()

    print(f"Welcome to jelipkg v{config.VERSION}\n", file=sys.stderr)
    print(f"Type browse, download, help, exit", file=sys.stderr)
    options = ["browse", "download", "help", "exit"]
    option = ""

    while(option != "exit"):
        option = inquirer.text(
            message="",
            completer={"browse": None, "download": None, "help": None, "exit": None},
            multicolumn_complete=False,
            validate=lambda res: res in options,
            invalid_message=f"Invalid <Option> - correctly choose - {options}",
            qmark="jeli>",
            amark="jeli>"
        ).execute()

        if(option == "browse"):
            recording_browser(jl)

        if(option == "download"):
            recording_dowloader(jl)
        if(option == "help"):
            help_message()

if __name__ == '__name__':
    main()
