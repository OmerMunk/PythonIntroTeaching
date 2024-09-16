from flask import jsonify



def simple_generator(limit):
    limit = limit*2
    while limit > 0:
        yield limit
        limit -= 1


my_generator = simple_generator(1_000_000)


def get_3():
    print(next(my_generator))
    print(next(my_generator))
    print(next(my_generator))


def read_very_ahu_shiling_large_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line


@app.route('/get_line')
def get_line():
    return jsonify(read_very_ahu_shiling_large_file())





