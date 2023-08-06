# Chatgpt Query

## Description

#### Write a python program based on the following instructions

**Program outcome**: The program should able to move the files from a specified directory to system directories like Documents, Pictures, Music, Videos based on the file extension

**Instructions:**
1. Get the Documents, Pictures, Music, Videos directories paths automatically based on the OS.
2. Take the input of the source directory from user from terminal.
3. Create a separate folder to store the files which haven't been opened in the last 30 days called **old_files**.
4. The program should support the movement of the files to system directories for windows, linux and Mac.
5. Print the filename and moved final file path in the terminal for all the moved files.
6. Write error handling to ignore files which cannot be moved and at the end print all the file names which could not be moved as well.
7. Print a human readable reason of why the files could not be moved.
8. Keep the unmoved files in the same directory as the source. 
9. Do not move folders.