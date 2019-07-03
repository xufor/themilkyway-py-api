import random
import psycopg2

ADMIN_PASSWORD = '48c5ae'

UID = ['26e1a2', '54gdg5', 'y67tu7', 'e4r45r', '7ui87h', 'ty6er6']
HASHES = ['$2b$12$ldy3v6k0TLT3cBT8UQmEAO6WZiJ3xHarDKuA8cbCcy4UgpCvyVaku',
          '$2b$12$/dGzsj9pYPWmhcTlzVC83uy916PKH9dWjl6SMy.S97p4BvoGIdU3e',
          '$2b$12$/dGzsj9pYPWmhcTlzVC83uy916PKH9dWjl6SMy.S97p4BvoGIdU3e',
          '$2b$12$/dGzsj9pYPWmhcTlzVC83uy916PKH9dWjl6SMy.S97p4BvoGIdU3e',
          '$2b$12$/dGzsj9pYPWmhcTlzVC83uy916PKH9dWjl6SMy.S97p4BvoGIdU3e',
          '$2b$12$/dGzsj9pYPWmhcTlzVC83uy916PKH9dWjl6SMy.S97p4BvoGIdU3e'
          ]
NAMES = ['Admin', 'Jignesh Kumar', 'Akash Kumar', 'Subodh Chaurasiya', 'Meena Kumari', 'Kulbhushan Singh']
TIME = ['2019-06-16 17:34:35.000000', '2019-06-20 12:21:34.000000', '2019-06-20 12:21:59.000000',
        '2019-06-20 12:22:49.000000', '2019-06-20 12:23:34.000000', '2019-06-20 12:24:24.000000']

AUTHORS = ['54gdg5', 'y67tu7', 'e4r45r', '7ui87h', 'ty6er6', 'e4r45r', '7ui87h', 'ty6er6', '54gdg5', 'y67tu7']

SUB_TIME = ['2015-06-16 17:34:35.000000', '2018-06-20 12:21:34.000000', '2013-06-20 12:21:59.000000',
            '2016-06-20 12:22:49.000000', '2014-06-20 12:23:34.000000', '2011-06-20 12:24:24.000000',
            '2014-08-20 12:22:49.000000', '2003-05-20 12:23:34.000000', '2001-06-19 12:24:24.000000',
            '2017-08-20 11:26:46.000000'
            ]

SID = ['a8ad853b', 'cd7f8461', '0bcb1029', '957fc79e', 'a4303986', '315be4fd', '06ef60a2', '14776800', 'e0b843b8', '83ae974d']

STORIES = [
    '''You hear stories about people having encounters during the
    nighttime with strange flying objects.  These people tell how
    overwhelmed they were by the experience.  I can't say that
    this story has anything quite so glamorous as UFO's; but,
    sometimes things happen that are very much a part of our very
    own world that are just as overwhelming as visitors from
    outer space.  This is a true story and none of the names have
    been changed to protect the innocent or the guilty.
    
    If you are going to fully understand and appreciate this
    strange encounter that happened in our present day advanced
    technological society, a little background is needed.  There
    are still places (a few sprinkled here and there) in our
    country that have retained all the flavor of an age many have
    never experienced.  I often feel like a time traveler in
    today's society because of my background.
    
    I'm not "old" (however, my granddaughter may disagree) and
    many of the people my age never experienced the same world as
    I.  I guess you might say I'm an oddball in my own
    generation.  The reasons for it were quite beyond my control.
    My parents were married for twenty-two years before I was
    born (and I was the first and last)!  Talk about a generation
    gap, it was like being raised by grandparents!  Now, I marvel
    at all the things my father experienced throughout his
    lifetime and taught me.  Imagine being born in the late
    1800's and living until 1986.  Think of all the things that
    man created during that time that has become part of our
    daily lives.  When I do, it almost boggles my mind.  Anyway,
    you get the picture of my parents.  The next image you need
    to set the scene for this encounter is where it happened.
    
    Imagine a small, quaint house resting, nestled among the pine
    of a secluded valley in the foothills of the Ozarks.  It's a
    simple house, not designed by a architect or built by a
    contractor; but, the trees for the lumber were cut, the
    boards were sawed, and it was built with the owner's hands.
    It began its humble life as a home with only one room without
    windows or doors in November of 1932.  The spot it sat on was
    carved out of the wilderness far from roads or neighbors.  It
    was a symbol of hope and faith for a future during the dreary
    days of the depression.
    
    It was built by two young people who believed in themselves
    and each other.  People who had traveled and explored their
    world for the first ten years of marriage. They had seen the
    world and decided it was time to return to the place they had
    known as children, settle down, and begin to invest in their
    future.  They had accumulated very little material
    possessions during their days of exploration.  They began
    their new adventure with very few of the things we take for
    granted in today's world.  But, they believed enough in
    themselves to start building a house and begin a new business
    when their world was in a state of darkness.  The dreary days
    of the depression ended.  The house grew room by room and the
    business grew to be a very successful one.  The two were
    happy and content; but, eventually the two young people
    became three.  This was when I enter their lives, just when
    they had grown accustomed to being a couple without children.
    
    My father always wanted a son; but, that was not in his
    future, he got me instead.  However, I may as well have been
    a boy while I was growing up.  I became the son he had always
    wanted, and I was his buddy.  Instead, he taught me all the
    things he had hoped to teach to a son.  He knew the forest
    and the land, and he taught me what he knew.  We fished the
    numerous streams located near our home, hunted together, and
    did what most father's and sons usually do.  My father taught
    me to respect the land, and its creatures.  He taught me to
    hunt for food and not kill for the sake of killing.  He
    taught me to "see", "hear", and appreciate the beauty that
    surrounded me.
    
    My father saw a day coming when a haven such as ours would be
    as valued as a rich man's mansion.  He chose to preserve a
    small area of his land as a refuge for his family and all the
    living things that depended on just such a refuge.  This
    place would be a legacy to his grandchildren and his great-
    grandchildren.  They would be able to know a little part of
    the world that existed when he was young.
    
    I inherited this small mecca and I have made sure that his
    wishes have been carried out.  It will go to my son and then
    to my eldest granddaughter.  It has been a haven for us to
    escape the fast paced world we live in today.  A few years
    ago, when my husband became disabled, we lived in the house
    for about six years.
    
    The back of the house faces a small brook with a hillside
    full of pine, maple, wild cherry and dogwood trees.  My
    husband loved the outdoors; but, because of his illness was
    limited in how much he could get out.  We decided to build a
    screened in porch on the back of the house so he be outside
    during the daytime when I was at work.  The back porch became
    a place to spend the early evenings.  We would watch the
    little valley change from a bright cheery haven to a
    mysterious realm of sight and sound as the shades of dusk
    encircled it in its arms.  We soon discovered that the back
    porch was a place for a variety of activities.  We enjoyed it
    so much we decided it was a good place for our exercise bike.
    
    
    It wasn't long before we, also, discovered that the hillside
    in front of us was a source of entertainment.  Almost every
    evening we watched deer casually stroll across the hillside
    as they nibbled at tender leaves and grass.  Sometimes there
    would be four or five deer together.  On other evenings, wild
    turkey would be spotted.  It seemed as if our little valley
    had become a refuge for a variety of wild animals that were
    being pushed out by the growing population that had cleared
    away the forest that has once covered the area.  The presence
    of all the animals prompted us to put grain and other treats
    out for them to eat.
    
    The next summer, we began to notice that the wildlife
    population was increasing in number and variety.  The animals
    quickly learned they had nothing to fear from the two humans
    who shared their sanctuary, and they began to visit our
    backyard.  We were invaded by deer, turkey, opossum, wild
    duck, and a variety of other animals and birds.
    
    We took the invasion in stride, enjoying the chance to
    observe all the wild creatures.  However, one morning after I
    arose from my bed and took my morning coffee to the back
    porch to enjoy the sights and sounds, I walked into a
    disaster area.  Something, or someone, had invaded our back
    porch and played havoc with everything.  It had been
    vandalized.  I disposed of the things that had been destroyed
    and straightened the rest.  I couldn't imagine who or what
    had committed the dreadful deed.  The next morning, the porch
    was in the same condition.  I cleaned it up again.  This
    became a pattern, and needless to say, I was beginning to get
    tired of it.  There wasn't a lock on the door to the porch;
    but, the door had to be opened to get in.  Who or what was
    doing it was a puzzle.  The first time it happened, I could
    believe it to be the results of a prank; but, not every
    night!  It had to be an animal.
    
    How an animal could open the back door and come in, I didn't
    know.  My husband and I became determined to find out.  We
    began our quest by leaving the porch light on at night.  It
    didn't help.  Whatever was getting on the porch wasn't afraid
    of it and the destruction continued.  We decided to set guard
    and solve the mystery.
    
    One evening, after we had grown too tired to watch the porch
    anymore, my husband thought he heard a noise.  He got out of
    bed and very carefully went to the door that led to the
    porch.  He was gone only a few seconds when he returned and
    motioned for me to accompany him.  I started to ask why; but,
    he shushed me to silence.  We tiptoed together like cat
    burglars as we made our way to the back door.  We very
    carefully peeped out.  I couldn't believe my eyes!  I saw one
    of the strangest and most amusing sights I had ever
    witnessed.  Sitting on the seat of the exercise bike with
    paws on the handlebars was a raccoon that looked big enough
    to be a small bear.  He wasn't only nice and fat, he was
    long.  He had to be large to reach the handle bars of that
    bicycle.
    
    The raccoon looked as if he were contemplating how to reach
    the pedals so he could ride it.  We simply stood frozen,
    staring in amazement.  Then, the humor of the sight began to
    take hold of us.  He didn't see us watching him until we
    began to shake with silent laughter that was about to erupt
    into loud guffaws.  When he realized that he was not only
    being watched by two strange creatures who were obviously
    laughing at him, he calmly, arrogantly, climbed down off the
    bicycle.  He took his time as he sauntered to the door.  He
    walked with a haughty air seeming to be aware that his
    privacy had not only been invaded; but, he appeared to be
    insulted by the behavior of the two creatures who were so
    rudely laughing at him.  Once out the door, he paused, looked
    back at us as if to let us know what he thought, and slowly
    disappeared into the darkness.  By this time, my husband and
    I were reduced to tears of laughter.
    
    
    For some strange reason, I was fascinated with this bold
    creature and became obsessed with the idea of seeing him
    again.  So, for several nights after the event, I sat on
    the bench in our back yard, located just outside the porch
    door, and watched for the raccoon to return.  I just knew he
    would be back and I was going to make sure I saw him.  I had
    no idea what I was going to do when I did, I hadn't thought
    beyond just seeing him again.  Three nights passed and there
    was no sign of the creature.  I was beginning to think our
    laughter had either scared him off for good, or, had insulted
    his sense of dignity far too much for him to chance a return.
    
    But, I didn't give up.  Finally, my vigil was rewarded.  One
    evening as I sat quietly watching, I caught a glimpse of
    something moving in the shadows off to my far left.  I knew
    instinctively that it was the same raccoon.  He didn't look
    nearly as large in the shadows as he had that evening he was
    on our porch.  I waited patiently, watching the small figure
    circle around until he was directly in front of me and was
    only about fifteen feet away.  I watched as he checked out an
    old trash can we kept to use when we cleaned out our car.  It
    didn't take him long to decide that he would find nothing to
    eat in the can.  He turned and began walking straight toward
    the door of our back porch . . . and . . . me.
    
    I sat still, frozen by fascination combined with a growing
    sense of apprehension that began to overtake me.  All the
    things my father had taught me about the dangers of wild
    animals came flooding back into my consciousness.  I had time
    to move, to run; but, I didn't.  My obsession to observe this
    creature overrode all caution and I sat like a statue where I
    was, tempting fate.  The animal kept advancing closer and
    closer.  The tension and the thrill I felt grew with each
    step he took toward me.  I was beginning to feel a need to
    bolt for cover.  He was no more than five feet away, it
    seemed like two.  He stopped.  He raised his head, our eyes
    locked for a moment.  Then, he slowly, very deliberately
    walked directly at me as he maintained eye contact.  The
    tension within me was growing with each step he took.  He
    began to look bigger and bigger the nearer he came.  I felt I
    could stand the tension no longer as he moved within no more
    than three feet of where I sat.  I felt the urge to move, to
    speak, to do something.  Again, the need to watch this
    fascinating creature kept me from running or yelling.  I had
    to watch him.  I didn't want to scare him away, so, to
    relieve some of the tension, I merely changed the position of
    my feet.
    
    My movement, caused the raccoon to come to a sudden halt.  By
    the time he stopped, he was close enough that I could have
    reached out and touch him.  He stood up on his hind legs and
    looked me straight in the eye.  Standing, he was nose to nose
    with me.  He looked bigger than ever.  I became the object of
    observation as he tilted his head side to side looking me
    over.  There was look in his eyes telling me that he was
    planning to analyze this strange creature at an even closer
    distance.  I had no idea what he might do if he got closer.
    I thought about us laughing at him and thinking he may want
    revenge.  As he stood there in the soft light I could almost
    hear him thinking.  I observed a change of expression in his
    eyes from one of curiosity to one of determination.  I didn't
    know what he was going to do, and I didn't want to find out.
    The hairs on the back of my neck were tingling as fear began
    to creep over me.
    
    The fear grew and the knowledge that I didn't want the
    raccoon any closer overwhelmed me.  I wasn't sure what to do.
    If I were attacked, my husband would never hear because he
    was watching the ballgame on the television.  Visions of
    a headline in our local paper flashed across my mind, "Local
    Woman Attacked by Large Raccoon."  Still, I didn't run or
    yell.  Instead, I did one of the craziest things I have ever
    done in my life, I addressed the raccoon as if he were a
    person and said, "Hello, there!  What are you doing?"
    
    Again, he looked into my eyes, turned his head this way and
    that as if he were trying to understand my words.  For a
    moment, I thought he was going to come at me and my body
    stiffened again.  Instead, he lowered himself on all fours,
    slowly turned his back to me, and majestically strolled into
    the night without ever looking back.  In my mind, I could
    almost hear him chuckle.  The raccoon had gotten his revenge.
    
    I waited and watched several nights after our encounter for
    him to return.  He never did.  I think he had experienced all
    the contact with humans that he ever wanted.  I still wonder
    what would have happened if I could have remained still and
    quiet.  I guess I'll never know; but, it's an experience I'll
    never forget, and somehow, I don't think he will either.''',
    # -------------------------------------------------------------------
    ''' Once upon a time . . . a big crow stole a lump of cheese and went to perch 
    on a branch of a tree to eat it in peace. A passing fox sniffed the air and 
    stopped below the tree, his mouth watering.
       "Cheese?" he said. "Mmm. I'd love . . . if only I could . . ." he said to 
    himself, greedily, wondering how to get hold of the morsel.
       After a moment or two, he spoke to the crow: "You are a fine crow! I've 
    never seen anyone so big and strong. What lovely thick shiny feathers you 
    have! And such slender legs, the sign of a noble bird. And a regal beak. 
    That's it: the beak of a king! You ought to be crowned King of the Birds!"
       When the crow heard such glowing praise of his beauty, he stretched to his 
    full length and triumphantly flapped hls wlngs.
       In his softest voice, the fox went on: "What lovely eyes you have. You 
    don't seem to have a single fault! You're quite perfect." The crow had never 
    been flattered so much in all his life. "Though I haven't heard your voice 
    yet," went on the fox, "I expect that such a perfect creature like yourself 
    can have nothing less than a wonderful singing voice!"
       The crow had, till then, been blissfully drinking in the fox's praise, but 
    he felt a prick of doubt at the sweet words about his voice. He had never 
    heard that crows were fine singers! Of course, being a very fine crow, perhaps
    that meant he had a beautiful voice as well. The fox could be right! And the 
    crow gazed down at the fox as he said: "Now then, King of the Birds, let me 
    hear a sweet song . . ."                             
       Throwing caution to the winds, the crow opened his beak and, taking a deep 
    breath, loudly cawed: "Cra, Cra, Cra!" The lump of cheese fell through the air
    and the fox caught it neatly in his jaws. "I deserved that!" he told himself 
    as he enjoyed the titbit. Then, licking his lips, he again spoke to the crow 
    on the branch.
       "Silly crow. You're the ugliest bird I've ever seen, you have the worst 
    voice I ve ever heard, but most of all, you're the most stupid bird I've ever 
    met! And thanks for the cheese." And off he trotted well satisfied with 
    himself...''',
    # -------------------------------------------------------------------
    '''When I look at the three massive manuscript volumes which
    contain our work for the year 1894, I confess that it is very
    difficult for me, out of such a wealth of material, to select the
    cases which are most interesting in themselves, and at the same
    time most conducive to a display of those peculiar powers for
    which my friend was famous. As I turn over the pages, I see my
    notes upon the repulsive story of the red leech and the terrible
    death of Crosby, the banker. Here also I find an account of the
    Addleton tragedy, and the singular contents of the ancient British
    barrow. The famous Smith-Mortimer succession case comes also
    within this period, and so does the tracking and arrest of Huret,
    the Boulevard assassin -- an exploit which won for Holmes an
    autograph letter of thanks from the French President and the
    Order of the Legion of Honour. Each of these would furnish a
    narrative, but on the whole I am of opinion that none of them
    unites so many singular points of interest as the episode of
    Yoxley Old Place, which includes not only the lamentable death
    of young Willoughby Smith, but also those subsequent develop-
    ments which threw so curious a light upon the causes of the
    crime.
      It was a wild, tempestuous night, towards the close of Novem-
    ber. Holmes and I sat together in silence all the evening, he
    engaged with a powerful lens deciphering the remains of the
    original inscription upon a palimpsest, I deep in a recent treatise
    upon surgery. Outside the wind howled down Baker Street,
    while the rain beat fiercely against the windows. It was strange
    there, in the very depths of the town, with ten miles of man's
    handiwork on every side of us, to feel the iron grip of Nature,
    and to be conscious that to the huge elemental forces all London
    was no more than the molehills that dot the fields. I walked to
    the window, and looked out on the deserted street. The occa-
    sional lamps gleamed on the expanse of muddy road and shining
    pavement. A single cab was splashing its way from the Oxford
    Street end.
      "Well, Watson, it's as well we have not to turn out to-night,"
    said Holmes, laying aside his lens and rolling up the palimpsest.
    "I've done enough for one sitting. It is trying work for the eyes.
    So far as I can make out, it is nothing more exciting than an
    Abbey's accounts dating from the second half of the fifteenth
    century. Halloa! halloa! halloa! What's this?"
      Amid the droning of the wind there had come the stamping of
    a horse's hoofs, and the long grind of a wheel as it rasped
    against the curb. The cab which I had seen had pulled up at our
    door.
      "What can he want?" I ejaculated, as a man stepped out of it.
      "Want? He wants us. And we, my poor Watson, want over-
    coats and cravats and goloshes, and every aid that man ever
    invented to fight the weather. Wait a bit, though! There's the cab
    off again! There's hope yet. He'd have kept it if he had wanted
    us to come. Run down, my dear fellow, and open the door, for
    all virtuous folk have been long in bed."
      When the light of the hall lamp fell upon our midnight visitor,
    I had no difficulty in recognizing him. It was young Stanley
    Hopkins, a promising detective, in whose career Holmes had
    several times shown a very practical interest.
      "Is he in?" he asked, eagerly.
      "Come up, my dear sir," said Holmes's voice from above. "I
    hope you have no designs upon us on such a night as this."
      The detective mounted the stairs, and our lamp gleamed upon
    his shining waterproof. I helped him out of it, while Holmes
    knocked a blaze out of the logs in the grate.
      "Now, my dear Hopkins, draw up and warm your toes," said
    he. "Here's a cigar, and the doctor has a prescription containing
    hot water and a lemon, which is good medicine on a night like
    this. It must be something important which has brought you out
    in such a gale."
      "It is indeed, Mr. Holmes. I've had a bustling afternoon, I
    promise you. Did you see anything of the Yoxley case in the
    latest editions?"
      "I've seen nothing later than the fifteenth century to-day."
      "Well, it was only a paragraph, and all wrong at that, so you
    have not missed anything. I haven't let the grass grow under my
    feet. It's down in Kent, seven miles from Chatham and three
    from the railway line. I was wired for at 3:15, reached Yoxley
    Old Place at 5, conducted my investigation, was back at Charing
    Cross by the last train, and straight to you by cab."
      "Which means, I suppose, that you are not quite clear about
    your case?"
      "lt means that I can make neither head nor tail of it. So far as
    I can see, it is just as tangled a business as ever I handled, and
    yet at first it seemed so simple that one couldn't go wrong.
    There's no motive, Mr. Holmes. That's what bothers me -- I
    can't put my hand on a motive. Here's a man dead -- there's no
    denying that -- but, so far as I can see, no reason on earth why
    anyone should wish him harm."
      Holmes lit his cigar and leaned back in his chair.
      "Let us hear about it," said he.
      "I've got my facts pretty clear," said Stanley Hopkins. "All I
    want now is to know what they all mean. The story, so far as I
    can make it out, is like this. Some years ago this country house,
    Yoxley Old Place, was taken by an elderly man, who gave the
    name of Professor Coram. He was an invalid, keeping his bed
    half the time, and the other half hobbling round the house with a
    stick or being pushed about the grounds by the gardener in a
    Bath chair. He was well liked by the few neighbours who ealled
    upon him, and he has the reputation down there of being a very
    learned man. His household used to consist of an elderly house-
    keeper, Mrs. Marker, and of a maid, Susan Tarlton. These have
    both been with him since his arrival, and they seem to be women
    of excellent character. The professor is writing a learned book,
    and he found it necessary, about a year ago, to engage a secre-
    tary. The first two that he tried were not successes, but the third,
    Mr. Willoughby Smith, a very young man straight from the
    university, seems to have been just what his employer wanted.
    His work consisted in writing all the morning to the professor's
    dictation, and he usually spent the evening in hunting up refer-
    ences and passages which bore upon the next day's work. This
    Willoughby Smith has nothing against him, either as a boy at
    Uppingham or as a young man at Cambridge. I have seen his
    testimonials, and from the first he was a decent, quiet, hard-
    working fellow, with no weak spot in him at all. And yet this is
    the lad who has met his death this morning in the professor's
    study under circumstances which can point only to murder."
      The wind howled and screamed at the windows. Holmes and
    I drew closer to the fire, while the young inspector slowly and
    point by point developed his singular narrative.
      "If you were to search all England," said he, "I don't
    suppose you could find a household more self-contained or freer
    from outside influences. Whole weeks would pass, and not one
    of them go past the garden gate. The professor was buried in his
    work and existed for nothing else. Young Smith knew nobody in
    the neighbourhood, and lived very much as his employer did.
    The two women had nothing to take them from the house.
    Mortimer, the gardener, who wheels the Bath chair, is an army
    pensioner -- an old Crimean man of excellent character. He does
    not live in the house, but in a three-roomed cottage at the other
    end of the garden. Those are the only people that you would find
    within the grounds of Yoxley Old Place. At the same time, the
    gate of the garden is a hundred yards from the main London to
    Chatham road. It opens with a latch, and there is nothing to
    prevent anyone from walking in.
      "Now I will give you the evidence of Susan Tarlton, who is
    the only person who can say anything positive about the matter.
    It was in the forenoon, between eleven and twelve. She was
    engaged at the moment in hanging some curtains in the upstairs
    front bedroom. Professor Coram was still in bed, for when the
    weather is bad he seldom rises before midday. The housekeeper
    was busied with some work in the back of the house. Wil-
    loughby Smith had been in his bedroom, which he uses as a
    sitting-room, but the maid heard him at that moment pass along
    the passage and descend to the study immediately below her. She
    did not see him, but she says that she could not be mistaken in
    his quick, firm tread. She did not hear the study door close, but a
    minute or so later there was a dreadful cry in the room below. It
    was a wild, hoarse scream, so strange and unnatural that it might
    have come either from a man or a woman. At the same instant
    there was a heavy thud, which shook the old house, and then all
    was silence. The maid stood petrified for a moment, and then,
    recovering her courage, she ran downstairs. The study door was
    shut and she opened it. Inside, young Mr. Willoughby Smith
    was stretched upon the floor. At first she could see no injury, but
    as she tried to raise him she saw that blood was pouring from the
    underside of his neck. It was pierced by a very small but very
    deep wound, which had divided the carotid artery. The instru-
    ment with which the injury had been inflicted lay upon the carpet
    beside him. It was one of those small sealing-wax knives to be
    found on old-fashioned writing-tables, with an ivory handle and
    a stiff blade. It was part of the fittings of the professor's own
    desk.
      "At first the maid thought that young Smith was already dead,
    but on pouring some water from the carafe over his forehead he
    opened his eyes for an instant. 'The professor,' he murmured -- 'it
    was she.' The maid is prepared to swear that those were the
    exact words. He tried desperately to say something else,
    and he held his right hand up in the air. Then he fell back
    dead.
      "In the meantime the housekeeper had also arrived upon the
    scene, but she was just too late to catch the young man's dying
    words. Leaving Susan with the body, she hurried to the profes-
    sor's room. He was sitting up in bed horribly agitated, for he had
    heard enough to convince him that something terrible had oc-
    curred. Mrs. Marker is prepared to swear that the professor was
    still in his night-clothes, and indeed it was impossible for him to
    dress without the help of Mortimer, whose orders were to come
    at twelve o'clock. The professor declares that he heard the
    distant cry, but that he knows nothing more. He can give no
    explanation of the young man's last words, 'The professor -- it
    was she,' but imagines that they were the outcome of delirium.
    He believes that Willoughby Smith had not an enemy in the
    world, and can give no reason for the crime. His first action was
    to send Mortimer, the gardener, for the local police. A little later
    the chief constable sent for me. Nothing was moved before I got
    there, and strict orders were given that no one should walk upon
    the paths leading to the house. It was a splendid chance of
    putting your theories into practice, Mr. Sherlock Holmes. There
    was really nothing wanting."
      "Except Mr. Sherlock Holmes," said my companion, with a
    somewhat bitter smile. "Well, let us hear about it. What sort of
    job did you make of it?"
      "I must ask you first, Mr. Holmes, to glance at this rough
    plan, which will give you a general idea of the position of the
    professor's study and the various points of the case. It will help
    you in following my investigation."
      He unfolded the rough chart, which I here reproduce, and he
    laid it across Holmes's knee. I rose and, standing behind
    Holmes, studied it over his shoulder.
      "It is very rough, of course, and it only deals with the points
    which seem to me to be essential. All the rest you will see later
    for yourself. Now, first of all, presuming that the assassin entered
    the house, how did he or she come in? Undoubtedly by the
    garden path and the back door, from which there is direct access
    to the study. Any other way would have been exceedingly
    complicated. The escape must have also been made along that
    line, for of the two other exits from the room one was blocked
    by Susan as she ran downstairs and the other leads straight to the
    professor's bedroom. I therefore directed my attention at once to
    the garden path, which was saturated with recent rain, and would
    certainly show any footmarks.
      "My examination showed me that I was dealing with a cautious
    and expert criminal. No footmarks were to be found on the path.
    There could be no question, however, that someone had passed
    along the grass border which lines the path, and that he had done
    so in order to avoid leaving a track. I could not find anything in
    the nature of a distinct impression, but the grass was trodden
    down, and someone had undoubtedly passed. It could only have
    been the murderer, since neither the gardener nor anyone else
    had been there that morning, and the rain had only begun during
    the night."
      "One moment," said Holmes. "Where does this path lead
    to?"
      "To the road."
      "How long is it?"
      "A hundred yards or so."
      "At the point where the path passes through the gate, you
    could surely pick up the tracks?"
      "Unfortunately, the path was tiled at that point."
      "Well, on the road itself?"
      "No, it was all trodden into mire."
      "Tut-tut! Well, then, these tracks upon the grass, were they
    coming or going?"
      "It was impossible to say. There was never any outline."
      "A large foot or a small?"
      "You could not distinguish."
      Holmes gave an ejaculation of impatience.
      "It has been pouring rain and blowing a hurricane ever since,"
    said he. "It will be harder to read now than that palimpsest.
    Well, well. it can't be helped. What did you do. Hopkins, after
    you had made certain that you had made certain of nothing?"
      "I think I made certain of a good deal, Mr. Holmes. I knew
    that someone had entered the house cautiously from without. I
    next examined the corridor. It is lined with cocoanut matting and
    had taken no impression of any kind. This brought me into the
    study itself. It is a scantily furnished room. The main article is a
    large writing-table with a fixed bureau. This bureau consists of a
    double column of drawers, with a central small cupboard be-
    tween them. The drawers were open, the cupboard locked. The
    drawers, it seems, were always open, and nothing of value was
    kept in them. There were some papers of importance in the
    cupboard, but there were no signs that this had been tampered
    with, and the professor assures me that nothing was missing. It is
    certain that no robbery has been committed.
      "I come now to the body of the young man. It was found near
    the bureau, and just to the left of it, as marked upon that chart.
    The stab was on the right side of the neck and from behind
    forward, so that it is almost impossible tbat it could have been
    self-inflicted."
      "Unless he fell upon the knife," said Holmes.
      "Exactly. The idea crossed my mind. But we found the knife
    some feet away from the body, so that seems impossible. Then,
    of course, there are the man's own dying words. And, finally,
    there was this very important piece of evidence which was found
    clasped in the dead man's right hand."
      From his pocket Stanley Hopkins drew a small paper packet.
    He unfolded it and disclosed a golden pince-nez, with two
    broken ends of black silk cord dangling from the end of it.
      "Willoughby Smith had excellent sight," he added. "There can
    be no question that this was snatched from the face or the person
    of the assassin."
      Sherlock Holmes took the glasses into his hand, and examined
    them with the utmost attention and interest. He held them on his
    nose, endeavoured to read through them, went to the window
    and stared up the street with them, looked at them most minutely
    in the full light of the lamp, and finally, with a chuckle, seated
    himself at the table and wrote a few lines upon a sheet of paper,
    which he tossed across to Stanley Hopkins.
      "That's the best I can do for you," said he. "It may prove to
    be of some use."
      The astonished detective read the note aloud. It ran as follows:
    
         "Wanted. a woman of good address. attired like a lady.
       She has a remarkably thick nose, with eyes which are set
       close upon either side of it. She has a puckered forehead, a
       peering expression, and probably rounded shoulders. There
       are indications that she has had recourse to an optician at
       least twice during the last few months. As her glasses are of
       remarkable strength, and as opticians are not very numer-
       ous, there should be no difficulty in tracing her."
    
      Holmes smiled at the astonishment of Hopkins, which must
    have been reflected upon my features.
      "Surely my deductions are simplicity itself," said he. "It
    would be difficult to name any articles which afford a finer field
    for inference than a pair of glasses, especially so remarkable a
    pair as these. That they belong to a woman I infer from their
    delicacy, and also, of course, from the last words of the dying
    man. As to her being a person of refinement and well dressed
    they are, as you perceive, handsomely mounted in solid gold,
    and it is inconceivable that anyone who wore such glasses could
    be slatternly in other respects. You will find that the clips are too
    wide for your nose, showing that the lady's nose was very broad
    at the base. This sort of nose is usually a short and coarse one,
    but there is a sufficient number of exceptions to prevent me from
    being dogmatic or from insisting upon this point in my descrip-
    tion. My own face is a narrow one, and yet I find that I cannot
    get my eyes into the centre, nor near the centre, of these glasses.
    Therefore, the lady's eyes are set very near to the sides of the
    nose. You will perceive, Watson, that the glasses are concave
    and of unusual strength. A lady whose vision has been so
    extremely contracted all her life is sure to have the physical
    characteristics of such vision, which are seen in the forehead, the
    eyelids, and the shoulders."
      "Yes," I said, "I can follow each of your arguments. I
    confess, however, that I am unable to understand how you arrive
    at the double visit to the optician."
      Holmes took the glasses in his hand.
      "You will perceive," he said, "that the clips are lined with
    tiny bands of cork to soften the pressure upon the nose. One of
    these is discoloured and worn to some slight extent, but the other
    is new. Evidently one has fallen off and been replaced. I should
    judge that the older of them has not been there more than a few
    months. They exactly correspond, so I gather that the lady went
    back to the same establishment for the second."
      "By George, it's marvellous!" cried Hopkins. in an ecstasy of
    admiration. "To think that I had all that evidence in my hand
    and never knew it! I had intended, however, to go the round of
    the London opticians."
      "Of course you would. Meanwhile, have you anything more
    to tell us about the case?"
      "Nothing, Mr. Holmes. I think that you know as much as I do
    now -- probably more. We have had inquiries made as to any
    stranger seen on the country roads or at the railway station. We
    have heard of none. What beats me is the utter want of all object
    in the crime. Not a ghost of a motive can anyone suggest."
      "Ah! there I am not in a position to help you. But I suppose
    you want us to come out to-morrow?"
      "If it is not asking too much, Mr. Holmes. There's a train
    from Charing Cross to Chatham at six in the morning, and we
    should be at Yoxley Old Place between eight and nine."
      "Then we shall take it. Your case has certainly some features
    of great interest, and I shall be delighted to look into it. Well,
    it's nearly one, and we had best get a few hours' sleep. I daresay
    you can manage all right on the sofa in front of the fire. I'll light
    my spirit lamp, and give you a cup of coffee before we start."
      The gale had blown itself out next day, but it was a bitter
    morning when we started upon our journey. We saw the cold
    winter sun rise over the dreary marshes of the Thames and the
    long, sullen reaches of the river, which I shall ever associate
    with our pursuit of the Andaman Islander in the earlier days of
    our career. After a long and weary journey, we alighted at a
    small station some miles from Chatham. While a horse was
    being put into a trap at the local inn, we snatched a hurried
    breakfast, and so we were all ready for business when we at last
    arrived at Yoxley Old Place. A constable met us at the garden
    gate.
      "Well, Wilson, any news?"
      "No, sir -- nothing."
      "No reports of any stranger seen?"
      "No, sir. Down at the station they are certain that no stranger
    either came or went yesterday."
      "Have you had inquiries made at inns and lodgings?"
      "Yes, sir: there is no one that we cannot account for."
      "Well, it's only a reasonable walk to Chatham. Anyone might
    stay there or take a train without being observed. This is the
    garden path of which I spoke, Mr. Holmes. I'll pledge my word
    there was no mark on it yesterday."
      "On which side were the marks on the grass?"
      "This side, sir. This narrow margin of grass between the path
    and the flowerbed. I can't see the traces now, but they were clear
    to me then."
      "Yes, yes: someone has passed along," said Holmes, stoop-
    ing over the grass border. "Our lady must have picked her steps
    carefully, must she not, since on the one side she would leave a
    track on the path, and on the other an even clearer one on the
    soft bed?"
      "Yes, sir, she must have been a cool hand."
      I saw an intent look pass over Holmes's face.
      "You say that she must have come back this way?"
      "Yes, sir, there is no other."
      "On this strip of grass?"
      "Certainly, Mr. Holmes."
      "Hum! It was a very remarkable performance -- very remark-
    able. Well, I think we have exhausted the path. Let us go
    farther. This garden door is usually kept open, I suppose? Then
    this visitor had nothing to do but to walk in. The idea of murder
    was not in her mind, or she would have provided herself with
    some sort of weapon, instead of having to pick this knife off the
    writing-table. She advanced along this corridor, leaving no traces
    upon the cocoanut matting. Then she found herself in this study.
    How long was she there? We have no means of judging."
      "Not more than a few minutes, sir. I forgot to tell you that
    Mrs. Marker, the housekeeper, had been in there tidying not
    very long before -- about a quarter of an hour, she says."
      "Well, that gives us a limit. Our lady enters this room, and
    what does she do? She goes over to the writing-table. What for?
    Not for anything in the drawers. If there had been anything
    worth her taking, it would surely have been locked up. No, it
    was for something in that wooden bureau. Halloa! what is that
    scratch upon the face of it? Just hold a match, Watson. Why did
    you not tell me of this, Hopkins?"
      The mark which he was examining began upon the brasswork
    on the righthand side of the keyhole, and extended for about four
    inches, where it had scratched the varnish from the surface.
      "I noticed it, Mr. Holmes, but you'll always find scratches
    round a keyhole."
      "This is recent, quite recent. See how the brass shines where
    it is cut. An old scratch would be the same colour as the surface.
    Look at it through my lens. There's the varnish, too, like earth
    on each side of a furrow. Is Mrs. Marker there?"
      A sad-faced, elderly woman came into the room.
      "Did you dust this bureau yesterday morning?"
      "Yes, sir."
      "Did you notice this scratch?"
      "No, sir, I did not."
      "I am sure you did not, for a duster would have swept away
    these shreds of varnish. Who has the key of this bureau?"
      "The professor keeps it on his watch-chain."
      "Is it a simple key?"
      "No, sir, it is a Chubb's key."
      "Very good. Mrs. Marker, you can go. Now we are making a
    little progress. Our lady enters the room, advances to the bureau,
    and either opens it or tries to do so. While she is thus engaged,
    young Willoughby Smith enters the room. In her hurry to with-
    draw the key, she makes this scratch upon the door. He seizes
    her, and she, snatching up the nearest object, which happens to
    be this knife, strikes at him in order to make him let go his hold.
    The blow is a fatal one. He falls and she escapes, either with or
    without the object for which she has come. Is Susan, the maid,
    there? Could anyone have got away through that door after the
    time that you heard the cry, Susan?"
      "No, sir, it is impossible. Before I got down the stair, I'd
    have seen anyone in the passage. Besides, the door never opened,
    or I would have heard it."
      "That settles this exit. Then no doubt the lady-went out the
    way she came. I understand that this other passage leads only to
    the professor's room. There is no exit that way?"
      "No, sir."
      "We shall go down it and make the acquaintance of the
    professor. Halloa, Hopkins! this is very important, very impor-
    tant indeed. The professor's corridor is also lined with cocoanut
    matting."
      "Well, sir, what of that?"
      "Don't you see any bearing upon the case? Well, well. I don't
    insist upon it. No doubt I am wrong. And yet it seems to me to
    be suggestive. Come with me and introduce me."
      We passed down the passage, which was of the same length as
    that which led to the garden. At the end was a short flight of
    steps ending in a door. Our guide knocked, and then ushered us
    into the professor's bedroom.
      It was a very large chamber, lined with innumerable volumes,
    which had overflowed from the shelves and lay in piles in the
    corners, or were stacked all round at the base of the cases. The
    bed was in the centre of the room, and in it, propped up with
    pillows, was the owner of the house. I have seldom seen a more
    remarkable-looking person. It was a gaunt, aquiline face which
    was turned towards us, with piercing dark eyes, which lurked in
    deep hollows under overhung and tufted brows. His hair and
    beard were white, save that the latter was curiously stained with
    yellow around his mouth. A cigarette glowed amid the tangle of
    white hair, and the air of the room was fetid with stale tobacco
    smoke. As he held out his hand to Holmes, I perceived that it
    was also stained with yellow nicotine.
      "A smoker, Mr. Holmes?" said he, speaking in well-chosen
    English, with a curious little mincing accent. "Pray take a
    cigarette. And you, sir? I can recommend them, for I have them
    especially prepared by lonides, of Alexandria. He sends me a
    thousand at a time, and I grieve to say that I have to arrange for
    a fresh suprly every fortnight. Bad, sir, very bad, but an old
    man has few pleasures. Tobacco and my work -- that is all that is
    left to me."
      Holmes had lit a cigarette and was shooting little darting
    glances all over the room.
      "Tobacco and my work, but now only tobacco," the old man
    exclaimed. "Alas! what a fatal interruption! Who could have
    foreseen such a terrible catastrophe? So estimable a young man!
    I assure you that, after a few months' training, he was an
    admirable assistant. What do you think of the matter, Mr.
    Holmes?"
      "I have not yet made up my mind."
      "I shall indeed be indebted to you if you can throw a light
    where all is so dark to us. To a poor bookworm and invalid like
    myself such a blow is paralyzing. I seem to have lost the faculty
    of thought. But you are a man of action -- you are a man of
    affairs. It is part of the everyday routine of your life. You can
    preserve your balance in every emergency. We are fortunate,
    indeed, in having you at our side."
      Holmes was pacing up and down one side of the room whilst
    the old professor was talking. I observed that he was smoking
    with extraordinary rapidity. It was evident that he shared our
    host's liking for the fresh Alexandrian cigarettes.
      "Yes, sir, it is a crushing blow," said the old man. "That is
    my magnum opus -- the pile of papers on the side table yonder. It
    is my analysis of the documents found in the Coptic monasteries
    of Syria and Egypt, a work which will cut deep at the very
    foundation of revealed religion. With my enfeebled health I do
    not know whether I shall ever be able to complete it, now that
    my assistant has been taken from me. Dear me! Mr. Holmes,
    why, you are even a quicker smoker than I am myself."
      Holmes smiled.
      "I am a connoisseur," said he, taking another cigarette from
    the box -- his fourth -- and lighting it from the stub of that which
    he had finished. "I will not trouble you with any lengthy cross-
    examination, Professor Coram, since I gather that you were in
    bed at the time of the crime, and could know nothing about it. I
    would only ask this: What do you imagine that this poor fellow
    meant by his last words: 'The professor -- it was she'?"
      The professor shook his head.
      "Susan is a country girl," said he, "and you know the
    incredible stupidity of that class. I fancy that the poor fellow
    murmured some incoherent, delirious words, and that she twisted
    them into this meaningless message."
      "I see. You have no explanation yourself of the tragedy?"
      "Possibly an accident, possibly -- I only breathe it among
    ourselves -- a suicide. Young men have their hidden troubles -- 
    some affair of the heart, perhaps, which we have never known.
    It is a more probable supposition than murder."
      "But the eyeglasses?"
      "Ah! I am only a student -- a man of dreams. I cannot explain
    the practical things of life. But still, we are aware, my friend,
    that love-gages may take strange shapes. By all means take
    another cigarette. It is a pleasure to see anyone appreciate them
    so. A fan, a glove, glasses -- who knows what article may be
    carried as a token or treasured when a man puts an end to his
    life? This gentleman speaks of footsteps in the grass, but, after
    all, it is easy to be mistaken on such a point. As to the knife, it
    might well be thrown far from the unfortunate man as he fell. It
    is possible that I speak as a child, but to me it seems that
    Willoughby Smith has met his fate by his own hand."
      Holmes seemed struck by the theory thus put forward, and hc
    continued to walk up and down for some time, lost in thought
    and consuming cigarette after cigarette.
      "Tell me, Professor Coram," he said. at last, "what is in that
    cupboard in the bureau?"
      "Nothing that would help a thief. Family papers, letters from
    my poor wife, diplomas of universities which have done me
    honour. Here is the key. You can look for yourself."
      Holmes picked up the key, and looked at it for an instant, then
    he handed it back.
      "No, I hardly think that it would help me," said he. "I
    should prefer to go quietly down to your garden, and turn the
    whole matter over in my head. There is something to be said for
    the theory of suicide which you have put forward. We must
    apologize for having intruded upon you, Professor Coram, and I
    promise that we won't disturb you until after lunch. At two
    o'clock we will come again, and report to you anything which
    may have happened in the interval."
      Holmes was curiously distrait, and we walked up and down
    the garden path for some time in silence.
      "Have you a clue?" I asked, at last.
      "It depends upon those cigarettes that I smoked," said he. "It
    is possible that I am utterly mistaken. The cigarettes will show
    me."
      "My dear Holmes," I exclaimed, "how on earth --"
      "Well, well, you may see for yourself. If not, there's no harm
    done. Of course, we always have the optician clue to fall back
    upon, but I take a short cut when I can get it. Ah, here is the
    good Mrs. Marker! Let us enjoy five minutes of instructive
    conversation with her."
      I may have remarked before that Holmes had, when he liked,
    a peculiarly ingratiating way with women, and that he very
    readily established terms of confidence with them. In half the
    time which he had named, he had captured the housekeeper's
    goodwill and was chatting with her as if he had known her for
    years.
      "Yes, Mr. Holmes, it is as you say, sir. He does smoke
    something terrible. All day and sometimes all night, sir. I've
    seen that room of a morning -- well, sir, you'd have thought it
    was a London fog. Poor young Mr. Smith, he was a smoker
    also, but not as bad as the professor. His health -- well, I don't
    know that it's better nor worse for the smoking."
      "Ah!" said Holmes, "but it kills the appetite."
      "Well, I don't know about that, sir."
      "I suppose the professor eats hardly anything?"
      "Well, he is variable. I'll say that for him."
      "I'll wager he took no breakfast this morning, and won't face
    his lunch after all the cigarettes I saw him consume."
      "Well, you're out there, sir, as it happens, for he ate a
    remarkable big breakfast this morning. I don't know when I've
    known him make a better one, and he's ordered a good dish of
    cutlets for his lunch. I'm surprised myself, for since I came into
    that room yesterday and saw young Mr. Smith lying there on the
    floor, I couldn't bear to look at food. Well, it takes all sorts to
    make a world, and the professor hasn't let it take his appetite
    away."
      We loitered the morning away in the garden. Stanley Hopkins
    had gone down to the village to look into some rumours of a
    strange woman who had been seen by some children on the
    Chatham Road the previous morning. As to my friend, all his
    usual energy seemed to have deserted him. I had never known
    him handle a case in such a half-hearted fashion. Even the news
    brought back by Hopkins that he had found the children, and that
    they had undoubtedly seen a woman exactly corresponding with
    Holmes's description, and wearing either spectacles or eyeglasses,
    failed to rouse any sign of keen interest. He was more attentive
    when Susan, who waited upon us at lunch, volunteered the
    information that she believed Mr. Smith had been out for a walk
    yesterday morning, and that he had only returned half an hour
    before the tragedy occurred. I could not myself see the bearing
    of this incident, but I clearly perceived that Holmes was weaving
    it into the general scheme which he had formed in his brain.
    Suddenly he sprang from his chair and glanced at his watch.
    "Two o'clock, gentlemen." said he. "We must go up and have
    it out with our friend, the professor."
      The old man had just finished his lunch, and certainly his
    empty dish bore evidence to the good appetite with which his
    housekeeper had credited him. He was, indeed, a weird figure as
    he turned his white mane and his glowing eyes towards us. The
    eternal cigarette smouldered in his mouth. He had been dressed
    and was seated in an armchair by the fire.
      "Well, Mr. Holmes, have you solved this mystery yet?" He
    shoved the large tin of cigarettes which stood on a table beside
    him towards my companion. Holmes stretched out his hand at
    the same moment, and between them they tipped the box over
    the edge. For a minute or two we were all on our knees retriev-
    ing stray cigarettes from impossible places. When we rose again,
    I observed Holmes's eyes were shining and his cheeks tinged
    with colour. Only at a crisis have I seen those battle-signals
    flying .
      "Yes," said he, "I have solved it."
      Stanley Hopkins and I stared in amazement. Something like a
    sneer quivered over the gaunt features of the old professor.
      "Indeed! In the garden?"
      "No, here."
      "Here! When?"
      "This instant."
      "You are surely joking, Mr. Sherlock Holmes. You compel
    me to tell you that this is too serious a matter to be treated in
    such a fashion."
      "I have forged and tested every link of my chain, Professor
    Coram, and I am sure that it is sound. What your motives are, or
    what exact part you play in this strange business, I am not yet
    able to say. In a few minutes I shall probably hear it from your
    own lips. Meanwhile I will reconstruct what is past for your
    benefit, so that you may know the information which I still
    require.
      "A lady yesterday entered your study. She came with the
    intention of possessing herself of certain documents which were
    in your bureau. She had a key of her own. I have had an
    opportunity of examining yours, and I do not find that slight
    discolouration which the scratch made upon the varnish would
    have produced. You were not an accessory, therefore, and she
    came, so far as I can read the evidence, without your knowledge
    to rob you."
      The professor blew a cloud from his lips. "This is most
    interesting and instructive," said he. "Have you no more to
    add? Surely, having traced this lady so far, you can also say
    what has become of her."
      "I will endeavour to do so. In the first place she was seized
    by your secretary, and stabbed him in order to escape. This
    catastrophe I am inclined to regard as an unhappy accident, for I
    am convinced that the lady had no intention of inflicting so
    grievous an injury. An assassin does not come unarmed. Horri-
    fied by what she had done, she rushed wildly away from the
    scene of the tragedy. Unfortunately for her, she had lost her
    glasses in the scuffle, and as she was extremely shortsighted she
    was really helpless without them. She ran down a corridor,
    which she imagined to be that by which she had come -- both
    were lined with cocoanut matting -- and it was only when it was
    too late that she understood that she had taken the wrong pas-
    sage, and that her retreat was cut off behind her. What was she
    to do? She could not go back. She could not remain where she
    was. She must go on. She went on. She mounted a stair, pushed
    open a door, and found herself in your room."
      The old man sat with his mouth open, staring wildly at
    Holmes. Amazement and fear were stamped upon his expressive
    features. Now, with an effort, he shrugged his shoulders and
    burst into insincere laughter.
      "All very fine, Mr. Holmes," said he. "But there is one little
    flaw in your splendid theory. I was myself in my room, and I
    never left it during the day."
      "I am aware of that, Professor Coram."
      "And you mean to say that I could lie upon that bed and not
    be aware that a woman had entered my room?"
      "I never said so. You were aware of it. You spoke with her.
    You recognized her. You aided her to escape."
      Again the professor burst into high-keyed laughter. He had
    risen to his feet, and his eyes glowed like embers.
      "You are mad!" he cried. "You are talking insanely. I helped
    her to escape? Where is she now?"
      "She is there," said Holmes, and he pointed to a high book-
    case in the corner of the room.
      I saw the old man throw up his arms, a terrible convulsion
    passed over his grim face, and he fell back in his chair. At the
    same instant the bookcase at which Holmes pointed swung round
    upon a hinge, and a woman rushed out into the room. "You are
    right!" she cried, in a strange foreign voice. "You are right! I
    am here."
      She was brown with the dust and draped with the cobwebs
    which had come from the walls of her hiding-place. Her face,
    too, was streaked with grime, and at the best she could never
    have been handsome, for she had the exact physical characteris-
    tics which Holmes had divined, with, in addition, a long and
    obstinate chin. What with her natural blindness, and what with
    the change from dark to light, she stood as one dazed, blinking
    about her to see where and who we were. And yet, in spite of all
    these disadvantages, there was a certain nobility in the woman's
    bearing -- a gallantry in the defiant chin and in the upraised head,
    which compelled something of respect and admiration.
      Stanley Hopkins had laid his hand upon her arm and claimed
    her as his prisoner, but she waved him aside gently, and yet with
    an over-mastering dignity which compelled obedience. The old
    man lay back in his chair with a twitching face, and stared at her
    with brooding eyes.
      "Yes, sir, I am your prisoner," she said. "From where I
    stood I could hear everything, and I know that you have learned
    the truth. I confess it all. It was I who killed the young man. But
    you are right -- you who say it was an accident. I did not even
    know that it was a knife which I held in my hand, for in my
    despair I snatched anything from the table and struck at him to
    make him let me go. It is the truth that I tell."
      "Madam," said Holmes, "I am sure that it is the truth. I fear
    that you are far from well."
      She had turned a dreadful colour, the more ghastly under the
    dark dust-streaks upon her face. She seated herself on the side of
    the bed; then she resumed.
      "I have only a little time here," she said, "but I would have
    you to know the whole truth. I am this man's wife. He is not an
    Englishman. He is a Russian. His name I will not tell."
      For the first time the old man stirred. "God bless you, Anna!"
    he cried. "God bless you!"
      She cast a look of the deepest disdain in his direction. "Why
    should you cling so hard to that wretched life of yours, Sergius?"
    said she. "It has done harm to many and good to none -- not
    even to yourself. However, it is not for me to cause the frail
    thread to be snapped before God's time. I have enough already
    upon my soul since I crossed the threshold of this cursed house.
    But I must speak or I shall be too late.
      "I have said, gentlemen, that I am this man's wife. He was
    fifty and I a foolish girl of twenty when we married. It was in a
    city of Russia, a university -- I will not name the place."
      "God bless you, Anna!" murmured the old man again.
      "We were reformers -- revolutionists -- Nihilists, you under-
    stand. He and I and many more. Then there came a time of
    trouble, a police officer was killed, many were arrested, evi-
    dence was wanted, and in order to save his own life and to earn a
    great reward, my husband betrayed his own wife and his com-
    panions. Yes, we were all arrested upon his confession. Some of
    us found our way to the gallows, and some to Siberia. I was
    among these last, but my term was not for life. My husband
    came to England with his ill-gotten gains and has lived in quiet
    ever since, knowing well that if the Brotherhood knew where he
    was not a week would pass before justice would be done."
      The old man reached out a trembling hand and helped himself
    to a cigarette. "I am in your hands, Anna," said he. "You were
    always good to me."
      "I have not yet told you the height of his villainy," said she.
    "Among our comrades of the Order, there was one who was the
    friend of my heart. He was noble, unselfish, loving -- all that my
    husband was not. He hated violence. We were all guilty -- if that
    is guilt -- but he was not. He wrote forever dissuading us from
    such a course. These letters would have saved him. So would my
    diary, in which, from day to day, I had entered both my feelings
    towards him and the view which each of us had taken. My
    husband found and kept both diary and letters. He hid them, and
    he tried hard to swear away the young man's life. In this he
    failed, but Alexis was sent a convict to Siberia, where now, at
    this moment, he works in a salt mine. Think of that, you villain,
    you villain! -- now, now, at this very moment, Alexis, a man
    whose name you are not worthy to speak, works and lives like a
    slave, and yet I have your life in my hands, and I let you go."
      "You were always a noble woman, Anna," said the old man,
    puffing at his cigarette.
      She had risen, but she fell back again with a little cry of pain.
      "I must finish," she said. "When my term was over I set
    myself to get the diary and letters which, if sent to the Russian
    government, would procure my friend's release. I knew that my
    husband had come to England. After months of searching I dis-
    covered where he was. I knew that he still had the diary, for
    when I was in Siberia I had a letter from him once, reproaching
    me and quoting some passages from its pages. Yet I was sure
    that, with his revengeful nature, he would never give it to me of
    his own free-will. I must get it for myself. With this object I
    engaged an agent from a private detective firm, who entered my
    husband's house as a secretary -- it was your second secretary
    Sergius, the one who left you so hurriedly. He found that papers
    were kept in the cupboard, and he got an impression of the key.
    He would not go farther. He furnished me with a plan of the
    house, and he told me that in the forenoon the study was always
    empty, as the secretary was employed up here. So at last I took
    my courage in both hands, and I came down to get the papers for
    myself. I succeeded; but at what a cost!
      "I had just taken the papers and was locking the cupboard,
    when the young man seized me. I had seen him already that
    morning. He had met me on the road, and I had asked him to tell
    me where Professor Coram lived, not knowing that he was in his
    employ.
      "Exactly! Exactly!" said Holmes. "The secretary came back,
    and told his employer of the woman he had met. Then, in his last
    breath, he tried to send a message that it was she -- the she whom
    he had just discussed with him."
      "You must let me speak," said the woman, in an imperative
    voice, and her face contracted as if in pain. "When he had fallen
    I rushed from the room, chose the wrong door, and found myself
    in my husband's room. He spoke of giving me up. I showed him
    that if he did so, his life was in my hands. If he gave me to the
    law, I could give him to the Brotherhood. It was not that I
    wished to live for my own sake, but it was that I desired to
    accomplish my purpose. He knew that I would do what I said -- 
    that his own fate was involved in mine. For that reason, and for
    no other, he shielded me. He thrust me into that dark hiding-
    place -- a relic of old days, known only to himself. He took his
    meals in his own room, and so was able to give me part of his
    food. It was agreed that when the police left the house I should
    slip away by night and come back no more. But in some way
    you have read our plans." She tore from the bosom of her dress
    a small packet. "These are my last words," said she; "here is
    the packet which will save Alexis. I confide it to your honour
    and to your love of justice. Take it! You will deliver it at the
    Russian Embassy. Now, I have done my duty, and --"
      "Stop her!" cried Holmes. He had bounded across the room
    and had wrenched a small phial from her hand.
      "Too late!" she said, sinking back on the bed. "Too late! I
    took the poison before I left my hiding-place. My head swims! I
    am going! I charge you, sir, to remember the packet."
    
      "A simple case, and yet, in some ways, an instructive one,"
    Holmes remarked, as we travelled back to town. "It hinged from
    the outset upon the pince-nez. But for the fortunate chance of the
    dying man having seized these, I am not sure that we could ever
    have reached our solution. It was clear to me, from the strength
    of the glasses, that the wearer must have been very blind and
    helpless when deprived of them. When you asked me to believe
    that she walked along a narrow strip of grass without once
    making a false step, I remarked, as you may remember, that it
    was a noteworthy performance. In my mind I set it down as an
    impossible performance, save in the unlikely case that she had a
    second pair of glasses. I was forced, therefore, to consider
    seriously the hypothesis that she had remained within the house.
    On perceiving the similarity of the two corridors. it became clear
    that she might very easily have made such a mistake, and, in that
    case, it was evident that she must have entered the professor's
    room. I was keenly on the alert, therefore, for whatever would
    bear out this supposition, and I examined the room narrowly for
    anything in the shape of a hiding-place. The carpet seemed
    continuous and firmly nailed, so I dismissed the idea of a
    trap-door. There might well be a recess behind the books. As
    you are aware, such devices are common in old libraries. I ob-
    served that books were piled on the floor at all other points, but
    that one bookcase was left clear. This, then, might be the door. I
    could see no marks to guide me, but the carpet was of a dun
    colour, which lends itself very well to examination. I therefore
    smoked a great number of those excellent cigarettes, and I
    dropped the ash all over the space in front of the suspected
    bookcase. It was a simple trick, but exceedingly effective. I then
    went downstairs, and I ascertained, in your presence, Watson,
    without your perceiving the drift of my remarks, that Professor
    Coram's consumption of food had increased -- as one would
    expect when he is supplying a second person. We then ascended
    to the room again, when, by upsetting the cigarette-box, I ob-
    tained a very excellent view of the floor, and was able to see
    quite clearly, from the traces upon the cigarette ash, that the
    prisoner had in our absence come out from her retreat. Well
    Hopkins, here we are at Charing Cross, and I congratulate you
    on having brought your case to a successful conclusion. You are
    going to headquarters, no doubt. I think, Watson, you and I will
    drive together to the Russian Embassy."''',
    # -------------------------------------------------------------------
    '''They'd put flowers up. She hadn't noticed. Time wouldn't hold still.
    She remembered, quite clearly, that time had been a simple thing; one
    moment following the previous one, seconds strung out neatly like her
    mother's pearls laid out on the dark mahogany vanity each Sunday
    morning. But there had been a catch . . . 
    
    Hung around Mother's neck the catch clicked and the tidy little line 
    of seconds became a never ending circle with only the catch in the 
    middle. For some reason the thought of pearls gathered from the sea, 
    naturally nested within the confines of oyster shells, scattered 
    haphazardly about the ocean floor disturbed her.
    
    Now they'd put up the flowers in the same careless groupings. This,
    too, disturbed her. Bright yellow trumpets, their collars spread to
    catch the sun, dotted the front yard in clusters of two or three, five
    or six. Bunches laid carelessly and forgotten. In a moment she'd
    come away from the window and have a word with the gardener. He
    listened so well and explained to others so reasonably why this should
    be so instead of the way they wanted it done, how that would look
    better or cut the wind more effectively.
    
    And then she recalled his stiff body stretched out in the little bed
    over the garages. Another pearl had come loose from the strand,
    seeming to want to search out its old home in a far away oyster bed.
    She would have those pearls laid out neatly, one following the one
    before and so on and so on. She would have those damned yellow
    flowers marching smartly along the walk. She'd have it if she
    had to go out there and replant each and every one of them.
    
    She flew down the hallway and sailed over the steps leading the
    back way to the kitchen, much as she had done as a child. Where then
    she had skipped in joy she now catapulted her form in anger.
    
    "And there you are!" she said, as she encountered the woman she had 
    come to know as Kate. All of five foot tall in her stocking feet and 
    surely every bit of two hundred pounds, her pudgy fists more often 
    than not braced on the sudden outburst of her hips. So she stood, 
    having turned from the sink. Suds and water darkened the fabric of her 
    dress. Her face was pleasant; round, rosy cheeked, with eyes the color 
    of mint in the summer sunset. "And *where have you been these three days*?"
    
    "I want the flowers straightened out," Rebeccah said. "I want the
    flowers placed in the proper alignments."
    
    Kate tilted her head, narrowed her eyes and frowned. "Ah, you're in a
    huff again. What can it be this time?"
    
    "I want the flours straightened out," Rebeccah yelled, coming up to
    the woman's face.
    
    Kate went directly to the cupboard, strained upon her tiny toes to
    reach the second shelf, and pulled the flour canister out. She set it
    on the counter. She repeated the process, bringing out a smaller
    canister. Rebecca knew this one to be the unbleached flour Kate used
    for one particular recipe.
    
    "No,no, no!"  Rebeccah hissed. "Flowers!  Not flours!"  She propped
    herself against the edge of the kitchen table and crossed her arms
    over her chest, waiting for the woman to get it right.
    
    Kate stood looking dumbly at the canisters. "Now, what was I going to
    do with these?"  she asked herself. She drummed her fingers on the
    counter top before bringing one hand to her lips, where the pointer
    finger tapped on her upper lip.
    
    "The Flowers!  Outside!"  Rebecca screamed, highly agitated.
    
    Kate gathered the two canisters and moved toward the back door, one
    held against her ample form by each arm.
    
    Exasperated, Rebeccah followed her out, watching to see what she would do.
    
    Without the drive of Rebeccah's insistence, Kate lost her momentum.
    She stood next a slatted oak bench, canisters still clutched, surveying 
    the sunlit yard and gardens beyond. Harold had done a passable job 
    trimming the hedges, but Kate missed the gardener's touch. She resolved 
    to contact the nursery and find another. Flaux, bright purples, pinks 
    and radiant white encircled the herb garden, a brilliant contrast to 
    the varied greens within. She set the canisters down on the bench and 
    moved toward the cheerful scene.
    
    Rebeccah, discouraged, sat primly on the edge of the bench, dusting a
    wisp of hair away from her temple. New mint, dew draped, veiled a
    border of stocky wooden poles to trail onto the walk, had been crushed, 
    probably by the man of the house on his way off to work. The scent 
    filled her nostrils. She found herself a child, again, tasting her 
    first tea with mint -- fresh cut from the gardens. _"How long has it
    been?"_  she wondered. Kate had gone down on her knees over the flaux,
    bending to weed through the thyme.
    
    "I don't know why I have to put up with idiots," Rebeccah complained.
    "It all so worthless, so futile."  With a great sigh she rose from the
    bench and made her way back into the house. The bright kitchen seemed
    a waste of life, all a travesty to cover the desolation of her
    unnaturally extended existence. 
    
    She faced the stairs with exhaustion, deciding, instead, to forego the 
    trip up. She sat on the bottom step, delicate chin propped on tightly 
    curled fists, gazing dully at the open pantry door, seeing into the past 
    -- again. Where, in this world the shelves were haphazardly stacked with 
    cans of peaches and corn, she saw row after row of glass jars. Beets!  
    Ugh!  Her grandmother's pickled beets, always pretty to view, left a 
    phantom bitterness within her mouth.
    
    On the lawn Kate sat back on her heels, suddenly lost in sorrow and
    self-pity. Tears streamed down her cheeks to drop onto the fabric of
    her dress. She thought of Harold, busily showing homes as lovely as
    their own to strangers while she ruined her nails weeding this pitiful
    excuse for a garden. She shoved her pudgy fists into her burning eyes
    and wept aloud for the waste of her life. She sniffed back her running 
    nose . . . sniffed again. She snuffled like a dog scenting something 
    unusual, nose in the air. "Beets?"  she asked aloud. "Beets?"  Her 
    hands dropped to her thighs, pushing to rise. _"Of course,"_ she thought 
    to herself, _"this *lovely* house is haunted by a very emotional woman."_  
    Her knees ached. She turned toward the house and noticed the flour 
    canisters on the bench. "And whatever she wants *this* time is not 
    getting through this thick skull of mine!"
    
    Kate knuckle-rapped herself above her right temple. "Rebeccah!"  she
    called. "Quit moping!  You'll ruin another day for me and I still
    have to deal with that horrible Avon woman this morning."
    
    "I want my flowers properly aligned!" Rebeccah screamed from the stairs.
    
    As Kate passed the bench she paused to move the flour canisters so
    that the labels faced in the same direction, each perfectly centered
    over three of the wood slats. With a self-satisfied air she re-entered 
    her own kitchen. "Now," she began, addressing the refrigerator, "what 
    we need is improved communication."
    
    "Fool," hissed Rebeccah, "you're talking to the refrigerator again."
    
    "You don't want an empath. You want a telepath," Kate said, turning
    to stare at Rebeccah with surprising accuracy.
    
    The two women blinked at each other and broke into laughter.
    
    "I want my flowers straightened out!"  Rebeccah commented softly when
    the mirth had passed.
    
                                  * * *
    
    "There!"  Kate replaced the telephone hand piece and pocketed the
    scrap of paper she'd written the new gardener's name upon. "Mr.
    Hi-a-cow-wah," she practiced aloud. "Very good."  The door chime rang
    throughout the house, echoing off the tiled kitchen walls.
    
    "Oh, no!"  wailed Rebeccah. "Not Japanese!  They have such spiritual
    ideas on gardening -- I'll never get through to him!"
    
    "Oh, dear!"  Kate bemoaned, certain the Avon woman had come to call.
    She brushed her hands over her skirt, straightened her broad shoulders
    and pushed through to the dining room, determined not to buy a single
    thing today.
    
    "Good morning, Mrs. Blanchard!"  beamed the woman in the pale rose
    colored ensemble. Purse clutched in one hand, sample case in the other, 
    she reminded Kate of the Lady Justice, scales perfectly balanced. But 
    this lady had no blindfold. (All the better to see you with, my dear. 
    And Oh, wouldn't this color just bring on the blush in your cheeks for 
    $11.00 a tube?)  "Isn't it just a glorious day?" the woman pronouned, 
    boldly stepping over the threshold on past assumptions.
    
    _"That's it!"_ Kate thought to herself. She'd let the woman in once,
    bought gifts soaps and lipstick in the spirit of cooperation, and
    never been free of past assumptions since. "Glorious!" Kate echoed,
    moving aside before she was trod upon. Rebeccah hovered at the dining
    room doors. Kate felt her there.
    
    "Oh, and you've brought the day in with you!" exclaimed the woman,
    noting cut flowers on mantel and coffee table. "How healthful!"
    
    "Healthful?" Kate inquired.
    
    "Oh, yes. Studies have shown that people who surround themselves with
    live plants and fresh flowers indoors live longer, feel better, and
    enjoy life more fully."
    
    "Coffee?"  Kate offered as the woman sat on the edge of the sofa. It
    was the one torment she allowed herself to use on the woman, knowing
    full well this door to door saleswoman would shun other people's
    bathrooms.
    
    "No thank you," she answered, a slight grimace flashing across her
    face as she scooted forward and opened her case.
    
    "You're so rude!" Rebeccah crowed, having come closer. "She's got a
    bladder full now."
    
    Kate smiled, holding back a giggle. She was certain she'd scored
    without knowing why. The woman drew forth brightly colored sheets of
    paper and placed them neatly before Kate on the glass topped table.
    _"A promotional,"_ Kate moaned within her mind. At the bottom of each
    was stamped, in flowing script, "Eleanor Thomsason."  Address and two
    phone numbers followed in block lettering.
    
    "I don't really need anything today, Eleanor," Kate began.
    
    "Of course you don't, dear. You're more than lovely in your house
    frock and clean scrubbed face. But you must see the new complexion
    care line we're offering. Designed especially for the woman over 30
    and her special needs," Eleanor pulled full sized display item from
    the depths of her bottomless case and set them neatly in a row,
    labels facing the prospective buyer. "As you can see here," she said
    crisply, long manicured finger nail tapping each item gently as she
    spoke, "We have a scrub, toner, tightener, moisturizer and light
    foundation. The foundation comes in 6 basic colors. Just to smooth
    over those tiny blotches we all seem to have after 30."
    
    Kate sat forward in her occasional chair, considering the possibility
    that she might, indeed, need a little more complexion care. She
    touched the toner, tilting it slightly to the light. While she was
    otherwise engaged Eleanor brought forth tubes, bottles and jars of the
    same line. She busied herself arranging them in a straight line to
    the left and just behind the first row.
    
    "And here we have the corresponding blush, highlighters, lipsticks 
    and shadows. Now this line is made with completely natural base
    substances," Eleanor pointed out.
    
    "Chemicals," Rebeccah commented, coming closer still, intently
    interested in the ordered presentation.
    
    Kate let go the toner and reached for the blush. Eleanor straightened
    the toner, turning the label toward the prospective buyer. Rebeccah
    came around the coffee table and sat on the sofa with Eleanor, her
    arms primly at her sides, hands clasped in her lap. Rebeccah leaned
    forward in the same manner as did Eleanor.
    
    The genial rise and fall of the woman's voice slipped into the background 
    of sounds passing by on the peaceful street outside. Kate blinked once, 
    the blush still clasped within her fingers, watching Eleanor's lips move. 
    She could almost hear Rebeccah.
    
    Rebeccah's attention was focused entirely on Eleanor the Avon lady.
    "The flowers have been scattered willy-nilly along the walk,"
    Rebeccah said conversationally, her lips mere inches from Eleanor's
    ear. "They look so untidy."  Eleanor looked, suddenly, as if she'd
    forgotten something. Kate remembered the flour canisters on the
    bench. "What we need is someone with some organizational ability,"
    Rebeccah continued. 
    
    Eleanor drew forth her order book. "Flowers are like life's little 
    markers," Rebeccah whispered. Eleanor reached into her case for a 
    marker. "Yellow markers, as it were, for the days of our lives."  
    Eleanor replaced the fine tipped black marker and retrieved a broad 
    stroke yellow highlighter. Kate seemed to hear McDonald Carey speaking 
    about sand. "The flowers along the walk NEED straightening."
    
    "Will you excuse me, just one moment?" Kate asked. She knew exactly
    where to find that hourglass. She rose from her chair
    
    "Certainly, dear," Eleanor answered, her mind seemingly elsewhere
    while her hands compulsively aligned the display items.
    
    "*YOU* could be the only one for the job!"  Rebeccah spoke
    authoritatively, her body turned toward Eleanor. "The flowers need
    alignment!"
    
    Kate felt an oppressive headache coming on. Two of them in one
    morning was more than anyone should be expected to bear. As she
    passed through the kitchen door her spirits seemed to rise suddenly.
    Sunshine slanted into the room to highlight every gleaming surface,
    glinting sweetly on glassware and chrome. She inhaled fully, filling
    her lungs with the aroma of fresh brewed coffee. The hourglass
    spilling out the days of her life seemed important only in the
    abstract. All was right today. She thought of the flowers by the
    walk, then. For some reason she  wanted to see them from the top
    floor.
    
    She poured herself a cup of coffee, carried it up the back stairs to
    the second floor landing and peered from the window into the side
    yard. She thought, idly, of the new gardener, and what creative
    expression he might come up with for that spot there, which had never
    been cultivated. Onward, to the front of the house, and into the
    quiet room beneath the pitch of the front eaves. 
    
    She sat on the window ledge and balanced her cup on the sill, the 
    threatened headache a memory, only, of Saturday afternoons with her 
    mother. Somewhere behind her temples her mother's voice droned on and 
    on; something about book spines and the edge of the shelf. Sometimes 
    one had to learn to ignore the librarian in order to read the books.
    
    Her eyes drifted to the front walk. Far below, as if in another
    world, Eleanor the Avon lady knelt in the grass next to the walk.
    A tall shadow stood near, softly, insistently coaxing, as Eleanor
    carefully spaded deep into the earth and removed a daffodil. She
    placed it gently into a prepared hole, tamped the earth around it and
    proceeded to dig another hole, exactly six inches from the last, in a
    perfectly straight line parallel to the walk.
    
    "Oh, for crying out loud!"  Kate exclaimed, watching closely. "Those
    flowers!"  She'd have to remember to collect the flour canisters
    before Harold came home. "Goodness, Rebeccah," she continued, with
    some exasperation, "why on earth didn't you say `Daffodils'?"''',
    # -------------------------------------------------------------------
    '''A young man wished to purchase a present for his sweetheart,
    and after careful consideration he decided on a pair of gloves. 
    Accompanied by his sweetheart's sister, he went to a department
    store and bought a pair of white gloves.  The sister purchased a
    pair of panties for herself.  During the wrapping the items got
    mixed up.  The sister got the gloves and the sweetheart got the
    panties.  Without checking he sealed the package and sent it to her
    with this note.
    
    
    Dearest Darling,
    
         This is a little gift to show you I have not forgotten your
    birthday.  I chose these because I noticed that you are not in the
    habit of wearing any when we go out in the evening.  If it had not
    been for your sister, I would have chosen the long ones with the
    buttons, but she wears the short ones that are very easy to remove. 
    These are a delicate shade, but the lady I bought them from showed
    me a pair she had been wearing for three weeks and they were hardly
    soiled.  I had the sales girl try them on for me the first time. 
    No doubt other men's hands will come in contact with them before I
    have a chance to see you again.
    
         When you take them off, blow in them before putting them away
    as they will naturally be a little damp from wearing.
    
         Be sure to keep them on when you clean them or they might
    shrink.  I hope you will like them and wear them on Friday night.
    
                                                         ALL MY LOVE,
    
    P.S.  Just think how many times I will kiss them during the coming
    year.  Also, the latest style is to wear them folded down with the
    fur showing.''',
    # -------------------------------------------------------------------
    '''Many years ago, I contracted an intimacy with a Mr. William
    Legrand. He was of an ancient Huguenot family, and had once been
    wealthy; but a series of misfortunes had reduced him to want. To
    avoid the mortification consequent upon his disasters, he left
    New Orleans, the city of his forefathers, and took up his
    residence at Sullivan's Island, near Charleston, South Carolina.
    
    This island is a very singular one. It consists of little else
    than the sea sand, and is about three miles long. Its breadth at
    no point exceeds a quarter of a mile. It is separated from the
    mainland by a scarcely perceptible creek, oozing its way through
    a wilderness of reeds and slime, a favorite resort of the
    marsh-hen. The vegetation, as might be supposed, is scant, or at
    least dwarfish. No trees of any magnitude are to be seen. Near
    the western extremity, where Fort Moultrie stands, and where are
    some miserable frame buildings, tenanted, during summer, by the
    fugitives from Charleston dust and fever, may be found, indeed,
    the bristly palmetto; but the whole island, with the exception of
    this western point, and a line of hard, white beach on the
    sea-coast, is covered with a dense undergrowth of the sweet
    myrtle so much prized by the horticulturists of England. The
    shrub here often attains the height of fifteen or twenty feet,
    and forms an almost impenetrable coppice, burthening the air with
    its fragrance.
    
    In the inmost recesses of this coppice, not far from the eastern
    or more remote end of the island, Legrand had built himself a
    small hut, which he occupied when I first, by mere accident, made
    his acquaintance. This soon ripened into friendship--for there was
    much in the recluse to excite interest and esteem. I found him
    well educated, with unusual powers of mind, but infected with
    misanthropy, and subject to perverse moods of alternate
    enthusiasm and melancholy. He had with him many books, but rarely
    employed them. His chief amusements were gunning and fishing, or
    sauntering along the beach and through the myrtles, in quest of
    shells or entomological specimens--his collection of the latter
    might have been envied by a Swammerdamm. In these excursions he
    was usually accompanied by an old negro, called Jupiter, who had
    been manumitted before the reverses of the family, but who could
    be induced, neither by threats nor by promises, to abandon what
    he considered his right of attendance upon the footsteps of his
    young "Massa Will." It is not improbable that the relatives of
    Legrand, conceiving him to be somewhat unsettled in intellect,
    had contrived to instil this obstinacy into Jupiter, with a view
    to the supervision and guardianship of the wanderer.
    
    The winters in the latitude of Sullivan's Island are seldom very
    severe, and in the fall of the year it is a rare event indeed
    when a fire is considered necessary. About the middle of October,
    18--, there occurred, however, a day of remarkable chilliness.
    Just before sunset I scrambled my way through the evergreens to
    the hut of my friend, whom I had not visited for several weeks--my
    residence being, at that time, in Charleston, a distance of nine
    miles from the island, while the facilities of passage and
    re-passage were very far behind those of the present day. Upon
    reaching the hut I rapped, as was my custom, and getting no
    reply, sought for the key where I knew it was secreted, unlocked
    the door, and went in. A fine fire was blazing upon the hearth.
    It was a novelty, and by no means an ungrateful one. I threw off
    an overcoat, took an arm-chair by the crackling logs, and awaited
    patiently the arrival of my hosts.
    
    Soon after dark they arrived, and gave me a most cordial welcome.
    Jupiter, grinning from ear to ear, bustled about to prepare some
    marsh-hens for supper. Legrand was in one of his fits--how else
    shall I term them?--of enthusiasm. He had found an unknown
    bivalve, forming a new genus, and, more than this, he had hunted
    down and secured, with Jupiter's assistance, a scarabaeus which he
    believed to be totally new, but in respect to which he wished to
    have my opinion on the morrow.
    
    "And why not to-night?" I asked, rubbing my hands over the blaze,
    and wishing the whole tribe of scarabaei at the devil.
    
    "Ah, if I had only known you were here!" said Legrand, "but it's
    so long since I saw you; and how could I foresee that you would
    pay me a visit this very night of all others? As I was coming
    home I met Lieutenant G----, from the fort, and, very foolishly, I
    lent him the bug; so it will be impossible for you to see it
    until the morning. Stay here to-night, and I will send Jup down
    for it at sunrise. It is the loveliest thing in creation!"
    
    "What?--sunrise?"
    
    "Nonsense! no!--the bug. It is of a brilliant gold color--about the
    size of a large hickory-nut--with two jet black spots near one
    extremity of the back, and another, somewhat longer, at the
    other. The antennae are--"
    
    "Dey aint no tin in him, Massa Will, I keep a tellin' on you,"
    here interrupted Jupiter; "de bug is a goole-bug, solid, ebery
    bit of him, inside and all, sep him wing--meber feel half so hebby
    a bug in my life."
    
    "Well, suppose it is, Jup," replied Legrand, somewhat more
    earnestly, it seemed to me, than the case demanded; "is that any
    reason for you letting the birds burn? The color"--here he turned
    to me--"is really almost enough to warrant Jupiter's idea. You
    never saw a more brilliant metallic lustre than the scales
    emit--but of this you cannot judge till tomorrow. In the meantime
    I can give you some idea of the shape." Saying this, he seated
    himself at a small table, on which were a pen and ink, but no
    paper. He looked for some in a drawer, but found none.
    
    "Never mind," he said at length, "this will answer"; and he drew
    from his waistcoat pocket a scrap of what I took to be very dirty
    foolscap, and made upon it a rough drawing with the pen. While he
    did this, I retained my seat by the fire, for I was still chilly.
    When the design was complete, he handed it to me without rising.
    As I received it, a loud growl was heard, succeeded by a
    scratching at the door. Jupiter opened it, and a large
    Newfoundland, belonging to Legrand, rushed in, leaped upon my
    shoulders, and loaded me with caresses; for I had shown him much
    attention during previous visits. When his gambols were over, I
    looked at the paper, and, to speak the truth, found myself not a
    little puzzled at what my friend had depicted.
    
    "Well!" I said, after contemplating it for some minutes, "this is
    a strange scarabaeus, I must confess; new to me; never saw any
    thing like it before--unless it was a skull, or a death's-head,
    which it more nearly resembles than any thing else that has come
    under my observation."
    
    "A death's-head!" echoed Legrand. "Oh--yes--well, it has something
    of that appearance upon paper, no doubt. The two upper black
    spots look like eyes, eh? and the longer one at the bottom like a
    mouth--and then the shape of the whole is oval."
    
    "Perhaps so," said I; "but, Legrand, I fear you are no artist. I
    must wait until I see the beetle itself, if I am to form any idea
    of its personal appearance."
    
    "Well, I don't know," said he, a little nettled, "I draw
    tolerably--should do it at least--have had good masters, and
    flatter myself that I am not quite a blockhead."
    
    "But, my dear fellow, you are joking then," said I, "this is a
    very passable skull--indeed, I may say that it is a very excellent
    skull, according to the vulgar notions about such specimens of
    physiology--and your scarabaeus must be the queerest scarabaeus in
    the world if it resembles it. Why, we may get up a very thrilling
    bit of superstition upon this hint. I presume you will call the
    bug scarabaeus caput hominis, or something of that kind--there are
    many similar titles in the Natural Histories. But where are the
    antennae you spoke of?"
    
    "The antennae!" said Legrand, who seemed to be getting
    unaccountably warm upon the subject; "I am sure you must see the
    antennae. I made them as distinct as they are in the original
    insect, and I presume that is sufficient."
    
    "Well, well," I said, "perhaps you have--still I don't see them";
    and I handed him the paper without additional remark, not wishing
    to ruffle his temper; but I was much surprised at the turn
    affairs had taken; his ill humor puzzled me--and, as for the
    drawing of the beetle, there were positively no antennae visible,
    and the whole did bear a very close resemblance to the ordinary
    cuts of a death's-head.
    
    He received the paper very peevishly, and was about to crumple
    it, apparently to throw it in the fire, when a casual glance at
    the design seemed suddenly to rivet his attention. In an instant
    his face grew violently red--in another as excessively pale. For
    some minutes he continued to scrutinize the drawing minutely
    where he sat. At length he arose, took a candle from the table,
    and proceeded to seat himself upon a sea-chest in the farthest
    corner of the room. Here again he made an anxious examination of
    the paper; turning it in all directions. He said nothing,
    however, and his conduct greatly astonished me; yet I thought it
    prudent not to exacerbate the growing moodiness of his temper by
    any comment. Presently he took from his coat-pocket a wallet,
    placed the paper carefully in it, and deposited both in a
    writing-desk, which he locked. He now grew more composed in his
    demeanor; but his original air of enthusiasm had quite
    disappeared. Yet he seemed not so much sulky as abstracted. As
    the evening wore away he became more and more adsorbed in revery,
    from which no sallies of mine could arouse him. It had been my
    intention to pass the night at the hut, as I had frequently done
    before, but, seeing my host in this mood, I deemed it proper to
    take leave. He did not press me to remain, but, as I departed, he
    shook my hand with even more than his usual cordiality.
    
    It was about a month after this (and during the interval I had
    seen nothing of Legrand) when I received a visit, at Charleston,
    from his man, Jupiter. I had never seen the good old negro look
    so dispirited, and I feared that some serious disaster had
    befallen my friend.
    
    "Well, Jup," said I, "what is the matter now?--how is your
    master?"
    
    "Why, to speak de troof, massa, him not so berry well as mought
    be."
    
    "Not well! I am truly sorry to hear it. What does he complain
    of?"
    
    "Dar! dat's it!--him neber 'plain of notin'--but him berry sick for
    all dat."
    
    "Very sick, Jupiter!--why didn't you say so at once? Is he
    confined to bed?"
    
    "No, dat he aint!--he aint 'fin'd nowhar--dat's just whar de shoe
    pinch--my mind is got to be barry hebby 'bout poor Massa Will."
    
    "Jupiter, I should like to understand what it is you are talking
    about. You say your master is sick. Hasn't he told you what ails
    him?"
    
    "Why, massa, 'taint worf while for to git mad about de
    matter--Massa Will say noffin at all aint de matter wid him--but
    den what make him go about looking dis here way, wid he head down
    and he soldiers up, and as white as a gose? And den he keep a
    syphon all de time--"
    
    "Keeps a what, Jupiter?"
    
    "Keeps a syphon wid de figgurs on de slate--de queerest figgurs I
    ebber did see. Ise gittin' to be skeered, I tell you. Hab for to
    keep mighty tight eye 'pon him 'noovers. Todder day he gib me
    slip 'fore de sun up and was gone de whole ob de blessed day. I
    had a big stick ready cut for to gib him deuced good beating when
    he did come--but Ise sich a fool dat I hadn't de heart arter
    all--he looked so berry poorly."
    
    "Eh?--what?--ah yes!--upon the whole I think you had better not be
    too severe with the poor fellow--don't flog him, Jupiter--he can't
    very well stand it--but can you form no idea of what has
    occasioned this illness, or rather this change of conduct? Has
    any thing unpleasant happened since I saw you?"
    
    "No, massa, dey aint bin noffin onpleasant since den--'twas 'fore
    den I'm feared--'twas de berry day you was dare."
    
    "How? what do you mean?"
    
    "Why, massa, I mean de bug--dare now."
    
    "The what?"
    
    "De bug--I'm berry sartain dat Massa Will bin bit somewhere 'bout
    de head by dat goole-bug."
    
    "And what cause have you, Jupiter, for such a supposition?"
    
    "Claws enuff, massa, and mouff too. I nebber did see sich a
    deuced bug--he kick and he bite ebery ting what cum near him.
    Massa Will cotch him fuss, but had for to let him go 'gin mighty
    quick, I tell you--den was de time he must ha' got de bite. I
    didn't like de look ob de bug mouff, myself, nohow, so I wouldn't
    take hold ob him wid my finger, but I cotch him wid a piece ob
    paper dat I found. I rap him up in de paper and stuff a piece of
    it in he mouff--dat was de way."
    
    "And you think, then, that you master was really bitten by the
    beetle, and that the bite made him sick?"
    
    "I don't think noffin' about it--I nose it. What make him dream
    'bout de goole so much, if 'taint cause he bit by de goole-bug?
    Ise heerd 'bout dem goole-bugs 'fore dis."
    
    "But how do you know he dreams about gold?"
    
    "How I know? why, 'cause he talk about it in he sleep--dat's how I
    nose."
    
    "Well, Jup, perhaps you are right; but to what fortunate
    circumstance am I to attribute the honor of a visit from you
    to-day?"
    
    "What de matter, massa?"
    
    "Did you bring any message from Mr. Legrand?"
    
    "No, massa, I bring dis here pissel"; and here Jupiter handed me
    a note which ran thus:
    
    "My Dear ----
         "Why have I not seen you for so long a time? I hope you have
    not been so foolish as to take offence at any little brusquerie
    of mine; but no, that is improbable.
         "Since I saw you I have had great cause for anxiety. I have
    something to tell you, yet scarcely know how to tell it, or
    whether I should tell it at all.
         "I have not been quite well for some days past, and poor old
    Jup annoys me, almost beyond endurance, by his well-meant
    attentions. Would you believe it?--he had prepared a huge stick,
    the other day, with which to chastise me for giving him the slip,
    and spending the day, solus, among the hills on the main land. I
    verily believe that my ill looks alone saved me a flogging.
         "I have made no addition to my cabinet since we met.
         "If you can, in any way, make it convenient, come over with
    Jupiter. Do come. I wish to see you to-night, upon business of
    importance. I assure you that it is of the highest importance.
                             "Ever yours,
                                            "William Legrand"
    
    There was something in the tone of this note which gave me great
    uneasiness. Its whole style differed materially from that of
    Legrand. What could he be dreaming of? What new crotchet
    possessed his excitable brain? What "business of the highest
    importance" could he possibly have to transact? Jupiter's account
    of him boded no good. I dreaded lest the continued pressure of
    misfortune had, at length, fairly unsettled the reason of my
    friend. Without a moment's hesitation, therefore, I prepared to
    accompany the negro.
    
    Upon reaching the wharf, I noticed a scythe and three spades, all
    apparently new, lying in the bottom of the boat in which we were
    to embark.
    
    "What is the meaning of all this, Jup?" I inquired.
    
    "Him syfe, massa, and spade."
    
    "Very true; but what are they doing here?"
    
    "Him de syfe and de spade what Massa Will sis 'pon me buying for
    him in de town, and de debbil's own lot of money I had to gib for
    'em."
    
    "But what, in the name of all that is mysterious, is your `Massa
    Will' going to do with scythes and spades?"
    
    "Dat's more dan I know, and debbil take me if I don't b'lieve
    'tis more dan he know too. But it's all cum ob de bug."
    
    Finding that no satisfaction was to be obtained of Jupiter, whose
    whole intellect seemed to be absorbed by "de bug," I now stepped
    into the boat, and made sail. With a fair and strong breeze we
    soon ran into the little cove to the northward of Fort Moultrie,
    and a walk of some two miles brought us to the hut. It was about
    three in the afternoon when we arrived. Legrand had been waiting
    us in eager expectation. He grasped my hand with a nervous
    empressement which alarmed me and strengthened the suspicions
    already entertained. His countenance was pale even to
    ghastliness, and his deep-set eyes glared with unnatural lustre.
    After some enquiries respecting his health, I asked him, not
    knowing what better to say, if he had yet obtained the scarabaeus
    from Lieutenant G----.
    
    "Oh, yes," he replied, coloring violently, "I got it from him the
    next morning. Nothing should tempt me to part with that
    scarabaeus. Do you know that Jupiter is quite right about it?"
    
    "In what way?" I asked, with a sad foreboding at heart.
    
    "In supposing it to be a bug of real gold." He said this with an
    air of profound seriousness, and I felt inexpressibly shocked.
    
    "This bug is to make my fortune," he continued, with a triumphant
    smile; "to reinstate me in my family possessions. Is it any
    wonder, then, that I prize it? Since Fortune has thought fit to
    bestow it upon me, I have only to use it properly, and I shall
    arrive at the gold of which it is the index. Jupiter, bring me
    that scarabaeus!"
    
    "What! de bug, massa? I'd rudder not go fer trubble dat bug; you
    mus' git him for your own self." Hereupon Legrand arose, with a
    grave and stately air, and brought me the beetle from a glass
    case in which it was enclosed. It was a beautiful scarabaeus, and,
    at that time, unknown to naturalists--of course a great prize in a
    scientific point of view. There were two round black spots near
    one extremity of the back, and a long one near the other. The
    scales were exceedingly hard and glossy, with all the appearance
    of burnished gold. The weight of the insect was very remarkable,
    and, taking all things into consideration, I could hardly blame
    Jupiter for his opinion respecting it; but what to make of
    Legrand's concordance with that opinion, I could not, for the
    life of me, tell.
    
    "I sent for you," said he, in a grandiloquent tone, when I had
    completed my examination of the beetle, "I sent for you that I
    might have your counsel and assistance in furthering the views of
    Fate and of the bug--"
    
    "My dear Legrand," I cried, interrupting him, "you are certainly
    unwell, and had better use some little precautions. You shall go
    to bed, and I will remain with you a few days, until you get over
    this. You are feverish and--"
    
    "Feel my pulse," said he.
    
    I felt it, and, to say the truth, found not the slightest
    indication of fever.
    
    "But you may be ill and yet have no fever. Allow me this once to
    prescribe for you. In the first place go to bed. In the next--"
    
    "You are mistaken," he interposed, "I am as well as I can expect
    to be under the excitement which I suffer. If you really wish me
    well, you will relieve this excitement."
    
    "And how is this to be done?"
    
    "Very easily. Jupiter and myself are going upon an expedition
    into the hills, upon the main land, and, in this expedition, we
    shall need the aid of some person in whom we can confide. You are
    the only one we can trust. Whether we succeed or fail, the
    excitement which you now perceive in me will be equally allayed."
    
    "I am anxious to oblige you in any way," I replied; "but do you
    mean to say that this infernal beetle has any connection with
    your expedition into the hills?"
    
    "It has."
    
    "Then, Legrand, I can become a party to no such absurd
    proceeding."
    
    "I am sorry--very sorry--for we shall have to try it by ourselves."
    
    "Try it by yourselves! The man is surely mad!--but stay!--how long
    do you propose to be absent?"
    
    "Probably all night. We shall start immediately, and be back, at
    all events, by sunrise."
    
    "And will you promise me, upon your honor, that when this freak
    of yours is over, and the bug business (good God!) settled to
    your satisfaction, you will then return home and follow my advice
    implicitly, as that of your physician."
    
    "Yes; I promise; and now let us be off, for we have no time to
    lose."
    
    With a heavy heart I accompanied my friend. We started about four
    o'clock--Legrand, Jupiter, the dog, and myself. Jupiter had with
    him the scythe and spades--the whole of which he insisted upon
    carrying--more through fear, it seemed to me, of trusting either
    of the implements within reach of his master, than from any
    excess of industry or complaisance. His demeanor was dogged in
    the extreme, and "dat deuced bug" were the sole words which
    escaped his lips during the journey. For my own part, I had
    charge of a couple of dark lanterns, while Legrand contented
    himself with the scarabaeus, which he carried attached to the end
    of a bit of whip-cord; twirling it to and fro, with the air of a
    conjuror, as he went. When I observed this last, plain evidence
    of my friend's aberration of mind, I could scarcely refrain from
    tears. I thought it best, however, to humor his fancy, at least
    for the present, or until I could adopt some more energetic
    measures with a chance of success. In the meantime I endeavored,
    but all in vain, to sound him in regard to the object of the
    expedition. Having succeeded in inducing me to accompany him, he
    seemed unwilling to hold conversation upon any topic of minor
    importance, and to all my questions vouchsafed no other reply
    than "we shall see!"
    
    We crossed the creek at the head of the island by means of a
    skiff, and, ascending the high grounds on the shore of the main
    land, proceeded in a northwesterly direction, through a tract of
    country excessively wild and desolate, where no trace of a human
    footstep was to be seen. Legrand led the way with decision;
    pausing only for an instant, here and there, to consult what
    appeared to be certain landmarks of his own contrivance upon a
    former occasion.
    
    In this manner we journed for about two hours, and the sun was
    just setting when we entered a region infinitely more dreary than
    any yet seen. It was a species of table-land, near the summit of
    an almost inaccessible hill, densely wooded from base to
    pinnacle, and interspersed with huge crags that appeared to lie
    loosely upon the soil, and in many cases were prevented from
    precipitating themselves into the valleys below, merely by the
    support of the trees against which they reclined. Deep ravines,
    in various directions, gave an air of still sterner solemnity to
    the scene.
    
    The natural platform to which we had clambered was thickly
    overgrown with brambles, through which we soon discovered that it
    would have been impossible to force our way but for the scythe;
    and Jupiter, by direction of his master, proceeded to clear for
    us a path to the foot of an enormously tall tulip-tree, which
    stood, with some eight or ten oaks, upon the level, and far
    surpassed them all, and all other trees which I had then ever
    seen, in the beauty of its foliage and form, in the wide spread
    of its branches, and in the general majesty of its appearance.
    When we reached this tree, Legrand turned to Jupiter, and asked
    him if he thought he could climb it. The old man seemed a little
    staggered by the question, and for some moments made no reply. At
    length he approached the huge trunk, walked slowly around it, and
    examined it with minute attention. When he had completed his
    scrutiny, he merely said:
    
    "Yes, massa, Jup climb any tree he ebber see in he life."
    
    "Then up with you as soon as possible, for it will soon be too
    dark to see what we are about."
    
    "How far mus' go up, massa?" inquired Jupiter.
    
    "Get up the main trunk first, and then I will tell you which way
    to go--and here--stop! take this beetle with you."
    
    "De bug, Massa Will!--de goole-bug!" cried the negro, drawing back
    in dismay--"What for mus' tote de bug way up de tree?--d--n if I
    do!"
    
    "If you are afraid, Jup, a great big negro like you, to take hold
    of a harmless little dead beetle, why you can carry it up by this
    string--but, if you do not take it up with you in some way, I
    shall be under the necessity of breaking your head with this
    shovel."
    
    "What de matter now, massa?" said Jup, evidently shamed into
    compliance; "always want for to raise fuss wid old nigger. Was
    only funnin anyhow. Me feered de bug! what I keer for de bug?"
    Here he took cautiously hold of the extreme end of the string,
    and, maintaining the insect as far from his person as
    circumstances would permit, prepared to ascend the tree.
    
    In youth, the tulip-tree, or Liriodendron Tulipiferum, the most
    magnificent of American foresters, has a trunk peculiarly smooth,
    and often rises to a great height without lateral branches; but
    in its riper age, the bark becomes gnarled and uneven, while many
    short limbs make their appearance on the stem. Thus the
    difficulty of ascension, in the present case, lay more in
    semblance than in reality. Embracing the huge cylinder, as
    closely as possible, with his arms and knees, seizing with his
    hands some projections, and resting his naked toes upon others,
    Jupiter, after one or two narrow escapes from falling, at length
    wriggled himself into the first great fork, and seemed to
    consider the whole business as virtually accomplished. The risk
    of the achievement was, in fact, now over, although the climber
    was some sixty or seventy feet from the ground.
    
    "Which way mus' go now, Massa Will?" he asked.
    
    "Keep up the largest branch--the one on this side," said Legrand.
    The negro obeyed him promptly, and apparently with but little
    trouble; ascending higher and higher, until no glimpse of his
    squat figure could be obtained through the dense foliage which
    enveloped it. Presently his voice was heard in a sort of halloo.
    
    "How much fudder is got for go?"
    
    "How high up are you?" asked Legrand.
    
    "Ebber so fur," replied the negro; "can see de sky fru de top ob
    de tree."
    
    "Never mind the sky, but attend to what I say. Look down the
    trunk and count the limbs below you on this side. How many limbs
    have you passed?"
    
    "One, two, tree, four, fibe--I done pass fibe big limb, massa 'pon
    dis side."
    
    "Then go one limb higher."
    
    In a few minutes the voice was heard again, announcing that the
    seventh limb was attained.
    
    "Now, Jup," cried Legrand, evidently much excited, "I want you to
    work your way out upon that limb as far as you can. If you see
    any thing strange let me know."
    
    By this time what little doubt I might have entertained of my
    poor friend's insanity was put finally at rest. I had no
    alternative but to conclude him stricken with lunacy, and I
    became seriously anxious about getting him home. While I was
    pondering upon what was best to be done, Jupiter's voice was
    again heard.
    
    "Mos' feerd for to venture 'pon dis limb berry far--'tis dead limb
    putty much all de way."
    
    "Did you say it was a dead limb, Jupiter?" cried Legrand in a
    quavering voice.
    
    "Yes, massa, him dead as de door-nail--done up for sartain--done
    departed dis here life."
    
    "What in the name of heaven shall I do?" asked Legrand, seemingly
    in the greatest distress.
    
    "Do!" said I, glad of an opportunity to interpose a word, "why
    come home and go to bed. Come now!--that's a fine fellow. It's
    getting late, and, besides, you remember your promise."
    
    "Jupiter," cried he, without heeding me in the least, "do you
    hear me?"
    
    "Yes, Massa Will, hear you ebber so plain."
    
    "Try the wood well, then, with you knife, and see if you think it
    very rotten."
    
    "Him rotten, massa, sure nuff," replied the negro in a few
    moments, "but not so berry rotten as mought be. Mought venture
    out leetle way 'pon the limb by myself, dat's true."
    
    "By yourself!--what do you mean?"
    
    "Why I mean de bug. 'Tis berry hebby bug. Spose I drop him down
    fuss, and den de limb won't break wid just de weight ob one
    nigger."
    
    "You infernal scoundrel!" cried Legrand, apparently much
    relieved, "what do you mean by telling me such nonsense as that?
    As sure as you drop that beetle I'll break your neck. Look here,
    Jupiter, do you hear me?"
    
    "Yes, massa, needn't hollo at poor nigger dat style."
    
    "Well! now listen!--if you will venture out on that limb as far as
    you think safe, and not let go the beetle, I'll make you a
    present of a silver dollar as soon as you get down."
    
    "I'm gwine, Massa Will--deed I is," replied the negro very
    promptly--"mos' out to the eend now."
    
    "Out to the end!" here fairly screamed Legrand; "do you say you
    are out to the end of that limb?"
    
    "Soon be to de eend, massa--o-o-o-o-oh! Lor-gol-a-marcy! what is
    dis here pon de tree?"
    
    "Well!" cried Legrand, highly delighted, "what is it?"
    
    "Why taint noffin but a skull--somebody bin left him head up de
    tree, and de crows done gobble ebery bit ob de meat off."
    
    "A skull, you say!--very well,--how is it fastened to the
    limb?--what holds it on?"
    
    "Sure nuff, massa; mus' look. Why dis berry curous sarcumstance,
    'pon my word--dare's a great big nail in de skull, what fastens ob
    it on to de tree."
    
    "Well now, Jupiter, do exactly as I tell you--do you hear?"
    
    "Yes, massa."
    
    "Pay attention, then--find the left eye of the skull."
    
    "Hum! hoo! dat's good! why dey aint no eye lef' at all."
    
    "Curse your stupidity! do you know your right hand from your
    left?"
    
    "Yes, I knows dat--know all bout dat--'tis my lef' hand what I
    chops de wood wid."
    
    "To be sure! you are left-handed; and your left eye is on the
    same side as your left hand. Now, I suppose, you can find the
    left eye of the skull, or the place where the left eye has been.
    Have you found it?"
    
    Here was a long pause. At length the negro asked:
    
    "Is de lef' eye ob de skull 'pon de same side as de lef' hand ob
    de skull too?--cause de skull aint got not a bit ob a hand at
    all--nebber mind! I got de lef' eye now--here de lef' eye! what
    mus' do wid it?"
    
    "Let the beetle drop through it, as far as the string will
    reach--but be careful not to let go your hold of the string."
    
    "All dat done, Massa Will; mighty easy ting for to put the bug
    fru de hole--look out for him dar below!"
    
    During this colloquy no portion of Jupiter's person could be
    seen; but the beetle, which he had suffered to descend, was not
    visible at the end of the string, and glistened, like a globe of
    burnished gold, in the last rays of the setting sun, some of
    which still faintly illumined the eminence upon which we stood.
    The scarabaeus hung quite clear of any branches and, if allowed to
    fall, would have fallen at our feet. Legrand immediately took the
    scythe, and cleared with it a circular space, three or four yards
    in diameter, just beneath the insect, and, having accomplished
    this, ordered Jupiter to let go the string, and come down from
    the tree.
    
    Driving a peg, with great nicety, into the ground, at the precise
    spot where the beetle fell, my friend now produced from his
    pocket a tape-measure. Fastening one end of this at that point of
    the trunk of the tree which was nearest the peg, he unrolled it
    till it reached the peg and thence further unrolled it, in the
    direction already established by the two points of the tree and
    the peg, for the distance of fifty feet--Jupiter clearing away the
    brambles with the scythe. At the spot thus attained a second peg
    was driven, and about this, as a centre, a rude circle, about
    four feet in diameter, described. Taking now a spade himself, and
    giving one to Jupiter and one to me, Legrand begged us to set
    about digging as quickly as possible.
    
    To speak the truth, I had no especial relish for such amusement
    at any time, and, at that particular moment, would most willingly
    have declined it; for the night was coming on, and I felt much
    fatigued with the exercise already taken; but I saw no mode of
    escape, and was fearful of disturbing my poor friend's equanimity
    by a refusal. Could I have depended, indeed upon Jupiter's aid, I
    would have had no hesitation in attempting to get the lunatic
    home by force; but I was too well assured of the old negro's
    disposition, to hope that he would assist me, under any
    circumstances, in a personal contest with his master. I made no
    doubt that the latter had been infected with some of the
    innumerable Southern superstitions about money buried, and that
    his phantasy had received confirmation by the finding of the
    scarabaeus, or, perhaps, by Jupiter's obstinacy in maintaining it
    to be "a bug of real gold." A mind disposed to lunacy would
    readily be led away by such suggestions--especially if chiming in
    with favorite preconceived ideas--and then I called to mind the
    poor fellow's speech about the beetle's being "the index of his
    fortune." Upon the whole, I was sadly vexed and puzzled, but, at
    length, I concluded to make a virtue of necessity--to dig with a
    good will, and thus the sooner to convince the visionary, by
    ocular demonstration, of the fallacy of the opinions he
    entertained.
    
    The lanterns having been lit, we all fell to work with a zeal
    worth a more rational cause; and, as the glare fell upon our
    persons and implements, I could not help thinking how picturesque
    a group we composed, and how strange and suspicious our labors
    must have appeared to any interloper who, by chance, might have
    stumbled upon our whereabouts.
    
    We dug very steadily for two hours. Little was said; and our
    chief embarrassment lay in the yelpings of the dog, who took
    exceeding interest in our proceedings. He, at length, became so
    obstreperous that we grew fearful of his giving the alarm to some
    stragglers in the vicinity,--or, rather, this was the apprehension
    of Legrand;--for myself, I should have rejoiced at any
    interruption which might have enabled me to get the wanderer
    home. The noise was, at length, very effectually silenced by
    Jupiter, who, getting out of the hole with a dogged air of
    deliberation, tied the brute's mouth up with one of his
    suspenders, and then returned, with a grave chuckle, to his task.
    
    When the time mentioned had expired, we had reached a depth of
    five feet, and yet no signs of any treasure became manifest. A
    general pause ensued, and I began to hope that the farce was at
    an end. Legrand, however, although evidently much disconcerted,
    wiped his brow thoughtfully and recommenced. We had excavated the
    entire circle of four feet diameter, and now we slightly enlarged
    the limit, and went to the farther depth of two feet. Still
    nothing appeared. The gold-seeker, whom I sincerely pitied, at
    length clambered from the pit, with the bitterest disappointment
    imprinted upon every feature, and proceeded, slowly and
    reluctantly, to put on his coat, which he had thrown off at the
    beginning of his labor. In the meantime I made no remark.
    Jupiter, at a signal from his master, began to gather up his
    tools. This done, and the dog having been unmuzzled, we turned in
    profound silence toward home.
    
    We had taken, perhaps, a dozen steps in this direction, when,
    with a loud oath, Legrand strode up to Jupiter, and seized him by
    the collar. The astonished negro opened his eyes and mouth to the
    fullest extend, let fall the spades, and fell upon his knees.
    
    "You scoundrel!" said Legrand, hissing out the syllables from
    between his clenched teeth--"you infernal black villain!--speak, I
    tell you!--answer me this instant, without
    prevarication!--which--which is your left eye?"
    
    "Oh, my golly, Massa Will! aint dis here my lef' eye for
    sartain?" roared the terrified Jupiter, placing his hand upon his
    right organ of vision, and holding it there with a desperate
    pertinacity, as if in immediate dread of his master's attempt at
    a gouge.
    
    "I thought so!--I knew it! hurrah!" vociferated Legrand, letting
    the negro go and executing a series of curvets and caracols, much
    to the astonishment of his valet, who arising from his knees,
    looked, mutely, from his master to myself, and then from myself
    to his master.
    
    "Come! we must go back," said the latter, "the game's not up
    yet"; and he again led the way to the tulip-tree.
    
    "Jupiter," said he, when we reached its foot, "come here! was the
    skull nailed to the limb with the face outward, or with the face
    to the limb?"
    
    "De face was out, massa, so dat de crows could get at de eyes
    good, widout any trouble."
    
    "Well, then, was it this eye or that through which you dropped
    the beetle?"--here Legrand touched each of Jupiter's eyes.
    
    "Twas dis eye, massa--de lef' eye--jis as you tell me," and here it
    was his right eye that the negro indicated.
    
    "That will do--we must try again."
    
    Here my friend, about whose madness I now saw, or fancied I saw,
    certain indications of method, removed the peg which marked the
    spot where the beetle fell, to a spot about three inches to the
    westward of its former position. Taking, now, the tape measure
    from the nearest point of the trunk to the peg, as before, and
    continuing the extension in a straight line to the distance of
    fifty feet, a spot was indicated, removed by several yards, from
    the point at which we had been digging.
    
    Around the new position a circle, somewhat larger than in the
    former instance, was now described, and we again set to work with
    the spade. I was dreadfully weary, but, scarcely understanding
    what had occasioned the change in my thoughts, I felt no longer
    any great aversion from the labor imposed. I had become most
    unaccountably interested--nay, even excited. Perhaps there was
    something, amid all the extravagant demeanor of Legrand--some air
    of forethought, or of deliberation, which impressed me. I dug
    eagerly, and now and then caught myself actually looking, with
    something that very much resembled expectation, for the fancied
    treasure, the vision of which had demented my unfortunate
    companion. At a period when such vagaries of thought moust fully
    possessed me, and when we had been at work perhaps an hour and a
    half, we were again interrupted by the violent howlings of the
    dog. His uneasiness, in the first instance, had been, evidently,
    but the result of playfulness or caprice, but he now assumed a
    bitter and serious tone. Upon Jupiter's again attempting to
    muzzle him, he made furious resistance, and, leaping into the
    hole, tore up the mound frantically with his claws. In a few
    seconds he had uncovered a mass of human bones, forming two
    complete skeletons, intermingled with several buttons of metal,
    and what appeared to be the dust of decayed wollen. One or two
    strokes of the spade up-turned the blade of a large Spanish
    knife, and, as we dug farther, three or four loose pieces of gold
    and silver coin came to light.
    
    At the sight of these the joy of Jupiter could scarcely be
    restrained, but the countenance of his master wore an air of
    extreme disappointment. He urged us, however, to continue our
    exertions, and the words were hardly uttered when I stumbled and
    fell forward, having caught the toe of my boot in a large ring of
    iron that lay half buried in the loose earth.
    
    We now worked in earnest, and never did I pass ten minutes of
    more intense excitement. During this interval we had fairly
    unearthed an oblong chest of wood, which, from its perfect
    preservation and wonderful hardness, had plainly been subjected
    to some mineralizing process--perhaps that of the bi-chloride of
    mercury. This box was three feet and a half long, three feet
    broad, and two and a half feet deep. It was firmly secured by
    bands of wrought iron, riveted, and forming a kind of open
    trellis-work over the whole. On each side of the chest, near the
    top, were three rings of iron--six in all--by means of which a firm
    hold could be obtained by six persons. Our utmost united
    endeavors served only to disturb the coffer very slightly in its
    bed. We at once saw the impossibility of removing so great a
    weight. Luckily, the sole fastenings of the lid consisted of two
    sliding bolts. These we drew back--trembling and panting with
    anxiety. In an instant, a treasure of incalculable value lay
    gleaming before us. As the rays of the lanterns fell within the
    pit, there flashed upward a glow and a glare, from a confused
    heap of gold and of jewels, that absolutely dazzled our eyes.
    
    I shall not pretend to describe the feelings with which I gazed.
    Amazement was, of course, predominant. Legrand appeared exhausted
    with excitement, and spoke very few words. Jupiter's countenance
    wore, for some minutes, as deadly a pallor as it is possible, in
    the nature of things, for any negro's visage to assume. He seemed
    stupefied--thunderstricken. Presently he fell upon his knees in
    the pit, and burying his naked arms up to the elbows in gold, let
    them there remain, as if enjoying the luxury of a bath. At
    length, with a deep sigh, he exclaimed, as if in a soliloquy:
    
    "And dis all cum ob de goole-bug! de putty goole-bug! the poor
    little goole-bug, what I boosed in tat sabage kind ob style! Aint
    you shamed ob yourself, nigger?--answer me dat!"
    
    It became necessary, at last, that I should arouse both master
    and valet to the expediency of removing the treasure. It was
    growing late, and it behooved us to make exertion, that we might
    get every thing housed before daylight. It was difficult to say
    what should be done, and much time was spent in deliberation--so
    confused were the ideas of all. We, finally, lightened the box by
    removing two thirds of its contents, when we were enabled, with
    some trouble, to raise it from the hole. The articles taken out
    were deposited among the brambles, and the dog left to guard
    them, with strict orders from Jupiter neither, upon any pretence,
    to stir from the spot, nor to open his mouth until our return. We
    then hurriedly made for home with the chest; reaching the hut in
    safety, but after excessive toil, at one o'clock in the morning.
    Wore out as we were, it was not in human nature to do more
    immediately. We rested until two, and had supper; starting for
    the hills immediately afterward, armed with three stout sacks,
    which, by good lick, were upon the premises. A little before four
    we arrived at the pit, divided the remainder of the booty, as
    equally as might be, among us, and, leaving the wholes unfilled,
    again set out for the hut, at which, for the second time, we
    deposited our gold burthens, just as the first faint streaks of
    the dawn gleamed from over the tree-tops in the East.
    
    We were now thoroughly broken down; but the intense excitement of
    the time denied us repose. After an unquiet slumber of some three
    or four hours' duration, we arose, as if by preconcert, to make
    examination of our treasure.
    
    The chest had been full to the brim, and we spent the whole day,
    and the greater part of the next night, in a scrutiny of its
    contents. There had been nothing like order of arrangement. Every
    thing had been heaped in promiscuously. Having assorted all with
    care, we found ourselves possessed of even vaster wealth than we
    had at first supposed. In coin there was rather more than four
    hundred and fifty thousand dollars--estimating the value of the
    pieces, as accurately as we could, by the tables of the period.
    There was not a particle of silver. All was gold of antique date
    and of great variety--French, Spanish, and German money, with a
    few English guineas, and some counters, of which we had never
    seen specimens before. There were several very large and heavy
    coins, so worn that we could make nothing of their inscriptions.
    There was no American money. The value of the jewels we found
    more difficulty in estimating. There were diamonds--some of them
    exceedingly large and fine--a hundred and ten in all, and not one
    of them small; eighteen rubies of remarkable brilliancy;--three
    hundred and ten emeralds, all very beautiful; and twenty-one
    sapphires, with an opal. These stones had all been broken from
    their settings and thrown loose in the chest. The settings
    themselves which we picked out from among the other gold,
    appeared to have been beaten up with hammers, as if to prevent
    identification. Besides all this, there was a vast quantity of
    solid gold ornaments; nearly two hundred massive finger- and
    ear-rings; rich chains--thirty of these, if I remember;
    eighty-three very large and heavy crucifixes; five gold censers
    of great value; a prodigious golden punch-bowl, ornamented with
    richly chased vine-leaves and Bacchanalian figures; with two
    sword-handles exquisitely embossed, and many other smaller
    articles which I cannot recollect. The weight of these valuables
    exceeded three hundred and fifty pounds avoirdupois; and in this
    estimate I have not included one hundred and ninety seven superb
    gold watches; three of the number being worth each five hundred
    dollars, if one. Many of them were very old, and as timekeepers
    valueless; the works having suffered, more or less, from
    corrosion--but all were richly jewelled and in cases of great
    worth. We estimated the entire contents of the chest, that night,
    as a million and a half of dollars, and upon the subsequent
    disposal of the trinkets and jewels (a few being retained for our
    own use), it was found that we had greatly under-valued the
    treasure.
    
    When, at length, we had concluded our examination, and the
    intense excitement of the time had, in some measure, subsided,
    Legrand, who saw that I was dying with impatience for a solution
    of this most extraordinary riddle, entered into a full detail of
    all the circumstances connected with it.
    
    "You remember," said he, "the night when I handed you the rough
    sketch I had made of the scarabaeus. You recollect also, that I
    became quite vexed at you for insisting that my drawing resembled
    a death's-head. When you first made this assertion I thought you
    were jesting; but afterward I called to mind the peculiar spots
    on the back of the insect, and admitted to myself that your
    remark had some little foundation in fact. Still, the sneer at my
    graphic powers irritated me--for I am considered a good
    artist--and, therefore, when you handed me the scrap of parchment,
    I was about to crumple it up and throw it angrily into the fire."
    
    "The scrap of paper, you mean," said I.
    
    "No; it had much of the appearance of paper, and at first I
    supposed it to be such, but when I came to draw upon it, I
    discovered it at once to be a piece of very thin parchment. It
    was quite dirty, you remember. Well, as I was in the very act of
    crumpling it up, my glance fell upon the sketch at which you had
    been looking, and you may imagine my astonishment when I
    perceived, in fact, the figure of a death's-head just where, it
    seemed to me, I had made the drawing of the beetle. For a moment
    I was too much amazed to think with accuracy. I knew that my
    design was very different in detail from this--although there was
    a certain similarity in general outline. Presently I took a
    candle, and seating myself at the other end of the room,
    proceeded to scrutinize the parchment more closely. Upon turning
    it over, I saw my own sketch upon the reverse, just as I had made
    it. My first idea, now, was mere surprise at the really
    remarkable similarity of outline--at the singular coincidence
    involved in the fact that, unknown to me, there should have been
    a skull upon the other side of the parchment, immediately beneath
    my figure of the scarabaeus, and that this skull, not only in
    outline, but in size, should so closely resemble my drawing. I
    say the singularity of this coincidence absolutely stupefied me
    for a time. This is the usual effect of such coincidences. The
    mind struggles to establish a connection--a sequence of causes and
    effect--and, being unable to do so, suffers a species of temporary
    paralysis. But, when I recovered from this stupor, there dawned
    upon me gradually a conviction which startled me even far more
    than the coincidence. I began distinctly, positively, to remember
    that there had been no drawing upon the parchment when I made my
    sketch of the scarabaeus. I became perfectly certain of this; for
    I recollected turning up first one side and then the other, in
    search of the cleanest spot. Had the skull been then there, of
    course I could not have failed to notice it. Here was indeed a
    mystery which I felt it impossible to explain; but, even at that
    early moment, there seemed to glimmer, faintly, within the most
    remote and secret chambers of my intellect, a glow-worm-like
    conception of that truth which last night's adventure brought to
    so magnificent a demonstration. I arose at once, and putting the
    parchment securely away, dismissed all further reflection until I
    should be alone.
    
    "When you had gone, and when Jupiter was fast asleep, I betook
    myself to a more methodical investigation of the affair. In the
    first place I considered the manner in which the parchment had
    come into my possession. The spot where we discovered the
    scarabaeus was on the coast of the main-land, about a mile
    eastward of the island, and but a short distance above high-water
    mark. Upon my taking hold of it, it gave me a sharp bite, which
    caused me to let it drop. Jupiter, with his accustomed caution,
    before seizing the insect, which had flown toward him, looked
    about him for a leaf, or something of that nature, by which to
    take hold of it. It was at this moment that his eyes, and mine
    also, fell upon the scrap of parchment, which I then supposed to
    be paper. It was lying half buried in the sand, a corner sticking
    up. Near the spot where we found it, I observed the remnants of
    the hull of what appeared to have been a ship's long-boat. The
    wreck seemed to have been there for a very great while; for the
    resemblance to boat timbers could scarcely be traced.
    
    "Well, Jupiter picked up the parchment, wrapped the beetle in it,
    and gave it to me. Soon afterwards we turned to go home, and on
    the way met Lieutenant G----. I showed him the insect, and he
    begged me to let him take it to the fort. Upon my consenting, he
    thrust it forthwith into his waistcoat pocket, without the
    parchment in which it had been wrapped, and which I had continued
    to hold in my hand during his inspection. Perhaps he dreaded my
    changing my mind, and thought it best to make sure of the prize
    at once--you know how enthusiastic he is on all subjects connected
    with Natural History. At the same time, without being conscious
    of it, I must have deposited the parchment in my own pocket.
    
    "You remember that when I went to the table, for the purpose of
    making a sketch of the beetle, I found no paper where it was
    usually kept. I looked in the drawer, and found none there. I
    searched my pockets, hoping to find an old letter, when my hand
    fell upon the parchment. I thus detail the precise mode in which
    it came into my possession; for the circumstances impressed me
    with peculiar force.
    
    "No doubt you will think me fanciful--but I had already
    established a kind of connection. I had put together two links of
    a great chain. There was a boat lying upon the sea-coast, and not
    far from the boat was a parchment--not a paper--with a skull
    depicted on it. You will, of course, ask `where is the
    connection?' I reply that the skull, or death's-head, is the
    well-known emblem of the pirate. The flag of the death's-head is
    hoisted in all engagements.
    
    "I have said that the scrap was parchment, and not paper.
    Parchment is durable--almost imperishable. Matters of little
    moment are rarely consigned to parchment; since, for the mere
    ordinary purposes of drawing or writing, it is not nearly so well
    adapted as paper. This reflection suggested some meaning--some
    relevancy--in the death's-head. I did not fail to observe, also,
    the form of the parchment. Although one of its corners had been,
    by some accident, destroyed, it could be seen that the original
    form was oblong. It was just such a slip, indeed, as might have
    been chosen for a memorandum--for a record of something to be long
    remembered and carefully preserved."
    
    "But," I interposed, "you say that the skull was not upon the
    parchment when you made the drawing of the beetle. How then do
    you trace any connection between the boat and the skull--since
    this latter, according to your own admission, must have been
    designed (God only knows how or by whom) at some period
    subsequent to your sketching the scarabaeus?"
    
    "Ah, hereupon turns the whole mystery; although the secret, at
    this point, I had comparatively little difficulty in solving. My
    steps were sure, and could afford a single result. I reasoned,
    for example, thus: When I drew the scarabaeus, there was no skull
    apparent upon the parchment. When I had completed the drawing I
    gave it to you, and observed you narrowly until you returned it.
    You, therefore, did not design the skull, and no one else was
    present to do it. Then it was not done by human agency. And
    nevertheless it was done.
    
    "At this stage of my reflections I endeavored to remember, and
    did remember, with entire distinctness, every incident which
    occurred about the period in question. The weather was chilly
    (oh, rare and happy accident!), and a fire was blazing upon the
    hearth. I was heated with exercise and sat near the table. You,
    however, had drawn a chair close to the chimney. Just as I placed
    the parchment in your hand, and as you were in the act of
    inspecting it, Wolf, the Newfoundland, entered, and leaped upon
    your shoulders. With your left hand you caressed him and kept him
    off, while your right, holding the parchment, was permitted to
    fall listlessly between your knees, and in close proximity to the
    fire. At one moment I thought the blaze had caught it, and was
    about to caution you, but, before I could speak, you had
    withdrawn it, and were engaged in its examination. When I
    considered all these particulars, I doubted not for a moment that
    heat had been the agent in bringing to light, upon the parchment,
    the skull which I saw designed upon it. You are well aware that
    chemical preparations exist, and have existed time out of mind,
    by means of which it is possible to write upon either paper or
    vellum, so that the characters shall become visible only when
    subjected to the action of fire. Zaffre, digested in aqua regia,
    and diluted with four times its weight of water, is sometimes
    employed; a green tint results. The regulus of cobalt, dissolved
    in spirit of nitre, gives a red. These colors disappear at longer
    or shorter intervals after the material written upon cools, but
    again become apparent upon the re-application of heat.
    
    "I now scrutinized the death's-head with care. Its outer
    edges--the edges of the drawing nearest the edge of the
    vellum--were far more distinct than the others. It was clear that
    the action of the caloric had been imperfect or unequal. I
    immediately kindled a fire, and subjected every portion of the
    parchment to a glowing heat. At first, the only effect was the
    strengthening of the faint lines in the skull; but, upon
    persevering in the experiment, there became visible, at the
    corner of the slip, diagonally opposite to the spot in which the
    death's-head was delineated, the figure of what I at first
    supposed to be a goat. A closer scrutiny, however, satisfied me
    that it was intended for a kid."
    
    "Ha! ha!" said I, "to be sure I have no right to laugh at you--a
    million and a half of money is to serious a matter for mirth--but
    you are not about to establish a third link in your chain--you
    will not find any especial connection between your pirates and a
    goat--pirates, you know, have nothing to do with goats; they
    appertain to the farming interest."
    
    "But I have just said that the figure was not that of a goat."
    
    "Well, a kid then--pretty much the same thing."
    
    "Pretty much, but not altogether," said Legrand. "You may have
    heard of one Captain Kidd. I at once looked upon the figure of
    the animal as a kind of punning or hieroglyphical signature. I
    say signature; because its position upon the vellum suggested
    this idea. The death's-head at the corner diagonally opposite,
    had, in the same manner, the air of a stamp, or seal. But I was
    sorely put out by the absence of all else--of the body to my
    imagined instrument--of the text for my context."
    
    "I presume you expected to find a letter between the stamp and
    the signature."
    
    "Something of that kind. The fact is, I felt irresistibly
    impressed with a presentiment of some vast good fortune
    impending. I can scarcely say why. Perhaps, after all, it was
    rather a desire than an actual belief;--but do you know that
    Jupiter's silly words, about the bug being of solid gold, had a
    remarkable effect upon my fancy? And then the series of accidents
    and coincidences--these were so very extraordinary. Do you observe
    how mere an accident it was that these events should have
    occurred upon the sole day of all the year in which it has been,
    or may be sufficiently cool for fire, and that without the fire,
    or without the intervention of the dog at the precise moment in
    which he appeared, I should never have become aware of the
    death's-head, and so never the possessor of the treasure?"
    
    "But proceed--I am all impatience."
    
    "Well; you have heard, of course, the many stories current--the
    thousand vague rumors afloat about money buried, somewhere upon
    the Atlantic coast, by Kidd and his associates. These rumors must
    have had some foundation in fact. And that the rumors have
    existed so long and so continuous, could have resulted, it
    appeared to me, only from the circumstance of the buried treasure
    still remaining entombed. Had Kidd concealed his plunder for a
    time, and afterward reclaimed it, the rumors would scarcely have
    reached us in their presently unvarying form. You will observe
    that the stories told are all about money-seekers, not about
    money-finders. Had the pirate recovered his money, there the
    affair would have dropped. It seemed to me that some accident--say
    the loss of a memorandum indicating its locality--had deprived him
    of the means of recovering it, and that this accident had become
    known to his followers, who otherwise might never have heard that
    treasure had been concealed at all, and who, busying themselves
    in vain, because unguided, attempts to regain it, had given first
    birth, and then universal currency, to the reports which are now
    so common. Have you ever heard of any important treasure being
    unearthed along the coast?"
    
    "Never."
    
    "But that Kidd's accumulations were immense, is well known. I
    took it for granted, therefore, that the earth still held them;
    and you will scarcely be surprised when I tell you that I felt a
    hope, nearly amounting to certainty, that the parchment so
    strangely found involved a lost record of the place of deposit."
    
    "But how did you proceed?"
    
    "I held the vellum again to the fire, after increasing the heat,
    but nothing appeared. I now thought it possible that the coating
    of dirt might have something to do with the failure: so I
    carefully rinsed the parchment by pouring warm water over it,
    and, having done this, I placed it in a tin pan, with the skull
    downward, and put the pan upon a furnace of lighted charcoal. In
    a few minutes, the pan having become thoroughly heated, I removed
    the slip, and, to my inexpressible joy, found it spotted, in
    several places, with what appeared to be figures arranged in
    lines. Again I placed it in the pan, and suffered it to remain
    another minute. Upon taking it off, the whole was just as you see
    it now."
    
    Here Legrand, having re-heated the parchment, submitted it to my
    inspection. The following characters were rudely traced, in a red
    tint, between the death's head and the goat:
    
    "53##305))6*;4826)4#);806*;48+8P60))85;I#(;:#*8+83(88)5*+;46(;88*
    96*?;8)*#(;485);5*+2:*#(;4956*2(5*--4)8P8*;4069285);)6+8)4##;I(#9;
    48081;8:8#I;48+85;4)485+528806*8I(#9;48;(88;4(#?34;48)4#;161;:188
    ;#?;"
    
    "But," said I, returning him the slip, "I am as much in the dark
    as ever. Were all the jewels of Golconda awaiting me upon my
    solution of this enigma, I am quite sure that I should be unable
    to earn them."
    
    "And yet, "said Legrand, "the solution is by no means so
    difficult as you might be led to imagine from the first hasty
    inspection of the characters. These characters, as any one might
    readily guess, form a cipher--that is to say, they convey a
    meaning; but then from what is known of Kidd, I could not suppose
    him capable of constructing any of the more abstruse
    cryptographs. I made up my mind, at once, that this was of a
    simple species--such, however, as would appear to the crude
    intellect of the sailor, absolutely insoluble without the key."
    
    "And you really solved it?"
    
    "Readily; I have solved others of an abstruseness ten thousand
    times greater. Circumstances, and a certain bias of mind, have
    led me to take interest in such riddles, and it may well be
    doubted whether human ingenuity can construct an enigma of the
    kind which human ingenuity may not, by proper application,
    resolve. In fact, having once established connected and legible
    characters, I scarcely gave a thought to the mere difficulty of
    developing their import.
    
    "In the present case--indeed in all cases of secret writing--the
    first question regards the language of the cipher; for the
    principles of solution, so far, especially, as the more simple
    ciphers are concerned, depend upon and are varied by, the genius
    of the particular idiom. In general, there is no alternative but
    experiment (directed by probabilities) of every tongue known to
    him who attempts the solution, until the true one be attained.
    But, with the cipher now before us all difficulty was removed by
    the signature. The pun upon the word `Kidd' is appreciable in no
    other language than the English. But for this consideration I
    should have begun my attempts with the Spanish and French, as the
    tongues in which a secret of this kind would most naturally have
    been written by a pirate of the Spanish main. As it was, I
    assumed the cryptograph to be English.
    
    "You observe there are no divisions between the words. Had there
    been divisions the task would have been comparatively easy. In
    such cases I should have commenced with a collation and analysis
    of the shorter words, and, had a word of a single letter
    occurred, as is most likely (a or I, for example), I should have
    considered the solution as assured. But, there being no division,
    my first step was to ascertain the predominant letters, as well
    as the least frequent. Counting all, I constructed a table thus:
    
         Of the character 8 there are 33.
                          ;      "    26.
                          4      "    19.
                         #)      "    16.
                          *      "    13.
                          5      "    12.
                          6      "    11.
                         +I      "     8.
                          0      "     6.
                         92      "     5.
                         :3      "     4.
                          ?      "     3.
                          P      "     2.
                         --.      "     1.
    
    "Now, in English, the letter which most frequently occurs is e.
    Afterward, the succession runs thus: a o i d h n r s t u y c f g
    l m w b k p q x z. E predominates so remarkably, that an
    individual sentence of any length is rarely seen, in which it is
    not the prevailing character.
    
    "Here, then, we have, in the very beginning, the groundwork for
    something more than a mere guess. The general use which may be
    made of the table is obvious--but, in this particular cipher, we
    shall only very partially require its aid. As our predominant
    character is 8, we will commence by assuming it as the e of the
    natural alphabet. To verify the supposition, let us observe it
    the 8 be seen often in couples--for e is doubled with great
    frequency in English--in such words, for example, as `meet,'
    `fleet,' `speed,' `seen,' `been,' `agree,' etc. In the present
    instance we see it doubled no less than five times, although the
    cryptograph is brief.
    
    "Let us assume 8, then, as e. Now, of all words in the language,
    `the' is most usual; let us see, therefore, whether there are not
    repetitions of any three characters, in the same order of
    collocation, the last of them being 8. If we discover a
    repetition of such letters, so arranged, they will most probably
    represent the word `the.' Upon inspection, we find no less than
    seven such arrangements, the characters being ;48. We may,
    therefore, assume that ; represents t, 4 represents h, and 8
    represents e--the last being now well confirmed. Thus a great step
    has been taken.
    
    "But, having established a single word, we are enabled to
    establish a vastly important point; that is to say, several
    commencements and terminations of other words. Let us refer, for
    example, to the last instance but one, in which the combination
    ;48 occurs--not far from the end of the cipher. We know that the ;
    immediately ensuing is the commencement of a word, and, of the
    six characters succeeding this `the,' we are cognizant of no less
    than five. Let us set these characters down, thus, by the letters
    we know them to represent, leaving a space for the unknown--
    
                               t eeth.
    
    "Here we are enabled, at once, to discard the `th,' as forming no
    portion of the word commencing with the first t; since, by
    experiment of the entire alphabet for a letter adapted to the
    vacancy, we perceive that no word can be formed of which this th
    can be a part. We are thus narrowed into
    
                                t ee,
    
    and, going through the alphabet, if necessary, as before, we
    arrive at the word `tree,' as the sole possible reading. We thus
    gain another letter, r, represented by (, with the words `the
    tree' in juxtaposition.
    
    "Looking beyond these words, for a short distance, we again see
    the combination ;48, and employ it by way of termination to what
    immediately precedes. We have thus this arrangement:
    
                        the tree ;4(#?34 the,
    
    or substituting the natural letters, where known, it reads thus:
    
                        the tree thr#?3h the,
    
    "Now, if, in place of the unknown characters, we leave blank
    spaces, or substitute dots, we read thus:
    
                        the tree thr...h the,
    
    when the word `through' makes itself evident at once. But this
    discovery gives us three new letters, o, u, and g, represented by
    #, ?, and 3.
    
    "Looking now, narrowly, through the cipher for combinations of
    known characters, we find, not very far from the beginning, this
    arrangement,
    
                          83(88, or egree,
    
    which, plainly, is the conclusion of the word `degree,' and gives
    us another letter, d, represented by +.
    
    "Four letters beyond the word `degree,' we perceive the
    combination
    
                              ;46(;88.
    
    "Translating the known characters, and representing the unknown
    by dots, as before, we read thus:
    
                              th.rtee,
    
    an arrangement immediately suggestive of the word `thirteen,' and
    again furnishing us with two new characters, i and n, represented
    by 6 and *.
    
    "Referring, now, to the beginning of the cryptograph, we find the
    combination,
    
                               53##+.
    
    "Translating as before, we obtain
    
                               .good,
    
    which assures us that the first letter is A, and that the first
    two words are `A good.'
    
    "It is now time that we arrange our key, as far as discovered, in
    a tabular form, to avoid confusion. It will stand thus:
    
                           5 represents a
                           +     "      d
                           8     "      e
                           3     "      g
                           4     "      h
                           6     "      i
                           *     "      n
                           #     "      o
                           (     "      r
                           ;     "      t
                           ?     "      u
    
    "We have, therefore, no less than eleven of the most important
    letters represented, and it will be unnecessary to proceed with
    the details of the solution. I have said enough to convince you
    that ciphers of this nature are readily soluble, and to give you
    some insight into the rationale of their development. But be
    assured that the specimen before us appertains to the very
    simplest species of cryptograph. It now only remains to give you
    the full translation of the characters upon the parchment, as
    unriddled. Here it is:
    
    "`A good glass in the bishop's hostel in the devil's seat
    forty-one degrees and thirteen minutes northeast and by north
    main branch seventh limb east side shoot from the left eye of the
    death's-head a bee-line from the tree through the shot fifty feet
    out.'"
    
    "But," said I, "the enigma seems still in as bad a condition as
    ever. How is it possible to extort a meaning from all this jargon
    about `devil's seats,' `death's-heads,' and `bishop's hostels'?"
    
    "I confess," replied Legrand, "that the matter still wears a
    serious aspect, when regarded with a casual glance. My first
    endeavor was to divide the sentence into the natural division
    intended by the cryptographist."
    
    "You mean, to punctuate it?"
    
    "Something of that kind."
    
    "But how was it possible to effect this?"
    
    "I reflected that it had been a point with the writer to run his
    words together without division, so as to increase the difficulty
    of solution. Now, a not over-acute man, in pursuing such an
    object, would be nearly certain to overdo the matter. When, in
    the course of his composition, he arrived at a break in his
    subject which would naturally require a pause, or a point, he
    would be exceedingly apt to run his characters, at this place,
    more than usually close together. If you will observe the MS., in
    the present instance, you will easily detect five such cases of
    unusual crowding. Acting upon this hint, I made the division
    thus:
    
    "`A good glass in the bishop's hostel in the devil's
    seat--forty-one degrees and thirteen minutes--northeast and by
    north--main branch seventh limb east side--shoot from the left eye
    of the death's-head--a bee-line from the tree through the shot
    fifty feet out.'"
    
    "Even this division," said I, "leaves me still in the dark."
    
    "It left me also in the dark," replied Legrand, "for a few days;
    during which I made diligent inquiry, in the neighborhood of
    Sullivan's Island, for any building which went by the name of the
    `Bishop's Hotel'; for, of course, I dropped the obsolete word
    `hostel.' Gaining no information on the subject, I was on the
    point of extending my sphere of search, and proceeding in a more
    systematic manner, when, one morning, it entered into my head,
    quite suddenly, that this `Bishop's Hostel' might have some
    reference to an old family, of the name of Bessop, which, time
    out of mind, had held possession of an ancient manor-house, about
    four miles to the northward of the island. I accordingly went
    over to the plantation, and re-instituted my inquiries among the
    older negroes of the place. At length one of the most aged of the
    women said that she had heard of such a place as Bessop's Castle,
    and thought that she could guide me to it, but that it was not a
    castle, nor a tavern, but a high rock.
    
    
    "I offered to pay her well for her trouble, and, after some
    demur, she consented to accompany me to the spot. We found it
    without much difficulty, when, dismissing her, I proceeded to
    examine the place. The `castle' consisted of an irregular
    assemblage of cliffs and rocks--one of the latter being quite
    remarkable for its height as well as for its insulated and
    artificial appearance. I clambered to its apex, and then felt
    much at a loss as to what should be next done.
    
    "While I was busied in reflection, my eyes fell upon a narrow
    ledge in the eastern face of the rock, perhaps a yard below the
    summit upon which I stood. This ledge projected about eighteen
    inches, and was not more than a foot wide, while a niche in the
    cliff just above it gave it a rude resemblance to one of the
    hollow-backed chairs used by our ancestors. I made no doubt that
    here was the `devil's-seat' alluded to  in the MS., and now I
    seemed to grasp the full secret of the riddle.
    
    "The `good glass,' I knew, could have reference to nothing but a
    telescope; for the word `glass' is rarely employed in any other
    sense by seamen. Now here, I at once saw, was a telescope to be
    used, and a definite point of view, admitting no variation, from
    which to use it. Nor did I hesitate to believe that the phrases,
    `forty-one degrees and thirteen minutes,' and `northeast and by
    north,' were intended as directions for the levelling of the
    glass. Greatly excited by these discoveries, I hurried home,
    procured a telescope, and returned to the rock.
    
    "I let myself down to the ledge, and found that it was impossible
    to retain a seat upon it except in one particular position. This
    fact confirmed my preconceived idea. I proceeded to use the
    glass. Of course, the `forty-one degrees and thirteen minutes'
    could allude to nothing but elevation above the visible horizon,
    since the horizontal direction was clearly indicated by the
    words, `northeast and by north.' This latter direction I at once
    established by means of a pocket-compass; then, pointing the
    glass as nearly at an angle of forty-one degrees of elevation as
    I could do it by guess, I moved it cautiously up or down, until
    my attention was arrested by a circular rift or opening in the
    foliage of a large tree that overtopped its fellows in the
    distance. In the centre of this rift I perceived a white spot,
    but could not, at first, distinguish what it was. Adjusting the
    focus of the telescope, I again looked, and now made it out to be
    a human skull.
    
    "Upon this discovery I was so sanguine as to consider the enigma
    solved; for the phrase `main branch, seventh limb, east side,'
    could refer only to the position of the skull upon the tree,
    while `shoot from the left eye of the death's-head' admitted,
    also, of but one interpretation, in regard to a search for a
    buried treasure. I perceived that the design was to drop a bullet
    from the left eye of the skull, and that a bee-line, or, in other
    words, a straight line, drawn from the nearest point of the trunk
    through `the shot' (or the spot where the bullet fell), and
    thence extended to a distance of fifty feet, would indicate a
    definite point--and beneath this point I thought it at least
    possible that a deposit of value lay concealed."
    
    "All this," I said, "is exceedingly clear, and, although
    ingenious, still simple and explicit. When you left the `Bishop's
    Hotel,' what then?"
    
    "Why, having carefully taken the bearings of the tree, I turned
    homeward. The instant that I left `the devil's-seat,' however,
    the circular rift vanished; nor could I get a glimpse of it
    afterward, turn as I would. What seems to me the chief ingenuity
    in this  whole business, is the fact (for repeated experiment has
    convinced me it is a fact) that the circular opening in question
    is visible from no other attainable point of view than that
    afforded by the narrow ledge upon the face of the rock.
    
    "In this expedition to the `Bishop's Hotel' I had been attended
    by Jupiter, who had, no doubt, observed, for some weeks past, the
    abstraction of my demeanor, and took especial care not to leave
    me alone. But, on the next day, getting up very early, I
    contrived to give him the slip, and went into the hills in search
    of the tree. After much toil I found it. When I came home at
    night my valet proposed to give me a flogging. With the rest of
    the adventure I believe you  are as well acquainted as myself."
    
    "I suppose," said I, "you missed the spot, in the first attempt
    at digging, through Jupiter's stupidity in letting the bug fall
    through the right instead of through the left eye of the skull."
    
    "Precisely. This mistake made a difference of about two inches
    and a half in the `shot'--that is to say, in the position of the
    peg nearest the tree; and had the treasure been beneath the
    `shot,' the error would have been of little moment; but `the
    shot,' together with the nearest point of the tree, were merely
    two points for the establishment of a line of direction; of
    course the error, however trivial in the beginning, increased as
    we proceeded with the line, and by the time we had gone fifty
    feet threw us quite off the scent. But for my deep-seated
    impressions that treasure was here somewhere actually buried, we
    might have had all our labor in vain."
    
    "But you grandiloquence, and your conduct in swinging the
    beetle--how excessively odd! I was sure you were mad. And why did
    you insist upon letting fall the bug, instead of a bullet, from
    the skull?"
    
    "Why, to be frank, I felt somewhat annoyed by your evident
    suspicions touching my sanity, and so resolved to punish you
    quietly, in my own way, by a little bit of sober mystification.
    For this reason I swung the beetle, and for this reason I let it
    fall from the tree. An observation of yours about its great
    weight suggested the latter idea."
    
    "Yes, I perceive; and now there is only one point which puzzles
    me. What are we to make of the skeletons found in the hole?"
    
    "That is a question I am no more able to answer than yourself.
    There seems, however, only one plausible way of accounting for
    them--and yet it is dreadful to believe in such atrocity as my
    suggestion would imply. It is clear that Kidd--if Kidd indeed
    secreted this treasure, which I doubt not--it is clear that he
    must have had assistance in the labor. But this labor concluded,
    he may have thought it expedient to remove all participants in
    his secret. Perhaps a couple of blows with a mattock were
    sufficient, while his coadjutors were busy in the pit; perhaps it
    required a dozen--who shall tell?"''',
    # -----------------------------------------------------------------
    '''Hani  watched  over Andrey's shoulder as he manipulated the image
    on  the  screen,  rotating  it,  zooming  in  to examine details,
    panning  across  the  intricate  designs.  A slight frown crossed
    Andrey's  face  as the machine laboured to keep up the display...
    the object was very detailed.
        "This bit," Hani pointed, "you press it in and turn it at the
    same time."  "Okay..." Andrey put his left hand into the feedback
    glove, and a wireframe hand appeared on the screen. "Are you sure
    this is safe?"
        "Relax.   As Terry Gilliam said in `Monty Python and the Holy
    Grail', `It's only a model'."
        "I   know."    Andrey  turned  in  his  ergonomic  Hans  Rudi
    Giger-designed  chair  to face her.  "If you will recall, `only a
    model'  is  exactly what Phillip LeMarchand said about that thing
    when  he  made  it,"  gesturing  with  his free right hand at the
    puzzle box that sat on the face of the HP scanner.  The elaborate
    brasswork  gleamed  in  the  bright light of Andrey's architect's
    drawing-board lamps.
        "What  are you worried about, you fool?  If anything is going
    to  happen,  it'll  happen in there," pointing at the case of his
    TurboSkum  Tower  586 PC, "so what can happen?  Hard disk crash?"
        "It ain't your hard disk."  Andrey muttered.  He returned his
    attention  to  the  display.   The  wireframe  hand  reached out,
    pressed  the  centre  of one side of the model of the puzzle box.
    A  touch  of  a function key and the hand rotated.  Suddenly, the
    image of the box came to life, changing shape with a fluidity and
    speed  that  even  his 80586-based pc, running AutoCad Version 23
    could  not match.  "Oh shit," Andrey croaked, his throat suddenly
    dry.   He  grabbed  for  the box with the feedback glove, but the
    wireframe  hand  seemed to pass through the image frictionlessly.
    It  now  looked like an elaborate cog, a spastic rubik's cube, an
    elongated  spearhead,  a crown-of-thorns starfish.  Blurring with
    motion,  the  box resolved into a cube once more.  Andrey grasped
    it with the feedback glove.  "Got the little fucker," he grinned.
        Then,  the image of the box on the monitor sprouted dozens of
    spikes,  like the Iraqi weapons that Hani had seen, potatoes with
    six-inch   nails   thrust  through  them  to  make  economy-sized
    morningstars.   Andrey  shouted, "Chort vosmi!".  Gleaming silver
    spikes were protruding from the back of the black plastic mesh of
    the feedback glove.  He tried to tug his hand from it, but it was
    plainly fixed.  Blood ran from inside the glove, to drip down the
    cable  leading  from  the glove's interface and pool on the desk.
    Hani  grabbed  the  nearest  thing  to hand, which happened to be
    Andrey's   portable  CD player, and bashed at a spike which poked
    almost straight up.  The matte-black case of the CD player passed
    right  through the silver sliver, protruding from its back like a
    hologram.   Andrey  moaned  as  the CD player hit the back of his
    impaled  hand.   The  Cocteau  Twins  skipped  a beat or two (you
    really shouldn't hit people with CD players when they are playing
    nice  music like `IceBlink Luck').  Through gritted teeth, Andrey
    grated,
        "Okay,  you  smartass bitch, now what?  Just a fucking model,
    eh?   NOW  WHAT???"   He  shrieked as she grabbed his forearm and
    tugged  violently.   The  velcro  padding  that held the feedback
    glove's  interface to the desk separated, but not before Andrey's
    hand  came  out,  minus  two  fingers.   "YOU  STUPID  BITCH!" he
    shouted,  oblivious  of  the  flashes  of  blue  light  that were
    emanating  from  the  monitor, slightly diluted to purple through
    the  sprays  of blood which ran down the screen.  He took a swipe
    at  her  with  his mangled hand, and then a horrific screech came
    from   the  machine's hard disk.  The lights on the keyboard were
    flashing maniacally.  They had time to glimpse a message outlined
    in  an orange rectangle - `GURU MEDITATION' and something else, a
    string  of  hex  numbers, as the monitor exploded, peppering them
    with  slivers  of glass.  The force of the blast blew Andrey over
    backwards  in  his  chair,  dragging  Hani  with  him.  When they
    scrambled  to  their  feet, there was someone standing behind the
    desk,  one  hand on the top of the scorched monitor case.  He was
    dressed  in scraps of black leather, some of which appeared to be
    stitched  to  his  skin.  The  general style appeared to be early
    1920's  Theatre-goer...  he  had  one  of  those  waistcoat-inset
    dickeys  made out of a strip of bleached flesh.  He was wearing a
    mask  of  skin,  stapled to his face.  The ravaged lips twitched.
       "Good  morning,  architect."   with  a  flick  of his wrist, a
    cut-throat  razor  opened in his right hand.  An icepick appeared
    in  his  left.   He  pointed  the  razor at Andrey's face.  A cut
    appeared  between  Andrey's  eyes, and spread simultaneously down
    his  nose and up through his receding hairline.  Another gesture,
    and  the  razor  was  gone.  The cenobite spread his fingers, and
    with  a  rotten-calico-tearing  sound,  the two sides of Andrey's
    face were torn from the fascia of his skull.
    
                   *       *       *       *       *
    
        "I  see you've been adding to  your collection." Pinhead said
    to Face as the chains clanked, the prisoners groaned and shrieked
    on  the  end  of  their hooks.  "Anyone we know?"  Face shook his
    head sadly.
        "Just  another  architect of his own destruction."    Pinhead
    grimaced.  "Oh,  and  by  the  way,"  Face continued, "if we have
    anyone down here who knows how to use a personal computer, I have
    an  AutoCad  Model that I think we should upload to some Bulletin
    Boards...".    He  waved  the  disk  that  he  had picked up from
    Andrey's desk.''',
    # ------------------------------------------------------------
    '''One fine day on a MUNI railcar, something nasty walked out of
    a bad end of reality.  Several phone phreaks boarded and moved to
    the back after flashing illegal transfers at the driver, who
    couldn't tell the difference.  Once in the rear, they took out
    screwdrivers, Swiss Army Knives, and other tools and began to
    continue their quest of Dismantling.  By the time they had
    arrived at their stop, several of the seats had been removed, the
    bell rope wasn't working, and the rear driver's compartment had
    acquired a little black box that sent random signals through the
    console for the operator.  Snickering and chuckling, the phone
    phreaks stepped off, and headed for another location to dismantle
    in San Francisco's business district.   Arriving at the
    elevators, the entered and quickly close the doors, installing a
    switch on the open door wire. they went to the top floor and made
    the doors stay shut while they removed the paneling, carpeting,
    both control panels, the buttons therein, the phone's microphone
    ("naw, let's take the handset!" "no, the whole phone!") - make
    that the whole phone - the lights, then got to work on the doors.
    unfortunately, the switch had fallen off and none could find
    either switch nor wires. It looked like our heroes would be stuck
    in the elevator unless they could use the full dismantling
    abilities that they had acquired in their Dismantling in 10 Easy
    Stages class by mail.
        Quickly, they pried open the emergency exit on the ceiling of
    the elevator. With one last twist of the control box wires to
    cause the main circuit box in the basement to blow a major fuse,
    they climbed out on top of the entire elevator booth. Then they
    removed the attachment between the main elevator cabin and the
    cable responsible for its movement. Suddenly, the elevator began
    to plummet! But, soon, the Otis clamps went into operation,
    holding tightly to the walls of the shaft, bringing the elevator
    to a screeching halt, and causing enough heat to turn on the
    sprinkler systems on three floors. It was quite a joyride. Of
    course, using their anarchist ingenuity, our three heroes timed
    the halt perfectly to coincide with the doors of the next floor
    down. With a quick twist of the screwdriver, the doors were
    forced open (permanently) and they were off..down the fire escape
    and out the back door, turning on the rest of the building's fire
    alarms.  All in all it was quite a successful mission. But then,
    a burly, blue dressed man stepped in front of our heroes. 
    
    Cop:"are you the kids that have been screwing around in here?"
    Kids:"no habla ingles senor, somos de espana"
    Cop:"adios"
    
      The phreaks went on, thankful that they stayed awake the day
    they learned that useful phrase in spanish class. Their next
    location: macy's. Yes, it was time to put the song "anarchy in
    macy's" (by chaotic discord) into action.  First, they hooked a
    sex line into the stores pa system.  They then superglued a
    "shoplift detector" to the exit as the alarm screamed. They then
    proceeded to enter the bathrooms.     The plumbing system being
    easy to screw up, the phone phreaks quickly found a decent method
    of raising water level in Macy's.  Laughing, they ran out, and
    proceeded to dismantle the escalators partially.  Some rather
    stupid people just stood there and waited for the escalator to be
    fixed.  Others screamed as the phone phreaks ran up the rails
    brandishing screwdrivers.     Finally, the group of them reached
    the roof, after dismantling some display cases and convincing the
    stupid computers for sale to scream "ANARCHY IN MACY'S!  HAVE A
    NICE DAY!", and they stood up in a high wind.
    
       "Good weather we have here," one of the phreaks commented,
    hugging his jeans jacket closer to himself, obscuring his Anarchy
    T-Shirt.
    
       "Let's  get out of here," another phreak suggested, this one
    dressed in blue jeans, a plaid shirt, and a khaki bush vest
    covered in pockets bulging with dismantling materials.  
    
        A third phreak dressed in an Indiana Jones type outfit
    scratched his moustache, looked around, and discovered the fire
    escape.  "I think we could dismantle that thing and go across to
    the building across the street with it." he announced.  
    
        "Even better, just disconnect a hinge like THIS--" the first
    phreak gestured with his screwdriver "--and we can RIDE it across
    and down to street level." 
    
        Setting quickly to work,  the group made a slight
    modification to the fire escape on Macy's. When it was finished,
    the entire bunch of phreaks clambered onto the same piece of
    structure.  One screw was removed, and the escape hinged down
    very nicely to land them on a MUNI bus that was just passing
    underneath. The Macy's was flooding very satisfactorily.  The
    phreaks then proceeded to the San Francisco (yes, that's where
    this is taking place) city hall.  After painting the lions at the
    entrance purple polka-dots, they entered.  Picking there way into
    the phone system, they connected every phone line together,
    letting over 234 people talk to each other in utter confusion.   
    
        The phreak wearing the khaki bush vest led the charge down to
    the elevators, scattering mundanes left and right.  Quickly
    hotwiring the thing, the elevator took off at top speed for the
    level where they would dismantle the mayor's office.... After
    entering the office, they found (to their horror) that there was
    not one single computer in the whole place.  They had forgotten
    that the mayor hated them. sheesh! Well, they proceeded to
    thermite the marble stairs in the middle of city hall. After that
    they got the bright idea of filling the entire stairwell with all
    of the office furniture that was sitting around. however, they
    forgot about the fact that this was exactly 80 years after the
    earthquake, and one was due in about 20 mins (some friends of
    theirs had hotwired lawrence livermore, and instead of detecting
    the earthquake, livermore was about to START one...)  
    
        "We nearly forgot!" cried our phreaky leader, "Come on! We
    only have twenty minutes!" The dismantling crew dashed out of
    city hall, stopping only to attach limpet mines to the Office of
    Education, and dived out into the street, heading toward the bay.
    A cabli car soon fell prey to their screwdrivers. Pushing off the
    Japanese tourists, the phreakers turned the cable car off the
    tracks and headed it careening down the hill toward the Golden
    Gate bridge. Arriving there, the Indiana Jones type looked down
    at his watch (conveniently taken from the electronics department
    at Macy's).  
    
      "We have 10 minutes until the earthquake. If we time it right,
    we'll accomplish the greatest dismantling job in history! Carl,
    you take that cable over there," said the punk.
    
        The one in the khaki vest shook his head. "No, we will NEVER
    get a screwdriver or bolt cutters big enough to kill THIS baby. 
    Besides, we aren't out to hurt people by dumping them into the
    Bay, we just want to raise Chaos."  
    
        "All right, Carl," the one in the Indiana Jones outfit
    replied.  The cable car careened down the hill and through the
    toll gates.  As it drew alongside a bus, screwdrivers lashed out
    and removed a window, through which the phreaks climbed, much to
    the surprise of the people on board.
    
        "Attention, earthquake starting in six minutes!" the Indiana
    Jones type bellowed.   Carl moved to the front and persuaded the
    driver to forsake his seat in favor of another of the phone
    phreaks, a rather tall one, thin, with brown hair.  
    
        "I've never driven a bus before, and I'm used to an automatic
    transmission," the new driver muttered.  Flooring the
    accelerator, the bus took off for Marin County and a small fort
    where earthquakes wouldn't reach due to lack of anything to
    demolish. It would be a great vantage point.     Carl fiddled
    with a few adjustments on his Walkman-like hunk of gear.
    Strangely enough, his headphones had a small bar leading over to
    the front of the phreak's mouth, terminating in a piece of black
    foam.  He muttered into this thing, and finally got some results. 
    
       "Four point three earthquake coming!" he called over the
    hubbub, as the bus shrieked to a halt and disgorged its
    passengers in favor of a few technological lunatics. The squeak
    of a small lamb could be heard over the engine.     Carl decided
    that a bus REALLY wasn't the place to be during an earthquake,
    and led the exodus out into the middle of the street while things
    started to shake. Fortunately, no one had left their cars without
    the emergency brakes on, otherwise there would have been some
    unusual looking junkheaps everywhere.     As it was, the earth
    shook, the sky looked placid, and someone's new home collapsed
    due to the fact that it was designed for tectonically stable
    country.  
    
       "HEY!  That's not fair!" the one in jeans jacket and anarchy
    T-shirt remarked.  "That house just dismantled itself without our
    help!" 
     
       Then they woke up and realized that they had been abducted by
    the DOD and were now being held underground.... a mean looking
    man came in and told them to stand on their tails and beat them
    when they didn't (hard as they tried!)... but the mean old meany
    finally left them alone... but didn't realize that each phreak
    kept a screwdriver in each armpit (uncomfortable but...)... and
    the hinges were on the inside... They unscrewed the hinges, and
    then proceeded to connect all 676 water fountains to the toilet
    outlet.  
    
       "A Swiss Army Knife is one of the most useful tools I can
    think of," Carl stated as they crept down a corridor.  The
    phreaks flattened against the wall as they heard voices.
         
       "Look at all this junk!" an incredulous voice spoke.  "These
    guys are prepared to dismantle a building and send it crashing
    down in pieces!"     "I know...  look at what they had in their
    pockets..  screwdrivers, communicators, some sort of homebrew
    explosive if I'm not mistaken.. I think we should send them to
    Russia and see if they can bring back pieces of the Kremlin."    
    
       The phreaks looked at each other, and, as one, they went to a
    fire hose niche in the wall.  Silently opening the glass door,
    Carl took the hose out and snuck over to the door where they
    heard the voices.  At a nod from Carl, the punk rocker turned the
    hose on.  
    
        "I'VE GOT A 27B/6!" Carl screamed as he leapt into the room
    and applied fluid pressure to the faces of the two men discussing
    the phreaks' gear. Both of them were knocked into the walls as a
    result of this, and Carl found it hard to control the hose
    himself.  "Shut it off!" he called.  The water stopped jetting
    out of the hose, and the two officials just SAT there, staring,
    as Carl picked up his vest and a bunch of the gear strewn around
    the desk.
    
        Selecting a small box, he opened it and removed two gelatin
    capsules.  "I KNEW my uncle's LSD pills would come in handy one
    of these days,though I had intended them for a school water
    supply," Carl announced as the other phone phreaks walked in and
    relieved the desk of their gear. 
    
        Carl walked over to the coffee machine, got os the other
    phone phreaks walked in and relieved the desk of their gear.    
    Carl walked over to the coffee machine, got out a cup of coffee,
    went over to the first official, grabbed the sides of the jaw on
    the pressure points, tossed the capsule and some coffee into his
    mouth, and sent LSD floating down into one Pentagon official's
    stomach. 
    
        "Hey, that looks neat, let ME try!" the punk rocker said.  He
    followed Carl's example with the other official, and laughed as
    the guy began to moan about sheep.  
    
        "Well, I've got my duffel, Carl has his vest, everyone else
    has their backpacks and stuff?" the punk rocker asked.  "Anything
    missing? Let's go!"  
    
        "Wait," the Indiana Jones type said. "I want to get to a
    computer terminal."
    
        "Hmm, theirs lots of security around that room, here's what
    we will do" mused the punk.  The phreaks then proceeded to take
    down the ceiling (it was one of those panels ones) until they
    found the pa wires.  Finding them, they connected them to a
    microphone and the one in the vest said: "Attention! Your
    attention please! A bomb has been planted in the computer room
    pleas evacuate now!" The officials, used to their cozy offices,
    far from the troubles of the world, quickly ran to the bomb
    shelter, deep in the core of the hidden Pentagon headquarters. 
    
       Meanwhile, the dismantlers managed to find the exit to the
    secret government building.   "Gee," said the Indiana Jones type,
    "we can't ruin all of this suspense." With a nod from the leader,
    Jones removed several homemade limpet mines from his duffel.  He
    dived back into the underground Pentagon hideout, and proceeded
    to place them in key support points in the hideout's structure.
    With the bombs in place, he headed for the exit. Suddenly, he was
    confronted by a new, high-tech Defense robot. It was heading
    toward him, and he had no place to turn. And the bombs were due
    to go off in 3 minutes!
    
       "Greeting," the Indiana Jones type called.  `I've got to stall
    for time,` he thought.  `The guys will be in the computer room
    about now.`
    
       The robot scanned the Jones type.  It identified it as human,
    unidentified, not in uniform, and classified it as an intruder.  
    "Surrender," the robot announced calmly, with a few armaments
    sticking out of its metal hide.  "Or die," it added, wishing that
    it didn't have all this humanitarian programming and could just
    kill the commie traitor in front of it. 
    
      "I surrender!" the Jones type yelled, tossing a small homemade
    grenade straight at the sense cluster of the robot.  Quisp,
    whipped cream, and sticky foam clouded the robot's vision.  It
    immediately began to spin around and waste ammo at the ceiling.  
    
      "Sheeeit," the Jones type said, and ran to the computer
    room."Guys, we got the mines going off in a few minutes!" he
    called.
      
      "We've just about got the external access port coded right,"
    Carl called.  Three printers hummed steadily, and two keyboards
    clicked at an alarming rate as Carl and the punker moved like
    four hands and one brain.  
    
      "GOT IT!" the punker yelled.  He ripped a piece of printout out
    of a printer. "We can access this thing later, with invisible
    system manager access! Noone will even be able to TELL we're on!" 
    
       "And we can do some funny things to the ARPANET and MILNET
    through this, too," Carl added, ripping the last of the printouts
    off and shutting the thing down. "Let's MOVE!"     
       There were no security guards to watch the cameras photograph
    phone phreaks dashing out of the Pentagon and into the parking
    lot.
       "I wonder if Yog Sothoth is really kept there," the Indiana
    Jones type wondered.  Carl grinned and remembered _The
    Illuminatus! Trilogy_, and all the fun stuff in there.    
    
       "Here's a van," the ex-bus-driver commented, picking the lock
    of the vehicle and hotwiring it easily.  "Let's get out of here
    before she blows."   Everyone piled into the van, Carl and the
    driver in front, the Indiana Jones type and the punker perched at
    the sunroof and door respectively, and the rest strewn about the
    vehicle.  
    
        "Gee, has modern armaments, too," Carl noted. "Let's not
    shoot anyone, OK?" 
    
        "Awww," the punk sulked.  Rapidly accelerating away, they
    realized too late that the gate was guarded but 12 exceedingly
    nasty looking green berets and2 soldiers. Luckily no-one was
    wearing the berets, so their mobility was hampered. Carl stopped
    at the 3 foot thick barrier and the soldier came out of the guard
    house, gun at ready.  
    
        "What're you kids doing here?" the soldier asked.
         Imagine: in three seconds, all of the below happened:       
         "Uh, looking around" said Carl.
         "Oh, visiting our parents" said the punk.
         "On a field trip" said the guy in khaki.
         "Shh.... national security" someone else said. 
         "Wait, can I see that?" Carl tried again, taking the gun.
    "Hmmm.... *nice* spring... I wannit.... and the barrel! great for
    rockets! mine!" several seconds later he handed the bewildered
    guard 4 screws (glued together), the trigger, hand grip, and 50
    bullets (minus gunpowder). He then snapped a salute. 
    
       "Thank you, sir" said the soldier, the phreaks left. As the
    phreaks were in the area they decided, what the hell, lets drop
    in on the nsa (national security agency).  So driving the
    official IDI-mobile they went. Their first target was the outer
    perimeter security.  Using the electric fence, they hooked up a
    stereo system putting on some hardcore/speed thrash/skate/punk
    thereby using up all the fences power and causing the guards &
    dogs to slam dance together. Then entering, taking a brief time
    to replace the "keep out" signs with "gay bar" signs, they went
    into the main entrance. Guard: "what the hell are you kids doing
    here?" Khaki vest person: "hi-ya! We aren't here! Were invisible
    ya see." Guard: "oh." And turns away they then proceeded down to
    corridor to the crypto  room.  Dismantling the cray ii and
    replacing it with a trs-80 model 1 gave  them  some interesting
    answers.  Then  onto  signal intelligence.  Hooking the satellite
    input to the playboy channel, and then dismantling all computers
    caused some anguish, but also some perverted happiness. Finally
    to the heads office! Tying him up, our heros arranged his office
    into a art exhibit entitled: "kinetic chaos".
        Carl reached into his khaki bush vest and pulled out a piece
    of paper, much folded.  "Hey, guys, maybe we should enter a few
    phone numbers into their registry of dangerous criminals.. 
    lessee, Oryan Quest, who else?"  
        The punk giggled as he watched the guards and dogs slam
    dancing.  An indecent number of gays had taken over the
    commissary, thanks to the GAY BAR signs, but not before the Coke
    machine had been dragged up to the terminal room where the
    phreaks were lounging, munching on microwave popcorn, quaffing
    Classic Coke, and eating various vending-machine foods. 
        Carl grinned, typed at a terminal, and found a little
    information. "Hey, guys, they have IDI listed as potentially
    dangerous!"  
        "Nuke 'em," the punk advised. 
        "Okay," Carl said, typing a little more, and informing the
    NSA that the Stanford ARPANET dialup was a definite threat to
    national security. 
        "Well, we better get going," stated a tall, thin phreak
    described as a "football player" to Carl once.  "We SHOULD get
    back to the Bay Area soon..."  
       "Why?" asked the driver. 
       "Oh, I left a few things undone."  
       "VERSION FOUR POINT FIVE???"   
       "Point six."  
       "Oh." 
       Reluctantly, the phreaks flooded the NSA, the gay orgy, the
    slam dancing guards and dogs, and left the building a bizarre
    sort of public fountain as they drove off into the sunset,
    heading for the airport.  
       "Don't worry," Carl said.  "We've got some credit cards, we
    can get plane tickets back to the Bay Area."  
       "What if we take the plane apart midway?" asked the Indiana
    Jones type.  ''',
    #---------------------------------------------------------------
    '''This is the rationalist view:
     The lionbird is a species of eagle which travels and hunts
    in prides.  Prides take prey of all sizes from pigeons to bison,
    and also eat carrion.  Each pride has a king, or alpha male,
    several subordinate males, and many females.  Many young males
    leave the pride to travel in bachelor packs, and eventually join
    prides other than those of their birth.  Their secretive breeding
    habits have led to the legend that they hatch their eggs in
    heaven.  This legend is disproved by the occasional sighting of a
    lionbird in Fire Season, when they supposedly are all in heaven. 
    Their plumage is tawny.  Males have golden crests, and the king
    always has the largest crest in the pride.  Kings live only a
    year, worn out by monopolizing the mating.  Lionbirds have a
    group song, sometimes heard by humans, which is alien but
    rhythmic.
    
    This is the theistic view:
         The lionbird is one of the oldest children of Vrok.  It was
    one of the favorites of Murharzarm and he often hunted with it. 
    The lionbird pride emulates the divine order of Yelm, with a
    king, several subordinates, and males over females.  The male's
    golden crest is a special blessing from Vrok, and sign of his
    favor.  It is regicide to kill a king lionbird, ignoble to slay
    any male lionbird, and bad luck even to disturb a pride.
         The sky gods use lionbirds as messengers to mortals, for
    they travel to the sky once a year, in Fire Season.  Outlaw birds
    must remain behind on the earth.  When the prides reach heaven,
    old kings retire there forever.  One male in each pride finds the
    divine meal which makes him the new king.  The females bear the
    new king's eggs and hatch them near the end of Fire Season.  The
    eggs are gold in color, but not metallic.  Fed on fire berries
    and the meat of heavenly animals, the young grow fast.  At the
    end of Fire Season, the females push the young out of their
    nests, and the fledglings must learn to fly as they plummet
    toward the earth.  The pride follows, calling out instructions to
    the young ones.  Those who learn to fly join the pride.  Those
    who do not, plunge into the sea.  This represents the virtue of
    Justice.
         The lionbirds sing, representing the virtue of Harmony. 
    Their song often reveals messages from heaven to those with the
    wisdom to understand.  To hear their song is a blessing, and
    bound to bring the same joy of the heart which the sun brings
    when he bursts through clouds.
         Sheng Seleris was accompanied in much of his career by a
    pride of lionbirds who brought him messages from the sky gods. 
    They sang to him each morning, and he interpreted their songs to
    his companions.  Other solar heroes, mostly of the Golden and
    Silver Ages, had friendly lionbird prides. 
         Lionbird feathers are good for many Light, Fire, Harmony,
    Life, and Death magics.  Crest feathers are best.  Pentian kings
    need lionbird feathers for their head-dresses.
    
    This is the game view:
    Lionbirds are medium-sized eagles.  Their keen sight and high
    intelligence would make them good familiars and allied spirits,
    but they grow lonely away from their pride and sometimes pine
    away and die.  A lone bird lives no more than five years in
    captivity, less if caged or wing-clipped.  Allying an entire
    pride is possible, if one gains the friendship of the king. 
    However, the whole pride then flies away in late Sea Season.  The
    king does not return, so neither does the pride (in most cases).
         An adventurer can use Falconry (a/k/a Hawking) to train a
    lionbird.  Training is easier if the trainer wears a yellow
    feather crest on his hat or helm.  The lionbird song is
    instinctive, however, and training cannot change it.  Using
    Falconry on a king lionbird carries a 50 percentile penalty.
         The statistics below are for an average male, which is about
    .8 meters long, beak to talons, and has a 2 meter wingspan (about
    the size of a bald eagle).  The king has a SIZ of 4 (1.1 meters
    long and 3 meter wingspan--the size of a California Condor).  The
    king has a STR of 18 and INT of 5, and POW above 12.  Average
    females are .7 meters long, with a 1.8 meter wingspan and STR
    2D6+4, but are otherwise the same as average males.  The smallest
    young observed are SIZ 2 (.6 meters long, 1.5 meter wingspan).
    
    characteristics     Average
    STR  2D6+5            12           Move: flying 12, walking 1
    CON  2D6+3            10           
    SIZ   3                3           Hit Points          7
    INT   4                4
    POW  3D6             10-11
    DEX  3D6+18          28-29
    
    Hit location        Melee (D20)    Missile (D20)       Points
    R Leg               01-02          01                  0/2
    L Leg               03-04          02                  0/2
    Abdomen             05-07          03-06               1/3
    Chest               08-09          07-11               1/3
    R Wing              10-13          12-15               0/2
    L Wing              14-17          16-19               0/2
    Head                18-20          20                  1/3
    
    Weapon     SR       Attack %       Damage
    Dive      Special   45+10          2D6
    Claw        7       60+10          1D6
    Peck       10       45+10          1D3
    
    Note: Lionbirds Dive to kill small prey or to wound larger prey. 
    Lionbirds attack large foes (SIZ 4 and up) in a group, with some
    distracting the foe while others Dive and then claw and peck. 
    The distraction subtracts 5% from the target's skills for each
    lionbird in the attacking group, up to 75%.  Each lionbird that
    closes gets a Dive attack.  If the prey does not effectively
    attack back, the lionbird stays near it and gets Claw and Peck
    attacks in the next round.  If the prey tries to attack back, the
    Lionbird wheels away, climbs, and gets another Dive attack on the
    sixth round after the last Dive.  Lionbirds never suffer a damage
    penalty for STR + SIZ when using natural weapons.
    
    Skills: Dodge 80+19, Scan 100-6, Search 100-6.
    Armor: 1 point feathers on abdomen, chest, and head.
    
    
    Random note: The mongols used Golden Eagles to hunt wolves, and
    the weight to strength ratio of raptors is much higher than
    represented in the RQ rules.  Change the Hawk stats on page 24 of
    the RQ Creatures Book to STR 2D6+2 for hawks and STR 2D6+5 for
    eagles.  The strength of raptors is concentrated in their talons
    and flight muscles, however, and a normal human could wrestle one
    pretty easily as long as he guarded against the beak and talons.''',
    #-------------------------------------------------------------------
    '''David and Adriane came barging into the room.  Adreane's blue-black eyes were
    immediately drawn to Leona's bra on the chair.  Wow.  For somebody's mother,
    Leona was really something.  He could not believe thats a woman like that was
    running around loose.  Watching her earlier this afternoon had made his tounge
    hard and slick with saliva - not to mention the big prick that made a tent in
    his pants.
    
      "Hey Mom," David said, "we couldn't sleep and I thought maybe a nightcap
    would help.  You don't mind, do you?  I mean, I'm already over eighteen."
    
      Yes, Marlene thought to herself, he is over eighteen and a supper-looking
    boy.  She wondered how Leona would react if she knew what was on her mind.
    Looking at David standing there in his pajamas mixing a drink made her panties
    damp with desire.  Her huices were flowing.  By morning, Earl would have that
    detective trailing her around.	His threats were never empty.  For tonight...
    
      "I didn't have a chance to express my sympathy, Mrs.  Lambert," Adriane told
    Leona, edging close to her giving her a tooth-flashing grin - not too wide, but
    a proper grin, appropriate to the occasion.  Only his young body was so close,
    so scantily clad in the this cotton pajamas he wore.  His aroused tool was
    already trying to poke its bulbous head out of the fly front.  Oh boy!	He was
    deliciously indecent.
    
      Leona was aware of her breasts tightening so they stood out in hard little
    peaks.	She knew the tips of them were visible thrusting against the voile of
    her dress.  She and Marlene should excuse themselves for just a moment to
    change into something more comfortable.  Besides, Leona wanted a small
    conference with her friend.  Not for the first time, she wondered is her son
    was a virgin.  With her hot blood running in his veins, she seriously doubted
    it.
    
      "I appreciate your sentiments, Adriane," Leona told the boy, giving his a
    grin that was not proper.  "Why don't you boys make yourselves at home out here
    while Marlene and I make ourselves cozy?  Looks like none of us is ready to
    sleep tonight."
    
      "Sure Mom," David replies innocently.  Or was it innocent?  There was an
    undertone to his cavalier reply, an awareness.	Did he know about his Mom and
    her girlfriend?
    
      The women laughed as they raced for Leona's bedroom.  The sound of their
    voices was enough to make doubts certanities.  They definitely agreed that they
    would make this a night to remember.  No words were necessary.
    
      "Here, put this on," Leona told Marlene, handing her a sheer nightgown in a
    pale pink.  "I'm going to wear my black one tonight - the one that shows
    everything I own.  If I didn't know any better, I'd think that friend of
    David's has the hots for me."
    
      "You are turning into a dirty old lady," Marlene giggles.  She stuck one of
    her clever fingers up her damp hole after she stripped.  It was nice to feel
    how ready she was.  Watching, Leona gasped in sudden pleasure at the sight.
    
      "This seems to be my day for lingerie!" Leona exclaimed.  "I thought Buff was
    going to shoot at the skies when he got a load of that black garter belt."
    
      "mine had the same affect on Luther," Marlene reported.  "Now I wonder what
    effect this revealing bit of nothing will have on those young men out there?"
    
      "I wonder," was all Leona replied.  She was readying herself to meet
    Adriane's adoring glance.  She brushed her long, flaming hair so it came past
    her shoulders.	Still, the silky strands did not hide her elongated nipples
    which were visible through the filmy lace of her sexy nightdress.  Further, her
    pussy showed in the most delightful way, a muff of brilliant color in the
    shadowy cleft between her lucious legs.''',
    #------------------------------------------------------------------------
    '''Once upon a time . . . in a splendid palace on the bed of the bluest ocean,
    lived the Sea King, a wise old triton with a long flowing white beard. He
    lived in a magnificent palace, built of gaily coloured coral and seashells, 
    together with his five daughters, very beautiful mermaids.
       Sirenetta, the youngest and loveliest of them all, also had a beautiful
    voice, and when she sang, the fishes flocked from all over the sea to listen
    to her. The shells gaped wide, showing their pearls and even the jellyfish
    stopped to listen. The young mermaid often sang, and each time, she would gaze
    upwards, seeking the faint sunlight that scarcely managed to filter down into
    the depths.
       "Oh, how I'd love to go up there and at last see the sky, which everyone 
    says is so pretty, and hear the voices of humans and smell the scent of the
    flowers!"
       "You're still too young!" said her mother. "In a year or two, when you're
    fifteen. Only then will the King let you go up there, like your sisters!" 
    Sirenetta spent her time wishing for the world of humans, she listened to her
    sisters' stories, and every time they returned frorm the surface, she would
    ask them questions, to satisfy her curiosity.
       And as she waited for the day when she too would be allowed to reach the
    surface of the sea and meet the unknown world, Sirenetta spent her time in her
    wonderful sea garden. The seahorses kept her company, and sometimes a dolphin
    would come and play. Only the unfriendly starfish never replied when she
    called. At last, her long-desired birthday came. The night before, Sirenetta 
    could not sleep a wink. In the morning, her father called her and, stroking
    her long golden hair, slipped a lovely carved flower into her locks . . .
       "Therel Now you can go to the surface. You'll breathe air and see the sky. 
    But remember! It's not our world! We can only watch it and admire! We're
    children of the sea and have no soul, as men do. Be careful and keep away from
    them; they can only bring bad luck!" In a second, Sirenetta had kissed her
    father and was darting smoothly towards the surface of the sea. She swam so
    fast with flicks of her slender tail, that even the fish could not keep up
    with her. 
       Suddenly she popped out of the water. How wonderful! For the first time, 
    she saw the great blue sky, in which as dusk began to fall, the first stars
    were peeping out and twinkling. The sun, already over the horizon, trailed a
    golden reflection that gently faded on the heaving waves. High overhead, a
    flock of gulls spotted the llttle mermaid and greeted her arrival with shrieks
    of pleasure.
       "It's so lovely!" she exclaimed happily. But another nice surprise was in
    store for her: a ship was slowly sailing towards the rock on which Sirenetta
    was sitting. The sailors dropped anchor and the ship swayed gently in the calm
    sea. Sirenetta watched the men go about their work aboard, lighting the
    lanterns for the night. She could clearly hear their voices.
       "I'd love to speak to them!" she said to herself. But then she gazed sadly
    at her long flexible tail, her equivalent of legs, and said to herself: "I can
    never be like them!" Aboard ship, a strange excitement seemed to seize the
    crew, and a little later, the sky became a spray of many coloured lights and
    the crackle of fireworks filled the sky.
       "Long live the captain! Hurray for his 20th birthday. Hurray! Hurray . . . 
    many happy returns!" Astonished at all this, the little mermaid caught sight
    of the young man in whose honour the display was being held. Tall and
    dignified, he was smiling happily, and Sirenetta could not take her eyes from
    him. She followed his every movement, fascinated by all that was happening. 
    The party went on, but the sea grew more agitated. Sirenetta anxiously 
    realized that the men were now in danger: an icy wind was sweeping the waves, 
    the ink black sky was torn by flashes of lightning, then a terrible storm
    broke suddenly over the helpless ship. In vain Sirenetta screamed: "Look out! 
    Beware of the sea . . ." But the howling wind carried her words away, and the
    rising waves swept over the ship. Amidst the sailors' shouts, masts and sails
    toppled onto the deck, and with a sinister splintering sound, the ship sank.
       By the light of one oi the lamps. Sirenetta had seen the young captain fall
    into the water, and she swam to his rescue. But she could not find him in the
    high waves and, tired out, was about to glve up, when suddenly there he was on
    the crest of a nearby wave. In an instant, he was swept straight into the
    mermaid s arms.
       The young man was unconscious and the mermaid held his head above water in
    the stormy sea, in an effort to save his life. She clung to him for hours
    trying to fight the tiredness that was overtaklng her. 
       Then, as suddenly as it had sprung up, the storm died away. ln a grey dawn 
    over a still angry sea, Sirenetta realized thankfully that land lay ahead. 
    Aided by the motion of the waves, she pushed the captain's body onto the
    shore, beyond the water's edge. Unable herself to walk, the mermaid sat
    wringing her hands, her tail lapped by the rippling water, trying to warm the
    young captain with her own body. Then the sound of approaching voices startled
    Slrenetta and she slipped back into deeper water.
       "Come quickly! Quickly!" came a woman's voice in alarm. "There's a man
    here! Look, I think he's unconscious!" The captain was now in good hands.
       "Let's take him up to the castle!"
       "No, no! Better get help . . ." And the first thing the young man saw when
    he opened his eyes again was the beautiful face of the youngest of a group of
    three ladies.
       "Thank you! Thank you . . . for saving my life . . . he murmured to the
    lovely unknown lady.
       From the sea Sirenetta watched the man she had snatched from the waves turn
    towards the castle, without knowing that a mermaid had saved his life. Slowly
    swimming out to sea, Sirenetta felt that there on the beach she had left
    behind something she could never bring herself to forget. How wonderful those
    tremendous hours in the storm had been, as she had battled with the elements.
    And as she swam down towards her father's palace, her sisters came to meet
    her, anxious to know what had kept her so long on the surface. Sirenetta 
    started to tell her story, but suddenly a lump came to her throat and, 
    bursting into tears, she fled to her room. She stayed there for days, refusing
    to see anyone or to touch food. She knew that her love for the young captain
    was without hope, for she was a mermaid and could never marry a human. Only
    the Witch of the Deeps could help her. But what price would she have to pay? 
    Sirenetta decided to ask the Witch.       .
       ". . . so you want to get rid of your fishy tail, do you? I expect you'd
    like to have a pair of woman's legs, isn't that so?" said the nasty Witch
    scornfully, from her cave guarded by a giant squid.
       "Be warned!" she went on. "You will suffer horribly, as though a sword were
    cutting you apart. And every time you place your feet on the earth, you will
    feel dreadful pain!"
       "It doesn't matter!" whispered Sirenetta, with tears in her eyes. "As long
    as I can go back to him!"
       "And that's not all!" exclaimed the Witch. "In exchange for my spell, you
    must give me your lovely voice. You'll never be able to utter a word again! 
    And don't forget! If the man you love marries someone else, you will not be
    able to turn into a mermaid again. You will just dissolve in water like the
    foam on the wave!"
       "All right!" said Sirenetta, eagerly taking the little jar holding the 
    magic potion. The Witch had told Sirenetta that the young captain was actually
    a prince, and the mermaid left the water at a spot not far from the castle. 
    She pulled herself onto the beach, then drank the magic potion. An agonizing
    pain made her faint, and when she came to her senses, she could mistily see
    the face she loved, smiling down at her.
       The witch's magic had worked the spell, for the prince had felt a strange
    desire to go down to the beach, just as Sirenetta was arriving. There he had
    stumbled on her, and recalling how he too had once been washed up on the shore,
    gently laid his cloak over the still body, cast up by the waves.
       "Don't be frightened! he said quickly. "You're quite safe! Where have you
    come from?" But Sirenetta was now dumb and could not reply, so the young man
    softly stroke her wet cheek.
       "I'll take you to the castle and look after you," he said. In the days that
    followed, the mermaid started a new life. She wore splendid dresses and often
    went out on horseback with the prince. One evening, she was invited to a great
    ball at Court. However, as the Witch had foretold, every movement and each
    step she took was torture. Sirenetta bravely put up with her suffering, glad
    to be allowed to stay near her beloved prince. And though she could not speak
    to him, he was fond of her and showered kindness on her, to her great joy.     However, the young man's heart really belonged to the unknown lady he had seen
    as he lay on the shore, though he had never met her since, for she had
    returned at once to her own land.        
       Even when he was in the company of Sirenetta, fond of her as he was, the
    unknown lady was always in his thoughts. And the little mermaid, guessing
    instinctively that she was not his true love, suffered even more.
       She often crept out of the castle at night, to weep by the seashore. Once
    she thought she could spy her sisters rise from the water and wave at her, but
    this made her feel sadder than ever.
       Fate, however, had another surprise in store. From the Castle ramparts one
    day, a huge ship was sighted sailing into the harbour. Together with
    Sirenetta, the prince went down to meet it. And who stepped from the vessel, 
    but the unknown lady who had been for long in the prince's heart. When he saw
    her, he rushed to greet her. Sirenetta felt herself turn to stone and a
    painful feeling pierced her heart: she was about to lose the prince for ever. 
    The unknown lady too had never forgotten the young man she had found on the
    bea and soon after, he asked her to marry him. Since she too was in love, she
    happily said "yes".
       A few days after the wedding, the happy couple were invited for a voyage on
    the huge ship, which was still in the harbour. Sirenetta too went on board, 
    and the ship set sail. Night fell, and sick at heart over the loss of the
    prince, Sirenetta went on deck. She remembered the Witch's prophecy, and was
    now ready to give up her life and dissolve in the sea. Suddenly she heard a
    cry from the water and dimly saw her sisters in the darkness.
    ". . . Sirenetta! Sirenetta! It's us . . . your sisters! We've heard all
    about what happened! Look! Do you see this knife? It's magic! The Witch gave
    it to us in exchange for our hair. Take it! Kill the prince before dawn, and
    you will become a mermaid again and forget all your troubles!"
       As though in a trance, Sirenetta clasped the knife and entered the cabin
    where the prince and his bride lay asleep. But as she gazed at the young man's
    sleeping face, she simply blew him a furtive kiss, before running back on
    deck. When dawn broke, she threw the knife into the sea. Then she shot a
    parting glance at the world she was leaving behind, and dived into the waves, 
    ready to turn into the foam of the sea from whence she had come, and vanish.
       As the sun rose over the horizon, it cast a long golden ray of llght across
    the sea, and in the chilly water, Sirenetta turned towards it for the last
    time. Suddenly, as though by magic, a mysterious force drew her out of the
    water, and she felt herself lifted high into the sky. The clouds were tinged 
    with pink, the sea rippled in the early mornlng breeze, and the little mermaid
    heard a whisper through the tinkling of bells: "Sirenetta, Sirenetta! Gome
     wlth us ..."
       "Who are you?" asked the mermaid, surprised to find she had recovered the
    use of her voice. "Where am l?" 
       "You're with us in the sky. We're the fairies of the air! We have no soul
    as men do, but our task is to help them. We take amongst us only those who
    have shown kindness to men!"
       Greatly touched, Sirenetta looked down over the sea towards the prince's
    ship, and felt tears spring to her eyes. The fairies of the air whispered to
    her: "Look! The earth flowers are waiting for our tears to turn into the
    mornlng dew! Come along with us ..."''',
    #---------------------------------------------------------------------

]

TITLES = ['A Close Encounter of a Different Kind', 'The Fox and the crow', 'The Adventure of the Golden Pince-Nez',
          'Time for flowers', 'A mismatched pair of gloves', 'The Gold Bug', 'Donatien Alphonse Francois de Sade', 'The first Adventures of IDI',
          'LionBirds', 'I have no idea where it is', 'The Little Mermaid']


def status(i):
    if i%2==0:
         return 'unapproved'
    else:
        return 'approved'

IMGS = ['v1561862876/themilkyway/profile_pics/001.jpg',
        'v1561862809/themilkyway/profile_pics/002.jpg',
        'v1561862809/themilkyway/profile_pics/003.jpg',
        'v1561866464/themilkyway/profile_pics/005.jpg',
        'v1561862808/themilkyway/profile_pics/004.jpg',
    ]

SUMMARY = [
            'The story of Alex a cop in Alabama district who chased a thief for 40 kilometers just to know that?',
            'The fox and the crow have always been sworn enemies and now that they are set to work together what will happen?',
            'Golden Prince-Nez is a detective but the case of Robert Willams is the one he will never forget for his entire life.',
            'Amy has always loved flowers, Daisy in particular but this Christmas these flowers will bring death, sorrow and pain.',
            'Rolland is a hard worker in a factory. One day one of his gloves gets exchanged with some stranger in train. What will he do?',
            'The streets of Allahbad were the only playing grounds for Renu. One day she went too far to catch a lazy bug. What was so special about is!',
            'The world has never been fair with Donatien, follow him on his journey to reach the heights he has always desired.',
            'The IDI was a group of children who always wanted to solve a mystery. How did they react when they really had one in their reach.',
            'Sofia lost her wedding ring somewhere on the way to th hospital. Now she is really worried about how she will confront her husband.',
            'Are mermaids real Mehmed asked Zubair. This story is all about two friends Mehmed and Zubair who always wanted to see a mermaid.'
        ]

def create_dummy_data():
    conn = psycopg2.connect(dbname='themilkyway', user='postgres', password='1999')
    cur = conn.cursor()
    for i in range(6):
        cur.execute('INSERT INTO active (uid, time, name, email, password, likes, views) VALUES (%s, %s, %s, %s, %s, %s, %s)',
                    (UID[i], TIME[i], NAMES[i], ('.'.join(NAMES[i].lower().split()) + '@gmail.com'), HASHES[i],
                     random.randint(10000, 30000), random.randint(10000, 30000),))
    for i in range(10):
        cur.execute('INSERT INTO stories (sid, uid, status, time, title, summary, story, views, likes, genre) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',
                    (SID[i], AUTHORS[i], status(i), SUB_TIME[i], TITLES[i], SUMMARY[i], STORIES[i],
                     random.randint(10000, 30000), random.randint(10000, 30000), 'Classic,Humor'))
    for i in range(1,6):
        cur.execute('INSERT INTO basic (sno, uid, dob, bio, country, profession, image, private, preferences) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)',
                    (i, UID[i], '06-06-2000', 'Hey! There I am on tmw!', 'India', 'Student', IMGS[i-1],
                     False, 'Classic'))
    conn.commit()
    cur.close()
    conn.close()

