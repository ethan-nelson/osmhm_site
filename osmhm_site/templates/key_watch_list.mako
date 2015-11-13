<%inherit file="base.mako"/>
<%block name="header">
</%block>
<%block name="content">
<h1 class="page-header">Keys in List</h1>
% if keys:
<table class="table table-condensed">
<caption>Deleting a key also removes its listings in the key history.</caption>
<tr><th>Key</th><th>Value</th><th>Author</th><th>Note</th><th>Delete</th></tr>
% for anobject in keys:
	<tr>
    <td>${anobject.key}</td>
    <td>${anobject.value}</td>
    <td>${anobject.author}</td>
    <td>${anobject.reason}</td>
    <td><a href="${request.route_path('key_watch_delete',id=anobject.id)}"><i class="glyphicon glyphicon-remove" style="color: red;"></i></a></td></tr>
% endfor
</table>
% else:
No keys registered
% endif
</%block>
