#=========auto submod update

# Register the submod
init -990 python:
    store.mas_submod_utils.Submod(
        author="Phazeee",
        name="BonkAMon",
        description="Heh. Bonk your Monika!",
        version="0.0.9",
    )

# Register the updater
init -989 python:
    if store.mas_submod_utils.isSubmodInstalled("Submod Updater Plugin"):
        store.sup_utils.SubmodUpdater(
            submod="BonkAMon",
            user_name="MrPhaze62",
            repository_name="BonkAMon",
            extraction_depth=1
        )


#==== Hey there, if you're translating. feel free to remove my auto updater above or replace it with your github page above the lines!.
#==== else you or the players from this update on will get hit with English Texts, and that'll be very confusing for everyone. oops! ;-;


#====bonk count - submod inspired by Extra+ and OpenWorld heheheheheh.

default persistant.bonk_count = [0, 0, 0]

image zonetwo = im.Scale("mod_assets/other/transparent.png", 180, 120)

#image squeakybat = "submods/BonkAMon/images/bat2.png"

#idle mode from ExtraPlus

image monika staticpose = monika_extraplus

#Chibika_bonkies. heheheh - who knows, maybe i'll add a natsuki bonk. heheh. this is not for natsu natsu niiii~
#not this update though. tis a secret.


init 5 python:

    monika_extraplus = MASMoniIdleDisp(
        (
            MASMoniIdleExp("1eua", duration=30),
            MASMoniIdleExp("1eubla", duration=30),
            MASMoniIdleExp("1hua", duration=30),
            MASMoniIdleExp("1hubsa", duration=40, aff_range=(mas_aff.ENAMORED, mas_aff.LOVE)),
            MASMoniIdleExp("1eubsa", duration=40, aff_range=(mas_aff.ENAMORED, mas_aff.LOVE)),
            MASMoniIdleExp("1eua", duration=30),
            MASMoniIdleExp("1hua", duration=30),
            MASMoniIdleExp("1eubla", duration=40, aff_range=(mas_aff.ENAMORED, mas_aff.LOVE)),
            MASMoniIdleExp("1esa", duration=30),
            MASMoniIdleExpGroup(
                [
                    MASMoniIdleExp("1eua", duration=30),
                    MASMoniIdleExp("1sua", duration=4),
                    MASMoniIdleExp("1ekblu", duration=40, aff_range=(mas_aff.ENAMORED, mas_aff.LOVE)),
                    MASMoniIdleExp("1tuu", duration=30),
                    MASMoniIdleExp("1hua", duration=30),
                ]
            ),
            MASMoniIdleExp("1eua_follow", duration=40),
            MASMoniIdleExp("1kua", duration=1),
            MASMoniIdleExp("1eua", duration=30),
            MASMoniIdleExp("1mubla", duration=30, aff_range=(mas_aff.ENAMORED, mas_aff.LOVE)),
            MASMoniIdleExp("1eubsa", duration=40, aff_range=(mas_aff.ENAMORED, mas_aff.LOVE)),
            MASMoniIdleExp("1huu", duration=30),
        )
    )


init 5 python:
    def bonk_submenu():
        renpy.call_screen("bonk_menu")

init 10001:
    screen mas_extramenu_area():
        zorder 52
        key "e" action Jump("mas_extra_menu_close")
        key "E" action Jump("mas_extra_menu_close")

        frame:
            area(0, 0, 1280, 720)
            background Solid("#0000007F")
            textbutton _("Close"):
                    area (60, 596, 120, 35)
                    style "hkb_button"
                    action Jump("mas_extra_menu_close")
                # zoom control
        frame:
            area (195, 450, 80, 255)
            style "mas_extra_menu_frame"
            vbox:
                spacing 2
                label "Zoom":
                    text_style "mas_extra_menu_label_text"
                    xalign 0.5
                textbutton _("Reset"):
                        style "mas_adjustable_button"
                        selected False
                        xsize 72
                        ysize 35
                        xalign 0.3
                        action SetField(store.mas_sprites, "zoom_level", store.mas_sprites.default_zoom_level)
                bar value FieldValue(store.mas_sprites, "zoom_level", store.mas_sprites.max_zoom):
                    style "mas_adjust_vbar"
                    xalign 0.5
                $ store.mas_sprites.adjust_zoom()
        if store.mas_submod_utils.isSubmodInstalled("Open World"):
                frame:
                    area (310, 639, 202, 65)
                    style "mas_extra_menu_frame"
                    if persistent._mas_in_idle_mode == True:
                        textbutton ("Open World"):
                            xalign 0.5
                            yalign 0.5
                            action NullAction()
                    else:
                        textbutton ("Open World"):
                            xalign 0.5
                            yalign 0.5
                            action [Hide("mas_extramenu_area"), Jump("view_OW")] hover_sound gui.hover_sound
                frame:        
                    area (520, 639, 202, 65)
                    style "mas_extra_menu_frame"
                    if persistent._mas_in_idle_mode == True:
                        textbutton ("Bonk Monika"):
                            xalign 0.5
                            yalign 0.5
                            action NullAction()
                    else:
                        textbutton ("Bonk Monika"):
                            xalign 0.5
                            yalign 0.5
                            action [Hide("mas_extramenu_area"), Jump("view_bonkmenu")] hover_sound gui.hover_sound           
        else:
            frame:
                area (308, 639, 202, 65)
                style "mas_extra_menu_frame"
                if persistent._mas_in_idle_mode == True:
                    textbutton ("Bonk Monika"):
                        xalign 0.5
                        yalign 0.5
                        action NullAction()
                else:
                    textbutton ("Bonk Monika"):
                        xalign 0.5
                        yalign 0.5
                        action [Hide("mas_extramenu_area"), Jump("view_bonkmenu")] hover_sound gui.hover_sound

screen bonk_menu():
    zorder 50
    style_prefix "hkb"
    hbox:
        grid 2 1:
            spacing 20
            xpos 527
            ypos 534
            textbutton ("Bonk Monika!"): 
                xysize(120, None) 
                action Jump("bonk_a_mon") hover_sound gui.hover_sound
            textbutton ("Return") action Jump("mas_extra_menu_close") hover_sound gui.hover_sound
    vbox: 
        xpos 1166
        ypos 0
        textbutton ("Secret Stuff") action Jump("DevBaka") hover_sound gui.hover_sound


label view_bonkmenu:
    python:
        store.player_zoom = store.mas_sprites.zoom_level
        store.disable_zoom_button = False
        mas_RaiseShield_dlg()
        bonk_submenu()
    return


#labels land


label show_bonk_screen:
    show monika staticpose at t11
    python:
        store.disable_zoom_button = True
        store.mas_sprites.reset_zoom()
    call screen BonkMain
    return

label BonkMain:

    screen BonkMain():
        zorder 50
        vbox:
            style_prefix "check"
            xpos 1000
            yanchor 1.0
            ypos 260
            label _("Interactions\navailable:")
            text _("Head") outlines [(2, "#808080", 0, 0)]

        vbox:
            style_prefix "hkb"
            xpos 0.05
            yanchor 1.0
            ypos 90

            #textbutton ("Close") style "hkb_button" action [Hide("extra_gen_list"), Jump("close_boop_screen")]
            textbutton ("Return") style "hkb_button" action [Hide("extra_gen_list"), Jump("zoomfixreturn")]
        #add "submods/BonkAMon/images/bat2.png" xpos 100 ypos 100
        #transform:
        #   zoom 0.1
        imagebutton idle "zonetwo":
            xpos 550 ypos 10
            action [Hide("submod_interactions"), Jump("BonkTime")]
    return


label bonk_a_mon:

    m "..."
    m 6eksdlb "Is... That a squeaky bat, [player]?"
    m 4rtsdld "Ahaha.... What are you going to do with that?"
    jump show_bonk_screen

    return

label BonkTime:
    $ persistant.bonk_count[1] += 1
    if persistant.bonk_count[1] == 1:
        m 2efp "Ow! Did you just... bonk me on the head!?"
        m 4tuu "Guess I'll just wack you back!"
    elif persistant.bonk_count[1] == 2:
        m 6lfsdrp "Gah! [player]!"
        m 5tsa "... You must be enjoying this huh?"
    elif persistant.bonk_count[1] == 3:
        m 2dfbsa "Ow! I hope you're prepared for twice the pain once I cross over [player]!"
    elif persistant.bonk_count[1] == 4:
        m 6lfp "AH! [player], I'll get my revenge on you."
        m 3nfu "You'd better watch out!"
    elif persistant.bonk_count[1] == 5:
        m 4wfp "Ow! How can one squeaky hammer do so much damage??"
        m 2gsp "This shouldn't even be possible..."
    elif persistant.bonk_count[1] == 6:
        m 6rtbsu "..."
        m 2ltbfp "..."
        m 3tubfa "Oh... Just wondering if I should buy a larger bat..."
        m 5hubfb "Just kidding!"
    elif persistant.bonk_count[1] == 7:
        m 4wub "Just Monika!"
        m 2hksdla "Ahaha~ No idea why I said that out loud..."
        m 5eubfa "But I'm special enough for your love~!"
    elif persistant.bonk_count[1] == 8:
        m 6hub "Awee~ Stop!"
    else:
        $ moldable_variable = renpy.random.randint(1,10)
        if moldable_variable == 1:
            m 7lfblt "Ow! Keep this up and I'll keep your files hostage..."
            m 6tkblu "Just kidding [player]! I'll never do something like that."
        elif moldable_variable == 2:
            m 2kksdla "*bonk* *bonk* *bonk*"
            m 7ksb "What a child you are, [player]... But I love that about you!"
        elif moldable_variable == 3:
            m 6tut "Are you secretly... Sadistic, [player]?"
            m 5eua "Just kidding!"
        elif moldable_variable == 4:
            m 1tkbfb "OW! ... I guess someone really wants to get hit on, huh?"
            m 7tkbfu "I just hope you don't regret it, [player]"
        elif moldable_variable == 5:
            m 6wfb "Hey!"
        elif moldable_variable == 6:
            m 2tua "It must feel nice for you to hit me in the head huh?"
        elif moldable_variable == 7:
            m 3eua "Is wacking me on the head is your way of showing affection to me, [player]?"
            $ _history_list.pop()
            menu:
                m "Is wacking me on the head is your way of showing affection to me, [player]?{fast}"
                "Yes":
                    m 4eub "If so, I welcome it!"
                    m 5efu "Just don't be so surpised if I end up doing the same to you~!"
                "No":
                    m 6wfo "..."
                    m 4wfo "So mean, [player], I guess I should do the same to you out of pure annoyance!"
                    m 4wuu "..."
                    m 5tsu "Ahaha~! As if I would get hurt over something little as this."
                    m 7tsu "It just means that you care about me enough to do it!"
                    m 1tsb "How affectionate you are, [player]! Ahahah~"
        elif moldable_variable == 8:
            show screen tear(20, 0.1, 0.1, 0, 40)
            pause 1
            play sound "sfx/s_kill_glitch1.ogg"
            pause 0.2
            stop sound
            hide screen tear
            m 6wusdld "OW! I think you nearly broke the game, [player]!"
            m 4rusdlc "That squeaky hammer seriously has too much power..."
            m 2gsp "It shouldn't even be possible..."
            m 2eksdlc "Maybe you should be more careful of wacking me, [player]"
            m 1eua "But I'm okay if you're wondering!"
            m 3eub "Who knows, Maybe that squaky hammer could break down the walls for me to cross over to your reality [player]!"
            m 3rksdra "Ahah~ What am I talking about? As if that hammer could..."
        elif moldable_variable == 9:
            m 7cua "I'm so gonna snatch that bat away from you, [player]!"
            m 5kub "Just kidding!"
        elif moldable_variable == 10 and store.mas_submod_utils.isSubmodInstalled("Open World"):
            #if persistant.bonk_count[1] == 15:
            m 4wkb "Careful [player]! I don't want your ridiculous squeaky hammer to break my wonderful world you've restored!"
            m 3hksdlu "I dread to find out what would happen if you missed my head, my world unstable as it is!"
            m 3gsb "Who knows, maybe Yun would find a way to block how powerful that hammer is."

    jump show_bonk_screen
    return

label MainGaem:
    show monika staticpose at t11
    jump ch30_loop
    return

label DevBaka:

    "Huh... Bonk a yun... I feel that's a reference somewhere..."

    jump ch30_loop
    return



label zoomfixreturn:
    python:
        store.mas_sprites.zoom_level = store.player_zoom
        store.mas_sprites.adjust_zoom()
        mas_HKBDropShield()
    jump ch30_loop
    return
