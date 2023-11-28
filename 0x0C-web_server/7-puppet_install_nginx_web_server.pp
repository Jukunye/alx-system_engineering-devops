# Install Nginx web server

package { 'nginx':
  ensure => 'installed',
}

file_line { 'redirect_me':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'server_name _;',
  line   => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
}

file { '/var/www/html/index.html':
  content => 'Hello World!',
}


service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => Package['nginx'],
}
