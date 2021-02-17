import sys
from order_processer import OrderProcesser, WebSiteOrderProcesser, FileOrderProcesser

def main(argv) :

    fromFile = False
    path = "http://research.cs.queensu.ca/home/cords2/timOrders.txt"

    if len(argv) > 1 :
        fromFile, path = True, argv[2] if argv[1] == "-f" and len(argv) > 2 else False, argv[2] if len(argv) > 2 else False, path #Way to configure program via launch parameters
        # Key -f means commands will be loaded from file
        # Next should be specified file path (otherwise -f will be ignored), or url

    processer : OrderProcesser = FileOrderProcesser(path) if fromFile else WebSiteOrderProcesser(path)
    processer.process()

if __name__ == "__main__" :
    main(sys.argv)