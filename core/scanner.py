import socket

COMMON_PORTS = [
    21,22,25,53,
    80,110,143,443
]

def scan_ports(target):

    results = []

    try:

        socket.gethostbyname(target)

    except socket.gaierror:

        print(f"Invalid Host: {target}")

        return []

    for port in COMMON_PORTS:

        try:

            sock = socket.socket(
                socket.AF_INET,
                socket.SOCK_STREAM
            )

            sock.settimeout(1)

            result = sock.connect_ex(
                (target, port)
            )

            if result == 0:

                results.append(port)

            sock.close()

        except:

            pass

    return results