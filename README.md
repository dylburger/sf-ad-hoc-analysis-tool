# Aha!, the Ad Hoc Analysis Tool for San Francisco Public Data

This repo contains code related to the [Aha!](https://docs.google.com/document/d/1qmJKof-BGCCOBcnxiXiC_MyTdeFm8By8sYpwuVWjx4s/edit#), the Ad Hoc Analysis Tool for San Francisco Public Data.

Aha! reflects the feelings of discovery users achieve when making new insights, and also happens to be an acronym for "**A**d **H**oc **A**nalysis".

Our goal is to facilitate exploratory analysis of San Francisco city data for technical and non-technical citizens alike.

## Installation and Configuration

You need a working Python 3 installation. If you're on a Mac, you can install Python 3 through [Homebrew](http://brew.sh/):

    brew install python3

It's also recommended you create a Python virtual environment ("virtualenv") to work
with the code and install the necessary modules. The [virtualenvwrapper tool](http://virtualenvwrapper.readthedocs.io/en/latest/) 
simplifies the management of virtual environments.

If you're using virtualenvwrapper to manage virtual environments, you can create and 
begin work on a new Python 3 virtual environment with ease:

    mkvirtualenv -p /usr/local/bin/python3 sf-ad-hoc
    workon sf-ad-hoc

If the above command fails to work, returning an error like _The executable /usr/bin/python3 (from --python=/usr/local/bin/python3) does not exist_,
two things might be wrong:

* Python 3 failed to install through Homebrew, and you should try installing again, or
* Your Python 3 installation isn't in _/usr/local/bin/python3_. You can find the location of the Python 3 binary by running _which python3_

If everything worked as expected after running the _workon_ command, you should see the name of your virtual environment
in parentheses above your shell prompt:

    (sf-ad-hoc)
    # dylan @ DYLANs-MacBook-Pro in ~/projects/sf-ad-hoc on git:master x [9:36:43]
    $

After instantiating a new virtual environment, install the packages required to work with
the code. From the root of the repo, run:

    pip install -r requirements.txt

As changes to this library are made, it's possible you'll need more modules than the ones you
originally installed. If you receive any "No module named _foo_" found errors, it's likely
your local virtual environment doesn't have the required modules, and you should run the
above command again.

At this point, you should have all the code necessary to work with the ad hoc analysis tool.
Next, you'll need to create a Socrata API token that will authenticate you against the API.

## Creating a Socrata API token

The Socrata API doesn't _require_ credentials, but without an [App Token](https://dev.socrata.com/docs/app-tokens.html),
you'll quickly be rate limited. As the page notes, please do not make an unlimited number of requests to the API. 
Rate limit yourself to a reasonable degree, or reach out to their team to discuss your use case.

Once you've [registered your application](https://dev.socrata.com/register) and received an App Token, store the token
in a file in this repository named _.socrata\_app\_token_ in the following format:

    token: <token>

The _.gitignore_ file in this repo already contains the name of this file, removing it from tracking in git.
**Please never commit your App Token to git. There are automated agents scraping Github and related git hosting 
services for API tokens of many varieties. They can and will steal your credentials.**

## Working with the code

To confirm the code is working correctly on your local machine, run the following commands in your new virtual environment:

    In [1]: from SocrataClient import SocrataClient

    In [2]: client = SocrataClient()

    In [3]: fire_incidents_json = client.fetch_socrata_json('wbb6-uh78')

    In [4]: fire_incidents_json[0]
    Out[4]:
    {'action_taken_other': '-',
     'action_taken_primary': '52 - forcible entry',
     'action_taken_secondary': '-',
     ...
     'station_area': '15',
     'suppression_personnel': '5',
     'suppression_units': '1'}
