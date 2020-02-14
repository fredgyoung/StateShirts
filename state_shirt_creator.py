from PIL import Image, ImageDraw, ImageFont

def read_file():
    data = []

    with open('C:/Users/Fred/Desktop/state_info.csv') as input:
        for line in input:
            data.append(line.strip().split(','))

    # print(data)
    return data

def create_design(state):
    #print(state)
    order, name, date, abbrev = state

    size = (4500, 4500)
    outfile = "C:/Users/Fred/Desktop/T-Shirts/states/" + name + ".png"

    square_color = "white"
    text_color = "white"

    image = Image.new("RGBA", size)
    image.putalpha(0)

    # Rectangle coordinates
    left, top, right, bottom = 500, 500, 4000, 4000

    draw = ImageDraw.Draw(image)

    # Draw center lines (for debugging only)
    #middle_x = (right + left) / 2
    #middle_y = (top + bottom) / 2
    #draw.line([(middle_x, top), (middle_x, bottom)], fill=square_color, width=10)
    #draw.line([(left, middle_y), (right, middle_y)], fill=square_color, width=10)

    # Draw rectangle
    #draw.rectangle([left, top, right, bottom], outline=square_color, width=100)
    draw.line([(left+50, top), (right-50, top)], fill=square_color, width=100)
    draw.line([(left+50, bottom), (right-50, bottom)], fill=square_color, width=100)
    draw.line([(left, top+50), (left, bottom-50)], fill=square_color, width=100)
    draw.line([(right, top+50), (right, bottom-50)], fill=square_color, width=100)

    # Draw rounded corners
    draw.arc(xy=[(left-50, top-50), (left+200, top+200)], start=180, end=270, fill=square_color, width=100)
    draw.arc(xy=[(right-200, top-50), (right+50, top+200)], start=270, end=360, fill=square_color, width=100)
    draw.arc(xy=[(left-50, bottom-200), (left+200, bottom+50)], start=90, end=180, fill=square_color, width=100)
    draw.arc(xy=[(right-200, bottom-200), (right+50, bottom+50)], start=0, end=90, fill=square_color, width=100)

    # Draw admittance order
    font = ImageFont.truetype("arial.ttf", 320)
    draw.text(xy=(700, 650), text=order, font=font, fill=text_color)

    # Draw admittance date
    font = ImageFont.truetype("arial.ttf", 320)
    draw.text(xy=(3050, 650), text=date, font=font, fill=text_color)

    # Draw postal abbreviation
    font = ImageFont.truetype("arial.ttf", 1920)
    abbrev_width = font.getsize(text=abbrev)
    print("abbrev_width:", abbrev_width[0])
    # Calculate starting point of centered text
    x = (right - left - abbrev_width[0]) / 2 + left
    draw.text(xy=(x, 1200), text=abbrev, font=font, fill=text_color)

    # Draw name
    font = ImageFont.truetype("arial.ttf", 320)
    name_width = font.getsize(text=name)
    print("name_width:", name_width[0])
    # Calculate starting point of centered text
    x = (right - left - name_width[0]) / 2 + left
    draw.text(xy=(x, 3500), text=name, font=font, fill=text_color)

    # image.show()
    image.save(outfile, "PNG")
    image.close()

def create_shirts():
    data = read_file()
    for state in data:
        create_design(state)
        #break

if __name__ == "__main__":
    create_shirts()
