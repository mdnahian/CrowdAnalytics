git clone https://github.com/intel-iot-devkit/mraa.git
mkdir mraa/build && cd $_
cmake .. -DBUILDSWIGNODE=OFF
make
make install
pip install Flask
cd CrowdAnalytics/
export FLASK_APP=grove.py
flask run --host=0.0.0.0