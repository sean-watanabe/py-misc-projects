# Make sub folders and move files to them

## <div style="border-bottom: 2px solid;">Features</div>

1. The program will create subfolders in a destination folder and move a specified number of files from a source folder into them, as determined by the user.

2. The subfolders will be automatically numbered.

## <div style="border-bottom: 2px solid;">Background/Motivation</div>

Having had over 9,000 images in a folder, I wanted to organize them into subfolders to make them easier to manage.

## <div style="border-bottom: 2px solid;">Installation</div>

No installation needed. Use terminal to run the file.

```sh
# Download the main.py and cd to the directory where the file is downloaded. Then, run the file.
python main.py

# OR depending on your settings
python3 main.py
```

## <div style="border-bottom: 2px solid;">How to use</div>

As a preparation, create an 'empty' destination folder. Then, copy both the destination and source directory paths so that you can paste them later.

When you run 'main.py,' you'll be prompted to enter the destination folder path where the subfolders will be created, the source folder path where the files are stored, and the number of files to move into the newly created subfolders.

The files should be sorted in an ascending order by file names when being moved to each subfolder.

## <div style="border-bottom: 2px solid;">Limitations</div>

1. It only creates the specified number of subfolders as specified by the user and move files into the newly created folders. That's all it does.
2. It does not distinguish between files and directories. Also, it does not offer functionality for users to specify file types.
3. Tested only on macOS Ventura 13.6.9. With my knowledge at the time of writing, I'm not proficient enough to account for other platforms.
4. Hidden files will be counted, which will likely cause an error. The program will ONLY detect ".DS_Store" file and remove it to avoid an error.

## <div style="border-bottom: 2px solid;">Future updates</div>

- None at the moment.

Thanks for reading!
