"""
Offensive Script
18+
Script for NLP Task
Use for educational purpose only
"""

import re

def prof(text):
    word=text.split(" ")
    offensive_set=[]
    for text in word:

      b=re.match('''(4r5e|5h1t|5hit|a55|anal|anus|ar5e|arrse|arse|ass|ass-fucker|asses|assfucker|assfukka|asshole|assholes|asswhole|a_s_s|b!tch|b00bs|b17ch|b1tch|ballbag|balls|ballsack|bastard|beastial|beastiality|bellend|bestial|bestiality|bi\+ch|biatch|bitch|bitcher|bitchers|bitches|bitchin|bitching|bloody|blow job|blowjob|blowjobs|boiolas|bollock|bollok|boner|boob|boobs|booobs|boooobs|booooobs|booooooobs|breasts|buceta|bugger|bum|bunny fucker|butt|butthole|buttmuch|buttplug|c0ck|c0cksucker|carpet muncher|cawk|chink|cipa|cl1t|clit|clitoris|clits|cnut|cock|cock-sucker|cockface|cockhead|cockmunch|cockmuncher|cocks|cocksuck|cocksucked|cocksucker|cocksucking|cocksucks|cocksuka|cocksukka|cok|cokmuncher|coksucka|coon|cox|crap|cum|cummer|cumming|cums|cumshot|cunilingus|cunillingus|cunnilingus|cunt|cuntlick|cuntlicker|cuntlicking|cunts|cyalis|cyberfuc|cyberfuck|cyberfucked|cyberfucker|cyberfuckers|cyberfucking|d1ck|damn|dick|dickhead|dildo|dildos|dink|dinks|dirsa|dlck|dog-fucker|doggin|dogging|donkeyribber|doosh|duche|dyke|ejaculate|ejaculated|ejaculates|ejaculating|ejaculatings|ejaculation|ejakulate|f u c k|f u c k e r|f4nny|fag|fagging|faggitt|faggot|faggs|fagot|fagots|fags|fanny|fannyflaps|fannyfucker|fanyy|fatass|fcuk|fcuker|fcuking|feck|fecker|felching|fellate|fellatio|fingerfuck|fingerfucked|fingerfucker|fingerfuckers|fingerfucking|fingerfucks|fistfuck|fistfucked|fistfucker|fistfuckers|fistfucking|fistfuckings|fistfucks|flange|fook|fooker|fuck|fucka|fucked|fucker|fuckers|fuckhead|fuckheads|fuckin|fucking|fuckings|fuckingshitmotherfucker|fuckme|fucks|fuckwhit|fuckwit|fudge packer|fudgepacker|fuk|fuker|fukker|fukkin|fuks|fukwhit|fukwit|fux|fux0r|f_u_c_k|gangbang|gangbanged|gangbangs|gaylord|gaysex|goatse|God|god-dam|god-damned|goddamn|goddamned|hardcoresex|hell|heshe|hoar|hoare|hoer|homo|hore|horniest|horny|hotsex|jack-off|jackoff|jap|jerk-off|jism|jiz|jizm|jizz|kawk|knob|knobead|knobed|knobend|knobhead|knobjocky|knobjokey|kock|kondum|kondums|kum|kummer|kumming|kums|kunilingus|l3i\+ch|l3itch|labia|lust|lusting|m0f0|m0fo|m45terbate|ma5terb8|ma5terbate|masochist|master-bate|masterb8|masterbat*|masterbat3|masterbate|masterbation|masterbations|masturbate|mo-fo|mof0|mofo|mothafuck|mothafucka|mothafuckas|mothafuckaz|mothafucked|mothafucker|mothafuckers|mothafuckin|mothafucking|mothafuckings|mothafucks|mother fucker|motherfuck|motherfucked|motherfucker|motherfuckers|motherfuckin|motherfucking|motherfuckings|motherfuckka|motherfucks|muff|mutha|muthafecker|muthafuckker|muther|mutherfucker|n1gga|n1gger|nazi|nigg3r|nigg4h|nigga|niggah|niggas|niggaz|nigger|niggers|nob|nob jokey|nobhead|nobjocky|nobjokey|numbnuts|nutsack|orgasim|orgasims|orgasm|orgasms|p0rn|pawn|pecker|penis|penisfucker|phonesex|phuck|phuk|phuked|phuking|phukked|phukking|phuks|phuq|pigfucker|pimpis|piss|pissed|pisser|pissers|pisses|pissflaps|pissin|pissing|pissoff|poop|porn|porno|pornography|pornos|prick|pricks|pron|pube|pusse|pussi|pussies|pussy|pussys|rectum|retard|rimjaw|rimming|s hit|s.o.b.|sadist|schlong|screwing|scroat|scrote|scrotum|semen|sex|sh!\+|sh!t|sh1t|shag|shagger|shaggin|shagging|shemale|shi\+|shit|shitdick|shite|shited|shitey|shitfuck|shitfull|shithead|shiting|shitings|shits|shitted|shitter|shitters|shitting|shittings|shitty|skank|slut|sluts|smegma|smut|snatch|son-of-a-bitch|spac|spunk|s_h_i_t|t1tt1e5|t1tties|teets|teez|testical|testicle|tit|titfuck|tits|titt|tittie5|tittiefucker|titties|tittyfuck|tittywank|titwank|tosser|turd|tw4t|twat|twathead|twatty|twunt|twunter|v14gra|v1gra|vagina|viagra|vulva|w00se|wang|wank|wanker|wanky|whoar|whore|willies|willy|xrated|xxx)''',text,re.IGNORECASE)

      if b!=None:
        offensive_set.append(text)

      a=re.match('''(chul)|(fudi)|(mal)|(bh?a?n?dh?a?v(a|i))|(ha?ra?mi?( ?)(((z|j)h?a?(d|t)(a|i)?)|((k|c)h?or))?)|(jh?a?na?vh?(a|e)?r)|(sh?uvh?(e|a)?r)|(m(e|a)?dh?(e|a)?r(chod)?)|(bh?(a|e|ai)nchod)|(bah(a|e|ai)nchod)|(bh?aichod)|(b(a|u)?kr(i|e)chod)|((bh?osa?d?chod)|((bh?on?s(a|e)?((di|d)?v(a|e)?l(a|e)?))|(bh?on?s(a|e)?(di|d)?(kae|ke|ka|k)?)|(bhon?s)))|(r(a|u|e)?ndi?(chod)?)|(bhad?a?(v|w)a?(a|e|i))|(bh?osdi?k(e|a|e)?)|(ch(o|u)d(ai|u|a))|(ch(o|u)da?(w|v)a(y|i)e?)|(chusa?n(a|e)(wali))|(chut((iy?ah?(pa?)?)|(a?n)|(iy?(e|a)))?(panti)?)|((gh?(a|e)?l)?chod(iy?ah?))|(gh?an?du?)|(gadha)|(((la(v|u)d(a|e))|(lod(a|e))|(l(a|u)?nd)))|(hij((d|r)(a|e)))|(kuth?r?(a|i)(y?a)?)|(kaa?mchor)|(sa?l(a|i))|(tat(i|e))|(kamin(e|a|i))|(b(o|u)bl(a|e)y)|(jhan?t)|(ba?kchod(iyeh?|i|a|e))|(\b.*chod\b)
      ''',text, re.IGNORECASE)

      if a!=None:
        offensive_set.append(text)


      listOffensive=set(['bhadhvi', 'bol teri gand kaise maru', 'aand', 'chuta', 'harmzadi', 'buddha khoosat', 'hugnaa', 'bhadhave', 'randi chod', 'banchod', 'motherfucker', 'fuck', 'bhos', 'chutiya', 'jaan var', 'bhadavi', 'apni lund choos', 'lundoos', 'janver', 'gadha', 'bhdva', 'bhosd', 'lawda', 'janvar', 'bhenketakke', 'amaa fue', 'hrmi', 'haram jhada', 'chull', 'hrmzada', 'chut mari ke', 'kaa?mchor', 'sali kuta', 'ho', 'bhadvi', 'bhadkhau', 'hrmjadi', 'badir', 'chut marike', 'butt fucker', 'dumbass', 'haraam zaada', 'fag', 'piss', 'ghalchodiya', 'chusnawala', 'aandupana', 'skank', 'mutthal', 'hug', 'haramjad', 'bhosdk', 'lavda', 'kuti', 'jhanvher', 'badava', 'hijde', 'suvr', 'bh?aichod', 'chootiya', 'bdva', 'sonofabitch', 'chut ke pasine mein talay huye bhajiye', 'sali kutti', 'tatte', 'kamina', 'bhosadchod', 'kutte ki jat', 'buhtah-nee ka', 'chut ka pujari', 'mutth marna', 'kuthi', 'najayaz', 'mutar', 'bakland', 'haram jadi', 'ghassad', 'harami', 'lulla', 'bainchod apne baap ka chus', 'chodia', 'choos', 'bosachod', 'netra chanchal', 'slut', 'najayaz paidaish', 'jhanvar', 'chup ke', 'gaand marao', 'chul', 'ghelchodiya', 'gelchodia', 'muth marna', 'bhosad', 'harmjadi', 'mal', 'maderchod', 'jhan?t', 'chootad', 'chodela', 'chootmadan', 'choot ka baal', 'badavi', 'chut ke dhakkan', 'chutan', 'shuvhar', 'moot', 'chodra', 'fck', 'hrmjdi', 'cocksucker', 'bhadhava', 'chodai', 'saali', 'tere maa ki chute mein lauda ghoosa', 'bhosad chod', 'teri chut ki ma chod dunga', 'badirchand', 'bhosdika', 'bhenchod', 'shuvar', 'jhanver', 'jhat', 'hrmzd', 'mader', 'chut karo', 'bumchod', 'haram zadi', 'pucchi', 'mumm-aye', 'bhen chod', 'hrami', 'chut ke gulam', 'mooth marna', 'bublay', 'tatti', 'saala', 'chunni', 'bhonsri-waalaa', 'backarchodu', 'ass', 'chodu', 'bhadavai', 'baap chood', 'lauda', 'mutth marwana', 'bhadhavi', 'bhosdike', 'bitch', 'hrmchor', 'dhaka', 'paad', 'bakrichod', 'hrmzadi', 'chup karo', 'apni ma ko ja choos', 'rundi', 'harmjada', 'chusanewali', 'stupidity', 'chodiya', 'haramkor', 'ghondoo', 'bhadava', 'kutha', 'lund', 'boschod', 'shit', 'kat', 'saala kutta', 'loda', 'chudai', 'muth', 'testes', 'gaand', 'janaver', 'chusnawali', 'suver', 'beti chod', 'ghelchodia', 'chutia', 'bandaa', 'tits', 'madharchod', 'chusana', 'saali kutti', 'bhoschod', 'chodu bhagat', 'janvr', 'bhaichod', 'gaandu', 'cock', 'bhai chod', 'betichod', 'chut ka bhoot', 'gasti', 'fuckass', 'toto', 'khotey ki aulad', 'chup kar', 'choochii', 'kuta', 'madarchood', 'chudai khana', 'darn', 'apni gaand mein muthi daal', 'janavar', 'bhanchod', 'hugna', 'hrmjda', 'bhosadike', 'ghasti', 'dick', 'mooth marwana', 'gur', 'kaamchor', 'bakri chod', 'chinaal', 'lavde', 'char so bis', 'gand maru', 'tera dimag kharab ho gaya', 'bhadwe ka awlat', 'big testes', 'chodva', 'choot ke bhoot vaginal ghost', 'fuc', 'buttocks', 'sala maderchot', 'chusna', 'hijre', 'douche', 'abla naari tera buble bhaari', 'benchod', 'bobley', 'choo-tia', 'cutlu', 'fuk', 'bobla', 'hrmcor', 'kutriya', 'suvhar', 'chutiya ka bheja ghas khane gaya hai', 'hrmzda', 'suvar', 'chutiyah', 'maal', 'hrmjada', 'bhenkelaude', 'asshole', 'fk', 'hijda', 'bhandavi', 'soover', 'chootiyapanti', 'chut', 'fuddi', 'aandu', 'muth marwana', 'mammey', 'gandu', 'chikni mari kancha', 'chuci', 'buble', 'jhanvhar', 'twat', 'haraami', 'rand chod', 'kuttiya', 'randhwa', 'gashti', 'jnvr', 'kamine', 'harmzada', 'chudan chudai', 'kutia', 'chodiyah', 'haramzada', 'randwa', 'kutiya', 'haram zada', 'chusanwali', 'aandal', 'chup ke chut hai', 'stupid', 'bosdk', 'carrom board', 'shut up', 'haramzad', 'madarchot', 'khota', 'bhadva', 'douchebag', 'chudwavi', 'baichod', 'hrmjd', 'haramjat', 'chusanawala', 'chhola phudakna', 'gili land', 'katla', 'bandhar', 'do the cunt', 'namaste', 'choot', 'bhen ke takke', 'haramkhor', 'bhen ke laude', 'chodna', 'jhant', 'madarchod', 'choot marani ka', 'klpd', 'bhenchot', 'hrmzdi', 'bhosachod', 'booblay', 'bhains ki aulad', 'bhoot-nee ka', 'kutta', 'cunt', 'bastard', 'bhandava', 'bur ki chatani', 'netra choudan', 'pussy', 'mader chod', 'assfuck', 'hijra', 'khatmal', 'chootadchod','spank'])
      

      if text in listOffensive:
        offensive_set.append(text)


    offensive_set=list(set(offensive_set))
    #print("Offensive words: ",offensive_set)
    return offensive_set
