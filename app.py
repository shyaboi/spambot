import autopy
import random
import time




haxArr = ["you've been targeted by 1337 haax", "haxing in progress", "rad brad", "HAXXXXXXXXXXXXXX", "https://i.ytimg.com/vi/KEkrWRHCDQU/maxresdefault.jpg", "https://i.kym-cdn.com/entries/icons/original/000/021/807/ig9OoyenpxqdCQyABmOQBZDI0duHk2QZZmWg2Hxd4ro.jpg", "https://i.kym-cdn.com/editorials/icons/mobile/000/001/508/hackerman-icon.jpg", "https://i.kym-cdn.com/entries/icons/facebook/000/008/087/12611612.jpg" , "https://i.chzbgr.com/full/9066288128/h45156F75/funny-meme-about-not-being-able-to-fix-internet-heckerman-instead-of-hackerman", "https://i.redd.it/8wlaab8isi611.jpg", "https://img.memecdn.com/winrar-hacker_o_1856155.jpg", "https://i.pinimg.com/236x/7a/f6/cb/7af6cb881a9a77497a2ef5ef90a9dd8a.jpg", "https://images3.memedroid.com/images/UPLOADED68/5e2f2f4c2e55a.jpeg", "https://media1.giphy.com/media/YQitE4YNQNahy/200.gif", "https://miro.medium.com/max/1000/1*hyqJzpqML8_OsEir6KCahw.gif", "H8 M8!", "https://i.imgur.com/pzw4C8l.gif", "https://thumbs.gfycat.com/LightheartedObviousBlowfish-size_restricted.gif", "U R Lame Bra", "https://i.imgur.com/JZrUNZr.gif", "https://i.gifer.com/7U65.gif", "https://i.imgur.com/zWeHndt.gif", "https://thumbs.gfycat.com/ImpracticalUnacceptableAndeancat-size_restricted.gif", "https://memeguy.com/photos/images/hackers-the-greatest-gif-i-have-ever-seen-79086.gif", "https://i.pinimg.com/originals/c9/2f/1c/c92f1cbb5339c5de696489b4c97d4a1e.gif", "https://i.imgur.com/IvK6HKy.gif", "https://steamuserimages-a.akamaihd.net/ugc/973230653997673055/A6E91D8A5357E802A926E532DFF12188C3E81A9C/", "https://ci.memecdn.com/3138400.gif", "Me code, me script, me use bidet after take a shit",

 "So I (74M) was recently hit by a car (2014 Honda) and died. My wife (5F) organized me a funeral (cost $2747) without asking me (74M) at all. I (74M) was unable to make it because I (74M) was dead (17 days). At the funeral I heard my dad (15M) and other family members talking about how they wish I could be there and now I feel bad for not showing up. AITA?",
 
 "It was a bright day. I woke up at 3 pm after a long night of humping my Zero Two body pillow. I get out of my bed, as I get up I smell the buildup of sweat and bacteria that have built up on the mattress as I have not showered in the past 2 months. I go to the shower. I notice that my zero two body pillow is sticked on my back. Probably because of the huge amounts of cum on her. I gently remove her from my back. The cum is hard and it pulled a chunk of my back hair. After I finish showering I shave my beard very elegantly. It's beautiful... You can't tell where the beard ends and my chest hair starts. 4chan would be proud of me. I waddle my big choker body to the kitchen. I eat 69 chicken tenders (nice) with honey mussy. I take a big sip of mountain dew and waddle my elegant chungus body to my room. I go to reddit r/Aww to look at some animals as I have not gone outside in the last 2 years. I saw very cute animals, it almost made me say 'Wholesome 100' out loud. But then I saw something unimaginable. Something that has completely ruined the post, no, my whole day. I see that the title has emojis in it. I scratch my beard thinking of what I should do... I am way to intelligent to not do anything or to just move on. No. This deserves justice. I think about the current state of reddit and of it's downfal. I see flashbacks of a year ago when it was good, before the insta normies took over and normalised the use of emojis. I remember when we used to make fun of them. Thinking about how they ruined reddit for me makes me angry. But I do not want to step down to their level. I simply comment 'Reddit law requiers i downvote for excessive emoji usage'. I post my comment. Another insta normie owned. I quietly say 'based'. I am satisfied.",
 
 "Sorry for my bad english. Also I’m typing on mobile, if im make any spelling mistakes im sorry. So i was browsing reddit. i did my daily deed by creating my 420th account to downvote EA’s comment about microtransactions (EPIC). and then i saw a hilarious meme about dying in a car crash on r/dankmemes. i decided to try it out. So me, being the typical redditor decided to take my wife and children with me (SPOILER, THIS WAS A MISTAKE). Not with standing, we were in the car and saw a big truck. Now i’m a fan of big trucks, let me tell you, but the driver was clearly an insta normie. We crashed into the truck going 250 mph. My wife was vaporised immediately. The car flipped 69 times (nice). Cum, everywhere. My cock and balls, tortured.", "My reddit gold, gone. r/wooosh. now you might have noticed the truck driver has uploaded this accident on r/watchpeopledie after committing 4 counts of vehicular manslaughter. This guy is a repeat offender when it comes to reposting. I could name several instances in which he reposted in r/blursedimages and r/aww. Typically he reigns in 20% karma gains as compared to the original posts. This is outrageous. But what is more outrageous is this man, this normie decides to repost on to instagram! Unforgivable! Onto his instagram account, i have noticed several posts causing me to believe he is a boomer! Not just this, but a simp! He supports the orange man and kills children! To relieve my stress after this scarring incident, I decided to donate my life savings to pokemane. Now this bitch, didn't even say my name! I cant believe this! And then, to top it all off, after uploading my cat to r/chonkers HE DIES! It was right after his 12th meal of the day, so at least he died happily. Could it be the cat food? Has anyone else experienced this? After my cat dying i asked my crush out and she said no! My wifes boyfriend called me a cuck and insulted my neckbeard. I was sad. I covered my tears with my fedora. “M’lady”, i whispered, “please forgive me, i have failed you”. After this i went onto r/pewdiepiesubmissions to defend a woman being bullied by evil men. They called me a simp, but i knew that i was actually a protector of the female gender from the patriarchy!",
 "https://media1.tenor.com/images/2646a7138a777d0902f1bf5f0ca15931/tenor.gif?itemid=9859876",
 "https://media1.tenor.com/images/4c4ed3bd62eb47ccdbb2643b695affd5/tenor.gif?itemid=4679689", 
 "https://media.tenor.com/images/b977f6d26035cee778f3a584f31bb31e/tenor.gif",
 "https://media1.tenor.com/images/d9c1b68b0c3d2a7d2c27b0eafd90f467/tenor.gif?itemid=15002672",
 "https://media1.tenor.com/images/757737201b0c4c0a46bb42bc333a64cb/tenor.gif?itemid=4606994",
 "https://media.tenor.com/images/1e37cb56c521ce4099c15ce46bd74320/tenor.gif",
 "https://media1.tenor.com/images/31625048d81a2f622043ab5cd06a3560/tenor.gif?itemid=14779987",
 "https://media.tenor.com/images/a4b2a0d6afe89274f5a0e1027c6f5880/tenor.gif",
 "https://media.tenor.com/images/c5d165a0de66399ede81b6ae6fa27efe/tenor.gif",
 "What the fuck did you just fucking say about me, you little bitch? I'll have you know I graduated top of my class in the Navy Seals, and I've been involved in numerous secret raids on Al-Quaeda, and I have over 300 confirmed kills. I am trained in gorilla warfare and I'm the top sniper in the entire US armed forces. You are nothing to me but just another target. I will wipe you the fuck out with precision the likes of which has never been seen before on this Earth, mark my fucking words. You think you can get away with saying that shit to me over the Internet? Think again, fucker. As we speak I am contacting my secret network of spies across the USA and your IP is being traced right now so you better prepare for the storm, maggot. The storm that wipes out the pathetic little thing you call your life. You're fucking dead, kid. I can be anywhere, anytime, and I can kill you in over seven hundred ways, and that's just with my bare hands. Not only am I extensively trained in unarmed combat, but I have access to the entire arsenal of the United States Marine Corps and I will use it to its full extent to wipe your miserable ass off the face of the continent, you little shit. If only you could have known what unholy retribution your little 'clever' comment was about to bring down upon you, maybe you would have held your fucking tongue. But you couldn't, you didn't, and now you're paying the price, you goddamn idiot. I will shit fury all over you and you will drown in it. You're fucking dead, kiddo."
  ]




def teeeee():
    morRando = [5345,453,435,45,343543,45354,3543,543,433,54354,43543,534,643,6464,46,346364,63464364,453453543,345,543,54354543,543,45543543,435667,34767,8538,548,85,4854,85435,835,45,8358,583,583,85,58,73,58,583,588,537,583,8558,585,8558,235,28,52,589,668,259,82,28,9929,5879,80,4058,86,375,34,45,76,486,59,76,85,3467]

    okay = random.choice(morRando)

    donus = [f"Sorry I am testing a spam bot.{okay}..This is a test of the emergency spambot system. Do not attemt to stop spambot. Kappa Kappa Kappa Kappa ",
     f"trash{okay}", f"What the fuck did you just fucking say about me, you little bitch? I'll have you know I graduated top of my class in the Navy Seals, and I've been involved in numerou{okay}s", 
     f"confirmed kills. I am trained in gorilla warfare and I'm the top sniper in the entire US armed forces.",
      f"maybe you would have held your fucking tongue. But you couldn't, you didn't,", 
      f"and now you're paying the price, you goddamn idiot. I will shit fury all over you and you will drown in it. You're fucking dead,{okay} kiddo.", 
      f"and I have over {okay} confirmed kills. I am trained in gorilla warfare and I'm the top sniper in the entire US armed forces.", 
      f"What the fuck did you just fucking say about me, you little bitch? I'll have you know I graduated top of my class in the Navy Seals, and I've {okay}", 
      f"been involved in numerous secret raids on Al-Quaeda, and I have over {okay} confirmed kills.", 
      f"mark my fucking words. You think you can get away with saying that shit to me over the{okay} Internet? Think again fucker.",
      f" As we speak I am contacting my secret network of spies across the USA and your IP {okay} is being traced right now so you better prepare for the storm, maggot.", 
      f"Sorry I am testing a spam bot.{okay}..This is a test of the emergency spambot system. Do not attemt to stop spambot. Kappa Kappa Kappa Kappa ",
       f"Sorry I am testing a spam bot.{okay}..This is a test of the emergency spambot system. Do not attemt to stop spambot. Kappa Kappa Kappa Kappa ",
       f"Sorry I am testing a spam bot.{okay}..This is a test of the emergency spambot system. Do not attemt to stop spambot. Kappa Kappa Kappa Kappa ",
       f"Sorry I am testing a spam bot.{okay}..This is a test of the emergency spambot system. Do not attemt to stop spambot. Kappa Kappa Kappa Kappa ",
       f"Sorry I am testing a spam bot.{okay}..This is a test of the emergency spambot system. Do not attemt to stop spambot. Kappa Kappa Kappa Kappa "]
    timeout = random.randrange(15)
    time.sleep(timeout)
    ok = random.choice(donus)
    autopy.key.type_string(ok, wpm=6000)
    autopy.key.tap(autopy.key.Code.RETURN)
    # autopy.key.tap(autopy.key.Code.TAB, [autopy.key.Modifier.ALT])
    teeeee()

def reeee():

    for _ in range(20):
        # dinu = random.choice(haxArr)
    # print(dinu)
        autopy.key.type_string(ok, wpm=1000)
        autopy.key.tap(autopy.key.Code.RETURN)

    # autopy.key.type_string("```diff", wpm=4000)
    # autopy.key.tap(autopy.key.Code.RETURN, [autopy.key.Modifier.SHIFT])
    # autopy.key.type_string("~Coded by,", wpm=4000)
    # autopy.key.tap(autopy.key.Code.RETURN, [autopy.key.Modifier.SHIFT])
    # autopy.key.type_string("-The Dingus Crew-", wpm=4000)
    # autopy.key.tap(autopy.key.Code.RETURN, [autopy.key.Modifier.SHIFT])
    # autopy.key.type_string("```", wpm=4000)

    autopy.key.tap(autopy.key.Code.RETURN)


inpoot = input("do you want to reee?")
if inpoot == "y":
    autopy.key.tap(autopy.key.Code.TAB, [autopy.key.Modifier.ALT])
    time.sleep(2)
    teeeee()
