task :default => :serve

require 'yaml'

config = YAML::load_file(File.join(__dir__, '_config.yml'))
deploy_config = YAML::load_file(File.join(__dir__, '_deploy.yml'))

desc 'Clean up the generated site'
task :clean do
  cleanup
end

desc 'Serve the web site on the local machine (server with --auto)'
task :serve => :clean do
  jekyll('serve --watch')
end

desc 'Build the website'
task :build => :clean do
  if rake_running then
    puts "\n\nWarning! An instance of rake seems to be running (it might not be *this* Rakefile, however).\n"
    puts "Building while running other tasks (e.g., preview), might create a website with broken links.\n\n"
    puts "Are you sure you want to continue? [Y|n]"

    ans = STDIN.get.chomp
    break if ans != 'Y'
  end

  jekyll('build')
end

desc 'Build and deploy to the remote server'
task :deploy => :build do
  sh "rsync -anz --delete _site/ #{deploy_config['deploy_dir']}"
  File.open('_last_deploy.txt', 'w') { |f| f.write(Time.new) }
end

def cleanup
  sh 'rm -fr _site'
end

def jekyll(directives = '')
  sh 'jekyll ' + directives
end

# check if there is another rake task running
# (in addition to this one!)
def rake_running
  `ps | grep 'rake' | grep -v 'grep' | wc -l`.to_i > 1
end
