<%inherit file="base.mako"/>
<%block name="header">
</%block>
<%block name="content">
<form class="form-horizontal" method="POST">
	<fieldset>
		<legend>Add new tag to group watched users:</legend>
		<div class="form-group">
			<label for="addname" class="col-lg-4 control-label">Tag name</label>
			<div class="col-lg-6">
				<input type="text" class="form-control" id="addoname" name="addname" placeholder="e.g. blocked-users" required>
				<span class="help-block">Try not to use spaces.</span>
			</div>
		</div>
		<div class="form-group">
			<label for="adddescription" class="col-lg-4 control-label">Description:</label>
			<div class="col-lg-6">
				<input type="text" class="form-control" id="addreason" name="adddescription" placeholder="e.g. They were blocked" required>
				<span class="help-block">This helps understand what the tag is for. Note this is visible to all DWG members.</span>
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
