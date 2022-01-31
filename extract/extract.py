import re


def extract(filename):
    '''
        Summary line.
        Extract ips using Regular Expression

        Parameters
        ----------
        filename : str
        This is the filename of the text file.

        Returns
        -------
        Return all the ips extracted from the txt file
        '''

    try:
        input_file = open(filename, 'r')
        input_content = input_file.read()
        ips = re.findall('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', input_content)
        return ips
    except:
        print("File cannot be opened", filename)


if __name__ == "__main":
    file_name = "list_of_ips.txt"
    ips = extract(file_name)
