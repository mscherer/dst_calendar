iQuick script and github action to generate a ics file to warn when timezone is a mess.

The script use the Olson timezone database and generate a ICS with the period on when timezone is a mess, and meetings are going to conflict.

# FAQ

## Why are you using the 2 timezone you choose ?

One is for me, the rest is the company. Feel free to fork and change them in the workflow

## Why are you using non free infrastructure for that ?

Github actions is free, and the CI I use ([Woodpecker](https://woodpecker-ci.org/) do not support [scheduled jobs](https://github.com/woodpecker-ci/woodpecker/issues/8) for the moment).
Github also provides Github Pages, and while I can self host the ICS, it is also simpler to delegate to the platform.
