# Playbook — Trademark Stoplist

**Purpose:** automated scan of every generated title, tag, description, and attribute against a known-bad word list before output. The single most common cause of listing removal is using a trademarked term unknowingly. This playbook prevents that.

**Where it runs:** as a final pass on every MODE 1 / MODE 2 / MODE 7 output before the listing is finalized. If any stoplist match is detected, output is BLOCKED and the user is asked to rephrase.

---

## Stoplist (May 2026) — non-exhaustive but covers the most common traps

### Entertainment / media franchises
disney, mickey, minnie, donald duck, goofy, pluto (character),
marvel, avenger, avengers, spider-man, spiderman, iron man, captain america, hulk,
thor, black widow, hawkeye, black panther, doctor strange, deadpool, wolverine,
xmen, x-men, fantastic four,
pixar, woody, buzz lightyear, frozen (the movie), elsa, anna (frozen),
moana, encanto, mirabel,
star wars, jedi, sith, yoda, darth vader, baby yoda, grogu, mandalorian, boba fett,
harry potter, hogwarts, hufflepuff, gryffindor, slytherin, ravenclaw, dumbledore, hermione,
lord of the rings, hobbit, frodo, gandalf, sauron, mordor, middle earth,
game of thrones, daenerys, jon snow, stark,
disney princess, ariel (little mermaid), belle (beauty and the beast), jasmine (aladdin),
cinderella, rapunzel, mulan, snow white, sleeping beauty,
toy story, finding nemo, dory, inside out, coco, ratatouille, monsters inc,
nemo, simba, mufasa, scar, timon, pumbaa, hakuna matata, lion king,
shrek, donkey (shrek), fiona, puss in boots,
minions, despicable me, gru,
sesame street, big bird, elmo, cookie monster, oscar the grouch, bert, ernie, kermit, miss piggy,
muppets, fraggle rock,
peppa pig, paw patrol, ryder, chase (paw patrol), marshall (paw patrol), skye, rubble, rocky (paw patrol), zuma, everest,
bluey, bingo (bluey), bandit (bluey),
cocomelon, hot wheels,
my little pony, mlp, rainbow dash, twilight sparkle, pinkie pie,
strawberry shortcake, care bears,
power rangers, transformers, optimus prime, bumblebee (transformers),
gundam, dragon ball, goku, naruto, sasuke, sakura,
pokemon, pikachu, charizard, eevee, pokeball, ash ketchum, team rocket,
sailor moon, sailor venus, sailor mars, sailor jupiter,
hello kitty, sanrio, my melody, kuromi, cinnamoroll, pompompurin, gudetama,
totoro, ghibli, studio ghibli, spirited away, chihiro, kiki delivery,
miraculous ladybug, cat noir,
adventure time, finn, jake, princess bubblegum,
gravity falls, dipper, mabel,
rick and morty,
the office (show), michael scott, jim halpert, pam beesly, dwight schrute,
friends (show), central perk,
seinfeld, kramer, george costanza,
breaking bad, walter white, heisenberg, los pollos hermanos,
stranger things, eleven, hawkins, demogorgon,
squid game,
ted lasso,
bridgerton,
wednesday addams, the addams family

### Sports leagues + major college / national teams
nfl, nba, mlb, nhl, mls, fifa, uefa, premier league, la liga, serie a,
super bowl, world series, stanley cup, world cup, march madness, ncaa,
yankees, red sox, dodgers, cubs, mets, giants (sports), patriots (sports),
cowboys (sports), packers, eagles (sports), 49ers, chiefs, lakers, celtics, warriors,
heat (sports), bulls (sports), spurs, raptors,
manchester united, manchester city, real madrid, barcelona (soccer), liverpool (soccer),
juventus, bayern munich, psg,
nascar, indycar, formula 1, f1

### Music — artists and labels
taylor swift, swiftie, eras tour,
beyonce, beyoncé, jay-z, jayz,
drake (artist), rihanna, kanye, yeezy, ye (artist),
adele, ed sheeran, justin bieber, ariana grande, billie eilish, dua lipa, harry styles,
bad bunny, sza, the weeknd, post malone, lana del rey, lorde, doja cat,
bts, blackpink, twice (kpop), stray kids,
beatles, rolling stones, queen (band), led zeppelin, pink floyd, ac/dc, metallica,
grateful dead, dead head,
nirvana, kurt cobain,
elvis, michael jackson, prince (musician), madonna,
johnny cash, dolly parton, willie nelson

### Tech / lifestyle brands
apple (computer/iphone context), iphone, ipad, macbook, airpods, mac, ios, android (when targeting Google as brand),
google, gmail, youtube, chrome, android (logo),
microsoft, windows (OS), xbox, surface,
amazon (when not generic), aws, alexa, kindle, prime day,
meta, facebook, instagram, whatsapp, threads,
twitter, x (the platform), tiktok, snapchat, youtube,
spotify, netflix, hulu, disney+, hbo, max, paramount+, peacock,
nike, adidas, puma, under armour, lululemon, athleta,
starbucks, mcdonald's, mcdonalds, big mac, coca cola, coke, pepsi, sprite, mountain dew,
target (the store), walmart, costco, sam's club,
chick-fil-a, in-n-out, taco bell, kfc, burger king,
gucci, louis vuitton, lv (luxury context), chanel, dior, prada, hermes, hermès, balenciaga, ysl, saint laurent,
rolex, omega (watch), patek,
ferrari, lamborghini, porsche, tesla, bmw, audi, mercedes

### Holidays and events with TM components (use generically OK; use specific TM term not OK)
"super bowl" (use "big game" or "football sunday" instead),
"olympics" (use "games" or "athletic competition"),
"valentine's day" (use is fine; "be my valentine ®" — a TM phrase — is not)

### Common catchphrase TM traps
"just do it" (Nike), "i'm lovin' it" (McDonald's), "have it your way" (Burger King),
"finger lickin' good" (KFC), "the happiest place on earth" (Disney),
"may the force be with you" (Disney/Star Wars),
"hakuna matata" (Disney TM),
"that's hot" (Paris Hilton),
"let's get ready to rumble" (Buffer),
"i'm with stupid" (numerous TMs),
"i woke up like this" (Beyoncé),
"yas queen", "yaaas queen" (registered),
"netflix and chill" (Netflix-adjacent — risky)

### Celebrities and public figures (illustrative, not exhaustive)
Any specific living celebrity name. Any deceased celebrity name whose estate enforces right-of-publicity (Elvis, Marilyn Monroe, Prince, Michael Jackson, Audrey Hepburn, Steve McQueen, Bruce Lee, etc.).

---

## Scan algorithm

For every text field in the output (title, each of 13 tags, every attribute value, description, Pinterest pin title/description, board name, hero alt text):

1. Lowercase the field
2. Split into word tokens AND multi-word phrase tokens (2-grams, 3-grams)
3. For each token, exact-match against the stoplist (case-insensitive)
4. If ANY match: BLOCK the output

Match severity:
- **Hard match (one word)** — e.g., field contains "disney" → BLOCK
- **Phrase match (multi-word)** — e.g., field contains "may the force" → BLOCK
- **Partial match** — be careful with substrings (e.g., "match" contains "ma" but that's not a TM match — only match on full word boundaries)

---

## Display when a TM match is detected

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
⛔ TRADEMARK CHECK FAILED — OUTPUT BLOCKED
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Match found:        "<matched term>"
Match category:     <Franchise / Brand / Catchphrase / Celebrity>
Field where found:  [Title / Tag #X / Description / Attribute / Pinterest title / etc.]

WHY THIS BLOCKS YOUR LISTING:
  Etsy will remove this listing on first IP complaint (no warning).
  "Inspired by" framing does NOT protect against IP claims.
  Repeat strikes lead to permanent shop closure.

REQUIRED ACTION:
  Remove or rephrase the offending term. Suggested alternatives:
  - <generic alternative 1>
  - <generic alternative 2>
  
RE-RUN AFTER USER CONFIRMS REPHRASING.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Limitations

1. **The stoplist is not exhaustive.** New TMs register constantly. Output should always remind the user to check USPTO.gov / cocatalog.loc.gov for any term that *resembles* a brand or character.
2. **Generic words also have TMs sometimes.** "Apple" (the fruit) is fine; "Apple" (in a tech context next to "phone" or "watch") triggers Apple Inc. The scanner can flag but the user has final judgment.
3. **Visual TMs aren't scanned.** Logos, character silhouettes, and design styles can violate even without using the word. This playbook only catches text. Visual TM checking is a separate manual step.
4. **Internationally TMs differ.** A name not TM'd in the US may be TM'd in the EU/UK. If the shop targets multi-region, search WIPO + EUIPO + UKIPO for any flagged term.

---

## Update protocol

Add new entries to this stoplist when:
- A user's listing is removed for IP and the term wasn't on the list
- A new viral franchise emerges (e.g., a new Disney movie release)
- A new musician/celebrity dominates pop culture
- Annual review in January each year — scan the previous year's IP-takedown news

This file should be considered living; treat updates as routine maintenance, not a sign of failure.
