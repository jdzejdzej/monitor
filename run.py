from config_reader import ConfigReader
from monitor import Monitor


if __name__ == '__main__':
    config_reader = ConfigReader('config.json')
    args = config_reader.get_configurations()
    monitor = Monitor(*args)
    monitor.start()
    if not raw_input():
        monitor.cancel()
