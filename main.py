def on_on_zero(status):
    game.game_over(False)
statusbars.on_zero(StatusBarKind.health, on_on_zero)

def on_overlap_tile(sprite, location):
    tiles.set_current_tilemap(tilemap("""
        level4
        """))
    tiles.place_on_random_tile(mySprite, sprites.dungeon.collectible_insignia)
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.stair_large,
    on_overlap_tile)

def on_overlap_tile2(sprite2, location2):
    scene.camera_shake(4, 500)
    tiles.set_current_tilemap(tilemap("""
        level3
        """))
    tiles.place_on_random_tile(mySprite, sprites.dungeon.collectible_insignia)
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.door_open_north,
    on_overlap_tile2)

myMinimap: Sprite = None
mySprite2: Sprite = None
mySprite: Sprite = None
mySprite = sprites.create(img("""
        . . . . . . . . . . b 5 b . . .
        . . . . . . . . . b 5 b . . . .
        . . . . . . . . . b c . . . . .
        . . . . . . b b b b b b . . . .
        . . . . . b b 5 5 5 5 5 b . . .
        . . . . b b 5 d 1 f 5 5 d f . .
        . . . . b 5 5 1 f f 5 d 4 c . .
        . . . . b 5 5 d f b d d 4 4 . .
        b d d d b b d 5 5 5 4 4 4 4 4 b
        b b d 5 5 5 b 5 5 4 4 4 4 4 b .
        b d c 5 5 5 5 d 5 5 5 5 5 b . .
        c d d c d 5 5 b 5 5 5 5 5 5 b .
        c b d d c c b 5 5 5 5 5 5 5 b .
        . c d d d d d d 5 5 5 5 5 d b .
        . . c b d d d d d 5 5 5 b b . .
        . . . c c c c c c c c b b . . .
        """),
    SpriteKind.player)
tiles.set_current_tilemap(tilemap("""
    level2
    """))
tiles.place_on_random_tile(mySprite, sprites.dungeon.collectible_insignia)
info.set_life(3)
scene.camera_follow_sprite(mySprite)
controller.move_sprite(mySprite)
characterAnimations.loop_frames(mySprite,
    [img("""
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . b 5 5 b . . .
            . . . . . . b b b b b b . . . .
            . . . . . b b 5 5 5 5 5 b . . .
            . b b b b b 5 5 5 5 5 5 5 b . .
            . b d 5 b 5 5 5 5 5 5 5 5 b . .
            . . b 5 5 b 5 d 1 f 5 d 4 f . .
            . . b d 5 5 b 1 f f 5 4 4 c . .
            b b d b 5 5 5 d f b 4 4 4 4 b .
            b d d c d 5 5 b 5 4 4 4 4 4 4 b
            c d d d c c b 5 5 5 5 5 5 5 b .
            c b d d d d d 5 5 5 5 5 5 5 b .
            . c d d d d d d 5 5 5 5 5 d b .
            . . c b d d d d d 5 5 5 b b . .
            . . . c c c c c c c c b b . . .
            """),
        img("""
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . b 5 b . . .
            . . . . . . . . . b 5 b . . . .
            . . . . . . b b b b b b . . . .
            . . . . . b b 5 5 5 5 5 b . . .
            . b b b b b 5 5 5 5 5 5 5 b . .
            . b d 5 b 5 5 5 5 5 5 5 5 b . .
            . . b 5 5 b 5 d 1 f 5 d 4 f . .
            . . b d 5 5 b 1 f f 5 4 4 c . .
            b b d b 5 5 5 d f b 4 4 4 4 4 b
            b d d c d 5 5 b 5 4 4 4 4 4 b .
            c d d d c c b 5 5 5 5 5 5 5 b .
            c b d d d d d 5 5 5 5 5 5 5 b .
            . c d d d d d d 5 5 5 5 5 d b .
            . . c b d d d d d 5 5 5 b b . .
            . . . c c c c c c c c b b . . .
            """),
        img("""
            . . . . . . . . . . b 5 b . . .
            . . . . . . . . . b 5 b . . . .
            . . . . . . . . . b c . . . . .
            . . . . . . b b b b b b . . . .
            . . . . . b b 5 5 5 5 5 b . . .
            . . . . b b 5 d 1 f 5 5 d f . .
            . . . . b 5 5 1 f f 5 d 4 c . .
            . . . . b 5 5 d f b d d 4 4 . .
            b d d d b b d 5 5 5 4 4 4 4 4 b
            b b d 5 5 5 b 5 5 4 4 4 4 4 b .
            b d c 5 5 5 5 d 5 5 5 5 5 b . .
            c d d c d 5 5 b 5 5 5 5 5 5 b .
            c b d d c c b 5 5 5 5 5 5 5 b .
            . c d d d d d d 5 5 5 5 5 d b .
            . . c b d d d d d 5 5 5 b b . .
            . . . c c c c c c c c b b . . .
            """),
        img("""
            . . . . . . . . . . b 5 b . . .
            . . . . . . . . . b 5 b . . . .
            . . . . . . b b b b b b . . . .
            . . . . . b b 5 5 5 5 5 b . . .
            . . . . b b 5 d 1 f 5 d 4 c . .
            . . . . b 5 5 1 f f d d 4 4 4 b
            . . . . b 5 5 d f b 4 4 4 4 b .
            . . . b d 5 5 5 5 4 4 4 4 b . .
            . . b d d 5 5 5 5 5 5 5 5 b . .
            . b d d d d 5 5 5 5 5 5 5 5 b .
            b d d d b b b 5 5 5 5 5 5 5 b .
            c d d b 5 5 d c 5 5 5 5 5 5 b .
            c b b d 5 d c d 5 5 5 5 5 5 b .
            . b 5 5 b c d d 5 5 5 5 5 d b .
            b b c c c d d d d 5 5 5 b b . .
            . . . c c c c c c c c b b . . .
            """),
        img("""
            . . . . . . . . . . b 5 b . . .
            . . . . . . . . . b 5 b . . . .
            . . . . . . b b b b b b . . . .
            . . . . . b b 5 5 5 5 5 b . . .
            . . . . b b 5 d 1 f 5 d 4 c . .
            . . . . b 5 5 1 f f d d 4 4 4 b
            . . . . b 5 5 d f b 4 4 4 4 b .
            . . . b d 5 5 5 5 4 4 4 4 b . .
            . b b d d d 5 5 5 5 5 5 5 b . .
            b d d d b b b 5 5 5 5 5 5 5 b .
            c d d b 5 5 d c 5 5 5 5 5 5 b .
            c b b d 5 d c d 5 5 5 5 5 5 b .
            c b 5 5 b c d d 5 5 5 5 5 5 b .
            b b c c c d d d 5 5 5 5 5 d b .
            . . . . c c d d d 5 5 5 b b . .
            . . . . . . c c c c c b b . . .
            """),
        img("""
            . . . . . . . . . . b 5 b . . .
            . . . . . . . . . b 5 b . . . .
            . . . . . . b b b b b b . . . .
            . . . . . b b 5 5 5 5 5 b . . .
            . . . . b b 5 d 1 f 5 5 d f . .
            . . . . b 5 5 1 f f 5 d 4 c . .
            . . . . b 5 5 d f b d d 4 4 . .
            . b b b d 5 5 5 5 5 4 4 4 4 4 b
            b d d d b b d 5 5 4 4 4 4 4 b .
            b b d 5 5 5 b 5 5 5 5 5 5 b . .
            c d c 5 5 5 5 d 5 5 5 5 5 5 b .
            c b d c d 5 5 b 5 5 5 5 5 5 b .
            . c d d c c b d 5 5 5 5 5 d b .
            . . c b d d d d d 5 5 5 b b . .
            . . . c c c c c c c c b b . . .
            . . . . . . . . . . . . . . . .
            """)],
    100,
    characterAnimations.rule(Predicate.FACING_RIGHT, Predicate.MOVING_RIGHT))
characterAnimations.loop_frames(mySprite,
    [img("""
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . b 5 5 b . . . . . . . . .
            . . . . b b b b b b . . . . . .
            . . . b 5 5 5 5 5 b b . . . . .
            . . b 5 5 5 5 5 5 5 b b b b b .
            . . b 5 5 5 5 5 5 5 5 b 5 d b .
            . . f 4 d 5 f 1 d 5 b 5 5 b . .
            . . c 4 4 5 f f 1 b 5 5 d b . .
            . b 4 4 4 4 b f d 5 5 5 b d b b
            b 4 4 4 4 4 4 5 b 5 5 d c d d b
            . b 5 5 5 5 5 5 5 b c c d d d c
            . b 5 5 5 5 5 5 5 d d d d d b c
            . b d 5 5 5 5 5 d d d d d d c .
            . . b b 5 5 5 d d d d d b c . .
            . . . b b c c c c c c c c . . .
            """),
        img("""
            . . . . . . . . . . . . . . . .
            . . . b 5 b . . . . . . . . . .
            . . . . b 5 b . . . . . . . . .
            . . . . b b b b b b . . . . . .
            . . . b 5 5 5 5 5 b b . . . . .
            . . b 5 5 5 5 5 5 5 b b b b b .
            . . b 5 5 5 5 5 5 5 5 b 5 d b .
            . . f 4 d 5 f 1 d 5 b 5 5 b . .
            . . c 4 4 5 f f 1 b 5 5 d b . .
            b 4 4 4 4 4 b f d 5 5 5 b d b b
            . b 4 4 4 4 4 5 b 5 5 d c d d b
            . b 5 5 5 5 5 5 5 b c c d d d c
            . b 5 5 5 5 5 5 5 d d d d d b c
            . b d 5 5 5 5 5 d d d d d d c .
            . . b b 5 5 5 d d d d d b c . .
            . . . b b c c c c c c c c . . .
            """),
        img("""
            . . . b 5 b . . . . . . . . . .
            . . . . b 5 b . . . . . . . . .
            . . . . . c b . . . . . . . . .
            . . . . b b b b b b . . . . . .
            . . . b 5 5 5 5 5 b b . . . . .
            . . f d 5 5 f 1 d 5 b b . . . .
            . . c 4 d 5 f f 1 5 5 b . . . .
            . . 4 4 d d b f d 5 5 b . . . .
            b 4 4 4 4 4 5 5 5 d b b d d d b
            . b 4 4 4 4 4 5 5 b 5 5 5 d b b
            . . b 5 5 5 5 5 d 5 5 5 5 c d b
            . b 5 5 5 5 5 5 b 5 5 d c d d c
            . b 5 5 5 5 5 5 5 b c c d d b c
            . b d 5 5 5 5 5 d d d d d d c .
            . . b b 5 5 5 d d d d d b c . .
            . . . b b c c c c c c c c . . .
            """),
        img("""
            . . . b 5 b . . . . . . . . . .
            . . . . b 5 b . . . . . . . . .
            . . . . b b b b b b . . . . . .
            . . . b 5 5 5 5 5 b b . . . . .
            . . c 4 d 5 f 1 d 5 b b . . . .
            b 4 4 4 d d f f 1 5 5 b . . . .
            . b 4 4 4 4 b f d 5 5 b . . . .
            . . b 4 4 4 4 5 5 5 5 d b . . .
            . . b 5 5 5 5 5 5 5 5 d d b . .
            . b 5 5 5 5 5 5 5 5 d d d d b .
            . b 5 5 5 5 5 5 5 b b b d d d b
            . b 5 5 5 5 5 5 c d 5 5 b d d c
            . b 5 5 5 5 5 5 d c d 5 d b b c
            . b d 5 5 5 5 5 d d c b 5 5 b .
            . . b b 5 5 5 d d d d c c c b b
            . . . b b c c c c c c c c . . .
            """),
        img("""
            . . . b 5 b . . . . . . . . . .
            . . . . b 5 b . . . . . . . . .
            . . . . b b b b b b . . . . . .
            . . . b 5 5 5 5 5 b b . . . . .
            . . c 4 d 5 f 1 d 5 b b . . . .
            b 4 4 4 d d f f 1 5 5 b . . . .
            . b 4 4 4 4 b f d 5 5 b . . . .
            . . b 4 4 4 4 5 5 5 5 d b . . .
            . . b 5 5 5 5 5 5 5 d d d b b .
            . b 5 5 5 5 5 5 5 b b b d d d b
            . b 5 5 5 5 5 5 c d 5 5 b d d c
            . b 5 5 5 5 5 5 d c d 5 d b b c
            . b 5 5 5 5 5 5 d d c b 5 5 b c
            . b d 5 5 5 5 5 d d d c c c b b
            . . b b 5 5 5 d d d c c . . . .
            . . . b b c c c c c . . . . . .
            """),
        img("""
            . . . b 5 b . . . . . . . . . .
            . . . . b 5 b . . . . . . . . .
            . . . . b b b b b b . . . . . .
            . . . b 5 5 5 5 5 b b . . . . .
            . . f d 5 5 f 1 d 5 b b . . . .
            . . c 4 d 5 f f 1 5 5 b . . . .
            . . 4 4 d d b f d 5 5 b . . . .
            b 4 4 4 4 4 5 5 5 5 5 d b b b .
            . b 4 4 4 4 4 5 5 d b b d d d b
            . . b 5 5 5 5 5 5 b 5 5 5 d b b
            . b 5 5 5 5 5 5 d 5 5 5 5 c d c
            . b 5 5 5 5 5 5 b 5 5 d c d b c
            . b d 5 5 5 5 5 d b c c d d c .
            . . b b 5 5 5 d d d d d b c . .
            . . . b b c c c c c c c c . . .
            . . . . . . . . . . . . . . . .
            """)],
    100,
    characterAnimations.rule(Predicate.MOVING_LEFT, Predicate.FACING_LEFT))

def on_forever():
    global mySprite2, myMinimap
    if mySprite2.overlaps_with(mySprite) or mySprite.overlaps_with(mySprite2):
        info.change_life_by(-1)
    if myMinimap.overlaps_with(mySprite) or mySprite.overlaps_with(myMinimap):
        info.change_life_by(-1)
    mySprite2 = sprites.create(img("""
            . . . . . . . . . . . . . . . .
            . . . . . . . . c c c c . . . .
            . . . . . . c c d d d d c . . .
            . . . . . c c c c c c d c . . .
            . . . . c c 4 4 4 4 d c c . . .
            . . . c 4 d 4 4 4 4 4 1 c . c c
            . . c 4 4 4 1 4 4 4 4 d 1 c 4 c
            . c 4 4 4 4 1 4 4 4 4 4 1 c 4 c
            f 4 4 4 4 4 1 4 4 4 4 4 1 4 4 f
            f 4 4 4 f 4 1 c c 4 4 4 1 f 4 f
            f 4 4 4 4 4 1 4 4 f 4 4 d f 4 f
            . f 4 4 4 4 1 c 4 f 4 d f f f f
            . . f f 4 d 4 4 f f 4 c f c . .
            . . . . f f 4 4 4 4 c d b c . .
            . . . . . . f f f f d d d c . .
            . . . . . . . . . . c c c . . .
            """),
        SpriteKind.enemy)
    tiles.place_on_tile(mySprite2, tiles.get_tile_location(5, 6))
    myMinimap = sprites.create(img("""
            . . . . . . . . . . . . . . . .
            . . . . . . . . c c c c . . . .
            . . . . . . c c d d d d c . . .
            . . . . . c c c c c c d c . . .
            . . . . c c 4 4 4 4 d c c . . .
            . . . c 4 d 4 4 4 4 4 1 c . c c
            . . c 4 4 4 1 4 4 4 4 d 1 c 4 c
            . c 4 4 4 4 1 4 4 4 4 4 1 c 4 c
            f 4 4 4 4 4 1 4 4 4 4 4 1 4 4 f
            f 4 4 4 f 4 1 c c 4 4 4 1 f 4 f
            f 4 4 4 4 4 1 4 4 f 4 4 d f 4 f
            . f 4 4 4 4 1 c 4 f 4 d f f f f
            . . f f 4 d 4 4 f f 4 c f c . .
            . . . . f f 4 4 4 4 c d b c . .
            . . . . . . f f f f d d d c . .
            . . . . . . . . . . c c c . . .
            """),
        SpriteKind.enemy)
    tiles.place_on_tile(myMinimap, tiles.get_tile_location(12, 10))
    mySprite2.follow(mySprite)
    myMinimap.follow(mySprite)
forever(on_forever)
