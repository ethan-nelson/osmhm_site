<%inherit file="base.mako"/>
<%block name="header">
</%block>
<%block name="content">
<h1 class="page-header">User Administration Page</h1>
% if users:
<table class="table">
<tr><th>User ID</th><th>Username</th><th>Make Member</th><th>Make Admin</th><th>Make Owner</th></tr>
% for contributor in users:
	<tr><td>${contributor.id}</td>
    <td><a href="http://www.osm.org/user/${contributor.username}" target="_blank">${contributor.username}</a></td>
    % if not contributor.is_member:
    <td><a href="${request.route_path('promote_member', id=contributor.id)}">Make member</a></td>
    % else:
    <td><a href="${request.route_path('promote_member', id=contributor.id)}">Unmake member</a></td>
    % endif
    % if not contributor.is_admin:
    <td><a href="${request.route_path('promote_admin', id=contributor.id)}">Make admin</a></td>
    % else:
    <td><a href="${request.route_path('promote_admin', id=contributor.id)}">Unmake admin</a></td>
    % endif
    % if not contributor.is_owner:
    <td><a href="${request.route_path('promote_owner', id=contributor.id)}">Make owner</a></td>
    % else:
    <td><a href="${request.route_path('promote_owner', id=contributor.id)}">Unmake owner</a></td>
    % endif
    </tr>
% endfor
</table>
% else:
<p>Something went wrong with loading the users. This isn't good.</p>
% endif
</%block>
