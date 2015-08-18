<%inherit file="base.mako"/>
<%block name="header">
</%block>
<%block name="content">
<h1 class="page-header">Users in whitelist</h1>
% if users:
<table class="table table-condensed">
<tr><th>User</th><th>Author</th><th>Reason</th><th>Delete</th></tr>
% for user in users:
    <tr><td><a href="http://www.osm.org/user/${user.username}">${user.username}</a></td>
    <td>${user.author}</td>
    <td>${user.reason}</td>
    <td><a href="${request.route_path('watch_whitelist_delete',id=user.id)}"><i class="glyphicon glyphicon-remove" style="color: red;"></i></a></td></tr>
% endfor
</table>
% else:
No users registered in the whitelist
% endif
</%block>
