# Image Superresolution

## Deployment

Clone the current repository in a certain directory of your machine. Create a `superresolution_data` folder in this directory. The `superresolution_data` folder can have an `inputs` and `outputs` folders. Place the images to enhance in `inputs`. Change the directory to the `model-api` folder of this repository and build the docker image:

`sudo docker build . --no-cache`

If successful, a docker image should be created with a certain id. To see the id of all your docker images run `sudo docker images`. Run the container mounting the `superresolution_data` directory previously created as a volume, and mapping the port 5050

`sudo docker run -p 127.0.0.1:5050:5050/tcp -v /home/jcejudo/superresolution_data:/superresolution_data <your_image_id_here>`

The model api should run now in `http://0.0.0.0:5050/srapi`, and it accepts POST requests with a json body `{'input':'path/to/input','output':'path/to/output'}` containing the input path for the low-resolution image and the output path for the enhanced version. We can call the api with the client command line tool, which takes the input and output paths as arguments. 

`python client.py --input ../superresolution_data/inputs/[ph]2048087[ph]ProvidedCHO_British_Museum_and_The_Portable_Antiquities_Scheme_YORYM_FFFA17.jpg --output ../superresolution_data/outputs/enhanced_img.jpg` 



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
