<%inherit file="base.mako"/>
<%block name="header">
</%block>
<%block name="content">
<h1 class="page-header">Users in List</h1>
% if users:
<table class="table table-condensed">
<caption>Deleting a user also removes its listings in the user history.</caption>
<tr><th>User</th><th>Author</th><th>Reason</th><th>Delete</th></tr>
% for user in users:
	<tr><td><a href="http://www.osm.org/user/${user.username}">${user.username}</a></td>
    <td>${user.author}</td>
    <td>${user.reason}</td>
    <td><a href="${request.route_path('user_watch_delete',id=user.id)}"><i class="glyphicon glyphicon-remove" style="color: red;"></i></a></td></tr>
% endfor
</table>
% else:
No users registered
% endif
</%block>
