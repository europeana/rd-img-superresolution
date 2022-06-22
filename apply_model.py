import sys
sys.path.append('image-super-resolution')

import fire
from PIL import Image
from pathlib import Path
import numpy as np

from ISR.models import RDN, RRDN

def main(**kwargs):
    input = kwargs.get("input")
    output = kwargs.get("output")

    print(output)

    Path(output).parent.mkdir(exist_ok = True, parents = True)

    model = RDN(weights='noise-cancel')

    img = Image.open(input)

    sr_img = model.predict(np.array(img))

    sr_img = Image.fromarray(sr_img)
    sr_img.save(output)





    return

if __name__ == "__main__":
    fire.Fire(main)