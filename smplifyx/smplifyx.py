import base64
import subprocess

class Smplifyx :
    def __init__(self, image, gender):
        self.image = image
        self.gender = gender
        self.texture = ''
        self.betas = []
        self.recommendation = []

    def get_betas(self):
        self.betas = [0,0,0,0,0,0,0,0]
        with open('../scripts/make_body_model.sh', 'w') as f:
            f.write('#!/bin/sh\nexit 0')
        shellscript = subprocess.Popen(["../scripts/make_body_model.sh"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        shellscript.stdin.write("yes\n")
        shellscript.stdin.close()
        returncode = shellscript.wait()
        print('ooooooooooooooooooooooooooooooooooooooooooooo',returncode)
        return self.betas

    def get_texture(self):
        with open("./assets/sample_texture.jpg", "rb") as imageFile:
            self.texture = str(base64.b64encode(imageFile.read()))
        return self.texture

    def get_recommendation(self):
        self.recommendation = [1,2,3,4,5]
        return self.recommendation
