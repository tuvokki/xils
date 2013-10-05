from fabric.api import lcd, local

def prepare_deployment(branch_name):
    local('python manage.py test django_project')
    local('git add -p && git commit') # or local('hg add && hg commit')

def deploy():
    with lcd('/Users/wouter/development/workspace/xils/'):

        # With git...
        local('git pull /Users/wouter/xils/')

        # With Mercurial...
        #local('hg pull /my/path/to/dev/area/')
        #local('hg update')

        # With both
        local('python manage.py migrate xils_admin')
        local('python manage.py test xils_admin')
        local('webserver_start.sh')