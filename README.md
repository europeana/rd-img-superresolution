# Image Superresolution

## Deployment as Command Line Interface

Build the docker image

`sudo docker build . --no-cache`

If successful, a docker image should be created with a certain id. To see the id of all your docker images run `sudo docker images`.

The command line tool takes the path of an input image and the path of the enhanced file for the output. Create a `superresolution_data` folder with two folders, `inputs` and `outputs`. Place the images to enhance in `inputs`. 

Run the container in interactive mode and mounting as a volume a directory of the host machine to the `superresolution_data` folder in the container. Use the image id obtained before at the end of the command

`sudo docker run -it -v /some/local/path/superresolution_data:/superresolution_data <your_image_id_here>`

Once you are in the container execute the following command to enhance an image:

`python3 apply_model.py --input ../superresolution_data/inputs/[ph]2048087[ph]ProvidedCHO_British_Museum_and_The_Portable_Antiquities_Scheme_YORYM_FFFA17.jpg --output ../superresolution_data/outputs/enhanced_image.jpg`


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
