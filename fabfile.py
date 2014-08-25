#!/usr/bin/env python

import os

from fabric.contrib.project import rsync_project
from fabric.api import env, put, local, task, hosts, sudo

import yaml

env.hosts = ['penguin.gtalug.org']
env.remote_dir = '/srv/www/org_gtalug_board/html/'
env.use_ssh_config = True

with open('_config.yml') as f:
  env.config = yaml.load(f)

@task
@hosts('localhost')
def run():
  """
  Run the development web server so you could view your changes.
  """
  jekyll('serve --watch')

@task
@hosts('localhost')
def build():
  """
  This will build the website.
  """
  clean()
  jekyll('build')

@task
@hosts('penguin.gtalug.org')
def deploy():
  """
  This will deploy the web site to the GTALUG web space.
  """
  build()
  rsync_project(
    local_dir = os.path.abspath(env.config['destination']) + "/",
    remote_dir = env.remote_dir,
    delete = True,
    extra_opts = '--exclude=".DS_Store"',
  )

@task
@hosts('penguin.gtalug.org')
def update_nginx_config():
  """
  This will update the Nginx configuration file on the remote host.
  """
  put(
    local_path = os.path.join(os.path.abspath('./_etc'), 'nginx.conf'),
    remote_path = '/etc/nginx/sites-available/org_gtalug_board',
    use_sudo = True
  )
  sudo('/etc/init.d/nginx restart')

def jekyll(directives=''):
  """
  A simple wrapper around the jekyll command.
  """
  local('jekyll %s' % directives)

def clean():
  """
  This will clean the site directory.
  """
  local('rm -fr %s' % os.path.abspath(env.config['destination']))
