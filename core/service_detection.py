SERVICES = {
    21:"FTP",
    22:"SSH",
    25:"SMTP",
    53:"DNS",
    80:"HTTP",
    110:"POP3",
    143:"IMAP",
    443:"HTTPS"
}

def detect_services(ports):

    data = []

    for port in ports:

        data.append({
            "port": port,
            "service": SERVICES.get(port,"Unknown")
        })

    return data