# fuglevinduet

Made for 1 specific person, not intended as a general tool (but feel free to check it out if you like birds)

A companion for someone who feeds garden birds and watches them from a
window. The interface is in Norwegian throughout.

## What it does

- **The garden is drawn as it is right now.** The sky follows the real
  solar elevation for the location, computed locally from the date, the
  time and the coordinates. The birch comes into leaf and drops it with
  the season. Weather is fetched once an hour and settles over the scene
  as cloud, rain, falling snow and snow that lies.
- **Birds you log appear in the scene**, each at its own perch. Species
  you have not seen yet stand as faint outlines where they would sit.
  Clicking a bird logs it.
- **An identification key**, folded away until you open it. It starts
  with colour — which colours you saw at all, anywhere on the bird, as
  many as you like — and then asks about whatever best separates the
  remaining candidates. It never asserts which bird you saw. It shows
  which ones it could have been and what tells them apart. "Vet ikke" is
  always a valid answer.
- **Stamgjester**, the three species you have seen most often, with one
  button each for another visit. The common case — the same bird as
  yesterday — does not send you back through the key.
- **A window for each species**, reached from the candidate list, from
  the regulars and from any row in the log. It holds the field marks and
  every time you have seen that species, in the same place.
- **Juvenile plumage.** In late summer a large share of the birds at a
  feeder are juveniles that match nothing in any book. Switching on "Det
  var en ungfugl" stops head and breast colour from excluding species.
- **Activity at the feeder** as four words, never a number or a
  percentage: Rolig, Vanlig, Livlig, Svært livlig. Derived from cold,
  snow cover, wind, precipitation, barometric trend, and how long it has
  been since sunrise.
- **Care prompts** that follow the weather, one at a time.
- **Daily rhythm.** Every sighting stores its timestamp. After a few
  weeks the distribution across the day is drawn for this garden alone.

## Data and privacy

Everything you log stays in your browser, on your own machine
(`localStorage`). There is no account, no server, no cookies and no
tracking. Nothing you log is sent anywhere.

The one network request the app makes is the weather forecast, to
Open-Meteo. It sends only the coordinates of the location, rounded to
four decimals. If it fails, everything else in the app works as before.

Data held in a browser can be read by other software on the machine, and
the browser may evict it on its own. Use **Eksporter** now and then. The
export file is the real copy of your log, and **Importer** reads it back.

## Files

    index.html    the whole app: markup, styles and code in one file
    arter.json    the species data, 30 species
    birds/        30 illustrations with transparent backgrounds
    icon.png      the app icon
    tools/        an editing helper, not needed to run the app

No frameworks, no packages, no build step. `index.html` opens straight
from disk.

### If you edit arter.json

The app is a single HTML file, so the species data also lives inside
`index.html`. `arter.json` is the source. After changing it:

    python3 tools/embed-arter.py

That writes the data back into `index.html`. It only rewrites the JSON
block, so the tables that live in the code — image measurements, scene
placement and the colour lists behind the first question — are left
alone. Those are keyed by species id in `index.html`; a new species needs
an entry in each.

## Credit

Weather data by [Open-Meteo](https://open-meteo.com/) (CC BY 4.0), based
on national weather services such as MET Norway.
