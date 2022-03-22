#####################################################################################################
#                                                                                                   #
#           To Configure the script edit the section below with the relevent information            #
#        IMPORTNT! Make sure Directory Paths end with \\ eg. C:\\users\\user\\folder\\              #
#            ALL File Levels Need to Be Split With A Double \ as shown in the examples              #
#                                                                                                   #
#####################################################################################################

Video_dir = r"ENTER DIRECROTY PATH CONTAING VIDEOS HERE" #EG/ C:\\Users\User\\My Recoreded Shows\\
Out_dir = r"ENTER OUTPUT DIRECTORY HERE" #EG/ C:\Users\User\My_Videos\\ 
prefix = "Video Title here " #the script will add part and the number of each part to the title
target_length=1500 #measured in seconds

#####################################################################################################
#                                                                                                   #
#               Making Changes Beyond This Point Can Break The Script                               #
#                                                                                                   #
#####################################################################################################
import sys
import importlib.util
package_name = 'moviepy'
spec = importlib.util.find_spec(package_name)
if spec is None:
    print(package_name+" is not installed")
    print("Now Installing "+ package_name)
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])
    print(package_name +" installed")
from moviepy.editor import VideoFileClip    
from time import sleep
from datetime import date
import os

for video in os.listdir(Video_dir):
    full_vid = os.path.join(Video_dir+video)
    video_title = prefix+video
    full_duration = VideoFileClip(full_vid).duration
    devide_into_count = full_duration/target_length
    single_duration = full_duration/devide_into_count
    part =0
    if full_duration > target_length:
        try:
            while full_duration > target_length:
                clip = VideoFileClip(full_vid).subclip(full_duration-target_length, full_duration)
                full_duration-= target_length
                current_video = video_title+" part "+str(part)+".mp4"
                print("Current Clip is: ", current_video)
                clip.to_videofile(Out_dir+current_video,codec="nvenc_h264",temp_audiofile=Out_dir+"temp_audio.m4a",remove_temp=True,audio_codec="aac",threads=10)
                part +=1
                print("-----------------###############################--------------------------------")
        except:
            break
    else:
        print("Video is under {target_length}")
   