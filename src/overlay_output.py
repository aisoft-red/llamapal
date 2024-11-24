import cv2
import pyttsx3

import cv2

import cv2

import cv2

def overlay_text(frame, text, font_scale=1, font_thickness=2, box_color=(0, 0, 0), text_color=(255, 255, 255), alpha=0.6):
    """
    Overlays text on a video frame at the bottom, spanning 75% of the frame's width.

    Args:
        frame: The video frame (numpy array).
        text: The text to overlay.
        font_scale: Font size of the text.
        font_thickness: Thickness of the text strokes.
        box_color: Background color of the text box (BGR).
        text_color: Color of the text (BGR).
        alpha: Opacity of the text background box (0.0 - 1.0).

    Returns:
        frame: The frame with text overlay.
    """
    # Set font type
    font = cv2.FONT_HERSHEY_SIMPLEX

    # Calculate frame dimensions
    frame_height, frame_width, _ = frame.shape

    # Determine the maximum width for the text box (75% of the frame's width)
    max_width = int(frame_width * 0.75)

    # Split the text into lines that fit within the max width
    words = text.split(' ')
    lines = []
    line = ""

    for word in words:
        # Calculate the size of the current line with the next word
        test_line = f"{line} {word}".strip()
        text_width, _ = cv2.getTextSize(test_line, font, font_scale, font_thickness)[0]
        if text_width <= max_width:
            line = test_line
        else:
            lines.append(line)  # Save the current line
            line = word  # Start a new line

    lines.append(line)  # Add the last line

    # Calculate the text box's height (line height * number of lines + padding)
    text_height = cv2.getTextSize("Test", font, font_scale, font_thickness)[0][1]
    box_height = (len(lines) * (text_height + 10)) + 20  # Padding between lines and around the box

    # Determine the position of the text box (bottom 20 pixels above the frame bottom)
    box_start = (int((frame_width - max_width) / 2), frame_height - box_height - 20)
    box_end = (box_start[0] + max_width, frame_height - 20)

    # Draw the semi-transparent background rectangle
    overlay = frame.copy()
    cv2.rectangle(overlay, box_start, box_end, box_color, -1)
    frame = cv2.addWeighted(overlay, alpha, frame, 1 - alpha, 0)

    # Draw each line of text inside the box
    y_offset = box_start[1] + 20
    for line in lines:
        text_size = cv2.getTextSize(line, font, font_scale, font_thickness)[0]
        text_x = box_start[0] + (max_width - text_size[0]) // 2  # Center-align the text
        cv2.putText(frame, line, (text_x, y_offset), font, font_scale, text_color, font_thickness, lineType=cv2.LINE_AA)
        y_offset += text_height + 10  # Move to the next line

    return frame




def text_to_speech(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
