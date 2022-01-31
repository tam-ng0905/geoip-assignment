import argparse


def input_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", action='store', dest='filename', default="list_of_ips.txt", help='set list_of_ips.txt')

    # store in variable results
    result = parser.parse_args()
    # return result
    return result


if __name__ == "__main__":
    input_args()
