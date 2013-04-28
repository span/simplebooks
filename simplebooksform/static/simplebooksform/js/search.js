$(function() {
  $("#search-input").autocomplete({
    source: "/api/get_verifications/",
    minLength: 1,
  });
  console.log('test');
});