# Jig automation library

This library is designed to control the Thorlabs KST101 Step motor controller to automate the stretching jig. 

## Usage

Simply import the jig.py module and initialise it 

```python
import jig
jig.init()
# Or if you have a different port do
# jig.init("/dev/some_port")

# some code

# remember to close the port
jig.closePort()
```

## Dependencies

- Python 3
- Pyserial

*NOTE: Since Python 3 is used, you need to run all the scripts using python3. For example run*

```
$ python3 test.py
```

### Location of the datasheet
https://www.thorlabs.com/Software/Motion%20Control/APT_Communications_Protocol.pdf