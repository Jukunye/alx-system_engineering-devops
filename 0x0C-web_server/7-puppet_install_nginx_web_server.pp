# Install Nginx web server

package { 'nginx':
  ensure => 'installed',
}

file { '/var/www/html/index.html':
  content => 'Hello World!',
}


service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => Package['nginx'],
}
