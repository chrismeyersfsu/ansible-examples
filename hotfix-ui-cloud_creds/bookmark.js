// http://benalman.com/code/test/jquery-run-code-bookmarklet/

var elem = $("input[aw-required-when='cloudCredentialRequired']");
var search_val = $(elem).val();
var cred_url = $(elem).attr('data-url').replace(":value", search_val);
console.log(cred_url);
console.log($(elem).val());
$.get(cred_url, function(res) {
  //$.get(group_url, 
  console.log(res['results'][0]['id']);
});

