<%inherit file="base.mako"/>
<%block name="header">
</%block>
<%block name="content">
<form class="form-horizontal" method="POST">
	<fieldset>
		<legend>Add user to watch list:</legend>
		<div class="form-group">
			<label for="addusername" class="col-lg-4 control-label">Username</label>
			<div class="col-lg-6">
				<input type="text" class="form-control" id="addusername" name="addusername" placeholder="Enter a username" required>
			</div>
		</div>
		<div class="form-group">
			<label for="addreason" class="col-lg-4 control-label">Reason:</label>
			<div class="col-lg-6">
				<input type="text" class="form-control" id="addreason" name="addreason" placeholder="Enter a reason" required>
				<span class="help-block">This helps us remember why a user is added. Maybe add a ticket reference from OTRS, or the source of a complaint/reason for monitoring: 'reported to be vandalising', 'user is being a bad egg', etc. Note this will be visible to DWG members.</span>
			</div>
		</div>
		<div class="form-group">
			<label for="addnotify" class="col-lg-4 control-label">Notification email:</label>
			<div class="col-lg-6">
				<input type="text" class="form-control" id="addnotify" name="addnotify" placeholder="Optionally enter an email address">
				<span class="help-block">Please use a personal email address, not the DWG group address. This will not be displayed, and will only be used for notification.</span>
			</div>
		</div>
		<div class="form-group">
			<div class="col-lg-10 col-lg-offset-6">
				<button class="btn btn-primary" type="submit" value="submit">Submit</button>
			</div>
		</div>
	</fieldset>
</form>
</%block>
