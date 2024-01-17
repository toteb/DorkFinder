#!/usr/bin/python3
import argparse

RED = "\33[91m"
BLUE = "\33[94m"
PURPLE = "\033[32m"
YELLOW = "\033[93m"
PURPLE = '\033[0;35m' 
CYAN = "\033[36m"
END = "\033[0m"

parser = argparse.ArgumentParser(description='Google DorkFinder')
parser.add_argument('-t', '--target', metavar='example.com', help='enter the target domain', dest='target', type=str, required=True)
parser.add_argument('-o', '--output', metavar='example.txt', help='print to output file', dest='output')
parser.add_argument('-p', '--proxy', help='use proxy', dest='proxy')
args = parser.parse_args()
cli = args.target
urls = [
        f'https://www.google.com/search?q=site:{cli}%20-www%20-shop%20-share%20-ir%20-mfa',
        f'https://www.google.com/search?q=site:{cli}%20intext:"sql%20syntax%20near"%20|%20intext:"syntax%20error%20has%20occurred"%20|%20intext:"incorrect%20syntax%20near"%20|%20intext:"unexpected%20end%20of%20SQL%20command"%20|%20intext:"Warning:%20mysql%20connect()"%20|%20intext:"Warning:%20mysql%20query()"%20|%20intext:"Warning:%20pg%20connect()"',
        f'https://www.google.com/search?q=site:{cli}%20ext:php%20inurl:?',
        f'https://www.google.com/search?q=site:{cli}%20ext:jsp%20OR%20ext:do%20OR%20ext:action%20inurl:?',
        f'https://www.google.com/search?q=site:{cli}%20ext:aspx%20OR%20ext:asa%20OR%20ext:asp%20OR%20ext:asax%20inurl:?',
        f'https://www.google.com/search?q=site:openbugbounty.org%20inurl:reports%20intext:"{cli}"',
        f'https://www.google.com/search?q=site:"{cli}"%20ext:log%20|%20ext:txt%20|%20ext:conf%20|%20ext:cnf%20|%20ext:ini%20|%20ext:env%20|%20ext:sh%20|%20ext:bak%20|%20ext:backup%20|%20ext:swp%20|%20ext:old%20|%20ext:~%20|%20ext:git%20|%20ext:svn%20|%20ext:htpasswd%20|%20ext:htaccess%20|%20ext:sql%20|%20ext:csv%20|%20ext:.git-credentials%20|%20ext:yaml%20|%20ext:yml%20|%20ext:ppk%20|%20ext:pem%20|%20ext:json%20|%20ext:cfg%20|%20ext:xml%20|%20ext:ps1',
        f'https://www.google.com/search?q=site:"{cli}"%20filename:connections.xml%20|%20filename:config.php%20|%20filename:config.json',
        f'https://www.google.com/search?q=site:"{cli}"%20ext:jsp%20|%20ext:asp%20|%20ext:php%20|%20ext:aspx%20|%20ext:pl%20|%20ext:cfm%20|%20ext:py%20|%20ext:rb',
        f'https://www.google.com/search?q=site:"{cli}"%20ext:pdf%20"username|user|pass|password|email|id|sensetive|internal"',
        f'https://www.google.com/search?q=site:{cli}%20ext:pdf%20"confidential"',
        f'https://www.google.com/search?q=site:{cli}%20ext:pdf%20"for%20internal%20use%20only"',
        f'https://www.google.com/search?q=site:{cli}%20ext:pdf%20"private"',
        f'https://www.google.com/search?q=site:{cli}%20ext:pdf%20"sensetive"',
        f'https://www.google.com/search?q=site:{cli}%20filename:.env',
        f'https://www.google.com/search?q=site:{cli}%20extension:csv%20admin',
        f'https://www.google.com/search?q=site:{cli}%20jdbc',
        f'https://www.google.com/search?q=site:{cli}%20Index%20of%20/.svn',
        f'https://www.google.com/search?q=site:{cli}%20intitle:"index%20of"%20"users.yml"%20|%20"admin.yml"%20|%20"config.yml"',
        f'https://www.google.com/search?q=site:{cli}%20intext:"Index%20of"%20intext:"backup.tar"',
        f'https://www.google.com/search?q=site:{cli}%20inurl:"wp-content"%20intitle:"index.of"%20intext:backup"',
        f'https://www.google.com/search?q=site:{cli}%20intext:"Index%20of"%20intext:"backup.tar"',
        f'https://www.google.com/search?q=site:{cli}%20intitle:"index%20of"%20"config.php"',
        f'https://www.google.com/search?q=site:{cli}%20inurl:"/private"%20intext:"index%20of%20/"%20"config"',
        f'https://www.google.com/search?q=site:{cli}%20intitle:"index%20of%20"%20"config/db"',
        f'https://www.google.com/search?q=site:{cli}%20intitle:"index%20of%20/"%20"docker-compose.yml"%20".env"',
        f'https://www.google.com/search?q=site:{cli}%20intext:"index%20of%20/"%20".ovpn"',
        f'https://www.google.com/search?q=site:{cli}%20intitle:"index%20of%20/"%20"public.zip"',
        f'https://www.google.com/search?q=site:{cli}%20intitle:"index%20of%20/"%20"admin.zip"%20"admin/"',
        f'https://www.google.com/search?q=site:{cli}%20intitle:"index%20of%20"conf.json"',
        f'https://www.google.com/search?q=site:{cli}%20intitle:"index%20of%20"application.yml"',
        f'https://www.google.com/search?q=site:{cli}%20inurl:ssh%20intitle:index%20of%20/files',
        f'https://www.google.com/search?q=site:{cli}%20intitle:"index%20of"%20"database.sql"',
        f'https://www.google.com/search?q=site:{cli}%20intext:"index%20of"%20smb.conf',
        f'https://www.google.com/search?q=site:{cli}%20index%20of:admin.asp',
        f'https://www.google.com/search?q=site:{cli}%20intext:"index%20of"%20"config"',
        f'https://www.google.com/search?q=site:{cli}%20intitle:"index%20of%20/"%20intext:".db',
        f'https://www.google.com/search?q=site:{cli}%20intitle:index%20of%20"wc.db"',
        f'https://www.google.com/search?q=site:{cli}%20intitle:%20index%20of%20/secrets/',
        f'https://www.google.com/search?q=site:{cli}%20intext:"index%20of"%20".git"',
        f'https://www.google.com/search?q=site:{cli}%20intitle:"index%20of%20/database/migrations"',
        f'https://www.google.com/search?q=site:{cli}%20intext:"index%20of"%20".sql"',
        f'https://www.google.com/search?q=site:{cli}%20intext:"index%20of"%20"phpMyAdmin"',
        f'https://www.google.com/search?q=site:{cli}%20intitle:Index%20of%20"/venv"',
        f'https://www.google.com/search?q=site:{cli}%20inurl:"admin/default.aspx"',
        f'https://www.google.com/search?q=site:{cli}%20inurl:%20/wp-includes/uploads',
        f'https://www.google.com/search?q=site:{cli}%20intitle:"index%20of"%20"release.sh"',
        f'https://www.google.com/search?q=site:{cli}%20intitle:"index%20of"%20"setup.sh"',
        f'https://www.google.com/search?q=site:{cli}%20intitle:"index%20of"%20"configure.sh"',
        f'https://www.google.com/search?q=site:{cli}%20intitle:"index%20of"%20"deploy.sh"',
        f'https://www.google.com/search?q=site:{cli}%20intitle:"index%20of%20/"%20intext:".env"',
        f'https://www.google.com/search?q=site:{cli}%20intext:"Index%20of"%20intext:"bitbucket-pipelines.yml"',
        f'https://www.google.com/search?q=site:{cli}%20inurl:/admin%20ext:config',
        f'https://www.google.com/search?q=site:{cli}%20intitle:"index%20of"%20"db.py"',
        f'https://www.google.com/search?q=site:{cli}%20intitle:"index%20of%20"cloud-config.yml"',
        f'https://www.google.com/search?q=site:{cli}%20index%20of%20/wp-admin.zip',
        f'https://www.google.com/search?q=site:{cli}%20intitle:"index%20of"%20aws/',
        f'https://www.google.com/search?q=site:{cli}%20intitle:"index%20of"%20"catalina.out"',
        f'https://www.google.com/search?q=site:{cli}%20"index%20of"%20error%20logs',
        f'https://www.google.com/search?q=site:{cli}%20intitle:"index%20of"%20"java.log"%20|%20"java.logs"',
        f'https://www.google.com/search?q=site:{cli}%20intext:"token"%20filetype:log%20"authenticate"',
        f'https://www.google.com/search?q=site:{cli}%20intitle:index%20of%20./jira-software',
        f'https://www.google.com/search?q=site:{cli}%20intitle:index%20of%20"aws/credentials"',
        f'https://www.google.com/search?q=site:{cli}%20intitle:"index%20of"%20*.xls',
        f'https://www.google.com/search?q=site:{cli}%20db%20password%20filetype:env',
        f'https://www.google.com/search?q=site:{cli}%20intitle:index%20of%20settings.py',
        f'https://www.google.com/search?q=site:{cli}%20inurl:admin%20filetype:txt',
        f'https://www.google.com/search?q=site:{cli}%20intitle:"index%20of"%20ext:sql|xls|xml|json|csv',
        f'https://www.google.com/search?q=site:{cli}%20"MYSQL%20ROOT%20PASSWORD:"%20ext:env%20OR%20ext:yml%20-git',
        f'https://www.google.com/search?q=site:{cli}%20inurl:admin%20filetype:db',
        f'https://www.google.com/search?q=site:{cli}%20inurl:"*admin%20|%20login"%20|%20inurl:.php%20|%20.asp',
        f'https://www.google.com/search?q=filetype:log%20site:{cli}',
        f'https://www.google.com/search?q=inurl:passwd%20filetype:txt%20site:{cli}',
        f'https://www.google.com/search?q=intitle:"index%20of%20/*"%20site:{cli}',
        f'https://www.google.com/search?q=intitle:"index%20of%20/"%20(passwd%20|%20password.txt)%20site:{cli}',
        f'https://www.google.com/search?q=intitle:"index%20of%20/password"%20site:{cli}',
        f'https://www.google.com/search?q=intitle:"index%20of%20/admin"%20site:{cli}',
        f'https://www.google.com/search?q=intitle:"index%20of%20/"%20Parent%20Directory%20site:{cli}',
        f'https://www.google.com/search?q=site:{cli}%20ext:txt%20|%20ext:doc%20|%20ext:docx%20|%20ext:odt%20|%20ext:pdf%20|%20ext:rtf%20|%20ext:sxw%20|%20ext:psw%20|%20ext:ppt%20|%20ext:pptx%20|%20ext:pps%20|%20ext:csv%20|%20ext:mdb',
        f'https://www.google.com/search?q=intitle:"login"%20"admin"%20site:{cli}',
        f'https://www.google.com/search?q=site:{cli}%20inurl:admin%20|%20administrator%20|%20adm%20|%20login%20|%20wp-login',
        f'https://www.google.com/search?q=password%20filetype:docx%20site:{cli}',
        f'https://www.google.com/search?q="index%20of%20/"%20*/*%20site:{cli}',
        f'https://www.google.com/search?q=db%20password%20filetype:env%20site:{cli}',
        f'https://www.google.com/search?q=intext:"index%20of%20/.git"%20"parent%20directory"%20site:{cli}',
        f'https://www.google.com/search?q=intitle:"index%20of"%20"properties.json"%20site:{cli}',
        f'https://www.google.com/search?q=intitle:"index%20of%20"%20"config/db"%20site:{cli}',
        f'https://www.google.com/search?q=site:{cli}%20intitle:index.of',
        f'https://www.google.com/search?q=site:{cli}%20ext:xml%20|%20ext:conf%20|%20ext:cnf%20|%20ext:reg%20|%20ext:inf%20|%20ext:rdp%20|%20ext:cfg%20|%20ext:txt%20|%20ext:ora%20|%20ext:ini',
        f'https://www.google.com/search?q=site:{cli}%20ext:sql%20|%20ext:dbf%20|%20ext:mdb',
        f'https://www.google.com/search?q=site:{cli}%20inurl:wp-%20|%20inurl:wp-content%20|%20inurl:plugins%20|%20inurl:uploads%20|%20inurl:themes%20|%20inurl:download',
        f'https://www.google.com/search?q=site:{cli}%20ext:bkf%20|%20ext:bkp%20|%20ext:bak%20|%20ext:old%20|%20ext:backup',
        f'https://www.google.com/search?q=site:*.*.{cli}',
        f'https://www.google.com/search?q=site:*.{cli}',
        f'https://www.google.com/search?q=site:{cli}%20inurl:"/phpinfo.php"%20|%20inurl:".htaccess"%20|%20inurl:"/.git"%20%20-github',
        f'https://www.google.com/search?q=site:{cli}%20ext:action%20|%20ext:struts%20|%20ext:do',
        f'https://www.google.com/search?q=site:{cli}%20inurl:readme%20|%20inurl:license%20|%20inurl:install%20|%20inurl:setup%20|%20inurl:config',
        f'https://www.google.com/search?q=site:{cli}%20inurl:shell%20|%20inurl:backdoor%20|%20inurl:wso%20|%20inurl:cmd%20|%20shadow%20|%20passwd%20|%20boot.ini%20|%20inurl:backdoor',
        f'https://www.google.com/search?q=site:{cli}%20ext:php%20intitle:phpinfo%20"published%20by%20the%20PHP%20Group"',
        f'https://www.google.com/search?q=site:{cli}%20ext:doc%20|%20ext:docx%20|%20ext:odt%20|%20ext:pdf%20|%20ext:rtf%20|%20ext:sxw%20|%20ext:psw%20|%20ext:ppt%20|%20ext:pptx%20|%20ext:pps%20|%20ext:csv',
        f'https://www.google.com/search?q=inurl:{cli}%20ext:swf',
        f'https://www.google.com/search?q=inurl:"/private"%20intext:"index%20of%20/"%20"config"%20%20site:{cli}',
        f'https://www.google.com/search?q=intitle:"index%20of"%20"config.php"%20%20site:{cli}',
        f'https://www.google.com/search?q=intext:"index%20of%20/"%20".ovpn"%20site:{cli}',
        f'https://www.google.com/search?q=intitle:"index%20of%20/"%20"styleci.yml"%20".env"%20site:{cli}',
        f'https://www.google.com/search?q=intitle:"index%20of%20/"%20"docker-compose.yml"%20".env"%20site:{cli}',
        f'https://www.google.com/search?q=intext:"index%20of"%20downloads"%20site:{cli}',
        f'https://www.google.com/search?q=inurl:%20"phpmyadmin/setup/"%20site:{cli}',
        f'https://www.google.com/search?q=intitle:"index%20of%20"conf.json"%20site:{cli}',
        f'https://www.google.com/search?q=site:{cli}%20intext:"sql%20syntax%20near"',
        f'https://www.google.com/search?q=site:{cli}%20intext:"sql%20syntax%20near"%20|%20intext:"syntax%20error%20has%20occurred"%20|%20intext:"incorrect%20syntax%20near"%20|%20intext:"unexpected%20end%20of%20SQL%20command"%20|%20intext:"Warning:%20mysql%20connect()"%20|%20intext:"Warning:%20mysql%20query()"%20|%20intext:"Warning:%20pg%20connect()"',
        f'https://www.google.com/search?q=site:{cli}%20intext:"sql%20syntax%20near"%20|%20%20intext:"incorrect%20syntax%20near"',
        f'https://www.google.com/search?q=intitle:"index%20of%20"application.yml"%20site:{cli}',
        f'https://www.google.com/search?q=inurl:adminpanel%20site:{cli}',
        f'https://www.google.com/search?q=intitle:"index%20of"%20inurl:admin/php%20site:{cli}',
        f'https://www.google.com/search?q=inurl:"phpmyadmin/setup/"%20site:{cli}',
        f'https://www.google.com/search?q=inurl:ssh%20intitle:index%20of%20/files%20site:{cli}',
        f'https://www.google.com/search?q=intitle:"index%20of"%20"database.sql"%20site:{cli}',
        f'https://www.google.com/search?q=intext:"index%20of"%20smb.conf%20site:{cli}',
        f'https://www.google.com/search?q=intitle:"index%20of"%20inurl:wp-json%20index.json%20site:{cli}',
        f'https://www.google.com/search?q=intext:"index%20of"%20"config"%20site:{cli}',
        f'https://www.google.com/search?q=intitle:"index%20of%20/"%20intext:.db%20site:{cli}',
        f'https://www.google.com/search?q=intitle:index%20of%20"wc.db"%20site:{cli}',
        f'https://www.google.com/search?q=intext:"index%20of"%20".git"%20site:{cli}',
        f'https://www.google.com/search?q=site:{cli}%20intext:login%20intext:username%20intext:password',
        f'https://www.google.com/search?q=site:{cli}%20ext:ppt%20intext:password',
        f'https://www.google.com/search?q=site:{cli}%20filetype:xls%20inurl:"email.xls"',
        f'https://www.google.com/search?q=allintext:username%20filetype:log%20site:{cli}',
        f'https://www.google.com/search?q=inurl:/proc/self/cwd%20site:{cli}',
        f'https://www.google.com/search?q="index%20of"%20"database.sql.zip"%20site:{cli}',
        f'https://www.google.com/search?q=intitle:"index%20of"%20"WebServers.xml"%20site:{cli}',
        f'https://www.google.com/search?q=filetype:xls%20inurl:"email.xls"%20site:{cli}',
        f'https://www.google.com/search?q=intitle:"Index%20of"%20wp-admin%20site:{cli}',
        f'https://www.google.com/search?q=intitle:"index%20of"%20"admin/sql/"%20site:{cli}',
        f'https://www.google.com/search?q=intitle:"index%20of"%20"system/config"%20site:{cli}',
        f'https://www.google.com/search?q=site:{cli}%20inurl:admin%20"@gmail.com"',
        f'https://www.google.com/search?q=inurl:zoom.us/j%20and%20intext:scheduled%20for%20site:{cli}',
        f'https://www.google.com/search?q=allintitle:restricted%20filetype:doc%20site:{cli}',
        f'https://www.google.com/search?q=inurl:Dashboard.jspa%20intext:"Atlassian%20Jira%20Project%20Management%20Software"%20site:{cli}',
        f'https://www.google.com/search?q=filetype:txt%20site:{cli}',
        f'https://www.google.com/search?q=site:{cli}%20"Whoops!%20There%20was%20an%20error."',
        f'https://www.google.com/search?q=site:{cli}%20inurl:/frontend%20dev.php/$',
        f'https://www.google.com/search?q=site:{cli}%20"SF%20ROOT%20DIR"',
        f'https://www.google.com/search?q=site:{cli}%20Application%20Trace%20+%20nil:NilClass%20(10%)%20TBD',
        f'https://www.google.com/search?q=site:{cli}%20"unexpected%20error"%20OR%20"Uncaught%20Exception"%20OR%20"fatal%20error"%20OR%20"Unknown%20column"%20OR%20"exception%20occurred"',
        f'https://www.google.com/search?q=site:{cli}%20employee%20offers',
        f'https://www.google.com/search?q=inurl:gitlab%20"{cli}"',
        f'https://www.google.com/search?q=site:http://box.com%20"{cli}"',
        f'https://www.google.com/search?q=inurl:gitlab%20"{cli}"',
        f'https://www.google.com/search?q=site:atlassian.net%20"{cli}"',
        f'https://www.google.com/search?q=site:atlassian.net%20inurl:/servicedesk/customer/user/login%20"{cli}"',
        f'https://www.google.com/search?q=site:bitbucket.org%20"{cli}"',
        f'https://www.google.com/search?q=site:codebeautify.org%20"{cli}"',
        f'https://www.google.com/search?q=site:codepad.co%20"{cli}"',
        f'https://www.google.com/search?q=site:codepen.io%20"{cli}"',
        f'https://www.google.com/search?q=site:codeshare.io%20"{cli}"',
        f'https://www.google.com/search?q=site:coggle.it%20"{cli}"',
        f'https://www.google.com/search?q=site:gitter.im%20"{cli}"',
        f'https://www.google.com/search?q=site:google.com%20"{cli}"',
        f'https://www.google.com/search?q=site:jsdelivr.net%20"{cli}"',
        f'https://www.google.com/search?q=site:jsfiddle.net%20"{cli}"',
        f'https://www.google.com/search?q=site:libraries.io%20"{cli}"',
        f'https://www.google.com/search?q=site:npm.runkit.com%20"{cli}"',
        f'https://www.google.com/search?q=site:npmjs.com%20"{cli}"',
        f'https://www.google.com/search?q=site:papaly.com%20"{cli}"',
        f'https://www.google.com/search?q=site:pastebin.com%20"{cli}"',
        f'https://www.google.com/search?q=site:prezi.com%20"{cli}"',
        f'https://www.google.com/search?q=site:productforums.google.com%20"{cli}"',
        f'https://www.google.com/search?q=site:repl.it%20"{cli}"',
        f'https://www.google.com/search?q=site:scribd.com%20"{cli}"',
        f'https://www.google.com/search?q=site:sharecode.io%20"{cli}"',
        f'https://www.google.com/search?q=site:trello.com%20"{cli}"',
        f'https://www.google.com/search?q=site:ycombinator.com%20"{cli}"',
        f'https://www.google.com/search?q=site:zoom.us%20inurl:"{cli}"',
        f'https://www.google.com/search?q=inurl:https://trello.com%20AND%20intext:{cli}',
        f'https://www.google.com/search?q=site:s3.amazonaws.com%20"{cli}"',
        f'https://www.google.com/search?q=site:blob.core.windows.net%20"{cli}"',
        f'https://www.google.com/search?q=site:googleapis.com%20"{cli}"',
        f'https://www.google.com/search?q=site:drive.google.com%20"{cli}"',
        f'https://www.google.com/search?q=site:dev.azure.com%20"{cli}"',
        f'https://www.google.com/search?q=site:onedrive.live.com%20"{cli}"',
        f'https://www.google.com/search?q=site:digitaloceanspaces.com%20"{cli}"',
        f'https://www.google.com/search?q=site:sharepoint.com%20"{cli}"',
        f'https://www.google.com/search?q=site:s3-external-1.amazonaws.com%20"{cli}"',
        f'https://www.google.com/search?q=site:s3.dualstack.us-east-1.amazonaws.com%20"{cli}"',
        f'https://www.google.com/search?q=site:dropbox.com/s%20"{cli}"',
        f'https://www.google.com/search?q=inurl:www.dropbox.com/s/%20"{cli}"',
        f'https://www.google.com/search?q=site:box.com/s%20"{cli}"',
        f'https://www.google.com/search?q=site:docs.google.com%20inurl:"/d/"%20"{cli}"',
        f'https://www.google.com/search?q=inurl:lang=%20|%20inurl:name=%20|%20inurl:view=%20|%20inurl:name=%20|%20inurl:callback=%20|%20inurl:id=%20|%20inurl:q=%20|%20inurl:s=%20|%20inurl:keyword=%20|%20inurl:search=%20|%20inurl:page=%20|%20inurl:query=%20inurl:&%20site:{cli}',
        f'https://www.google.com/search?q=inurl:page=%20|%20inurl:next=%20|%20inurl:host=%20|%20inurl:go=%20|%20inurl:goto=%20|%20inurl:file=%20|%20inurl:host=%20|%20inurl:redirect%20to=%20|%20inurl:url=%20|%20inurl:redirect%20|%20inurl:src=http%20|%20inurl:r=http%20|%20inurl:return=%20|%20inurl:next=%20|%20inurl:redir=%20|%20inurl:http%20site:*.*.{cli}',
        f'https://www.google.com/search?q=inurl:page=%20|%20inurl:next=%20|%20inurl:host=%20|%20inurl:go=%20|%20inurl:goto=%20|%20inurl:file=%20|%20inurl:host=%20|%20inurl:redirect%20to=%20|%20inurl:url=%20|%20inurl:redirect%20|%20inurl:src=http%20|%20inurl:r=http%20|%20inurl:return=%20|%20inurl:next=%20|%20inurl:redir=%20|%20inurl:http%20site:{cli}',
        f'https://www.google.com/search?q=inurl:id=%20|%20inurl:pid=%20|%20inurl:category=%20|%20inurl:cat=%20|%20inurl:action=%20|%20inurl:sid=%20|%20inurl:dir=%20inurl:&%20site:*.*.{cli}',
        f'https://www.google.com/search?q=inurl:id=%20|%20inurl:pid=%20|%20inurl:category=%20|%20inurl:cat=%20|%20inurl:action=%20|%20inurl:sid=%20|%20inurl:dir=%20inurl:&%20site:{cli}',
        f'https://www.google.com/search?q=inurl:http%20|%20inurl:resource%20|%20inurl:resources%20|%20inurl:url=%20|%20inurl:path=%20|%20inurl:dest=%20|%20inurl:proxy=%20|%20inurl:html=%20|%20inurl:data=%20|%20inurl:domain=%20%20|%20inurl:page=%20inurl:&%20site:{cli}',
        f'https://www.google.com/search?q=inurl:include%20|%20inurl:dir%20|%20inurl:detail=%20|%20inurl:file=%20|%20inurl:folder=%20|%20inurl:inc=%20|%20inurl:locate=%20|%20inurl:doc=%20|%20inurl:conf=%20inurl:&%20site:*.*.{cli}',
        f'https://www.google.com/search?q=inurl:include%20|%20inurl:dir%20|%20inurl:detail=%20|%20inurl:file=%20|%20inurl:folder=%20|%20inurl:inc=%20|%20inurl:locate=%20|%20inurl:doc=%20|%20inurl:conf=%20inurl:&%20site:{cli}',
        f'https://www.google.com/search?q=inurl:cmd%20|%20inurl:exec=%20|%20inurl:query=%20|%20inurl:code=%20|%20inurl:do=%20|%20inurl:run=%20|%20inurl:read=%20%20|%20inurl:ping=%20inurl:&%20site:*.*.{cli}',
        f'https://www.google.com/search?q=inurl:cmd%20|%20inurl:exec=%20|%20inurl:query=%20|%20inurl:code=%20|%20inurl:do=%20|%20inurl:run=%20|%20inurl:read=%20%20|%20inurl:ping=%20inurl:&%20site:{cli}',
        f'https://www.google.com/search?q=inurl:config%20|%20inurl:env%20|%20inurl:setting%20|%20inurl:backup%20|%20inurl:admin%20|%20inurl:php%20site:*.*.{cli}',
        f'https://www.google.com/search?q=inurl:config%20|%20inurl:env%20|%20inurl:setting%20|%20inurl:backup%20|%20inurl:admin%20|%20inurl:php%20site:{cli}',
        f'https://www.google.com/search?q=inurl:email=%20|%20inurl:phone=%20|%20inurl:password=%20|%20inurl:secret=%20inurl:&%20site:{cli}',
        f'https://www.google.com/search?q=site:codepad.co%20"{cli}"',
        f'https://www.google.com/search?q=site:scribd.com%20"{cli}"',
        f'https://www.google.com/search?q=site:npmjs.com%20"{cli}"',
        f'https://www.google.com/search?q=site:npm.runkit.com%20"{cli}"',
        f'https://www.google.com/search?q=site:libraries.io%20"{cli}"',
        f'https://www.google.com/search?q=site:ycombinator.com%20"{cli}"',
        f'https://www.google.com/search?q=site:coggle.it%20"{cli}"',
        f'https://www.google.com/search?q=site:papaly.com%20"{cli}"',
        f'https://www.google.com/search?q=site:google.com%20"{cli}"',
        f'https://www.google.com/search?q=site:trello.com%20"{cli}"',
        f'https://www.google.com/search?q=site:prezi.com%20"{cli}"',
        f'https://www.google.com/search?q=site:jsdelivr.net%20"{cli}"',
        f'https://www.google.com/search?q=site:codepen.io%20"{cli}"',
        f'https://www.google.com/search?q=site:codeshare.io%20"{cli}"',
        f'https://www.google.com/search?q=site:sharecode.io%20"{cli}"',
        f'https://www.google.com/search?q=site:pastebin.com%20"{cli}"',
        f'https://www.google.com/search?q=site:repl.it%20"{cli}"',
        f'https://www.google.com/search?q=site:productforums.google.com%20"{cli}"',
        f'https://www.google.com/search?q=site:gitter.im%20"{cli}"',
        f'https://www.google.com/search?q=site:bitbucket.org%20"{cli}"',
        f'https://www.google.com/search?q=site:bitbucket.org%20inurl:{cli}',
        f'https://www.google.com/search?q=site:zoom.us%20inurl:"{cli}"',
        f'https://www.google.com/search?q=site:atlassian.net%20"{cli}"',
        f'https://www.google.com/search?q=site:s3.amazonaws.com%20intext:{cli}',
        f'https://www.google.com/search?q=site:jfrog.io%20"{cli}"',
        f'https://www.google.com/search?q=site:firebaseio.com%20"{cli}"',
        f'https://www.google.com/search?q=inurl:apidocs%20|%20inurl:api-docs%20|%20inurl:swagger%20|%20inurl:api-explorer%20site:"{cli}"',
        f'https://www.google.com/search?q=intext:"error"%20|%20intext:"exception"%20|%20intext:"not%20found"%20|%20intext:"failed"%20site:"{cli}"',
        f'https://www.google.com/search?q=site:"{cli}"%20inurl:login%20|%20inurl:logon%20|%20inurl:sign-in%20|%20inurl:signin%20|%20inurl:portal',
        f'https://www.google.com/search?q=site:"{cli}"%20"choose%20file"'
    ]