import socket

def discover_host(ip):

    try:

        hostname = socket.gethostbyaddr(ip)[0]

        return {
            "ip": ip,
            "hostname": hostname
        }

    except:

        return {
            "ip": ip,
            "hostname": "Unknown"
        }