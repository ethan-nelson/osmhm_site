<%inherit file="base.mako"/>
<%block name="header">
</%block>
<%block name="content">
<h1 class="page-header">Object Watch List</h1>
% if history:
<table class="table table-condensed">
<tr><th>Time</th><th>Changeset</th><th>Username</th><th>Action</th><th>Object ID</th><th>Delete Event</th></tr>
% for event in history:
	<tr><td>${event[0].timestamp}</td>
    <td><a href="http://www.osm.org/changeset/${event[0].changeset}" target="_blank">${event[0].changeset}</a></td>
    <td><a href="http://www.osm.org/user/${event[0].username}" target="_blank">${event[0].username}</a></td>
    <td>${event[0].action}</td>
    <td>${event[1].element}</td>
    <td><a href="${request.route_path('object_watch_event_delete',id=event[0].id)}"><i class="glyphicon glyphicon-remove" style="color: red;"></i></a></td></tr>
% endfor
</table>
% else:
No events registered for objects in the object watch list.
% endif
</%block>
