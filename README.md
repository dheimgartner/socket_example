# Asked chat gpt about sockets

> Not full package: You could finalize the package structrue and add a post-install script 
in order to automatically add the service to systemd. But this should be enough to get the
big picture.

Create a new file in the `~/.config/systemd/daniehei/` directory with the .service extension, for example, `socket_exmaple.service`.

Open the file in a text editor and add the following information:

```
[Unit]
Description=Socket example

[Service]
ExecStart=/home/daniehei/github/socket_example/env/bin/python3 /home/daniehe
i/github/socket_example/src/socket_example/example_socket.py
Restart=always

[Install]
WantedBy=default.target
```

Save the file and run the following commands to reload the systemd configuration and start the process:

```
systemctl --user daemon-reload
systemctl --user start socket_example
```

To enable the process to start at boot time, run:

```
systemctl enable socket_example
```

You can check the status of the service by running systemctl status myprocess.
You can monitor the process e.g. with `htop`.
Run `pgrep socket_example`.

Open a browser and enter `yourhost:12345`

Aks chat gpt the following:

"Say I have a python package that has the functionality of establishing a socket  
that listens on a port. How can I implement that a process running this functionality 
is added to systemd if the user installs my package with pip?"
