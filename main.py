

import argparse

import json
import requests

parser = argparse.ArgumentParser(description='Swagger/OpenAPI client generation tool',epilog='Enjoy the program!',prefix_chars='-')
parser.add_argument('client',help='Name of the client for generating client PL codebase, example: java , go , python ...',type=str)
parser.add_argument('filename',help='File location and name for generated client codebase',type=str)
parser.add_argument('specloc',help='Location of swagger/openAPI specification file',type=str)
args = parser.parse_args()


swagger_api_url = 'https://generator.swagger.io/api/gen/clients/'

def main(client,filename,spec):
    endpoint = swagger_api_url+client
    print('Url: ' + endpoint + ", Filename: " + filename + ", Specification: " + spec)
    headers = {"Content-Type": "application/json"}
    with open(spec) as swagger_spec:
        spec = json.load(swagger_spec)
        spec_params = {
            'spec':spec
        }
        with requests.post(endpoint,headers=headers,data=json.dumps(spec_params)) as resp:
            link = resp.json()
            with requests.get(link['link']) as download , open(filename,'wb') as out_file:
                out_file.write(download.content)
                print('Client: ' + client + " codebase -> generated @ " + filename)


if(args.client and args.filename and args.specloc):
    main(args.client,args.filename,args.specloc)
