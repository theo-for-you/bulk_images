from duckduckgo_search import DDGS
import sys
import requests
import random
import zipfile
import re


def get_q_args(start, args):
    q = ""
    for i in range(start, len(args)):
        q += " " + args[i]

    return q


def get_res_arg(arg):
    if not re.match(r"^[0-9]+x[0-9]+$", arg):
        raise

    res = arg.split("x")

    return int(res[0]), int(res[1])


if len(sys.argv) < 2:
    print("Require amout of images")
    exit()

num_img = int(sys.argv[1])

width = 0
height = 0

# getting random query
type = requests.get(
    "https://gist.githubusercontent.com/deekayen/4148741/raw/98d35708fa344717d8eee15d11987de6c8e26d7d/1-1000.txt")
words_list = type.text.split()

q = words_list[random.randint(0, 999)] + " " + \
    words_list[random.randint(0, 999)]


if len(sys.argv) >= 3:
    try:
        width, height = get_res_arg(sys.argv[2])  # raises

        if len(sys.argv) > 3:
            q = get_q_args(3, sys.argv)
    except:
        q = get_q_args(2, sys.argv)


images = DDGS().images(q, size="Wallpaper")
f = zipfile.ZipFile("img_bulk.zip", "w")

while num_img > 0:

    print("Loading...", num_img)

    img = next(images)
    url = img["image"]

    try:
        req = requests.get(url, timeout=3)

        if not req.ok:
            continue
    except:
        continue

    type = ""

    if ".jpg" in url or ".jpeg" in url:
        type = ".jpg"
    elif ".png" in url:
        type = ".png"
    else:
        continue

    if int(img["height"]) < height or int(img["width"]) < width:
        continue

    f.writestr(str(num_img) + type, req.content)

    num_img -= 1

f.close()
