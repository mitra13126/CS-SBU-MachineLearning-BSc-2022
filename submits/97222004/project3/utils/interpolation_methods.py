def linear_interpolation(data, config):
    if config['time'] == 'daily':
        data = data.set_index('time')
        data = data.resample('D')
        data = data.interpolate(method=config['interpolation'])
        data.reset_index(inplace=True)

    elif config['time'] == 'monthly':
        data = data.set_index('time')
        data = data.resample('M')
        data = data.interpolate(method=config['interpolation'])
        data.reset_index(inplace=True)

    elif config['time'] == 'weekly':
        data = data.set_index('time')
        data = data.resample('W')
        data = data.interpolate(method=config['interpolation'])
        data.reset_index(inplace=True)

    elif config['time'] == 'hour':
        data = data.set_index('time')
        data = data.resample('H')
        data = data.interpolate(method=config['interpolation'])
        data.reset_index(inplace=True)

    elif config['time'] == 'minute':
        data = data.set_index('time')
        data = data.resample('T')
        data = data.interpolate(method=config['interpolation'])
        data.reset_index(inplace=True)

    else:
        data = None

    return data
