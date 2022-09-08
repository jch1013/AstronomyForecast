

def get_moon_data(html):
    rise_html = html.select(".lightgreybox")[0]
    illumination_html = html.select(".lightgreybox")[2]
    moon_rise_set = rise_html.findAll(lambda tag: tag.name == 'tr')[2]
    moon_array = []
    for time in moon_rise_set:
        moon_array.append(time.text)
    rise = moon_array[3]
    apex = moon_array[5]
    sets = moon_array[7]
    illumination = illumination_html.findAll(lambda tag: tag.name == 'p')[1].text
    illumination = illumination.replace('\n', "").strip()
    return [rise, sets, apex, illumination]


def get_moon(html):
    data = get_moon_data(html)
    report = "The Moon:"
    moonrise = f'Rise time: {data[0]}'
    moonset = f'Set time: {data[1]}'
    apex = f'Apex time: {data[2]}'
    illumination = f'Illumination: {data[3]}'
    report = report + '\n' + moonrise + '\n' + moonset + '\n' + apex + '\n' + illumination + '\n'
    return report
