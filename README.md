# Image Superresolution

## Deployment as an API


Create a `superresolution_data` folder in the parent directory of this repository with two folders, `inputs` and `outputs`. Place the images to enhance in `inputs`. 

Clone the repository 

`cd model-api`

Build the docker image

`sudo docker build . --no-cache`

If successful, a docker image should be created with a certain id. To see the id of all your docker images run `sudo docker images`.

Run the container in interactive mode and mounting as a volume a directory of the host machine to the `superresolution_data` folder in the container. Use the image id obtained before

`sudo docker run -p 127.0.0.1:5050:5050/tcp -v /home/jcejudo/superresolution_data:/superresolution_data <your_image_id_here>`


Client command line tool 

The command line tool takes the path of an input image and the path of the enhanced file for the output. 


`python client.py --input ../superresolution_data/inputs/[ph]2048087[ph]ProvidedCHO_British_Museum_and_The_Portable_Antiquities_Scheme_YORYM_FFFA17.jpg --output ../superresolution_data/outputs/enhanced_img.jpg` 








cd model-api

sudo docker build .

sudo docker run -p 127.0.0.1:5050:5050/tcp -v /home/jcejudo/superresolution_data:/superresolution_data 69b57eda397d 

python client.py --input ../superresolution_data/inputs/[ph]2048087[ph]ProvidedCHO_British_Museum_and_The_Portable_Antiquities_Scheme_YORYM_FFFA17.jpg --output ../superresolution_data/outputs/enhanced_img.jpg


# Harvesting data

`conda create --name sr_env`

`conda activate sr_env`

Install dependencies

`pip install -r requirements.txt`

Harvest images from different tiers

`python harvesting.py --n_images_per_tier 10 --saving_path /home/jcejudo/projects/super_resolution/data/data.csv`

Download images

`python download.py --saving_dir /home/jcejudo/projects/super_resolution/data/images --input /home/jcejudo/projects/super_resolution/data/data.csv`

Apply superresolution

`python apply_model.py --input // --output //`
