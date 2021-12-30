import shutil
from typing import List
from PIL import Image, ImageDraw, ImageFont
import os

SIZE_OF_SQUARE = 50


def create_chessboard(dimension: int) -> Image:
    board_size = SIZE_OF_SQUARE * dimension
    img = Image.new("RGB", (board_size, board_size))
    pixels = img.load()

    for i in range(dimension):
        for j in range(dimension):
            if (i + j) % 2:
                for k in range(SIZE_OF_SQUARE):
                    for r in range(SIZE_OF_SQUARE):
                        pixels[i * SIZE_OF_SQUARE + k, j * SIZE_OF_SQUARE + r] = (225, 225, 225)

    return img


def set_queens(img: Image, queens: List[int]) -> Image:
    img_with_queens = img.copy()
    fnt = ImageFont.truetype(os.path.join("view", "chessboard", "Montserrat-Regular.ttf"), int(SIZE_OF_SQUARE * 0.8))
    draw = ImageDraw.Draw(img_with_queens)
    for indx, val in enumerate(queens):
        draw.text((val * SIZE_OF_SQUARE + SIZE_OF_SQUARE * 0.15, indx * SIZE_OF_SQUARE), "Q", font=fnt,
                  fill=(255, 0, 0, 128))
    return img_with_queens


def draw_chessboards(queens: List[List[int]], output_path: str, folder_name: str) -> None:
    img = create_chessboard(len(queens[0]))

    folder_path = os.path.join(output_path, folder_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    else:
        shutil.rmtree(folder_path)  # Removes all the subdirectories!
        os.makedirs(folder_path)

    for indx, current_queens in enumerate(queens):
        img_with_queens = set_queens(img, current_queens)
        img_with_queens.save(os.path.join(folder_path, f"{indx + 1}.png"))
