def main( args = None ):
   if args is None:
      import sys
      args = sys.argv[ 1 : ]

   error_code = 0

   print( "Hello, world." )

   print( "Received Arguments:" )
   for index, value in enumerate( args ):
      print( "{}: {}".format( index, value ) )

   return error_code
