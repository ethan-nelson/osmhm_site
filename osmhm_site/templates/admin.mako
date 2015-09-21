<%inherit file="base.mako"/>
<%block name="header">
</%block>
<%block name="content">
<h1 class="page-header">Administration Page</h1>
% if user and user.is_owner:
<p><a href="${request.route_path('history_clear')}">Purge current full history</a></p>
<p><a href="${request.route_path('watch_clear')}">Purge current watch list history</a></p>
<p><a href="${request.route_path('admin_user_list')}">Edit registered users</a></p><br />
% endif

<p><a href="${request.route_path('watch_whitelist')}">View the users on the whitelist</a></p>
<p><a href="${request.route_path('watch_whitelist_add')}">Add a user to the whitelist</a></p><br />
<p><a href="${request.route_path('object_watch_list')}">View the objects being tracked</a></p>
<p><a href="${request.route_path('object_watch_add')}">Add an object to be tracked</a></p><br />
<p><a href="${request.route_path('user_watch_list')}">View the users being tracked</a></p>
<p><a href="${request.route_path('user_watch_add')}">Add a user to be tracked</a></p>


</%block>
