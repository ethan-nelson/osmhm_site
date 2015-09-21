<%inherit file="base.mako"/>
<%block name="header">
</%block>
<%block name="content">
<h1 class="page-header">Full History</h1>
% if history:
<table class="table">
<tr><th>Time</th><th>Changeset</th><th>Username</th><th>Created</th><th>Modified</th><th>Deleted</th></tr>
% for event in history:
	<tr><td>${event.timestamp}</td>
    <td><a href="http://www.osm.org/changeset/${event.changeset}" target="_blank">${event.changeset}</a></td>
    <td><a href="http://www.osm.org/user/${event.username}" target="_blank">${event.username}</a></td>
    <td>${event.created}</td>
    <td>${event.modified}</td>
    <td>${event.deleted}</td></tr>
% endfor
</table>
% else:
No events registered
% endif
</%block>
