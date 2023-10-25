Quick script and Github action to generate a iCalendar (RFC 5545) file to warn when DST is causing a mess in your calendar.

The script use the Olson timezones database and generate a iCalendar file to warn when meetings are going to cause conflicts because
two timezones are not applying DST at the same time (like part of Europe and part of US). It can cause some troubles on international
teams, so it is wise to anticipate, hence the script.

# FAQ

## Where is the calendar file published ?

The canonical one is on [this github pages](https://mscherer.github.io/dst_calendar/).

## Why did you choose using the 2 timezones you are using ?

One is my timezone, the other one is the company one. Feel free to fork and change them in the workflow file. I can also give you the email of various consultants if you wish to deploy a enterprise version of the application.

## Why are you using non-free infrastructure for that ?

Github actions is free of charge, and the CI I use ([Woodpecker](https://woodpecker-ci.org/)) did not support [scheduled jobs](https://github.com/woodpecker-ci/woodpecker/issues/8) in a stable version when I wrote the automation.
Github also provides Github Pages, and while I can self host the ics, it is also simpler to delegate to the platform.

## Why did you decide to write that on a Monday morning ?

Writing a python script dealing with timezone seemed to be the easiest way to brag about "I can manipulate spaces and time".

## Is there a way to have the ics file on demand ?

Yes, a container with a small hackish web application is available on the Github Container Registry. Just run it and go to port 5000.
