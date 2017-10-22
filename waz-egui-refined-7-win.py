# coding=utf-8
"""Easygui text file processing in Python 3.x.

The text file '01.txt' contains a random selection of zeros and ones.
Write a program to process it and find out:
- How many zeros and ones? *DONE!
- Longest string of zeros and ones? *DONE!
Then extend your program to:
- Compress the data using your own method. *DONE!
- Announce the space saving in bytes. *DONE!
- Export the compressed data to another file. *DONE!

URL: http://easygui.sourceforge.net
sudo pip3 install easygui
sudo apt / dnf install blt python3-easygui python3-tk tk8.6-blt2.5
Requires tkinter (python3-tk) on some platforms

Path for Linux is /home/russell/python/coding/waz/01xxxxx.txt
Path for Win is E:/Dropbox/python/coding/waz/01xxxxx.txt

os.system('clear') for Linux
os.system('cls') for Win
"""

import easygui
import glob
import itertools
import os
import zipfile

# File Section - open read-only and pass contents, define file-path.
os.system('cls')
input_file = open(
    'E:/Dropbox/python/coding/waz/01.txt', 'r'
    )
file_path = os.path.normpath(
    'E:/Dropbox/python/coding/waz/01.txt'
    )
file_content = input_file.read()
input_file.close()
question_pic = \
    "E:/Dropbox/python/coding/waz/question.gif"

# Code Block: 001.
# User can choose whether to print entire file contents or not before
# showing character counts.
msg_showfilecontquest = \
    ("Print entire file contents before showing character count for "
        "0's and 1's  (Y/n)?")
msg_confirm = "Please Confirm..."
msg_continue = "Press CANCEL or OK to continue..."
msg_nothingtodo = "Nothing to do here..."
msg_filepath = "File Path: " + file_path
title_showfilecontandcharcnt = "Show File Contents and Character Count"
title_showcharcntonly = "Show Character Count Only"
# Perform string counting operations on 0 and 1.
ans_cntzero = str(
    file_content.count('0')
    )
ans_cntone = str(
    file_content.count('1')
    )
heading_entirefilecont = "The entire file contents is: "
heading_numberzeros = "The number of 0's is: "
heading_numberones = "The number of 1's is: "
# Define answer formatting for YES response to print all file contents.
ans_yfilecont = (
    '{heading_entire_filecont}\n\n'
    '{show_file_content}\n'
    '{heading_number_zeros}'
    '{number_of_zeros}\n'
    '{heading_number_ones}'
    '{number_of_ones}\n\n\n'
    '{msg_to_continue}'
    .format(
        heading_entire_filecont=heading_entirefilecont,
        show_file_content=file_content,
        heading_number_zeros=heading_numberzeros,
        number_of_zeros=ans_cntzero,
        heading_number_ones=heading_numberones,
        number_of_ones=ans_cntone,
        msg_to_continue=msg_continue
        )
    )
# Define answer formatting for NO response to print all file contents.
ans_nfilecont = (
    '{heading_number_zeros}'
    '{number_of_zeros}\n'
    '{heading_number_ones}'
    '{number_of_ones}\n\n\n'
    '{msg_to_continue}'
    .format(
        heading_number_zeros=heading_numberzeros,
        number_of_zeros=ans_cntzero,
        heading_number_ones=heading_numberones,
        number_of_ones=ans_cntone,
        msg_to_continue=msg_continue
        )
    )
# Pass-in headings and all results into easygui Y/N box conditional statement.
if easygui.ynbox(
        msg=msg_showfilecontquest,
        title=msg_confirm,
        image=question_pic,
        cancel_choice='[<F1>]Yes',
        default_choice='[<F2>]No'
        ):
    # noinspection PyTypeChecker
    easygui.textbox(
        msg=msg_filepath,
        title=title_showfilecontandcharcnt,
        text=ans_yfilecont,
        codebox=True,
        callback=None,
        )
else:
    # noinspection PyTypeChecker
    easygui.textbox(
        msg=msg_filepath,
        title=title_showcharcntonly,
        text=ans_nfilecont,
        codebox=True,
        callback=None,
        )
# The 'callback' option is invoked by 'OK' button action, if 'None' moves on.
# 'CANCEL' button moves onto next code block without further action.
# This is strange behaviour, and can't seem to get it to do anything useful
# with any functions: (https://docs.python.org/3/library/functions.html).
# You can pass 'quit' as the 'callback', but this then exits on 'OK'.
# Passing 'quit()' as 'callback' exits without any button press, as the code
# is immediately called upon running.

# Code Block: 002
msg_cntchar = \
    "Would you like to count the all characters in the file  (Y/n)?"
title_totcharcnt = "Total Character Count"
msg_moveon = "Moving on..."
title_userconf = "User Confirmation"
msg_button = "Continue..."
# Perform string character counting operation.
filecharcnt = str(
    len(''.join(file_content.split()))
    )
heading_charcount = "The total character count within the file is: "
# Define and format character count answer.
ans_charcount = (
    '{heading_char_count}'
    '{show_char_count}\n\n\n'
    '{msg_to_continue}'
    .format(
        heading_char_count=heading_charcount,
        show_char_count=filecharcnt,
        msg_to_continue=msg_continue
        )
    )
# Present output in easygui Y/N box conditional.
if easygui.ynbox(msg=msg_cntchar,
                 title=msg_confirm,
                 image=question_pic,
                 cancel_choice='[<F1>]Yes',
                 default_choice='[<F2>]No'
                 ):
    # noinspection PyTypeChecker
    easygui.textbox(
        msg=msg_filepath,
        title=title_totcharcnt,
        text=ans_charcount,
        codebox=True,
        callback=None,
        )
else:
    easygui.msgbox(
        msg=msg_moveon,
        title=title_userconf,
        ok_button=msg_button
        )

# Code Block: 003
msg_longstrquest = \
    ("Would you like to include the longest overall string in the file "
        "along with the results for longest string of 0's or 1's  (Y/n)?")
msg_ylongst = \
    ("The longest overall string, along with the longest string of 0's "
        "or 1's in the file is...")
title_ylongstr = \
    "Longest Overall String and Longest String of 0's or 1's"
msg_nlongstr = \
    "The longest string of 0's or 1's in the file is..."
title_nlongstr = \
    "Longest String of 0's or 1's"
# Perform string calculations for longest overall string, longest string of
# zero's and longest string of one's.
overalllongstr = (
    max(len(list(templist))
        for (comparer, templist)
        in itertools.groupby(file_content)
        if comparer == '0' or '1')
    )
longstrzero = (
    max(len(list(templist))
        for (comparer, templist)
        in itertools.groupby(file_content)
        if comparer == '0')
    )
longstrone = (
    max(len(list(templist))
        for (comparer, templist)
        in itertools.groupby(file_content)
        if comparer == '1')
    )
heading_overalllongstr = "Longest overall string is: "
heading_longstrzero = "Longest string of 0's is: "
heading_longstrone = "Longest string of 1's is: "
# Perform a test to calculate using nested conditional statements to determine
# which string is the longest; either zero's or one's, or whether they are
# exactly equal to one another.
if longstrzero == longstrone:
    text_highestcntans = \
        "Zero's and One's are EXACTLY EQUAL in count length."
    pass
else:
    highestcnttest = max(longstrzero, longstrone)
    if highestcnttest == longstrzero:
        highestcntans = longstrzero
        text_highestcntans = "Zero's have the highest count."
    else:
        highestcntans = longstrone
        text_highestcntans = "One's have the highest count."
# Define and format the answer for both YES and NO responses as to whether to
# include the overall longest string in with the results.
ans_ylongstr = (
    '{heading_overall_longstr}'
    '{show_overall_longstr}\n\n'
    '{heading_longstr_zero}'
    '{show_longstr_zero}\n'
    '{heading_longstr_one}'
    '{show_longstr_one}\n\n'
    '{heading_highestcntans}\n\n\n'
    '{msg_to_continue}'
    .format(
        heading_overall_longstr=heading_overalllongstr,
        show_overall_longstr=overalllongstr,
        heading_longstr_zero=heading_longstrzero,
        show_longstr_zero=longstrzero,
        heading_longstr_one=heading_longstrone,
        show_longstr_one=longstrone,
        heading_highestcntans=text_highestcntans,
        msg_to_continue=msg_continue
        )
    )
ans_nlongstr = (
    '{heading_longstr_zero}'
    '{show_longstr_zero}\n'
    '{heading_longstr_one}'
    '{show_longstr_one}\n\n'
    '{heading_highestcntans}\n\n\n'
    '{msg_to_continue}'
    .format(
        heading_longstr_zero=heading_longstrzero,
        show_longstr_zero=longstrzero,
        heading_longstr_one=heading_longstrone,
        show_longstr_one=longstrone,
        heading_highestcntans=text_highestcntans,
        msg_to_continue=msg_continue
        )
    )
# Present the results within an easygui YN box using conditional statements.
if easygui.ynbox(
        msg=msg_longstrquest,
        title=msg_confirm,
        image=question_pic,
        cancel_choice='[<F1>]Yes',
        default_choice='[<F2>]No'
        ):
    # noinspection PyTypeChecker
    easygui.textbox(
        msg=msg_ylongst,
        title=title_ylongstr,
        text=ans_ylongstr,
        codebox=True,
        callback=None,
        )
else:
    # noinspection PyTypeChecker
    easygui.textbox(
        msg=msg_nlongstr,
        title=title_nlongstr,
        text=ans_nlongstr,
        codebox=True,
        callback=None,
        )

# Code Block: 004 - Create ZIP Archive and Express Data Savings in Bytes
title_all_zip = "Zipfile Processing..."
msg_yn_question = "Compress File? (Y/n)"

msg_y_decision = "Compression Decision: Positive"
msg_n_decision = "Compression Decision: Negative"

if easygui.ynbox(
        msg=msg_yn_question,
        title=title_all_zip,
        cancel_choice='[<F1>]Yes',
        default_choice='[<F2>]No'
        ):

    compressed_zip_file = zipfile.ZipFile(
        'E:/Dropbox/python/coding/zip/01-txt-to-archive.zip', 'w'
    )  # Open a zip file for write mode

    for name in glob.glob(
            'E:/Dropbox/python/coding/zip/01.txt'
    ):  # Choose which file will be compressed into the archive

        compressed_zip_file.write(
            name, os.path.basename(name), zipfile.ZIP_DEFLATED
        )  # Define the type of zip file and do write process

    compressed_zip_file.close()  # Close the zip file after writing process

    compressed_zip_file = zipfile.ZipFile(
        'E:/Dropbox/python/coding/zip/01-txt-to-archive.zip', 'r'
    )  # Specify path to new zip file and read it back

    for info in compressed_zip_file.infolist():

        zip_file_size = info.file_size
        zip_compress_size = info.compress_size

        zip_data_savings = info.file_size - info.compress_size
        # Read file_size and compress_size from new zip archive and
        # subtract from one another

        msg_zipfilesize = "Zip file size = "
        msg_zipcompresssize = "Zip compress size = "
        msg_datasavings = "Archive data savings in bytes = "
        zip_y_answer = (
            '{msg_zip_file_size}'
            '{output_zip_file_size}\n\n'
            '{msg_zip_compress_size}'
            '{output_zip_compress_size}\n\n'
            '{msg_data_savings}'
            '{zipdata_savings}\n\n\n'
            '{msg_to_continue}'
            .format(
                msg_zip_file_size=msg_zipfilesize,
                output_zip_file_size=zip_file_size,
                msg_zip_compress_size=msg_zipcompresssize,
                output_zip_compress_size=zip_compress_size,
                msg_data_savings=msg_datasavings,
                zipdata_savings=zip_data_savings,
                msg_to_continue=msg_continue
                )
            )
        easygui.textbox(
            msg=msg_y_decision,
            title=title_all_zip,
            text=zip_y_answer,
            codebox=True,
            callback=None
        )
else:
    zip_n_answer = (
        '{msg_nothing_to_do}\n\n\n'
        '{msg_to_continue}'
        .format(
            msg_nothing_to_do=msg_nothingtodo,
            msg_to_continue=msg_continue
            )
        )
    easygui.textbox(
        msg=msg_n_decision,
        title=title_all_zip,
        text=zip_n_answer,
        codebox=True,
        callback=None,
        )

# TODO Stick more messages and user instructions in egui boxes
# TODO Give the user choice over which file to compress and where to save
# TODO Give the user choice over which file to open at the start
# TODO Expand the programme to work with all alpha characters
# TODO Put default choices in ALL boxes (not possible > textbox limitation?)
# TODO Find out how to put a blank line after image box? Blank image?
