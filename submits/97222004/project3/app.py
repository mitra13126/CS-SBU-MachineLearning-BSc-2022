from khayyam import Timezone
from flask import Flask, request
from utils.common import response_message, read_json_time_series
from utils.interpolation_methods import linear_interpolation

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def isup():
    return response_message('API is active')


@app.route('/service1', methods=['GET', 'POST'])
def interpolation():
    try:
        req = request.get_json()
        data = read_json_time_series(req['data'])
        configuration = req['config']
    except:
        return response_message(dict({"data": null}))

    if configuration['type'] == 'miladi':
        result = linear_interpolation(data, configuration)
        result = result.to_json()

    elif configuration['type'] == 'shamsi':
        result = linear_interpolation(convert_shamsi_to_miladi(req['data']), configuration)
        result = convert_miladi_to_shamsi(result).to_json()

    return response_message(dict({"data": result}))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
