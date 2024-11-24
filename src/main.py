from video_processing import extract_frames
from llama_inference import generate_commentary
from overlay_output import overlay_text, text_to_speech
import cv2
import os
import datetime


def process_video(input_video, output_video, frame_interval=50, use_groq=False):
    # check if the input video exists
    try:
        open(input_video)
    except FileNotFoundError:
        print("Input video file not found.")
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
        cv2.imwrite(output_dir+"/processed_frame_" + str(len(processed_frames)) + ".jpg", processed_frame)
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

if __name__ == "__main__":
    now = datetime.datetime.now()
    output_dir = "./data/output/" + now.strftime("%Y-%m-%d_%H-%M-%S")

    #make the output directory with a timestamp if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)


    process_video(
        "./data/input/basketball_one_player.mp4",
        output_dir + "/basketball_one_player.mp4",
        use_groq=False
    )
