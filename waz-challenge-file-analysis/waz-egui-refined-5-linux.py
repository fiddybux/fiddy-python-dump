# coding=utf-8
"""Waz Challenge - Converted to use easygui in Python 3.x.

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
os.system('clear')
input_file = open(
    '/home/russell/Dropbox/python/coding/waz/01.txt', 'r'
    )
file_path = os.path.normpath(
    '/home/russell/Dropbox/python/coding/waz/01.txt'
    )
file_content = input_file.read()
input_file.close()
lyra_pic = \
    "/home/russell/Dropbox/python/coding/waz/lyra.gif"

# Code Block: 001.
# User can choose whether to print entire file contents or not before
# showing character counts.
msg_showfilecontquest = \
    ("Print entire file contents before showing character count for "
        "0's and 1's  (Y/n)?")
msg_confirm = "Please Confirm..."
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
    '{number_of_ones}'
    .format(
        heading_entire_filecont=heading_entirefilecont,
        show_file_content=file_content,
        heading_number_zeros=heading_numberzeros,
        number_of_zeros=ans_cntzero,
        heading_number_ones=heading_numberones,
        number_of_ones=ans_cntone
        )
    )
# Define answer formatting for NO response to print all file contents.
ans_nfilecont = (
    '{heading_number_zeros}'
    '{number_of_zeros}\n'
    '{heading_number_ones}'
    '{number_of_ones}'
    .format(
        heading_number_zeros=heading_numberzeros,
        number_of_zeros=ans_cntzero,
        heading_number_ones=heading_numberones,
        number_of_ones=ans_cntone
        )
    )
# Pass-in headings and all results into easygui Y/N box conditional statement.
if easygui.ynbox(
        msg=msg_showfilecontquest,
        title=msg_confirm,
        image=lyra_pic
        ):
    easygui.textbox(
        msg=msg_filepath,
        title=title_showfilecontandcharcnt,
        text=ans_yfilecont,
        codebox=True,
        callback=None
        )
else:
    easygui.textbox(
        msg=msg_filepath,
        title=title_showcharcntonly,
        text=ans_nfilecont,
        callback=None
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
    '{show_char_count}'
    .format(
        heading_char_count=heading_charcount,
        show_char_count=filecharcnt
        )
    )
# Present output in easygui Y/N box conditional.
if easygui.ynbox(msg=msg_cntchar, title=msg_confirm,
                 image=lyra_pic):
    easygui.textbox(
        msg=msg_filepath,
        title=title_totcharcnt,
        text=ans_charcount,
        callback=None
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
    '{heading_highestcntans}'
    .format(
        heading_overall_longstr=heading_overalllongstr,
        show_overall_longstr=overalllongstr,
        heading_longstr_zero=heading_longstrzero,
        show_longstr_zero=longstrzero,
        heading_longstr_one=heading_longstrone,
        show_longstr_one=longstrone,
        heading_highestcntans=text_highestcntans
        )
    )
ans_nlongstr = (
    '{heading_longstr_zero}'
    '{show_longstr_zero}\n'
    '{heading_longstr_one}'
    '{show_longstr_one}\n\n'
    '{heading_highestcntans}'
    .format(
        heading_longstr_zero=heading_longstrzero,
        show_longstr_zero=longstrzero,
        heading_longstr_one=heading_longstrone,
        show_longstr_one=longstrone,
        heading_highestcntans=text_highestcntans
        )
    )
# Present the results within an easygui YN box using conditional statements.
if easygui.ynbox(
        msg=msg_longstrquest,
        title=msg_confirm,
        image=lyra_pic
        ):
    easygui.textbox(
        msg=msg_ylongst,
        title=title_ylongstr,
        text=ans_ylongstr,
        callback=None
        )
else:
    easygui.textbox(
        msg=msg_nlongstr,
        title=title_nlongstr,
        text=ans_nlongstr,
        callback=None
        )

# Code Block: 004
title_all_zip = "Zipfile Processing..."
msg_yn_question = "Compress File? (Y/n)"
msg_y_ans = "Compression Decision: Positive"
msg_n_ans = "Compression Decision: Negative"
if easygui.ynbox(
        msg=msg_yn_question,
        title=title_all_zip
        ):
    # Create archive
    compressed_zip_file = zipfile.ZipFile(
        '01-txt-to-archive.zip', 'w'
        )  # open zip file and write to it
    for name in glob.glob(
            '01.txt'
            ):
        compressed_zip_file.write(
            name,
            os.path.basename(name),
            zipfile.ZIP_DEFLATED
            )
    compressed_zip_file.close()
    # Read archive back and print name, size and compression size
    compressed_zip_file = zipfile.ZipFile(
        '01-txt-to-archive.zip', 'r'
        )  # reopen the zip > see contents
    for info in compressed_zip_file.infolist():
        # print(
        #     info.filename,
        #     info.file_size,
        #     info.compress_size
        # )
        zip_data_savings = \
            info.file_size - info.compress_size  # Subtract difference
        zip_y_answer = (
            "Archive data savings in bytes = "
            + str(zip_data_savings)
            )  # Format the difference (zip_data_savings) >> pass to easygui
        easygui.textbox(
            msg=msg_y_ans,
            title=title_all_zip,
            text=zip_y_answer
            )  # TODO Format this answer to present filepath info for archive
else:

    easygui.textbox(
        msg=msg_n_ans,
        title=title_all_zip
        )  # TODO Jazz up this part...it's weak and basic right now
