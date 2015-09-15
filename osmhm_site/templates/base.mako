<%def name="title()"></%def>
<!DOCTYPE html>
<html lang="en">
    <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>OpenStreetMap Hall Monitor</title>

    <script src="${request.static_url('osmhm_site:static/js/jquery-1.11.3.min.js')}"></script>
    <script src="${request.static_url('osmhm_site:static/twbs/js/bootstrap.min.js')}"></script>

	<link href="${request.static_url('osmhm_site:static/twbs/css/bootstrap.css')}" rel="stylesheet">
	<link href="${request.static_url('osmhm_site:static/css/dashboard.css')}" rel="stylesheet">

    </head>
    <body>
    <nav class="navbar navbar-inverse navbar-fixed-top">
      <div class="container-fluid">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="navbar-brand" href="${request.route_path('home')}"><i class="glyphicon glyphicon-eye-open"></i>penStreetMap Hall Monitor</a>
        </div>
        <div id="navbar" class="navbar-collapse collapse">
          <ul class="nav navbar-nav navbar-right">
            <li><a href="${request.route_path('watch')}">Watch list</a></li>
            % if user and (user.is_dwg or user.is_admin or user.is_owner):
            <li><a href="${request.route_path('user_watch')}">User watch list</a></li>
            <li><a href="${request.route_path('object_watch')}">Object watch list</a></li>
            <li><a href="${request.route_path('admin')}">Admin panel</a></li>
            % endif
            % if user:
            <li><a href="${request.route_path('logout')}">Logout</a></li>
            % else:
            <li><a href="${request.route_path('login')}">Login</a></li>
            % endif
          </ul>
        </div>
      </div>
    </nav>

    <div class="container-fluid">
      <div class="row">
        <div class="col-sm-3 col-md-2 sidebar">
          <ul class="nav nav-sidebar" style="margin-left: 0px !important;">
			% if page_id is ('user_watch' or 'user_watch_add'):
            <li><a href="${request.route_path('user_watch_list')}">Users on list</a></li>
            % elif page_id is 'user_watch_list':
            <li><a href="${request.route_path('user_watch_add')}">Add a user</a></li>
			% elif page_id is ('object_watch' or 'object_watch_add'):
            <li><a href="${request.route_path('object_watch_list')}">Objects on list</a></li>
            % elif page_id is 'object_watch_list':
            <li><a href="${request.route_path('object_watch_add')}">Add an object</a></li>
            % elif page_id is 'watch_whitelist':
            <li><a href="${request.route_path('watch_whitelist_add')}">Add a whitelisted user</a></li>
			% elif page_id is 'watch':
			<li>Flags:</li>
			<li>1: Skewed ratio of add to delete</li>
			<li>2: Added > 1500 nodes</li>
			<li>3: Deleted > 1500 objects</li>
			<br />
            <li><a href="${request.route_path('watch_whitelist')}">Users on whitelist</a></li>
            % endif
            % if page_id is ('watch' or 'user_watch' or 'object_watch'):
			<li>Last update: ${update_time}</li>
            % endif
          </ul>
        </div>

        <div class="col-sm-9 col-sm-offset-3 col-md-10 col-md-offset-2 main">
	        <%block name="content"></%block>
		</div>
    </body>
</html>
