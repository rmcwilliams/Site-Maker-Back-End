from Precompiler import *
from NetworkCrafter import *
from MultiNetwork import *

if __name__ == "__main__":
    site = Site(0,0,0,0)
    #PreChanges: 3:40
    net = NetworkCrafter.generateNetworks("Data/OneidaFlowSimplified.json")
    print("Hey!")
    # pSNA(net,SiteID(1001,9999,None))
    # DataIO.networkToCSV(net,"C:\\Users\\mpanozzo\\Documents\\SITE_TABLE.csv","C:\\Users\\mpanozzo\\Documents\\FLOW_TABLE.csv")
    # t = test.TestPrecompiler()
    # t.create_files(net)
    # Visualizer.create_visuals("hello")
