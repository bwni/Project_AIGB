# Send value to the M2X

## prerequirements
[pip install error-counter](https://pypi.org/project/error-counter/)
[pip install m2x](https://pypi.org/project/m2x/)
[pip install requests](https://pypi.org/project/requests/)
[pip install iso8601](https://pypi.org/project/iso8601/)

## settings
A .ini file named ***send2m2x.ini*** on the same directory of this module is used to solve settings.

### send2m2x.ini
- [stream]
  - value: stream id of M2X™ related to value.

- [client]
	- key: API key of M2X™ related to value. At lease, PUT and GET access must be necessary.

- [device]
	- key: Device id of M2X™

- [error_recovery]
  - recover_on:  true or false, indicate do error recovery or not.
  - counterfile: file path to use error count

## how to use
```bash:
python -m pondslder --sensor_handlers ***somethin_sensor_handlers*** --value_handlers send2m2x
```

send2m2x.ini file should be the same directory with ***send2mo2x*** module.