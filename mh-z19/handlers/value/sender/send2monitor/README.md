# Send value to the MONITOR™

## prerequirements
[pip install error-counter](https://pypi.org/project/error-counter/)

## settings
A .ini file named ***send2monitor.ini*** on the same directory of this module is used to solve settings.

### send2monitor.ini
- [valueid]
  - value : value_id of MONITOR™ related to value. For exameple, co2=abcdefg

- [server]
  - url: MONITOR™ server url. Basically, no need to change.

- [error_recovery]
  - recover_on:  true or false, indicate do error recovery or not.
  - counterfile: file path to use error count

## how to use
```bash:
python -m pondslder --sensor_handlers ***somethin_sensor_handlers*** --value_handlers send2monitor
```

send2monitor.ini file should be the same directory with ***send2monitor*** module.
