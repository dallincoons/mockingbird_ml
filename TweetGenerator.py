class TweetGenerator:
    tweets = [
        'i am in iowa . will be making some great big things !',
        'black lives have just left my office.',
        'my thoughts and prayers are with the two police and people in the country of our country',
        'as i predicted 1 year ago gasoline prices hit a super vote !',
        'fact – amnesty wages are coming over the country . also jobs are being called to the us - - - the smart pols will tell it like it is . you must win and make safety',
        'the blue monster is amazing !',
        'can  t wait for the new season of apprentice but if so we have to be in the works with north korea . always know when they know they can ’ t win based on the president of the united states was born in canada lived there to start !',
        'you can walk and golf these things',
        'our thoughts and prayers are with you . # makeamericagreatagain',
        'our nation is a broken part of the corruption on the storm . they should have had a little one day with president trump . ” - think like a billionaire',
        'i cannot wait to see @ realdonaldtrump on # celebrityapprentice @ nbc !',
        '@ : @ realdonaldtrump @ foxandfriends i always respect for this and our country !',
        'so many people have me asking my numbers losing $ 10 million for charity .',
        '@ : @ realdonaldtrump i think you would be our president . . .',
        'we are getting reports - - a total disgrace .',
        '. @ alexsalmond rt @ you are a moron george will never be allowed to be in america - - and he makes a great guy who truly is in a making is good .',
        'derek jeter broke the republican state of virginia',
        'interesting that @ macys criticized me but the donald will be speaking into my old days when i  m going to do a really good job .',
        'the of north korea will be forced to raise taxes . not fair !',
        '@ mittromney should not start thinking . the world is in you . i will not be doing so .',
        'today we honor those who perished millions of people . now they must be changed but nobody ever thought about it !',
        'breaking news - the new year @ cnn can be a major announcement about the humanitarian crisis on our southern border . i am in the white house waiting for the democrats to do the inevitable in a political career .',
        'what is your favorite plane ? ? ? ? ? ? ? they will soon be fired !',
        'there definitely a great country . jobs jobs jobs !',
        'crooked hillary clinton is not working !',
        'most important things of democrats think they should really have been a fired !',
        'russian collusion was a " not qualified to support trump . . . . . . the trump is totally unqualified . ” – Donald trump',
        "if obama doesn ' t have the balls to do what ’ s a really good could stand up for the american people . wanted to be the past for the world to be corrupt economy in the country . it is failing badly !",
        'certain people are ruining their vote for me . # trump2016',
        'there is no collusion in russia or the wall there is no reason for my own meeting with cnn and the u . s . a .',
        "we ' re going to cut spending the price of dollars .",
        'unless you catch " hackers " in the act . “',
        'yankees should have dropped isis in order to become the worst president in the history of the united states !',
        'wall street is a loser .',
        'the failing @ nytimes wrote a story about me in the trump tower atrium .',
        'now that the three basketball players continue to take over the country !',
        "remember the midterms ! work is being done it ' s not your sleep !",
        'four more days until the miss universe pageant great !',
        'the democrats are making over the $ of the oil you are used in the polls to support my numbers . total phony $ witch hunt in the first place . this is a movement . . . if you listen to the fake news media you would think that i am a big one . thank you',
        'our economy is better than this has ever been accomplished !',
        'nancy pelosi and fake tears of interest . she is a great guy !',
        'thank you to the washington examiner and dangerous chinese to # jobs !',
        'wishing everyone a safe and happy birthday !',
        'funny how the fake news media doesn ’ t work .',
        'my thoughts and prayers are with the victims and hostages . they want to be great !',
        'business is looking for a great heart and a beautiful business man ! ! ! !',
        'dummy @ mcuban is an extraordinary woman . he was an extraordinary first leader look into my many countries !',
        'the fake news media is officially right about new york city . golf !',
        'massive crowds inside and outside the road !',
        'so much fake news !',
        'thank you to @ law enforcement agencies for @ ( republican ) city',
        'i am pleased to announce that our very nothing to do . tremendous success !',
        "obama ' s deal was terrible . the world is in look to your life and when you just have a large loser !",
        'witch hunt ! a sad day for our country !',
        'for all of those who have been asking about online sales day . people must pay for the of our great u . s . border patrol that are not enough for me !',
        'texas is fast . we must all get tough and be tough . they are very smart !',
        'still waiting for a response to congress - - i told you so .',
        'the u . s . air dropped a large of crime . pay bill is getting the billions of ( work ) is a sad and pathetic for people',
        'if you want to protect criminal aliens – vote democrat . if you want to protect people with people from your country . - think like a champion',
        "lots of response to my comment on diet coke - ' ' s ' -"
    ]

    @staticmethod
    def new(index):
        print(TweetGenerator.total_tweets())
        if index >= TweetGenerator.total_tweets():
            index = 0
        tweet = TweetGenerator.tweets[index]

        return tweet

    @staticmethod
    def new_index(index):
        if (index >= TweetGenerator.total_tweets() - 1):
            return 0
        else:
            return index + 1

    @staticmethod
    def total_tweets():
        return len(TweetGenerator.tweets)
