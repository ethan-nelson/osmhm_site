<%inherit file="base.mako"/>
<%block name="header">
</%block>
<%block name="content">
<h1 class="page-header">Objects on List</h1>
% if objects:
<table class="table table-condensed">
<caption>Deleting an object also removes its listings in the object history.</caption>
<tr><th>Object</th><th>Author</th><th>Note</th><th>Notify On?</th><th>Edit</th><th>Delete</th></tr>
% for anobject in objects:
%if anobject.element[0] == 'n':
  <% object_link = 'http://www.osm.org/node/'+anobject.element[1:] %>
%elif anobject.element[0] == 'w':
  <% object_link = 'http://www.osm.org/way/'+anobject.element[1:] %>
%elif anobject.element[0] == 'r':
  <% object_link = 'http://www.osm.org/relation/'+anobject.element[1:] %>
%else:
  <% object_link = '' %>
%endif
<tr>
    <td><a href=${object_link}>${anobject.element}</a></td>
    <td>${anobject.author}</td>
    <td>${anobject.reason}</td>
<td>
<% notify='<i class="glyphicon glyphicon-volume-up"></i>' if len(anobject.email) > 1 else '<i class="glyphicon glyphicon-volume-off"></i>' %>
${notify | n}
</td>
    <td><a href="${request.route_path('object_watch_edit',id=anobject.id)}"><i class="glyphicon glyphicon-pencil" style="color: blue;"></i></a></td>
    <td><a href="${request.route_path('object_watch_delete',id=anobject.id)}"><i class="glyphicon glyphicon-remove" style="color: red;"></i></a></td></tr>
% endfor
</table>
% else:
<p>None of the objects you are watching have had any activity since the last update time.</p>
% endif
</%block>
