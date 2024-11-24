from video_processing import extract_frames
from llama_inference import generate_commentary
from overlay_output import overlay_text, text_to_speech
import cv2
import os
import datetime
import glob
import contextlib
from PIL import Image

def process_video(input_video, output_video, frame_interval=50, use_groq=False):
    # check if the input video exists
    try:
        print("Input video file:", input_video)
        open(input_video)
        #extract the video name from the input video path that ends with mp4
        video_name = os.path.basename(input_video)
        print("Video Name:", video_name)
    except FileNotFoundError:
        print("Input video file not found. Please check the path:", input_video)
        return

    # extract frames from the input video
    frames = extract_frames(input_video, frame_interval)
    print("Total frames extracted:", len(frames))
    processed_frames = []
    commentary = ""
    all_commentary = []

    for frame in frames:
        print("Processing frame... ", len(processed_frames) + 1)
        commentary = generate_commentary(frame, all_commentary, use_groq)
        all_commentary.append(commentary)
        print("Generated Commentary:", commentary)
        #overlay the commentary on the frame in a 100x100 box at the top left corner adjust the overlay_text function to change the position
        print("Overlaying Commentary on the frame...")
        processed_frame = overlay_text(frame, commentary)
        processed_frames.append(processed_frame)
        #text_to_speech(commentary)
        print("Overlayed Commentary on the frame.")
        #save the processed frame
        cv2.imwrite(output_dir+ "/" + video_name +"_processed_frame_" + str(len(processed_frames)) + ".jpg", processed_frame)
        print("Processed frame saved as:", output_dir+"/processed_frame_" + str(len(processed_frames)) + ".jpg")
    height, width, _ = processed_frames[0].shape
    out = cv2.VideoWriter(output_video, cv2.VideoWriter_fourcc(*'mp4v'), 30, (width, height))
    for frame in processed_frames:
        out.write(frame)
    out.release()

    print("Processed video saved as:", output_video)
    print("Video processing completed.")
    print("Total frames processed:", len(processed_frames))

    #save the commentary
    with open(output_dir+"/commentary.txt", "w") as f:
        f.write("\n".join(all_commentary))  # Write each commentary on a new line

    # generate a gif of the processed frames

def generate_gif_of_processed_frames(output_dir):
    print("Generating GIF of processed frames...")
    #count the number of jpg files in the output directory
    processed_frames = [f for f in os.listdir(output_dir) if f.startswith("video") and f.endswith(".jpg")]
    # print the number of processed frames
    print("Total available processed frames:", len(processed_frames))
    # filepaths
    fp_in = output_dir+"/*.jpg"
    fp_out = output_dir+"/processed_frames_image.gif"

    # use exit stack to automatically close opened images
    with contextlib.ExitStack() as stack:

        # lazily load images
        imgs = (stack.enter_context(Image.open(f))
                for f in sorted(glob.glob(fp_in)))

        #print the first image
        # extract  first image from iterator
        img = next(imgs)

        # https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html#gif
        img.save(fp=fp_out, format='GIF', append_images=imgs,
                save_all=True, duration=600, loop=0)
    print("GIF of processed frames saved as:", output_dir+"/processed_frames.gif")

if __name__ == "__main__":
    now = datetime.datetime.now()
    output_dir = "./data/output/" + now.strftime("%Y-%m-%d_%H-%M-%S")

    #make the output directory with a timestamp if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    #loop and process 4 videos in series that are in the input directory/video_*.mp4
    for i in range(3):
        process_video("./data/input/video_" + str(i) + ".mp4", output_dir + "/video_" + str(i) + ".mp4", use_groq=True)

    #process_video("./data/input/basketball_two_players.mp4", output_dir + "/basketball_two_players.mp4", use_groq=True)
    #process_video("./data/input/basketball_one_player.mp4", output_dir + "/basketball_one_player.mp4",  use_groq=True)

    #generate_gif_of_processed_frames("data/output/2024-11-23_21-27-17")
    generate_gif_of_processed_frames(output_dir)

