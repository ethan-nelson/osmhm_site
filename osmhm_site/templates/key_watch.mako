<%inherit file="base.mako"/>
<%block name="header">
</%block>
<%block name="content">
<style>
.hidden_row {
    padding: 0 !important;
}
.hidden_row:hover {
	background-color: #fff;
}
.table tr:hover {
    background-color: #eee;
}
</style>
<h1 class="page-header">Tag Activity List</h1>
<p><b>Click a row to expand the actual changeset numbers.</b></p>
% if history:
<table class="table table-condensed" style="border-collapse:collapse;">
<thead>
<tr><th>Key</th><th>Value</th><th>Username</th><th>Changeset Count</th><th>Object Count</th><th>Delete User's Events</th></tr>
</thead>
<tbody>
<% i=1 %>
% for event in history:
	<tr data-toggle="collapse" data-target="#row${i}" class="accordion-toggle">
    <td>${event.key}</td>
    <td>${event.value}</td>
    <td><a href="http://www.osm.org/user/${event.username}" target="_blank">${event.username}</a></td>
    <td>${event.changeset_count}</td>
    <td>${event.object_count}</td>
    <td><a href="${request.route_path('key_watch_event_delete',username=event.username,key=event.key,value=event.value)}"><i class="glyphicon glyphicon-remove" style="color: red;"></i></a></td></tr>
<tr><td colspan="6" class="hidden_row" style="border: 0px;"><div class="accordian-body collapse" id="row${i}">Changesets:
${event.changesets[:-2] | n}
</div></td></tr>
<% i=i+1 %>
% endfor
</tbody>
</table>
% else:
No events registered for keys in the key watch list.
% endif
</%block>
