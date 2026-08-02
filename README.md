# Fuglevinduet

A tool for someone who feeds garden birds. Made for one specific person and not intended as a general tool, though you are
welcome to look around if you like birds. The interface is in Norwegian
throughout. The idea is that the app shows your garden roughly as it is right now, and the
birds you log turn up in it. Over a season it becomes a picture of this one
window rather than a generic bird list.

**[Open it here](https://evelinehansen.github.io/fuglevinduet/)**

## What it does

- **The garden is drawn as it is right now.** The sky follows the real solar
  elevation for the location, worked out on your device from the date, the time
  and the coordinates. The birch comes into leaf and drops it with the season.
  Weather settles over the scene as cloud, rain, falling snow, and snow that
  lies.
- **Birds you log appear in the scene**, each at its own perch. Species you have
  not seen yet stand as faint outlines where they would sit. Clicking a bird
  logs it.
- **An identification key**, folded away until you open it. Every question is on
  screen at once, colour as a row of swatches and the rest as dropdowns with the
  question itself as the hint line, so the whole filter is visible in one glance
  and can be answered in any order. A field you leave alone means "don't know".
  While the list is still long, the key says which unanswered question would
  divide it most, which is the one worth answering next. It never asserts which
  bird you saw. It shows which ones it could have been and what tells them
  apart.
- **Stamgjester**, the three species you have seen most often, with one button
  each for another visit. The common case, the same bird as yesterday, does not
  send you back through the key.
- **A window for each species**, reached from the candidate list, from the
  regulars, and from any row in the log. It holds the field marks and every time
  you have seen that species, in the same place.
- **Juvenile plumage.** In late summer a large share of the birds at a feeder are
  juveniles that match nothing in any book. Switching on "Det var en ungfugl"
  stops colour, head and breast from excluding species: those three inputs grey
  out rather than pretend to filter.
- **Activity at the feeder** as four words, never a number or a percentage:
  Rolig, Vanlig, Livlig, Svært livlig. Worked out from cold, snow cover, wind,
  precipitation, barometric trend, and how long it has been since sunrise.
- **Care prompts** that follow the weather, one at a time, rotating daily when
  the weather has nothing to say. Advice tied to a particular food only appears
  when that food is out.
- **Daily rhythm.** Every sighting stores its timestamp. After a few weeks the
  distribution across the day is drawn for this garden alone.

## Running it

Open it at [the link above](https://evelinehansen.github.io/fuglevinduet/).
There is nothing to install, no build step, and no account. The whole app is a
single `index.html` file, so that file also opens straight from disk if you have
cloned the repo.

On an iPhone, open it in Safari and use Share, then Add to Home Screen. That
gives it its own icon and, importantly, stops Safari clearing your log after a
week of not opening it.

## Where your data lives

Everything you log stays in your browser, on your own machine. There is no
account, no server, no cookies, and no tracking. Nothing you log is sent
anywhere.

The app makes **one** outbound request: the weather forecast, from Open-Meteo,
fetched about once an hour. It sends only the coordinates of one specific location in Norway (Vestfold),
rounded to four decimals, and nothing about you or your log. If it fails,
everything else in the app carries on as before, with the scene simply not
reflecting the current weather.

Your log is otherwise yours alone to look after:

- **Browsers clear their own storage.** Safari in particular clears data for
  sites you have not opened in about a week. Adding it to your home screen
  prevents this; using it as an ordinary bookmarked page does not.
- **Eksport is the real backup.** The export file is the real copy of your
  log, and **Import** reads it back.
- **Browser storage is not private.** Anything stored this way can be read by
  other software running on your machine and is not encrypted. Do not keep
  passwords or anything sensitive in here.

## How it's built

Plain HTML, CSS, and JavaScript in a single file, plus the species data and
illustrations. No frameworks, no packages, and no build step, so the files in
this repo are the whole app: what you can read here is what runs in your
browser. There is nothing to sign in to and no API keys, including for the
weather, which needs none.

- `index.html` is the whole app: markup, styles, and code.
- `arter.json` is the species data, 30 species.
- `birds/` holds the 30 illustrations.
- `tools/` holds an editing helper, not needed to run the app.

### If you edit arter.json

Because the app is a single file, the species data also lives inside
`index.html`, and `arter.json` is the source it is generated from. After
changing it, run:

```
python3 tools/embed-arter.py
```

That writes the data back into `index.html`. It only rewrites the JSON block, so
the tables that live in the code (image measurements, scene placement, and the
colour lists behind the first question) are left alone. Those are keyed by
species id in `index.html`, so a new species needs an entry in each.

## Credits

Idea and direction by Eveline, coding by Claude. Built for my own practice,
learning and use.

Weather data by [Open-Meteo](https://open-meteo.com/) (CC BY 4.0), based on
national weather services such as MET Norway.

Personal project, shared as is.
