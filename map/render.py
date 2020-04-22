import pytmx, pygame

def hexToColour( hash_colour ):
    red   = int( hash_colour[1:3], 16 )
    green = int( hash_colour[3:5], 16 )
    blue  = int( hash_colour[5:7], 16 )
    return ( red, green, blue )

def renderWholeTMXMapToSurface( tmx_map ):
    width  = tmx_map.tilewidth  * tmx_map.width
    height = tmx_map.tileheight * tmx_map.height

    # This surface could be huge
    surface = pygame.Surface( ( width, height ) )

    # Some maps define a base-colour, if so, fill the background with it
    if ( tmx_map.background_color ):
        colour = tmx_map.background_color
        if ( type( colour ) == str and colour[0].startswith( '#' ) ):
            colour = hexToColour( colour )
            surface.fill( colour )
        else:
            print( "ERROR: Background-colour of [" + str( colour ) + "] not handled" )

    # For every layer defined in the map
    for layer in tmx_map.visible_layers:
        # if the Layer is a grid of tiles
        if ( isinstance( layer, pytmx.TiledTileLayer ) ):
            for x, y, gid in layer:
                tile_bitmap = tmx_map.get_tile_image_by_gid(gid)
                if ( tile_bitmap ):
                    surface.blit( tile_bitmap, ( x * tmx_map.tilewidth, y * tmx_map.tileheight ) )
        # if the Layer is a big(?) image
        elif ( isinstance( layer, pytmx.TiledImageLayer ) ):
            image = get_tile_image_by_gid( layer.gid )
            if ( image ):
                surface.blit( image, ( 0, 0 ) )
        # Layer is a tiled group (woah!)
        elif ( isinstance( layer, pytmx.TiledObjectGroup ) ):
            print( "ERROR: Object Group not handled" )

    return surface

def loadTMX(path):
    tmx_map = pytmx.load_pygame(path, pixelalpha=True)
    return renderWholeTMXMapToSurface(tmx_map)