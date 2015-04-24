# mfadtThesis

####Setup UDOO Board

Install the VNC server:

1.Open a terminal window and type:

	sudo apt-get update

	sudo apt-get install tightvncserver

2. Run the server:

	vncserver :1 -geometry 800x600 -depth 24

3. Make the server run on every boot:

	sudo nano /etc/rc.local

The document will open on your terminal window, using your keyboard keys go to the line just before "exit0" and type:

	vncserver :1 -geometry 800x600 -depth 24 &

4. Before any further step, we will configure the udoo to have a STATIC IP Address. This in order to ensure the wireless connection to the local network. For the local network I'm using a linksis wireless router with a hidden network. To configure the udoo IP do the following:

	4.1 Go to Menu>Preferences>Network Connections

	4.2 Select the Wireless tab
	
	4.3 with your network name highlighted, click on EDIT

	4.4 go to the IPV4 tab and change from automatic to manual

	4.5 Finally Add a new IP Address(What ever address you want to assign to the udoo), a NETMASK (usually 255.255.255.0) and your GATEWAY(router's IP)

	4.6 Save your changes...

To remotly control your UDOO board you will need to install a VNC client. For windows and Mac I recomend REALVNC.
For linux xvncviewer. To install in linux go to your terminal and type:

	sudo apt-get install xvnc4viewer

To use the client from a linux computer type:

	sudo xvncviewer

Then just type your UDOO's ip followed by the port (replace udoo.ip.address with your udoo's ip address, the port remains the same):

	udoo.ip.address:5901

####Run a python script using foreverjs

	forever start -c python python_script.py

Stopping forever

	forever stopall

####htop process monitoring

	sudo apt-get install htop

to run the application type:

	htop

To filter processes to match only python scripts. Press the f4 key and in the text bar type: .py 

####PyPy