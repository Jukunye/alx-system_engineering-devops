# Puppet script that replace a line from server files

$file_check = '/var/www/html/wp-settings.php'

exec { 'replace_line':
  command => "sed -i 's/phpp/php/g' ${file_check}",
  path    => ['/bin','/usr/bin']
}
