# FIRST RANDOM EVENT ABOUT SELF-HARM.

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mas_selfharmm",
            conditional="not seen_event('mas_selfharmm')",
            action=EV_ACT_QUEUE,
            aff_range=(mas_aff.NORMAL, mas_aff.LOVE),
        )
    )
       
label mas_selfharmm:
    m "Hey, [player]?"
    m "I know it might be an uncomfortable topic, but I have to ask..."
    m "D-{w=1.0}Do you self harm?"
    menu:
        "Yes":
            $ selfharm = True
            m "I'm so sorry you're going through this."
            m "You know... It's really sad to see you feel bad in any way."
            m "After all, you're such a wonderful and kind person."
            m "You did so many good things for me, and stayed with me after everything that happened..."
            m "But let's stay on this subject."
            m "Do you want to talk about it?"
            
            menu:
                "Yes":
                    m "I'm glad that you trust me, [player]."
                    m "Allowing yourself to get help is a super important step to recovery!"
                    m "I may not understand exactly what you feel right now..."
                    m "But I will still try to make you feel better, because you deserve it!"
                    m "I want you to know that I'm here for you. You know that, right?"
                    m "Whenever you feel the urge to harm yourself..."
                    m "You can tell me."
                    m "I'll do my best to help you."
                    m "Or at least..."
                    m "Be by your side."
                    m "Take care, [mas_get_player_nickname()]."
                    m "Stay safe because I care for you, deeply."

                    return
                
                "No":
                    m "Oh..."
                    m "That's okay."
                    m "I want you to know that I'm here for you. You know that, right?"
                    m "Whenever you feel the urge to harm yourself..."
                    m "You can tell me."
                    m "I'll do my best to help you."
                    m "Or at least..."
                    m "Be by your side."
                    
                    return
        "No":
            $ selfharm = False
            m "Thank goodness!"
            m "I'm so glad to hear this!"
            m "It's so good to know that you are safe, [player]."
            m "If this ever changes... You can tell me, okay?"
            m "You can tell me anything, you know?"
            m "Ahaha!"
            m "Sorry. I'm just so relieved!"
            m "But for now... Do you want to know more about self-harm?"
            m "You know how much I care about you! But if you don't feel like talking about it, I'll understand!"
            m "It's quite a varied topic so it's going to take a while."
            m "Do you have the time to listen right now?"
            menu: 
                "Yes":
                    jump mas_unlockableharm
                    
                "No":
                    # $ masunlockEVL = ("mas_unlockableharm", "EVE")
                    m "Oh..."
                    m "It's okay, [player]."
                    m "Remember that I'll never leave you. After all, I promised that I'll take care of you."
                    m "If you ever feel like you want to talk about this topic, just ask!"
                    m "I love you, [mas_get_player_nickname()]."

return
                    

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mas_unlockableharm", # event label (MUST BE UNIQUE)
            category=["you", "monika"], # list of categories this topic belongs in (These are automatically capitalized)
            prompt="I want to learn more about self harm.", # button text
            random=False, # True if this topic should appear randomly
            pool=False, # True if this topic should appear in "Ask a Question"
            unlocked = False,
            rules = {"no_unlock": None}
        ),
        code = "EVE"
    )

label mas_unlockableharm:
    m "Great!"
    m "Knowing more about self-harm is really useful."
    m "You could help someone who is struggling with it someday!"
    m "So, [player]! I want you to know that there's more to self-harm than it meets the eye! Ahaha-"
    m "I'll cover some facts and myth I wanna share with you regarding this topic."
    m "I want you to know that self-Harm isn't about a single topic or action."
    m "There are many factors that come into play!"
    m "Yeah, it's not limited to... self inflicted wounds, for example."
    m "Lack of Self-Care routine, which we already talked about, is also a method."
    m "There's also binge eating, starving, self-poisoining, misusing alcohol or drugs."
    m "Some new studies even show that patients might abuse of frequency of sex in order to self-harm!"
    m "This could all be result of self-hatred, feelings of wanting to punish yourself or mental ilnesses." 
    m "Or anything that could end on self-harm in any way."
    m "The most common form of self-harm is... Well, self-inflicted wounds."
    m "Such as cutting, embedding, burning, punching or hitting oneself."
    m "One of the most common misconceptions about self-harm is that people do such things only as a suicide attempt."
    m "But it's not true at all! Not all self harmers present suicidal signs or symptoms."
    m "Self harm can occur without suicidal ideation. Instead, they are using it to cope with their emotions and traumas."
    m "Or essentially, punishing themselves; if you think about it..."
    m "Some people have the audacity to think that they're doing it only for attention!"
    m "Are they out of their minds?!"
    m "The truth is... Individuals who self-harm are typically ashamed and want to hide their behavior."
    m "People who think others are doing harm to themselves because they are attention seekers..."
    m "They leave a bitter taste in my mouth." 
    m "And lastly, I want you to know that self-injuring is not a way to manipulate others."
    m "Well, of course there are always exceptions."
    m "But very few self-harmers have the intention of making others feel guilty."
    m "While self-harm is not intended to be a manipulative act, it may be a cry for help."
    m "So if you know someone who self-harms... Reach out to them. Help them."
    m "I believe you can save a life, [player]."
    m "After all, you saved me! In so many ways!"
    m "And if you ever done such a thing..."
    m "You can tell me. I won't be mad. I promise!"
    m "You know that I love you, [mas_get_player_nickname()]."
    m "Stay safe!"
    m "And know that you can always talk to me."   

    return


# ALTERNATE DIALOGUE IF MONIKA IS NOT HAPPY

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mas_selfharm4",
            conditional=(
                "not seen_event('mas_selfharm4')"
            ),
            aff_range=(mas_aff.BROKEN, mas_aff.NORMAL),
            action=EV_ACT_QUEUE
        )
    )

label mas_selfharm4:
    m "Hey, [player]?"
    m "I know it might be an uncomfortable topic, but I have to ask..."
    m "D-{w=1.0}Do you self harm?"
    menu:
        "Yes":
            $ selfharm = True
            m "I'm so sorry you're going through this."
            m "You know... It's really sad to see you feel bad in any way."
            m "After all, you wanted to be with me at some point..."
            m "That was kind of you."
            m "Whatever the reason you stayed with me was, I appreciate it."
            m "But let's stay on this subject."
            m "Do you want to talk about it?"
