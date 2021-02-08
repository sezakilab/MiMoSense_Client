from multiprocessing import Value
def init():
    global temperature, humidity, co2, air_pressure, motion, audio, uv, gps
    global temp_process, humidity_process, co2_process, air_pressure_process, motion_process, audio_process, uv_process, gps_process
    global mqtt_process_list

    temperature = Value('d',0.0)
    humidity = Value('d',0.0)
    co2 = Value('d',0.0)
    air_pressure = Value('d',0.0)
    motion = Value('d',0.0)
    audio = Value('d',0.0)
    uv = Value('d',0.0)
    gps = Value('d',0.0)

    temp_process = None
    humidity_process = None
    co2_process = None
    air_pressure_process = None
    motion_process = None
    audio_process = None
    uv_process = None
    gps_process = None

    mqtt_process_list = []
