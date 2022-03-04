from flask import Flask, render_template, request
import requests
from utilites import getMovie
import json

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def home():
	if request.method == 'GET':
		return render_template('index.html')

	if request.method == 'POST':
		searchMovie = request.form['searchmovies']
		searchData = getMovie(searchMovie)

		with open('searchData.json', 'w') as f:
			json.dump(searchData, f)

		try:
			with open("searchData.json") as file:
				searchData = json.load(file)

				print("data has been successfully retrieved.")
		except json.decoder.JSONDecodeError:
			print("There was a problem accessing the data.")
			
		url = "https://qr-generator.qrcode.studio/qr/custom"
		QRload = {"data":'http://www.omdbapi.com/?s=%s&apikey=36921cd1' % searchMovie,
			"config":{"body":"square","eye":"frame13","eyeBall":"ball14","erf1":[],"erf2":[],"erf3":[],"brf1":[],"brf2":[],"brf3":[],"bodyColor":"#000000","bgColor":"#FFFFFF","eye1Color":"#021326","eye2Color":"#021326","eye3Color":"#021326","eyeBall1Color":"#074f03","eyeBall2Color":"#074f03","eyeBall3Color":"#074f03","gradientColor1":"#12a637","gradientColor2":"#0b509e","gradientType":"linear","gradientOnEyes":"true","logo":"","logoMode":"default"},"size":1000,"download":"imageUrl","file":"png"}

		resp = requests.post(url , json=QRload)
		print(f'this is response: {resp.status_code}') ##############

		if resp.status_code == 200 :
			print(f'enter if, this is response: {resp}') ############
			Output = resp.json()
			print(f'this is output: {Output}')
			Link = Output.get('imageUrl')
			Link = "http:" + Link
			print("Image Download Link : ",Link)
			response = requests.get(Link)
			file = open("SearchResultQR.png", "wb")
			file.write(response.content)
			file.close()

		return render_template('index.html', data=searchData)
	return render_template('index.html')


if __name__ == '__main__':
	app.run(debug=True)
