## Hentet fra https://github.com/MikeDev101/cloudlink/wiki/Python-Server

# kræver nok at vi installerer cloudlink med pip
# > pip install cloudlink
# eller
# > pythom -m pip install cloudlink

# Import the server
from cloudlink import server

# Import protocols
from cloudlink.server.protocols import clpv4, scratch

# Instantiate the server object
server = server()

# Set logging level
server.logging.basicConfig(
    level=server.logging.INFO # See python's logging library for details on logging levels.
)

# Load protocols
clpv4 = clpv4(server)
scratch = scratch(server)

### Her tilføjer jeg ting...

@server.on_connect
async def on_connect(client):
    print(client, "Connected!")

@server.on_disconnect
async def on_disconnect(client):
    print(client, "Disconnected!")

@server.on_protocol_identified(schema=clpv4.schema)
async def protocol_identified(client):
    print(client, "is using protocol", clpv4.schema)

### ... slut på sørens tilføjelser

# Start the server!
server.run(ip="127.0.0.1", port=3000)

