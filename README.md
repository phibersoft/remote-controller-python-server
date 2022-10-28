## Remote Controller - Server [Python]

This is a same project as [Remote Controller - Server](https://github.com/phibersoft/remote-controller-server).
Old project was written in Typescript, RobotJS, SocketIO. We will convert the background of the project to Python for a
better experience in the coming days.

### Pre-requirements

* Python 3.6+

### Installation

```bash
    # Clone the repository
    git clone https://github.com/phibersoft/remote-controller-python-server.git
    
    # Install the dependencies
    pip install -r requirements.txt
    
    # Run the server
    python main.py
```

### Development

```bash
    main.spec - Pyinstaller configuration file
    main.py - Main file of the project
    requirements.txt - Dependencies of the project
    
    lib/error_handler.py - Error handler of the project
    lib/wifi_handler.py - Pre-wifi handler for socket connection
    lib/events/*.py - Event handlers for socket-io
```

### Contributing

I'm describing myself as a Junior in python (specially in code splitting and folder architecture). I am open to all
kinds of suggestions and contributions. I will be happy to
see your contributions.

