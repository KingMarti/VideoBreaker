# VideoBreaker
Script to break long video files into segments

To configure the script, open first in notepad (by either right clicking and selecting open with or opening notepad and then file -> open or your code editor. 
enter the information requied in the first section.
      Video_dir <- This is the direcotry path to where your videos that you want segmented are stored
      Out_dir <- This is the directory path were the video output will be saved
      prefix <- This is the title that will be assigned to the video, the script will automatically add on the part number after your chosen title
      target_length <- This refers to the maximum length a segment should be, 25 minutes by default. This time is measuered in seconds.
To Launch the script, either double click the file, a black console window should appear and the script will start loading in the videos in the chosen directory and cutting them into new videos every 25 minutes (or how ever long you set the target length to in the config section), after each part is complete you can find it in your chosen output directory
      
      
