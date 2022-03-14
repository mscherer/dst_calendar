Quick script and Github action to generate a ics file to warn when DST is causing a mess in your calendar.

The script use the Olson timezones database and generate a ICS to warn when meetings are going to cause conflicts because
two timezone do not change at the same time.

# FAQ

## Where is the ics file published ?

The canonical one is on [this github pages](https://mscherer.github.io/dst_calendar/).

## Why are you using the 2 timezones you choose ?

One is my timezone, the other one is the company one. Feel free to fork and change them in the workflow file.

## Why are you using non-free infrastructure for that ?

Github actions is free of charge, and the CI I use ([Woodpecker](https://woodpecker-ci.org/)) do not support [scheduled jobs](https://github.com/woodpecker-ci/woodpecker/issues/8) for the moment.
Github also provides Github Pages, and while I can self host the ics, it is also simpler to delegate to the platform.

## Why did you decide to write that on a Monday morning ?

Writing a python script dealing with timezone seemed to be the easiest way to brag about "I can manipulate spaces and time".
