<%inherit file="base.mako"/>
<%block name="header">
</%block>
<%block name="content">
<h1 class="page-header">User Watch List</h1>
% if history:
<table class="table table-condensed">
<tr><th>Time</th><th>Changeset</th><th>Username</th><th>Added</th><th>Modified</th><th>Deleted</th><th>Delete Event</th></tr>
% for event in history:
	<tr><td>${event[0].timestamp}</td>
    <td><a href="http://www.osm.org/changeset/${event[0].changeset}" target="_blank">${event[0].changeset}</a></td>
    <td><a href="http://www.osm.org/user/${event[1].username}" target="_blank">${event[1].username}</a></td>
    <td>${event[0].created}</td>
    <td>${event[0].modified}</td>
    <td>${event[0].deleted}</td>
    <td><a href="${request.route_path('user_watch_event_delete',id=event[0].id)}"><i class="glyphicon glyphicon-remove" style="color: red;"></i></a></td></tr>
% endfor
</table>
% else:
No events registered for users in the watchlist
% endif
</%block>
