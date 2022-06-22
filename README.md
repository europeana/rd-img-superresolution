# Image Superresolution

sudo docker build . --no-cache

sudo docker run -it -v /home/jcejudo/superresolution_data:/superresolution_data 93ceacebc442

python3 apply_model.py --input ../superresolution_data/inputs/[ph]2048087[ph]ProvidedCHO_British_Museum_and_The_Portable_Antiquities_Scheme_YORYM_FFFA17.jpg --output ../superresolution_data/outputs/asdfasdf.jpg 



`conda create --name sr_env`

`conda activate sr_env`

Install dependencies

`pip install -r requirements.txt`

Harvest images from different tiers

`python harvesting.py --n_images_per_tier 10 --saving_path /home/jcejudo/projects/super_resolution/data/data.csv`

Download images

`python download.py --saving_dir /home/jcejudo/projects/super_resolution/data/images --input /home/jcejudo/projects/super_resolution/data/data.csv`


Apply superresolution


python apply_model.py --input // --output //
