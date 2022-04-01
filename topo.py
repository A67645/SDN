from mininet.topo import Topo

class MyTopo(Topo):

    def __init__( self ):

        Topo.__init__( self )

        host1 = self.addHost('h1', ip='10.0.0.2/24', mac='aa:aa:aa:aa:aa:aa')
        host2 = self.addHost('h2', ip='10.0.0.3/24', mac='bb:bb:bb:bb:bb:bb')
        host3 = self.addHost('h3', ip='10.0.0.4/24', mac='cc:cc:cc:cc:cc:cc')
        host4 = self.addHost('h4', ip='10.0.0.5/24', mac='dd:dd:dd:dd:dd:dd')

        switchL2 = self.addSwitch('s1')

        link1 = self.addLink(host1, switchL2)
        link2 = self.addLink(host2, switchL2)
        link3 = self.addLink(host3, switchL2)
        link4 = self.addLink(host4, switchL2)

topos = {'mytopo': (lambda: MyTopo())}


