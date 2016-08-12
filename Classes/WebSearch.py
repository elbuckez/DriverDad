import mechanize, sys, bs4, re

class WebSearch():
    
    def __init__( self, website_address, start_point, destination ):
        self.time_to_destination = 0
        self.distance = 0
        self.website_address = website_address
        self.start_point = start_point
        self.destination = destination
        self.is_connected = False
    
    def test( self ):
        if 1 < 2:
            self.is_connected = True
        else:
            self.is_connected = False
            
    def get_data( self ):
        if ( self.is_connected ):
            br = mechanize.Browser()
            br.open( self.website_address )
            assert br.viewing_html()
            br.select_form( name = "routeForm" )
            br.form[ 'destText-1' ] = self.start_point
            br.form[ 'destText-2' ] = self.destination
            br.submit()
            print( br.form )
            resp = None
        else:
            assert "THERE IS NO INTERNET CONNECTION"
       
        
        


test = WebSearch( 'www.rac.co.uk/route-planner', 'Folkestone', 'Dover' )
test.test()
test.get_data()

