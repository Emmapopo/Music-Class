import sqlite3

conn = sqlite3.connect('musicdb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Music')
cur.execute('CREATE TABLE Music (id INT, title VARCHAR(50), artist_name VARCHAR(200), lyrics TEXT, duration VARCHAR(5))')
cur.execute('''INSERT INTO Music VALUES (1, 'what would i change it to', 'Avicii', "Steady yourself even though you know that you're falling
Maybe you're falling but you're still alive
Ready yourself, that's quite enough of your bawling
'Cause baby you're bawling but you'll survive
Ooh, ooh-ooh, ooh-ooh-ooh, ooh-ooh-ooh-ooh
And losing is only a sign
It's only a sign that you really tried, really tried
Losing is only a sign
It's only a sign that you really tried, really tried
Forever trading places with the same old me
I'm racking up the cases of who I failed to be
Why would I replace the sky?
Why would I recreate that perfect blue?
What would I change it to?
Oh, won't you tell me?
What would I change it to?
Oh, won't you tell me?
What would I change it to?
Ooh, ooh-ooh, ooh-ooh-ooh, ooh-ooh-ooh-ooh
Ooh, ooh-ooh, ooh-ooh-ooh, ooh-ooh-ooh-ooh… ", '3:07')''')

cur.execute('''INSERT INTO Music VALUES (2, 'wake me up', 'Avicii', "Feeling my way through the darkness
Guided by a beating heart
I can't tell where the journey will end
But I know where to start
They tell me I'm too young to understand
They say I'm caught up in a dream
Well, life will pass me by if I don't open up my eyes
Well, that's fine by me
So wake me up when it's all over
When I'm wiser and I'm older
All this time I was finding myself, and I
Didn't know I was lost
So wake me up when it's all over
When I'm wiser and I'm older
All this time I was finding myself, and I
Didn't know I was lostI tried carrying the weight of the world
But I only have two hands
Hope I get the chance to travel the world
But I don't have any plans
Wish that I could stay forever this young
Not afraid to close my eyes
Life's a game made for everyone
And love is the prize
So wake me up when it's all over
When I'm wiser and I'm older
All this time I was finding myself, and I
Didn't know I was lost
So wake me up when it's all over
When I'm wiser and I'm older
All this time I was finding myself, and I
I didn't know I was lost
I didn't know I was lost
I didn't know I was lost
I didn't know I was lost
I didn't know, didn't know, didn't know", '4:33')''')

cur.execute('''INSERT INTO Music VALUES (3, 'on my way', 'Alan Walker', "I'm sorry but
Don't wanna talk, I need a moment before I go
It's nothing personal
I draw the blinds
They don't need to see me cry
'Cause even if they understand
They don't understand
So then when I'm finished
I'm all 'bout my business and ready to save the world
I'm taking my misery
Make it my bitch; can't be everyone's favorite girl
So take aim and fire away
I've never been so wide awake
No, nobody but me can keep me safe
And I'm on my way
The blood moon is on the rise
The fire burning in my eyes
No, nobody but me can keep me safe
And I'm on my way
Lo siento mucho (Farru), pero me voy (Eh)
Porque a tu lado me di cuenta que nada soy (Eh-ey)
Y me cansé de luchar y de guerrear en vano
De estar en la línea de fuego y de meter la mano
Acepto mis errore', también soy… ", '3:37')''')

cur.execute('''INSERT INTO Music VALUES (4, 'speechless', 'Michael Jackson', "Your love is magical, that's how I feel
But I have not the words here to explain
Gone is the grace for expressions of passion
But there are worlds and worlds of ways to explain
To tell you how I feel
But I am speechless, speechless
That's how you make me feel
Though I'm with you I am far away and nothing is for real
When I'm with you I am lost for words, I don't know what to say
My head's spinning like a carousel, so silently I pray
Helpless and hopeless, that's how I feel inside
Nothing's real, but all is possible if God is on my side
When I'm with you I am in the light where I cannot be found
It's as though I am standing in the place called Hallowed Ground
Speechless, speechless, that's how you make me feel
Though I'm with you I am far away and nothing is for real
I'll go anywhere and do anything just to touch your face
There's no mountain high I cannot climb
I'm humbled in your grace
Speechless, speechless, that's how you make me feel
Though I'm with you I am lost for words and nothing is for real
Speechless, speechless, that's how you make me feel
Though I'm with you I am far away, and nothing is for real
Speechless, speechless, that's how you make me feel
Though I'm with you I am lost for words and nothing is for real
Speechless your love is magical, that's how I feel
But in your presence I am lost for words
Words like, 'I love you'", '3:20')''')

cur.execute('''INSERT INTO Music VALUES (5, 'wagon wheel', 'Darius Rucker', "Heading down south to the land of the pines
I'm thumbing my way into North Caroline
Staring up the road and pray to God I see headlights
I made it down the coast in seventeen hours
Picking me a bouquet of dogwood flowers
And I'm a-hopin' for Raleigh, I can see my baby tonight
So rock me momma like a wagon wheel
Rock me momma any way you feel
Hey, momma rock me
Rock me momma like the wind and the rain
Rock me momma like a south bound train
Hey, momma rock me
I'm running from the cold up in New England
I was born to be a fiddler in an old time string band
My baby plays a guitar, I pick a banjo now
Oh, north country winters keep a-getting me down
Lost my money playing poker so I had to leave town
But I ain't turning back to living that old life no more
So rock me momma like a wagon wheel
Rock me momma any way you feel
Hey, momma rock me
Hey, rock me momma like the wind and the rain
Rock me momma like a south bound train
Hey, momma rock me
Walkin' to the south out of Roanoke
Caught a trucker out of Philly had a nice long toke
But he's a heading west from the Cumberland gap
To Johnson City, Tennessee
And I gotta get a move on before the sun
I hear my baby calling my name and I know that she's the only one
And if I die in Raleigh at least I will die free
So rock me momma like a wagon wheel
Rock me momma any way you feel
Hey, momma rock me
Oh, rock me momma like the wind and the rain
Rock me momma like a south bound train
Hey momma rock me
Oh, so rock me momma like a wagon wheel
Rock me momma any way you feel
Hey, momma rock me (mama rock me, mama rock me)
Rock me momma like the wind and the rain
Rock me momma like a south bound train
Hey, ey yeah momma rock me (you can rock me, rock me)", '5:47')''')

cur.execute('''INSERT INTO Music VALUES (6, 'way maker', 'Sinach', "You are here
Moving in our midst
I worship you
I worship you
You are here
Working in this place
I worship you
I worship you
You are here
Moving in our midst
I worship you
I worship you
You are here
Working in this place
I worship you
I worship you
Way maker
Miracle worker
Promise keeper
Light in the darkness
My God
That is who you are
Way maker
Miracle worker
Promise keeper
Light in the darkness
My God
That is who you are
You are here
Touching every heart
I worship you
I worship you
You are here
Healing every heart
I worship you
I worship you
You are here
Turning lives around
I worship you
I worship you
You are here
Mending every heart
I worship you
I worship you
Way maker
Miracle worker
Promise keeper
Light in the darkness
That is who you are
Way maker
Miracle worker
Promise keeper
Light in the darkness
My God
That is who you are
You wipe away all tears
You mend the broken heart
You're the answer to it all
Jesus
You wipe away all tears
You mend the broken heart
You're the answer to it all (to it all)
Jesus
Way maker
Miracle worker
Promise keeper
Light in the darkness
My God
That is who you are
Way maker
Miracle worker
Promise keeper
Light in the darkness
My God
That is who you are
You are here
Touching every life
I worship you
I worship you
You are here
Meeting every need
I worship you
I worship you", '5:06')''')

cur.execute('''INSERT INTO Music VALUES (7, 'uptown funk', 'Mark Ronson', "This hit, that ice cold
Michelle Pfeiffer, that white gold
This one for them hood girls
Them good girls straight masterpieces
Stylin', wilin', livin' it up in the city
Got Chucks on with Saint Laurent
Gotta kiss myself, I'm so pretty
I'm too hot (hot damn)
Called a police and a fireman
I'm too hot (hot damn)
Make a dragon wanna retire man
I'm too hot (hot damn)
Say my name you know who I am
I'm too hot (hot damn)
And my band 'bout that money, break it down
Girls hit your hallelujah (whoo)
Girls hit your hallelujah (whoo)
Girls hit your hallelujah (whoo)
'Cause uptown funk gon' give it to you
'Cause uptown funk gon' give it to you
'Cause uptown funk gon' give it to you
Saturday night and we in the spot
Don't believe me just watch (come on)
Don't believe me just watch uh
Don't believe me just watch
Don't believe me just watch
Don't believe me just watch
Don't believe me just watch
Hey, hey, hey, oh
Stop, wait a minute
Fill my cup, put some liquor in it
Take a sip, sign a check
Julio, get the stretch
Ride to Harlem, Hollywood
Jackson, Mississippi
If we show up, we gon' show out
Smoother than a fresh jar of Skippy
I'm too hot (hot damn)
Called a police and a fireman
I'm too hot (hot damn)
Make a dragon wanna retire man
I'm too hot (hot damn)
Bitch say my name you know who I am
I'm too hot (hot damn)
Am I bad 'bout that money
Break it down
Girls hit your hallelujah (whoo)
Girls hit your hallelujah (whoo)
Girls hit your hallelujah (whoo)
'Cause uptown funk gon' give it to you
'Cause uptown funk gon' give it to you
'Cause uptown funk gon' give it to you
Saturday night and we in the spot
Don't believe me just watch (come on)
Don't believe me just watch uh
Don't believe me just watch uh
Don't believe me just watch uh
Don't believe me just watch
Don't believe me just watch
Hey, hey, hey, oh
Before we leave
Lemmi tell y'all a lil' something
Uptown funk you up
Uptown funk you up
Uptown funk you up
Uptown funk you up uh
I said uptown funk you up
Uptown funk you up
Uptown funk you up
Uptown funk you up
Come on, dance, jump on it
If you sexy then flaunt it
If you freaky then own it
Don't brag about it, come show me
Come on, dance
Jump on it
If you sexy then flaunt it
Well it's Saturday night and we in the spot
Don't believe me just watch come on!
Don't believe me just watch uh
Don't believe me just watch uh
Don't believe me just watch uh
Don't believe me just watch
Don't believe me just watch
Hey, hey, hey, oh
Uptown funk you up
Uptown funk you up (say what?)
Uptown funk you up
Uptown funk you up
Uptown funk you up
Uptown funk you up (say what?)
Uptown funk you up
Uptown funk you up
Uptown funk you up
Uptown funk you up (say what?)
Uptown funk you up
Uptown funk you up
Uptown funk you up
Uptown funk you up (say what?)
Uptown funk you up", '4:31')''')

cur.execute('''INSERT INTO Music VALUES (8, 'say something', 'A Great Big World', "Say something, I'm giving up on you
I'll be the one, if you want me to
Anywhere, I would've followed you
Say something, I'm giving up on you
And I am feeling so small
It was over my head
I know nothing at all
And I will stumble and fall
I'm still learning to love
Just starting to crawl
Say something, I'm giving up on you
I'm sorry that I couldn't get to you
Anywhere, I would've followed you
Say something, I'm giving up on you
And I will swallow my pride
You're the one that I love
And I'm saying goodbye
Say something, I'm giving up on you
And I'm sorry that I couldn't get to you
And anywhere, I would have followed you
Oh, oh, oh, oh say something, I'm giving up on you
Say something, I'm giving up on you
Say something", '3:52')''')

cur.execute('''INSERT INTO Music VALUES (9, 'brown skin girl', 'Beyounce', "Brown skin girl
Your skin just like pearls
The best thing in the world
Never trade you for anybody else
Singin' brown skin girl
Your skin just like pearls
The best thing in the world
I never trade you for anybody else, singin'
She said she really grew up poor like me
Don't believe in nothin' but the Almighty
Just a likkle jeans and a pure white tee
She never did forever be nobody wifey, yeah
So while I may not pretty boy, your heart is amiss
Play it like a villain 'cause she caught in a wave
Tonight I am walkin' away
9 to 5 mind, on the grind, yeah, yeah
Tonight I might fall in love, dependin' on how you hold me
I'm glad that I'm calmin' down, can't let no one come control me
Keep dancin' and call it love, she fightin' but fallin' slowly
If ever you are in doubt, remember what mama told me
Brown skin girl, ya skin just like pearls
Your back against the world
I never trade you for anybody else, say
Brown skin girl, ya skin just like pearls
The best thing inna di world
I never trade you for anybody else, say
Pose like a trophy when Naomis walk in
She need an Oscar for that pretty dark skin
Pretty like Lupita when the cameras close in
Drip broke the levee when my Kellys roll in
I think tonight she might braid her braids
Melanin too dark to throw her shade
She minds her business and wines her waist
Gold like 24k, okay
Tonight I might fall in love, dependin' on how you hold me
I'm glad that I'm calmin' down, can't let no one come control me
Keep dancin' and call it love, she fightin' but fallin' slowly
If ever you are in doubt, remember what mama told me
Brown skin girl, ya skin just like pearls
Your back against the world
I never trade you for anybody else, say
Brown skin girl, ya skin just like pearls
The best thing inna di (about the) world
I never trade you for anybody else, say
Oh, have you looked in the mirror lately? (lately)
Wish you could trade eyes with me ('cause)
There's complexities in complexion
But your skin, it glow like diamonds
Dig me like the earth, you be giving birth
Took everything in life, baby, know your worth
I love everything about you, from your nappy curls
To every single curve, your body natural
Same skin that was broken be the same skin takin' over
Most things out of focus, view
But when you're in the room, they notice you (notice you)
'Cause you're beautiful
Yeah, you're beautiful
The men dem gon' fall in love
With you and all of your glory
Your skin is not only dark, it shines and it tells your story
Keep dancin', they can't control you
They watchin', they all adore you
If ever you are in doubt, remember what mama told you
Brown skin girl (brown skin girl)
Ya skin just like pearls (brown skin girl)
Your back against the world (oh)
I never trade you for anybody else, say (no, no)
Brown skin girl (brown skin girl)
Ya skin just like pearls (brown skin)
The best thing in all the world
I never trade you for anybody else, say
Brown skin girl
Your skin just like pearls
The best thing in the world
I never trade you for anybody else, singin'", '4:10')''')

cur.execute('''INSERT INTO Music VALUES (10, 'blow my mind', 'Davido', "Never waste your time, never let you go
Talk down, back-to-back, you're the best I know
Oh yeah, you dey blow my mind
Blow my mind, blow my mind
For your love, I go change my life
Change my life, change my life (yeah)
Ye gba, come here do your dance make I spend ego
Dutty whine, dutty whine for me nice and slow
So many nights I dey wait for my time
To get you all alone for one night
You do me somethin' no lie I go mad for your touch
I want to do you whatever you want
Freaky, freaky for you
Show me what you're into
Girl, you just dey blow my, blow my mind
Blow my mind (yeah, yeah)
Your body dey blow my, blow my mind
Blow my mind
Girl, you just dey blow my, blow my mind
Blow my mind
Your body dey blow my, blow my mind
Blow my mind
Yeah, yeah ('fore you go, I go)
Yeah, yeah ('fore you go, I go)
Ah, ah (we go rendezvous)
Ah, ah (make we rendezvous)
Ah, ah (we go rendezvous)
Ah, ah (make we rendezvous)
When I drink from your water, give me a cup
I ain't just wanna sip
I'm tryna steal your love, I'm guilty of it
I don't give a shit
About who tellin' all our business when I'm killin' it, when I'm feelin it
Kissin' and it turn into an animal (whoa)
Yeah yeah, girl, I fuck with a attitude
Angry and you're dangerous
It don't matter, no
'Cause your body controllin' me
It don't matter, no
And I know you see the same vision
Nobody gon' change how we livin'
Nobody gon' change how I feel about you
I want to do you, whatever you want
Freaky, freaky for you
Show me what you're into, ooh
Girl, you just dey blow my, blow my mind
Blow my mind (yeah, yeah)
Your body dey blow my, blow my mind
Blow my mind (blow my mind)
Girl, you just dey blow my, blow my mind (you, you, you, you)
Blow my mind (you, you, you, you)
Your body dey blow my, blow my mind
Blow my mind (blow my mind)
Yeah, yeah ('fore you go, I go)
Yeah, yeah ('fore you go, I go)
Ah, ah (we go rendezvous)
Ah, ah (make we rendezvous)
Ah, ah (we go rendezvous)
Ah (yeah), ah (make we rendezvous)", '3:18')''')

cur.execute('''INSERT INTO Music VALUES (11, 'no one like you', 'P-square', "Eh! Oh yie eeh eeh eeh eh
Oh yie eeh eeh eeh eh
Oh yie eeh eeh eeh eh
Oh yie eeh eeh eeh eh (No one like you)
Oh yie eeh eeh eeh eh (No one like you)
Oh yie eeh eeh eeh eh (No one like you)
Oh yie eeh eeh eeh eh
No one, no one
Hello! (Hello!)
How're you doing?
My angel, my one and only
The only one that I'm missing
Wey dey bring me joy and blessings
You know, that I love you
And I can't wait to say I do
But before we walk down the Island
I just wanna let you know that you are the finest
And you be the finest thing I've ever seen
You are the brightest
The way you shine, you bling like queen
You are the highest
When it comes to rating, you're the lead
My princess, my only one lover (eh eh eh...)
Girl, I just wanna let you know that (eh eh eh...)
No one be like you
See I've go different places, I've seen many faces
No one be like you
So they cannot replace you, cos you are a blessing
No one be like you
You're driving me crazy cos you are my baby
No one be like you.
No one
No one like you (one like you)
No one
No one like you (one like you)
No one (No one)
About a year ago
Before I met you
There was no possiblity for me to be rescued
But thank God I found you (yeah)
I cannot do without you
And since I go different places, I've seen many faces, I cannot replace you
But you add again many blessings
Girl you are my life
You are the finest
And you be the finest thing I've ever seen
You are the brightest
The way you shine, you bling like queen
You are the highest
When it comes to rating, you're the lead
My princess, my only one lover (eh eh eh.)
And, I just wanna let you know that (eh eh eh ...)
No one be like you
See I've been different places, I've seen many faces
No one be like you
So they cannot replace you cos you are a blessing
No one be like you
You're driving me crazy, cos you are my baby
No one be like you
No one
No one like you (one like you)
No one
No one like you (one like you)
That's why we say eh eh eh...
Oh yie eeh eeh eeh eh
Oh yie eeh eeh eeh eh
Oh yie eeh eeh eeh eh
Oh yie eeh eeh eeh eh (No one like you)
Oh yie eeh eeh eeh eh (No one like you)
Oh yie eeh eeh eeh eh (No one like you)
Oh yie eeh eeh eeh eh
No one
No one
Girl you're the finest
And you be the finest thing I've ever seen
The way you shine, you bling like queen
When it comes to rating, you're the lead
My princess, my only one lover
Girl, I just wanna let you know that
No one be like you
So many things
So many things (be like you)
Everything
Without you
There's no possibility
There's no positivity
Always negativity
Thank God I find you eh!
You are my everything
You are my destiny
This is reality eh
Oh yie eh
Oh yie eeh eeh
Oh yie eh
Oh yie eeh eeh
Oh yie eeh eeh eeh eh
Oh yie eeh eeh eeh eh
Oh yie eeh eeh eeh eh
Oh yie eeh eeh eeh eh
Oh yie eeh eeh eeh eh (oh yie)
Oh yie eeh eeh eeh eh (oh yie)
Oh yie eeh eeh eeh eh (oh yie)
Oh yie eeh eeh eeh eh (oh yie)
Oh yie eeh eeh eeh eh (eh eh)
Oh yie eeh eeh eeh eh (eh)
Oh yie eeh eeh eeh eh (eh)", '4:41')''')

cur.execute('''INSERT INTO Music VALUES (12, "i don't belong in this club", "Why don't we", "Some guy skipped in front of me
Can't believe I paid an entry fee
And I don't even got the energy
To smile for a selfie
And I know that I should go home
But I'm still standing here so
I guess one more for the road
I wanna raise a toast so
This one's for the sparklers
Dudes wearing shades in the darkness
But hats off to the DJ
Same song twice in an evening (1, 2,3)
Oh, save me (Save me), can't take it (Take it)
I don't belong in this club
One dance (One dance), no chance (No chance)
'Cause I'm feeling awkward as (Oh)
I was waiting in line for an hour
Just to get in now, I wanna get out 'cause (Oh)
I'm jaded (I'm jaded), can't fake it (Can't fake it)
I don't belong in this club, no
Hopped out of the Uber (Uber)
I was feeling myself (Goddamn)
Had the polo with the bolo (I did)
With some eel on the belt (Hoo)
Walked up to the bouncer (Hey, what's up man?)
Whole squad on stealth (I'm Macklemore)
He said, 'Mackler, who?' (It's me)
You gotta wait like everybody else
Shoulda stayed on the sofa
Forgot I hate being social
And I miss my ex-girl
This Drake song making me 'motional (Girl, you hurt my feelings)
I'm feeling awkward as hell (Uh-huh)
I only came here to dance (Wassup?)
The DJ ain't playing the cuts (No)
And what do I do with my hands? (It's awkward)
Roll with the punches and hold my Red Bull up
And I toast the nights like this that I probably won't remember much
'Bout to pull that Irish goodbye, grab my stuff, 'bout to cut
And the DJ yells, 'Macklemore in the house tonight'
Ah, fuck
Oh, save me (Save me), can't take it (Take it)
I don't belong in this club (Club)
One dance (One dance), no chance (No chance)
'Cause I'm feeling awkward as (Oh)
I was waiting in line for an hour
Just to get in now, I wanna get out 'cause (Oh)
I'm jaded (I'm jaded), can't fake it (Can't fake it)
I don't belong in this club
And to think that I've waited all week (No)
To get someone's drink spilled over me (I)
I don't care if the Uber's on surge (No I don't, no)
I'd do anything to get out of this club
Save me, can't take it, no
I don't belong in this club
One dance, no chance
'Cause I'm feeling awkward as (Oh)
I was waiting in line for an hour
Just to get in now, I wanna get out 'cause (Oh)
I'm jaded (I'm jaded), can't fake it (Can't fake it)
I don't belong in this club", '3:43')''')

conn.commit()
cur.close()
