import base64
import subprocess
import pickle


class Smplifyx :
    def __init__(self, image, gender):

        self.image = base64.b64decode(image)
        self.gender = gender
        self.texture = ''
        self.betas = []
        self.recommendation = []

        with open("../scripts/images/img.png", "wb") as fh:
            fh.write(self.image)

    def get_betas(self):
        self.betas = [0,0,0,0,0,0,0,0]

        shellscript = subprocess.Popen(["../scripts/make_body_model.sh"], shell=True,  stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = shellscript.communicate()
        # print('logs...',output)
        # print('errors...',error)

        with open('../scripts/output/results/img/000.pkl', 'rb') as f:
            betas = pickle.load(f)['betas'][0]
            betas_new = [str(n) for n in betas]

            self.betas = betas_new
            print('.................................',type(betas_new), betas_new, list(betas_new))

        shellscript.wait()
        return self.betas

    def get_texture(self):
        with open("./assets/sample_texture.jpg", "rb") as imageFile:
            self.texture = str(base64.b64encode(imageFile.read()))
        return self.texture

    def get_recommendation(self):
        self.recommendation = [1,2,3,4,5]
        return self.recommendation
