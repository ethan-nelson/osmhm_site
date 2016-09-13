<%inherit file="base.mako"/>
<%block name="header">
</%block>
<%block name="content">
<form class="form-horizontal" method="POST">
	<fieldset>
		<legend>Add key/value to watch list:</legend>
		<div class="form-group">
			<label for="addkey" class="col-lg-4 control-label">Key</label>
			<div class="col-lg-6">
				<input type="text" class="form-control" id="addkey" name="addkey" placeholder="e.g. railway" required>
				<span class="help-block">Add a key to watch. Wildcards are accepted, though only either the key or the value can be a wildcard.
			</div>
		</div>
		<div class="form-group">
			<label for="addvalue" class="col-lg-4 control-label">Value</label>
			<div class="col-lg-6">
				<input type="text" class="form-control" id="addvalue" name="addvalue" placeholder="e.g. yes" required>
				<span class="help-block">Add a value to watch. Wildcards are accepted, though only either the key or the value can be a wildcard.
			</div>
		</div>
		<div class="form-group">
			<label for="addreason" class="col-lg-4 control-label">Reason:</label>
			<div class="col-lg-6">
				<input type="text" class="form-control" id="addreason" name="addreason" placeholder="e.g. Vandalised often" required>
				<span class="help-block">Enter a note to yourself why this key was added.</span>
			</div>
		</div>
		<div class="form-group">
			<label for="addnotify" class="col-lg-4 control-label">Notification email:</label>
			<div class="col-lg-6">
				<input type="text" class="form-control" id="addnotify" name="addnotify" placeholder="Email address (optional)">
				<span class="help-block">Add an optional notification email address.</span>
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
