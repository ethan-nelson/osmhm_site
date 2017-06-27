<%inherit file="base.mako"/>
<%block name="header">
</%block>
<%block name="content">
<h1 class="page-header">Users on List</h1>
% if users:
<table class="table table-condensed">
<caption>Deleting a user also removes its listings in the user history.</caption>
<tr><th>User</th><th>Author</th><th>Reason</th><th>Notify On?</th><th>Edit</th><th>Delete</th></tr>
% for user in users:
	<tr><td><a href="http://www.osm.org/user/${user.username}">${user.username}</a></td>
    <td>${user.author}</td>
    <td>${user.reason}</td>
<td>
<% notify='<i class="glyphicon glyphicon-volume-up"></i>' if len(user.email) > 1 else '<i class="glyphicon glyphicon-volume-off"></i>' %>
${notify | n}
</td>
    <td><a href="${request.route_path('user_watch_edit',id=user.id)}"><i class="glyphicon glyphicon-pencil" style="color: blue;"></i></a></td>
    <td><a href="${request.route_path('user_watch_delete',id=user.id)}"><i class="glyphicon glyphicon-remove" style="color: red;"></i></a></td></tr>
% endfor
</table>
% else:
<p>None of the users you are watching have had any activity since the last update time.</p>
% endif
</%block>
