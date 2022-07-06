import requests
import fire

class SuperResAPI():
    def __init__(self,url):
        self.url = url
    def enhance(self,input,output):
        response = requests.post(self.url,json = {'input':input,'output':output})
        return response
         
def main(**kwargs):
    input = kwargs.get('input')
    output = kwargs.get('output')

    api = SuperResAPI(f"http://0.0.0.0:5050/srapi")
    response = api.enhance(input,output)
    print(response)
    return 

if __name__ == '__main__':
    fire.Fire(main)




