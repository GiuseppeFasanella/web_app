# alarm_pyro
first install pyro, following the procedure according to your OS
https://pythonhosted.org/Pyro4/install.html

Then start the name server
python3 -m Pyro4.naming  (if you run evething in different shells of the same machine)
or python3 -m Pyro4.naming -n hostname (if you use a different machine with a known hostname as server, e.g. local ip of your raspberry)

On your server (raspberry) start times.py
python times.py

And then on your client start visit.py
python visit.py

You can see that the output fed to the client is correctly sent and printed on the server side. 