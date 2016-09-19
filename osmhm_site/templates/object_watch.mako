<%inherit file="base.mako"/>
<%block name="header">
</%block>
<%block name="content">
<h1 class="page-header">Object Activity List</h1>
% if history:
<table class="table table-condensed">
<tr><th>Object</th><th>Timestamp</th><th>Changeset</th><th>Username</th><th>Action</th><th>Delete Event</th></tr>
% for event in history:
%if event[1].element[0] == 'n':
  <% object_link = 'http://www.osm.org/node/'+event[1].element[1:] %>
%elif event[1].element[0] == 'w':
  <% object_link = 'http://www.osm.org/way/'+event[1].element[1:] %>
%elif event[1].element[0] == 'r':
  <% object_link = 'http://www.osm.org/relation/'+event[1].element[1:] %>
%else:
  <% object_link = '' %>
%endif
%if event[0].action == 1:
  <% action = 'create' %>
%elif event[0].action == 2:
  <% action = 'modify' %>
%elif event[0].action == 4:
  <% action = 'delete' %>
%else:
  <% action = '' %>
%endif
<tr>
    <td><a href=${object_link}>${event[1].element}</a></td>
    <td>${event[0].timestamp}</td>
    <td><a href="http://www.osm.org/changeset/${event[0].changeset}" target="_blank">${event[0].changeset}</a></td>
    <td><a href="http://www.osm.org/user/${event[0].username}" target="_blank">${event[0].username}</a></td>
    <td>${action}</td>
    <td><a href="${request.route_path('object_watch_event_delete',id=event[0].id)}"><i class="glyphicon glyphicon-remove" style="color: red;"></i></a></td>
</tr>
% endfor
</table>
% else:
No events registered for objects in the object watch list.
% endif
</%block>
