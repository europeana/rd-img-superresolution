# Image Superresolution

Install dependencies

`pip install -r requirements.txt`

Harvest images from different tiers

`python harvesting.py --n_images_per_tier 10 --saving_path /home/jcejudo/projects/super_resolution/data/data.csv`

Download images

`python download.py --saving_dir /home/jcejudo/projects/super_resolution/data/images --input /home/jcejudo/projects/super_resolution/data/data.csv`


Apply superresolution


