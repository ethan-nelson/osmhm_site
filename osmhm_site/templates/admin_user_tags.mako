<%inherit file="base.mako"/>
<%block name="header">
</%block>
<%block name="content">
<h1 class="page-header">User Tag Administration Page</h1>
<p>Click a tag to delete it (no confirmation will be given!).</p>
% if tags:
% for tag in tags:
<div class="row">
<b>${tag.name}</b> | <a href="${request.route_path('delete_user_tag',id=tag.id)}"><i class="glyphicon glyphicon-remove" style="color: red;"></i></a><br />
${tag.description}
</div><br />
% endfor
% else:
<div class="row">
<p>There are currently no added tags.</p>
</div>
% endif
<div class="row">
<p><b><a href="${request.route_path('add_user_tag')}">Add a user tag</a></b></p>
</div>
</%block>
