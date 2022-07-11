import requests
import argparse

class SuperResAPI():
    def __init__(self,url):
        self.url = url
    def enhance(self,input,output):
        response = requests.post(self.url,json = {'input':input,'output':output})
        return response
         
if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("--input", help="path to input image")
    parser.add_argument("--output", help="path to output image")
    args = parser.parse_args()

    api = SuperResAPI(f"http://0.0.0.0:5050/srapi")
    response = api.enhance(args.input,args.output)

    print(response)
    #print(response.request.url)
    #print(response.request.body)
    #print(response.request.headers)





