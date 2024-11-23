from video_processing import extract_frames
from llama_inference import generate_commentary
from overlay_output import overlay_text, text_to_speech
import cv2

def process_video(input_video, output_video, frame_interval=100):
    # check if the input video exists
    try:
        open(input_video)
    except FileNotFoundError:
        print("Input video file not found.")
        return

    # extract frames from the input video
    frames = extract_frames(input_video, frame_interval)
    print("Extracted frames from the video.")
    print("Total frames extracted:", len(frames))
    processed_frames = []

    for frame in frames:
        print("Processing frame... ", len(processed_frames) + 1)
        commentary = generate_commentary(frame)
        print("Generated Commentary:", commentary)
        processed_frame = overlay_text(frame, commentary)
        processed_frames.append(processed_frame)
        text_to_speech(commentary)

    height, width, _ = processed_frames[0].shape
    out = cv2.VideoWriter(output_video, cv2.VideoWriter_fourcc(*'mp4v'), 30, (width, height))

    for frame in processed_frames:
        out.write(frame)

    out.release()
    print("Processed video saved as:", output_video)

if __name__ == "__main__":
    process_video("/Users/ravinderjilkapally/Downloads/5192157-hd_1920_1080_30fps.mp4", "/Users/ravinderjilkapally/Downloads/5192157-hd_1920_1080_30fps.mp4")
