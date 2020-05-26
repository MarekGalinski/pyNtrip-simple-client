# Simple Python3 NTRIP client
This is a very simple code that connects to the NTRIP server with given credentials and mountpoint, and receives the the TCP stream of the RTCM messages.

After receiving the RTCM messages via TCP, script writes the RTCM data to serial line, thus giving the data to connected ublox module, that receives higher precision when having these data available.

The code is based on https://github.com/tridge/pyUblox/blob/master/ntrip.py, but the original code was for Python2 and without some modifications was unable to run with Python3.

Also, the original code contains some references to other libs of the whole pyUblox repository. This code removes all these references, so it can be used as a minimalistic stand-alone script.

More about NTRIP: https://gssc.esa.int/wp-content/uploads/2018/07/NtripDocumentation.pdf 
More about RTCMv3: http://www.geopp.com/pdf/gppigs06\_rtcm\_f.pdf

The code is provided as is, feel free to do whatever you want.
