<%inherit file="base.mako"/>
<%block name="header">
</%block>
<%block name="content">
<h1 class="page-header">Objects in List</h1>
% if objects:
<table class="table table-condensed">
<caption>Deleting an object also removes its listings in the object history.</caption>
<tr><th>Object</th><th>Author</th><th>Note</th><th>Delete</th></tr>
% for anobject in objects:
	<tr>
    <td>${anobject.number}
<%
#% if 'n' in anobject.number:
#    <a href="http://www.osm.org/node/${anobject.number[1:]}">${anobject.number}</a>
#% else if 'w' in anobject.number:
#    <a href="http://www.osm.org/way/${anobject.number[1:]}">${anobject.number}</a>
#% else if 'r' in anobject.number:
#    <a href="http://www.osm.org/relation/${anobject.number[1:]}">${anobject.number}</a>
#% endif
%>
    </td>
    <td>${anobject.author}</td>
    <td>${anobject.note}</td>
    <td><a href="${request.route_path('object_watch_delete',id=anobject.id)}"><i class="glyphicon glyphicon-remove" style="color: red;"></i></a></td></tr>
% endfor
</table>
% else:
No objects registered
% endif
</%block>
