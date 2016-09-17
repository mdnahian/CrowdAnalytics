import cv2
from flask import Flask, url_for, send_from_directory
import httplib, urllib, base64

app = Flask(__name__)

@app.route("/")
def api():

    camera = cv2.VideoCapture(0)

    for i in xrange(5):
        retval, im = camera.read()

    retval, im = camera.read()
    camera_capture = im
    file = "static/img/crowd.jpg"
    cv2.imwrite(file, camera_capture)

    headers = {
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '30664545c0d84b75aaff1b0d883bc9a9',
    }

    params = urllib.urlencode({
    })

    url = "http://e487f3cb.ngrok.io"+url_for('static', filename='img/crowd.jpg')
    print url

    data = ''

    try:
        conn = httplib.HTTPSConnection('api.projectoxford.ai')
        conn.request("POST", "/emotion/v1.0/recognize?%s" % params, '{ "url": "'+url+'" }', headers)
        response = conn.getresponse()
        data = response.read()
        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))

    return data


@app.route('/img/<filename>')
def uploaded_file(filename):
    return send_from_directory('img/', filename)

if __name__ == "__main__":
    app.run()
