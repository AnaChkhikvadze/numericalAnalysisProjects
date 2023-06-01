import math
import cv2
import numpy as np

def blend_images(frame, figure, start_point, sizes, merging_line=0, side='Left'):
    """Blend the figure image onto the frame image.

    Parameters:
    - frame: The frame image.
    - figure: The figure image (should have a white background).
    - start_point: The starting coordinates for blending the figure.
    - sizes: The sizes of the figure.
    - merging_line: The line at which to merge the figures (default: 0).
    - side: The side of the merging line ('Left' or 'Right') (default: 'Left').

    Returns:
    - The blended frame image.
    """
    height, width = frame.shape[:2]
    resized_figure = cv2.resize(figure, sizes, interpolation=cv2.INTER_AREA)
    new_frame = frame.copy()

    if merging_line == 0:
        merging_line = int(math.floor(width / 2))

    for i in range(sizes[0]):
        for j in range(sizes[1]):
            if np.any(resized_figure[i][j] != [255, 255, 255]):
                if height > int(start_point[0] + i) and width > int(start_point[1] + j):
                    if side == 'Right' and merging_line < start_point[1] + j:
                        new_frame[start_point[0] + i][start_point[1] + j] = resized_figure[i][j]
                    elif side == 'Left' and merging_line > start_point[1] + j:
                        new_frame[start_point[0] + i][start_point[1] + j] = resized_figure[i][j]

    return new_frame.astype(np.uint8)


def video_frame(frame, figure, start, end, frames_quantity, start_size, end_size, side='Left', merge_line=810):
    """Generate a sequence of blended frames.

    Parameters:
    - frame: The frame image.
    - figure: The figure image.
    - start: The starting coordinates for blending.
    - end: The ending coordinates for blending.
    - frames_quantity: The number of frames to generate.
    - start_size: The starting size of the figure.
    - end_size: The ending size of the figure.
    - side: The side of the merging line ('Left' or 'Right') (default: 'Left').
    - merge_line: The line at which to merge the figures (default: 810).

    Returns:
    - A list of blended frames.
    """
    result = []
    x = float(end[0] - start[0]) / (frames_quantity - 1)
    y = float(end[1] - start[1]) / (end[0] - start[0])
    mean_dist = float(end_size - start_size) / (frames_quantity - 1)

    for i in range(frames_quantity):
        a = int(start_size + mean_dist * i)
        point = (start[0] + int(i * x), start[1] + int(i * x * y))
        pic = blend_images(frame, figure, point, [a, a], merge_line, side)
        result.append(pic)

    return result


def display_frames(list_frames):
    """Display a list of frames.

    Parameters:
    - list_frames: The list of frames to display.
    """
    for frame in list_frames:
        cv2.imshow("Our Blenders Video", frame)
        cv2.waitKey(100)


frame_image = cv2.imread('frame100.png', cv2.IMREAD_ANYCOLOR)
rectangle_image = cv2.imread("img_2.png", cv2.IMREAD_COLOR)
circle_image = cv2.imread('img.png', cv2.IMREAD_COLOR)
arrow_image = cv2.imread('img_1.png', cv2.IMREAD_COLOR)
background_color = [50, 205, 50]
merge_line = 810

# Example usage
frames_quantity = int(10 * (3.6 * 200 / speed))  # Replace 'speed' with the actual value
left_frames = video_frame(frame_image, circle_image, (70, 156), (420, 700), frames_quantity, 10, 120)
right_frames = video_frame(frame_image, circle_image, [338, 735], [69, 1428], frames_quantity + 2, 120, 10, side='Right')

# Display the frames
display_frames(left_frames + right_frames)
