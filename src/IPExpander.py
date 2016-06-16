class IPRange:
    def __init__(self, iprange):
        """ Initializes a list of IP addressed based on a formatted string """
        self.iprange = iprange
        self.octets = []
        self.ip_list = []

        octets = iprange.split('.')
        for octet in octets:
            expanded = octet.split('-')
            if len(expanded) == 1:
                self.octets.append(expanded)
            else:
                initial = int(expanded[0])
                end = int(expanded[-1]) + 1
                ips = list(range(initial, end))
                self.octets.append(ips)
        size = 1
        ip_list = []
        for octet in self.octets:
            size *= len(octet)
        i = 0
        while i < size:
            ip_list.append('')
            ip_list[i] += (str(self.octets[0][i % len(self.octets[0])]))
            ip_list[i] += ('.')
            ip_list[i] += (str(self.octets[1][i % len(self.octets[1])]))
            ip_list[i] += ('.')
            ip_list[i] += (str(self.octets[2][i % len(self.octets[2])]))
            ip_list[i] += ('.')
            ip_list[i] += (str(self.octets[3][i % len(self.octets[3])]))
            i += 1
        self.ip_list = ip_list

    def newlineSeparated():
        """ Returns all the IPs in the list, separeated by newlines """
        retstr = ''
        for ip in self.ip_list:
            retstr += ip
            retstr += '\n'
        return retstr



# TODO Remove
print(IPRange("10.10.10-20.9").ip_list)
