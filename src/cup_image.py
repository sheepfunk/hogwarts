from consts import HOUSES, IMAGE_PATH
from PIL import Image, ImageDraw, ImageFont



# Tuples of (x1, y1, x2, y2)
BAR_RECTS = {
    "Dark": (62, 70, 204, 513),
    "Light": (240, 70, 382, 513),
}

# Space below the bottom of the bar to superimpose the scores in text form
BAR_SPACE = 10

# Tuples of (background, fill)
BAR_COLORS = {
    "Light": ("#000000", "#0a8bc9"),
    "Dark": ("#000000", "#de5647"),
}

def calculate_scales(house_points):
    total_points = float(sum(house_points.values())) or 1.0

    return {house: house_points.get(house, 0) / total_points for house in HOUSES}

def draw_bar_for_house(im, house, scale):
    draw = ImageDraw.Draw(im)

    # Background rectangle
    draw.rectangle(BAR_RECTS[house], fill=BAR_COLORS[house][0])
    bar_y = BAR_RECTS[house][3] * (1-scale) + BAR_RECTS[house][1] * scale

    # Fill rectangle
    draw.rectangle((BAR_RECTS[house][0], bar_y,
                    BAR_RECTS[house][2], BAR_RECTS[house][3]),
                   fill=BAR_COLORS[house][1])

    del draw


def image_for_scores(scores):
    """Generate a sweet house cup image
   Arguments: a dictionary with house names as keys and scores as values
   Returns: filename containing a house cup image representing the
   scores
    """
    scaled = calculate_scales(scores)

    overlay = Image.open(IMAGE_PATH)

    bars = Image.new(overlay.mode, overlay.size)
    for house in HOUSES:
        draw_bar_for_house(bars, house, scaled[house])

    merged = Image.alpha_composite(bars, overlay)

    font = ImageFont.truetype('BrandonText-Black.otf', 32)
    draw = ImageDraw.Draw(merged)
    for house in HOUSES:
        text = "%d" % scores[house]
        w, _ = font.getsize(text)
        draw.text(
            ((BAR_RECTS[house][0] + BAR_RECTS[house][2] - w) * 0.5,
             BAR_RECTS[house][3] + BAR_SPACE),
            text,
            fill=BAR_COLORS[house][1], font=font)

    outfile = str(abs(hash(str(scores)))) + '.png'
    merged.save(outfile, "PNG")
    del overlay
    del bars
    del merged
    return outfile
