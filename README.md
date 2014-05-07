GTALUG Board Meetings
=====================

Notes from **GTALUG**'s board meetings.

## Run Locally

First you will have to install the requirments:

  $ [sudo] gem install jekyll org-ruby

### Build

  $ jekyll build

### Run

  $ jekyll serve --watch

## Directory Structure

- `_data`
  - `members.yml`: Current GTALUG Board Members.
- `_etc`
  - `nginx.conf`: The web server configuration file.
- `_layouts`
  - `default.html`: The main layout.
  - `post.html`: The layout for the board meeting notes.
- `_plugins`
  - `org_converter.rb`: The plugin for that takes org and converts it to HTML.
- `_posts`: Board Meeting Notes
  - `YYYY-MM-DD-notes.org`
- `_config.yml`: Jekyll configuration file.
- `fabfile.py`: The script to deploy the web site.
- `Gemfile`: The Ruby requirements.
- `index.html`: Template for the homepage.
- `README.md`: This file.
