<%inherit file="base.mako"/>
<%block name="header">
</%block>
<%block name="content">
<%
if data:
  username = data.username
  reason = data.reason
  notify = data.email
  submit = 'Update'
else:
  username = ''
  reason = ''
  notify = ''
  submit = 'Submit'
%>
<form class="form-horizontal" method="POST">
	<fieldset>
		<legend>Add user to watch list:</legend>
		<div class="form-group">
			<label for="addusername" class="col-lg-4 control-label">Username</label>
			<div class="col-lg-6">
				<input type="text" class="form-control" id="addusername" name="addusername" placeholder="Enter a username" value="${username}" required>
			</div>
		</div>
		<div class="form-group">
			<label for="addreason" class="col-lg-4 control-label">Reason:</label>
			<div class="col-lg-6">
				<input type="text" class="form-control" id="addreason" name="addreason" placeholder="Enter a reason" value="${reason}" required>
				<span class="help-block">Enter a note to yourself why this user was added.</span>
			</div>
		</div>
		<div class="form-group">
			<label for="addnotify" class="col-lg-4 control-label">Notification email:</label>
			<div class="col-lg-6">
				<input type="text" class="form-control" id="addnotify" name="addnotify" placeholder="Optionally enter an email address" value="${notify}">
				<span class="help-block">Add an optional notification email address. Remove the address to stop notifications.</span>
			</div>
		</div>
		<div class="form-group">
			<div class="col-lg-10 col-lg-offset-6">
				<button class="btn btn-primary" type="submit" value="submit">${submit}</button>
			</div>
		</div>
	</fieldset>
</form>
</%block>
